from fastapi import APIRouter, Depends, HTTPException
from server.schemas import Review
from server.crud.reviews import add_review, search_review
from server.utils import get_db
from sqlalchemy.orm import Session


router = APIRouter()


# Adding new review
@router.post('/add-review')
def register_user(review: Review, session: Session = Depends(get_db)):
    add_review(review, session)
    return {"message": "Review added successfully."}


# Searching for review of a particular user
@router.get('/{user_id}/{plate_id}')
def get_review(user_id: int, plate_id: int, db_session: Session = Depends(get_db)):
    review_exists = search_review(user_id, plate_id, db_session)
    print(review_exists)
    return {"reviewPresent": review_exists}
