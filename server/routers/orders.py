from fastapi import APIRouter, Depends, HTTPException
from server.schemas import ShoppingCart, Order
from server.crud.orders import get_orders, add_order, check_order
from server.crud.cart_items import delete_all_cart_items
from server.utils import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()


@router.get("/{user_id}", response_model=List[Order])
async def search_orders(user_id, db_session: Session = Depends(get_db)):
    return get_orders(user_id, db_session)


# Placing new order for the current user
@router.post("/add-new-order/{user_id}")
async def add_new_order(
    user_id,
    items: List[ShoppingCart],
    db_session: Session = Depends(get_db),
):
    order = add_order(db_session, items)
    if order:
        delete_all_cart_items(user_id, db_session)  # Cleaning up the shopping cart
        return order
    else:
        raise HTTPException(status_code=500, detail="Error placing order")


# Checking if user has placed order on the plate (to display comment and rating feature)
@router.get("/check-order/{user_id}/{plate_id}")
async def check_if_order_exists(user_id: int, plate_id: int, db_session: Session = Depends(get_db)):
    order_exists = check_order(user_id, plate_id, db_session)
    return {"orderExists": order_exists}
