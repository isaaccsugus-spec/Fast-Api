from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="postgresql://postgres:ISAAC@localhost:5432/ecomerce_db"

engine = create_engine(DATABASE_URL)
sessionmaker = sessionmaker(autocomit=False, autoflush=False, bind=engine)
<<<<<<< HEAD
Base = declarative_base()
=======
Base = declarative_base
>>>>>>> b9f31fd139b225c59d85988d151aece48687f3ba
