from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Create the SQLAlchemy engine and base class
#engine = create_engine("mysql://username:password@host:port/database")


# Get the database connection string from the environment
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_name = os.environ.get('DB_NAME', 'users')

engine = create_engine(f"mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

Base.metadata.create_all(engine)

class UserService:
    def __init__(self):
        self.Session = sessionmaker(bind=engine)

    def create_user(self, name, email, password):
        session = self.Session()
        user = Users(name, email, password)
        session.add(user)
        session.commit()
        session.close()

    def get_user_by_id(self, user_id):
        session = self.Session()
        user = session.query(Users).filter_by(id=user_id).first()
        session.close()
        return user

    def get_all_users(self):
        session = self.Session()
        users = session.query(Users).all()
        session.close()
        return users

    def update_user(self, user_id, name, email, password):
        session = self.Session()
        user = session.query(Users).filter_by(id=user_id).first()
        user.name = name
        user.email = email
        user.password = password
        session.commit()
        session.close()

    def delete_user(self, user_id):
        session = self.Session()
        user = session.query(Users).filter_by(id=user_id).first()
        session.delete(user)
        session.commit()
        session.close()
