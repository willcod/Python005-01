from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType
from datetime import datetime


Base = declarative_base()

class UserTable(Base):

    __tablename__ = "UserTable"
    
    user_id = Column(
        Integer,
        primary_key=True,
        nullable=False
    )
    
    user_name = Column(
        String(100),
        nullable = False
    )

    age = Column(
        Integer,
        nullable=False
    )

    birthday = Column(
        DateTime,
        nullable = False
    )

    gender = Column(
        String(20),
        nullable=False
    )

    degree = Column(
        String(100),
        nullable=False
    )

    time_created = Column(
        DateTime,
        default=datetime.now
    )

    time_modified = Column(
        DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )

engine = create_engine(
            "mysql+pymysql://remoteUser:123456@47.103.136.85:3306/mydevdb?charset=utf8mb4",
            echo=True,
            encoding="utf-8")
        

sessionType = sessionmaker(bind=engine)
session = sessionType()

for result in session.query(UserTable):
    print(result)