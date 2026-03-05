from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from auth import verificar_token
import crud

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_db)
):
    # 1. Definimos el error genérico una sola vez (como en tu video)
    cred_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # 2. Verificamos el token
    payload = verificar_token(token)
    
    # Como nuestro auth.py devuelve None si hay error, comprobamos así:
    if payload is None:
        raise cred_exc
        
    email: str = payload.get("sub")
    if email is None:
        raise cred_exc
        
    user = crud.obtener_usuario_por_email(db, email=email)
    if user is None:
        raise cred_exc
        
    return user

def require_admin(current_user = Depends(get_current_user)):
    # Igual que en tu video, comprobamos el rol
    if not current_user.es_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="No autorizado: se requiere rol admin"
        )
    return current_user