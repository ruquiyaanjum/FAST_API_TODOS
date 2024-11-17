"""
defines the structure of the  items inside the database.
"""

from sqlalchemy import Column, Integer, String, Boolean  # Import data types
from database import Base  # Get base class
class TodoModel(Base):  # Create Todo table
      __tablename__ = "todos"  # Table name: 'todos'

      id = Column(Integer, primary_key=True, index=True)  # ID column, primary key
      title = Column(String(255), index=True)  # Title column, searchable
      description = Column(String(255), index=True, nullable=True)  # Description column, optional
      completed = Column(Boolean, default=False)  # Completed column, default is False

