from fastapi import APIRouter, Depends, HTTPException
from server.schemas import ShoppingCart
from server.crud.cart_items import add_item_to_cart, get_all_cart_items
from server.utils import get_db
from sqlalchemy.orm import Session


router = APIRouter()


# Add a dish to the shopping cart
@router.post("/add-to-cart")
def cart_item(cart_item: ShoppingCart, session: Session = Depends(get_db)):
    item = add_item_to_cart(cart_item, session)
    return item


# Route for retrieving all dishes on the shopping cart of the current user.
@router.get("/{user_id}")
def display_all_cart_items(user_id, session: Session = Depends(get_db)):
    items = get_all_cart_items(user_id, session)
    return items
