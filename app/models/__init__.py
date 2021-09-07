from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from app.models.auth.cuentas_usuarios import *
from app.models.core.modelos_principales import *
from app.models.dath.modelos import *