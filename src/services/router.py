from fastapi import APIRouter, Depends
from sqlalchemy import delete, select, insert, func
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from services.models import Opportunity, InfoTrainer, SubscriptionType, Trainer
from services.schemas import OpportunityBase, InfoTrainerBase, SubscriptionTypeBase, TrainerBase
# from src.database import get_async_session
# from src.services.models import Opportunity, InfoTrainer, SubscriptionType, Trainer
# from src.services.schemas import OpportunityBase, InfoTrainerBase, SubscriptionTypeBase, TrainerBase



router = APIRouter(
    prefix="/services",
    tags=["Services"]
)

@router.post("/opportunity/add")
async def add_opportunity(new_opportunity: OpportunityBase, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Opportunity).values(**new_opportunity.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.get("/opportunity/get_all")
async def get_all_opportunity(session: AsyncSession = Depends(get_async_session)):
    query = select(Opportunity)
    opportunitys = await session.execute(query)
    return opportunitys.scalars().all()

@router.delete("/opportunity/{id}")
async def delete_opportunity(id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Opportunity).where(Opportunity.id == id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.post("/subscription_type/add")
async def add_subscription_type(new_st: SubscriptionTypeBase, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(SubscriptionType).values(name=new_st.name, price=new_st.price).returning(SubscriptionType.id)
    res = await session.execute(stmt)
    subscription_type_id = res.fetchone()[0]
    opportunities = new_st.subscription_type_infos
    for oppurtunity in opportunities:
        oppurtunity_model = Opportunity(name=oppurtunity.name, subscription_type_id=subscription_type_id)
        session.add(oppurtunity_model)
    await session.commit()
    return {"status": "success"}

@router.get("/subscription_type/get_by_id/{id}")
async def get_subscription_type_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(SubscriptionType).where(SubscriptionType.id==id)
    res = await session.execute(query)
    return res.scalars().all()[0]

@router.get("/subscription_type/get_all")
async def get_all_subscription_type(session: AsyncSession = Depends(get_async_session)):
    query = select(SubscriptionType)
    res = await session.execute(query)
    return res.scalars().all()

# удаляет subscription_type и все opportunity, которые с ним связаны
@router.delete("/subscription_type/{id}")
async def delete_subscription_type(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(SubscriptionType).where(SubscriptionType.id==id)
    res = await session.execute(query)
    opportunities = res.fetchone()[0].subscription_type_infos
    for oppurtunity in opportunities:
        stmt = delete(Opportunity).where(Opportunity.id == oppurtunity.id)
        await session.execute(stmt)
    stmt = delete(SubscriptionType).where(SubscriptionType.id==id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}













@router.post("/info_trainer/add")
async def add_info_trainer(new_opportunity: InfoTrainerBase, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(InfoTrainer).values(**new_opportunity.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.get("/info_trainer/get_all")
async def get_all_info_trainer(session: AsyncSession = Depends(get_async_session)):
    query = select(InfoTrainer)
    opportunitys = await session.execute(query)
    return opportunitys.scalars().all()


@router.delete("/info_trainer/{id}")
async def delete_info_trainer(id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(InfoTrainer).where(InfoTrainer.id == id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


# создание subscription_type + добавление opportunity к созданному subscription_type при необходимости
@router.post("/trainer/add")
async def add_trainer(new_st: TrainerBase, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Trainer).values(name=new_st.name, price=new_st.price, img_path=new_st.img_path, age=new_st.age).returning(Trainer.id)
    res = await session.execute(stmt)
    trainer_id = res.fetchone()[0]
    opportunities = new_st.trainer_infos
    for oppurtunity in opportunities:
        oppurtunity_model = InfoTrainer(name=oppurtunity.name, trainer_id=trainer_id)
        session.add(oppurtunity_model)
    await session.commit()
    return {"status": "success"}

@router.get("/trainer/get_by_id/{id}")
async def get_trainer_by_id(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Trainer).where(Trainer.id==id)
    res = await session.execute(query)
    return res.scalars().all()[0]

@router.get("/trainer/get_all")
async def get_all_trainer(session: AsyncSession = Depends(get_async_session)):
    query = select(Trainer)
    res = await session.execute(query)
    return res.scalars().all()

# удаляет subscription_type и все opportunity, которые с ним связаны
@router.delete("/trainer/{id}")
async def delete_trainer(id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Trainer).where(Trainer.id==id)
    res = await session.execute(query)
    opportunities = res.fetchone()[0].trainer_infos
    for oppurtunity in opportunities:
        stmt = delete(InfoTrainer).where(InfoTrainer.id == oppurtunity.id)
        await session.execute(stmt)
    stmt = delete(Trainer).where(Trainer.id==id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
