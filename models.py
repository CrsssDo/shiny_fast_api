from numpy import product
from database import Base
from sqlalchemy import String,Boolean,Integer,Column

class User(Base):
    __tablename__='user'
    id = Column(Integer,primary_key = True)
    name = Column(String(255), nullable = False)
    email = Column(String(255), nullable = False)
    pass_word = Column(String(255), nullable = False)
    is_verified = Column(Boolean, default = False)
    image_url =  Column(String(255))


    