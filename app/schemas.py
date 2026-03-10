from pydantic import BaseModel , EmailStr
from typing import Optional
from typing import List

class ProductoBase(BaseModel):
    nombre: str
    precio: float
    en_stock: bool = True
    categoria_id: Optional[int] = None 

class ProductoCreate(ProductoBase):
    pass

class ProductoResponse(ProductoBase):
    id: int
    class Config:
        from_attributes = True

class CategoriaBase(BaseModel):
    nombre : str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    id:int
    class Config:
       from_attributes = True

class UsuarioBase(BaseModel):
    nombre : str
    email : EmailStr

class UsuarioCreate(UsuarioBase):
    password:str

    es_admin : bool =False

class UsuarioResponse(UsuarioBase):
    id:int
    es_admin : bool

    class Config:
        from_attributes = True

from typing import List

# ... (tus schemas anteriores) ...

# 1. Lo que te manda el Frontend (El carrito)
class ItemCarrito(BaseModel):
    producto_id: int
    cantidad: int

class PedidoCreate(BaseModel):
    items: List[ItemCarrito]  # Fíjate aquí: ¡Una lista de objetos Pydantic!

# 2. Lo que tú le devuelves al Frontend (La factura)
class DetallePedidoResponse(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    class Config:
        from_attributes = True

class PedidoResponse(BaseModel):
    id: int
    usuario_id: int
    detalles: List[DetallePedidoResponse] # Lista de los detalles
    class Config:
        from_attributes = True