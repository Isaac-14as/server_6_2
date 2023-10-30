from sqlalchemy import  Float, ForeignKey, Column, Integer, String

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from alembic import op

Base = declarative_base()


class SubscriptionType(Base):
    __tablename__ = "subscription_type"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    subscription_type_infos = relationship("Opportunity", back_populates="subscription_types", lazy='selectin')

class Opportunity(Base):
    __tablename__ = "opportunity"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subscription_type_id = Column(Integer, ForeignKey(SubscriptionType.id), nullable=True)
    subscription_types = relationship("SubscriptionType", back_populates="subscription_type_infos", lazy='selectin')


class Trainer(Base):
    __tablename__ = "trainer"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    img_path = Column(String, nullable=True)
    age = Column(Integer, nullable=False)
    trainer_infos = relationship("InfoTrainer", back_populates="trainer_o", lazy='selectin')

class InfoTrainer(Base):
    __tablename__ = "info_trainer"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    trainer_id = Column(Integer, ForeignKey(Trainer.id), nullable=True)
    trainer_o = relationship("Trainer", back_populates="trainer_infos", lazy='selectin')



