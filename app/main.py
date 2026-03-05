from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session 

import crud, schemas, utils, auth
from database import get_db

# Importamos las dependencias de seguridad (Asegúrate de tener el archivo dependencies.py)
from deps import get_current_user, require_admin

app = FastAPI()

# ==========================================
#                 PRODUCTOS
# ==========================================

@app.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)

@app.post("/productos", response_model=schemas.ProductoResponse)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    return crud.crear_producto(db=db, producto=producto)
    
@app.put("/productos/{producto_id}", response_model=schemas.ProductoResponse)
def actualizar_producto(producto_id: int, nuevo_producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = crud.actualizar_producto(db, producto_id, nuevo_producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    db_producto = crud.eliminar_producto(db, producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado", "producto_id": producto_id}


# ==========================================
#                 CATEGORÍAS
# ==========================================

@app.post("/categoria", response_model=schemas.CategoriaResponse)
def crear_categoria(categoria: schemas.CategoriaCreate, db: Session= Depends(get_db)):
    return crud.crear_categoria(db, categoria)

@app.get("/categoria", response_model=list[schemas.CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return crud.obtener_categorias(db)


# ==========================================
#           USUARIOS Y AUTENTICACIÓN
# ==========================================

# 1. Registrar un nuevo usuario
@app.post("/registro", response_model=schemas.UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    # Comprobamos si el email ya existe en la base de datos
    db_usuario = crud.obtener_usuario_por_email(db, email=usuario.email)
    if db_usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El email ya está registrado"
        )
    
    # Si no existe, lo creamos
    return crud.crear_usuario(db=db, usuario=usuario)

# 2. Iniciar sesión y obtener el token
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Buscamos al usuario por su email
    usuario = crud.obtener_usuario_por_email(db, email=form_data.username)
    
    # Verificamos que el usuario exista y que la contraseña coincida
    if not usuario or not utils.verify_password(form_data.password, usuario.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    # Generamos el token guardando el email en el 'sub'
    access_token = auth.crear_token(data={"sub": usuario.email})
    
    # Devolvemos el token
    return {"access_token": access_token, "token_type": "bearer"}

# 3. Ruta protegida: Ver mi propio perfil
@app.get("/perfil", response_model=schemas.UsuarioResponse)
def obtener_mi_perfil(usuario_actual = Depends(get_current_user)):
    # Esta ruta requiere un token válido proporcionado en la cabecera.
    # Si llega hasta aquí, devuelve los datos del usuario logueado.
    return usuario_actual