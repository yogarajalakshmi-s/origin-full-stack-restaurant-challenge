from fastapi import APIRouter, Depends, HTTPException, Request
from server.schemas import ShoppingCart
from server.crud.cart_items import add_item_to_cart, get_all_cart_items, get_all_plates, remove_plate_from_cart, update_plate_quantity
from server.utils import get_db
from sqlalchemy.orm import Session


router = APIRouter()


# Add a dish to the shopping cart
@router.post("/add-to-cart")
def cart_item(cart_item: ShoppingCart, session: Session = Depends(get_db)):
    item = add_item_to_cart(cart_item, session)
    return item


# Route for retrieving all shopping_cart entries.
@router.get("/{user_id}")
def get_cart_items(user_id, session: Session = Depends(get_db)):
    items = get_all_cart_items(user_id, session)
    return items


# Retrieving all plates, to display in the Shopping cart tab
@router.get("/items/{user_id}")
def get_plates_using_cart_details(user_id: int, db_session: Session = Depends(get_db)):
    plates_in_cart = get_all_plates(user_id, db_session)
    return plates_in_cart


# Deleting plate from shopping cart
@router.delete("/remove/{plate_id}/{user_id}")
def remove_item_from_the_cart(plate_id: int, user_id: int, db_session: Session = Depends(get_db)):
    remove_plate_from_cart(plate_id, user_id, db_session)
    return {"message": "Item removed successfully"}


# Updating plate quantity in the Shopping cart page
@router.put("/update-quantity/{user_id}/{plate_id}")
def update_quantity(user_id: int, plate_id: int, quantity: int, db_session: Session = Depends(get_db)):
    update_plate_quantity(user_id, plate_id, quantity, db_session)
    return {"message": "Plate quantity updated successfully."}
