import enum
from sqlalchemy import Enum, Column, Integer, String, TIMESTAMP, func
from database.db import Base 
from sqlalchemy.orm import relationship

class UserRole(enum.Enum):
    ADMIN = "Admin"
    USER = "User"

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)
    user_role = Column(Enum(UserRole), default=UserRole.USER)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    tasks = relationship("Tasks", back_populates="user")