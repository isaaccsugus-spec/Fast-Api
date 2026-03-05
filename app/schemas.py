from pydantic import BaseModel , EmailStr
from typing import Optional

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
        orm_mode = True

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
        orm_mode = True