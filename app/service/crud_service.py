from typing import Type, TypeVar, Generic, List
from sqlmodel import SQLModel, select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status

T = TypeVar("T", bound=SQLModel)


class CRUDService(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

    async def create(self, db: AsyncSession, obj_in: T) -> T:
        db.add(obj_in)
        await db.commit()
        await db.refresh(obj_in)
        return obj_in

    async def get(self, db: AsyncSession, id: int) -> T:
        obj = await db.get(self.model, id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Object not found"
            )
        return obj

    async def get_all(
        self, db: AsyncSession, skip: int = 0, limit: int = 10
    ) -> List[T]:
        statement = select(self.model).offset(skip).limit(limit)
        result = await db.execute(statement)
        return result.scalars().all()

    async def update(self, db: AsyncSession, id: int, obj_in: T) -> T:
        db_obj = await self.get(db, id)  # Validate and get the existing object
        if not db_obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Object not found"
            )
        obj_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if hasattr(db_obj, field):
                setattr(db_obj, field, obj_data[field])
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, id: int) -> T:
        obj = await self.get(db, id)  # Validate and get the existing object
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Object not found"
            )
        await db.delete(obj)
        await db.commit()
        return obj
