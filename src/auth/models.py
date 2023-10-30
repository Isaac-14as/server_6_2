from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Date, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, MetaData, Float
from database import Base
# from src.database import Base
from services.models import SubscriptionType, Trainer

# from src.services.models import SubscriptionType, Trainer
from sqlalchemy.orm import relationship

metadata = MetaData()



user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("gender", String, nullable=False),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("patronymic", String, nullable=True),
    Column("date_of_birth", Date, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column('sub_id', Integer, ForeignKey(SubscriptionType.id), nullable=True, default=None),
    Column('trainer_id', Integer, ForeignKey(Trainer.id), nullable=True, default=None),
    # relationship(SubscriptionType)
)

class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    gender = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    patronymic = Column(String, nullable=True)
    date_of_birth = Column(Date, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    sub_id = Column(Integer, ForeignKey(SubscriptionType.id), nullable=True, default=None)
    trainer_id = Column(Integer, ForeignKey(Trainer.id), nullable=True, default=None)
    # sub = relationship("SubscriptionType", lazy='selectin')

