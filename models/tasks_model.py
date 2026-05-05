import enum
from sqlalchemy import Enum, Column, Integer, String, TIMESTAMP, func, ForeignKey
from database.db import Base
from sqlalchemy.orm import relationship
from models.users_model import User

class ProjectStatus(str, enum.Enum):
    COMPLETED = "Completed"
    NOT_COMPLETED = "Not Completed"
    IN_PROGRESS = "In Progress"

class Tasks(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String)
    task_desc = Column(String)
    task_date = Column(TIMESTAMP, server_default=func.now())
    task_status = Column(Enum(ProjectStatus), default = ProjectStatus.NOT_COMPLETED)
    user_id = Column(Integer, ForeignKey(User.user_id), nullable=False)
    user = relationship("User" , back_populates = "tasks")