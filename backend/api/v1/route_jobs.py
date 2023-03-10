from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from backend.crud.crud_jobs import create_new_job
from backend.crud.crud_jobs import retreive_job
from backend.db.session import get_db
from backend.schemas.jobs import JobCreate
from backend.schemas.jobs import ShowJob

router = APIRouter()


@router.post('/', response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job, db=db, owner_id=current_user)
    return job


@router.get('/{id}', response_model=ShowJob)
def read_job(id: int, db: Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Job with this id {id} does not exist'
        )
    return job
