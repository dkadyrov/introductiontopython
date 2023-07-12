#%%
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Database(object):
    def __init__(self, db):
        self.engine = create_engine("sqlite:///{}".format(db))
        if database_exists(self.engine.url):
            Base.metadata.bind = self.engine
        else:
            Base.metadata.create_all(self.engine)
        DBSession = sessionmaker(bind=self.engine, autoflush=False)

        self.session = DBSession()
    
class Manufacturer(Base):
    __tablename__ = "Manufacturer"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    short_name = Column(String) 
    cereals = relationship("Cereal", backref=backref("Manufacturer"))

class Cereal(Base):
    __tablename__ = "Cereal"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    manufacturer_id = Column(Integer, ForeignKey("Manufacturer.id"))
    manufacturer = relationship("Manufacturer")
    rating = Column(Float)

db = Database("cereal.db")
#%%
import pandas as pd

data = pd.read_csv(r"../../04_Assignments/Assignment_4/cereal.csv")
#%%

mfrs = data.mfr.unique()
for m in mfrs:
    manufacturer = Manufacturer(
        name = m 
    )
    db.session.add(manufacturer)
    db.session.commit()
#%%
for i, row in data.iterrows():
    cereal = Cereal(
        name = row["name"],
        rating=row["rating"]
    )
    m = db.session.query(Manufacturer).filter(Manufacturer.name == row["mfr"]).first()
    cereal.manufacturer = m

    db.session.add(cereal)
db.session.commit()

# %%
