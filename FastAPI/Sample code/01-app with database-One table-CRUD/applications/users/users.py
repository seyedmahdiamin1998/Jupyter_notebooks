from http.client import HTTPException

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from . import schemas
from database import get_db
import models

router = APIRouter(
    prefix="/user",
    tags=["app1"]
)


@router.get('', status_code = 200)
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()

    return users


@router.get('/{email}', status_code = 200)
async def get_user(email, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User with the email {} is not available.'.format(email))

        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message': 'User with the id {} is not available.'.format(id)}

    return user

    
@router.post('', status_code = status.HTTP_201_CREATED)
async def create_user(user:schemas.User, db: Session = Depends(get_db)):

    user_data = db.query(models.User).filter(models.User.email==user.email).first()
    if user_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Email {0} already registered.'.format(user.email))

    new_user = models.User(email=user.email, password=user.password, is_active=user.is_active)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return user


@router.delete('/{email}', status_code = status.HTTP_204_NO_CONTENT)
async def remove_user(email, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User with the email {} is not available.'.format(email))
    user = db.query(models.User).filter(models.User.email==email).delete(synchronize_session=False)
    db.commit()

    return 'done'

@router.put('/{email}', status_code = status.HTTP_202_ACCEPTED)
async def create_user(user:schemas.UpdateUser, db: Session = Depends(get_db)):

    user_data = db.query(models.User).filter(models.User.email==user.email).first()
    if not user_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="User with email {0} did'nt registered.".format(user.email))
    db.query(models.User).filter(models.User.email==user.email).update({'is_active' : user.is_active})
    
    db.commit()

    return user