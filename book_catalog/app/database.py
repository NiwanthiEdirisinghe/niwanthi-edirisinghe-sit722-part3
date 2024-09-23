from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://books_9cns_user:NnzJo06hpkvMSnJi3VcDjKXeHZBWRjLf@dpg-crm02m5umphs73eenpug-a.singapore-postgres.render.com/books_9cns" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
