from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session 
import crud, schemas
from database import get_db

app = FastAPI()

# Quitamos la clase Productos de aquí y la lista "productos = []", 
# porque para eso estás importando "schemas" y usando la base de datos.

# Listar (Este ya lo tenías perfecto)
@app.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db: Session = Depends(get_db)):
    return crud.obtener_productos(db)

# Añadir (Le añadimos la base de datos db)
@app.post("/productos", response_model=schemas.ProductoResponse)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    # Llamamos a crud en lugar de hacer productos.append()
    return crud.crear_producto(db=db, producto=producto)
    
# Actualizar (Le añadimos la base de datos db)
@app.put("/productos/{producto_id}", response_model=schemas.ProductoResponse)
def actualizar_producto(producto_id: int, nuevo_producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    # Llamamos a crud para actualizar en la base de datos
    db_producto = crud.actualizar_producto(db, producto_id, nuevo_producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

# Eliminar (Le añadimos la base de datos db)
@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    # Llamamos a crud en lugar de usar .pop()
    db_producto = crud.eliminar_producto(db, producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado", "producto_id": producto_id}