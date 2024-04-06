from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    permissions = Column(JSON)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey('roles.id'))
