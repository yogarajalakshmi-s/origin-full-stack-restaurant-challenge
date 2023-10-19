from fastapi import APIRouter, Depends, HTTPException
from server.schemas import ShoppingCart, Order
from server.crud.orders import get_orders, add_order
from server.crud.cart_items import delete_cart_items
from server.utils import get_db
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()


@router.get("/{user_id}", response_model=List[Order])
async def search_orders(db_session: Session = Depends(get_db)):
    return get_orders(db_session)


@router.post("/add-new-order/{user_id}")
async def add_new_order(
    user_id,
    items: List[ShoppingCart],
    db_session: Session = Depends(get_db),
):
    order = add_order(db_session, items)
    delete_cart_items(user_id, db_session)  # Cleaning up the shopping cart
    return order
