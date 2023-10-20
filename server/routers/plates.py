from fastapi import APIRouter, Depends, HTTPException
from typing import List

from server.crud.plates import get_plates, add_plate, get_plates_count, get_plate
from server.schemas import PlateBase, Plate, PlateCount
from server.utils import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("", response_model=List[Plate])
async def search_plates(db_session: Session = Depends(get_db)):
    """Find Plates.

    """
    return get_plates(db_session)


@router.get("/{plate_id}")
def fetch_plate(plate_id, db_session: Session = Depends(get_db)):
    plate = get_plate(plate_id, db_session)
    if plate:
        return plate
    else:
        raise HTTPException(detail="Plate does not exist", status_code=404)


@router.get("/ranking", response_model=List[PlateCount])
async def search_plates_count(db_session: Session = Depends(get_db)):
    """Find the ranked order of plates"""
    return get_plates_count(db_session)


@router.post("", response_model=Plate)
async def post_new_plate(
    item: PlateBase,
    db_session: Session = Depends(get_db),
):
    """Find order by ID.

    """
    return add_plate(db_session, item)
