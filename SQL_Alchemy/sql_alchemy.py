##----------------------------#
#| Author Louq_Tech           |  
#| Reference of SQLAlchemy    |
##----------------------------#

from sqlalchemy import create_engine, Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://postgres:root@localhost/TestingSQLA', echo=True)
Base = declarative_base()

class Courses(Base):
    __tablename__ = 'Courses'
    course_id = Column(Integer, primary_key=True, autoincrement="auto")
    course_name = Column(String)
    uni_classes = relationship('UniClass', back_populates='course')

class UniClass(Base):
    __tablename__ = 'UniClass'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    course_id = Column(Integer, ForeignKey('Courses.course_id'))
    course = relationship("Courses", back_populates="uni_classes")

# Create tables in the database
Base.metadata.create_all(engine)
