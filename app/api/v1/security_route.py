from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.schemas.security_schemas import Token
from app.core.security import create_access_token, verify_password, get_current_user
from app.core.database import get_db
from app.models.user_model import UserModel as User

router = APIRouter(prefix="/security", tags=["Security"])

@router.post('/token', response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_db),
):
    result = await session.execute(select(User).where(User.nickname == form_data.username))
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect nickname or password'
        )

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect nickname or password'
        )

    access_token = create_access_token(data={'sub': user.nickname})

    return {'access_token': access_token, 'token_type': 'bearer'}

@router.post('/refresh_token', response_model=Token)
async def refresh_access_token(
    user: User = Depends(get_current_user),
):
    new_access_token = create_access_token(data={'sub': user.nickname})

    return {'access_token': new_access_token, 'token_type': 'bearer'}
