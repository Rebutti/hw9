from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import configparser
import pathlib

#  f'postgresql://username:password@domain_name:port/database_name'

file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)


db_name = config.get('DB', 'db_name')


url = f'sqlite:///{db_name}.db'
Base = declarative_base()
engine = create_engine(url, echo=True)

DBSession = sessionmaker(bind=engine)
session = DBSession()