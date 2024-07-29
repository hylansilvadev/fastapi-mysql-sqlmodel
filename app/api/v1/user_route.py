from typing import List
from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.database import get_db
from app.service.crud_service import CRUDService
from app.schemas.user_schemas import CreateUser, UpdateUser, UserResponse, User
from app.models.user_model import UserModel
from app.core.security import get_current_user, get_password_hash


router = APIRouter(prefix="/user", tags=["User"])

user_service = CRUDService(UserModel)


@router.post(
    "/",
    response_model=UserResponse,
    response_model_by_alias=False,
    status_code=status.HTTP_201_CREATED,
)
async def post_user(
    user: CreateUser, 
    db: AsyncSession = Depends(get_db),
):
    user_data = user.model_dump(exclude_unset=True)
    user_data["hashed_password"] = get_password_hash(user_data.pop("password"))
    db_user = UserModel(**user_data)
    return await user_service.create(db, db_user)


@router.get(
    "/",
    response_model=List[UserResponse],
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
async def get_all(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await user_service.get_all(db, skip=skip, limit=limit)


@router.get(
    "/{id}",
    response_model=UserResponse,
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
async def get_by_id(
    id: str, 
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return await user_service.get(db, id)


@router.patch(
    "/{id}",
    response_model=UserResponse,
    response_model_by_alias=False,
    status_code=status.HTTP_200_OK,
)
async def update_user(
    user_id: int, 
    user: UpdateUser, 
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    user_data = user.model_dump(exclude_unset=True)
    if "password" in user_data:
        user_data["hashed_password"] = get_password_hash(user_data.pop("password"))
    return await user_service.update(db, user_id, user_data)


@router.delete(
    "/{id}",
    response_model=None,
    response_model_by_alias=False,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_user(
    user_id: int, 
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    await user_service.delete(db, user_id)
