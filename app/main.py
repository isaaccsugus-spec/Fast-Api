from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Productos(BaseModel):
    nombre:str
    precio:float
    en_stock:bool

productos = []

# Listar
@app.get("/productos")
def listar_productos():
    return {"productos": productos}

# Añadir 
@app.post("/productos")
def crear_producto(producto: Productos):
    productos.append(producto)
    return {"message": "Producto creado", "producto": producto}
    
# Actualizar (Ahora pide un objeto Pydantic entero)
@app.put("/productos/{producto_id}")
def actualizar_producto(producto_id: int, nuevo_producto: Productos):
    productos[producto_id] = nuevo_producto
    return {"message": "Producto editado", "producto": nuevo_producto}

# Eliminar (¡AQUÍ ESTABA EL ERROR 2!)
@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int): # ERROR TUYO: Pusiste (id: int). Tiene que llamarse EXACTAMENTE igual que arriba en la ruta ({producto_id}).
    eliminado = productos.pop(producto_id)
    return {"message": "Producto eliminado", "producto": eliminado}