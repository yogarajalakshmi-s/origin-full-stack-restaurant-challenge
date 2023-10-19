from sqlalchemy.orm import Session
import server.models as md


# Adding item to the cart
def add_item_to_cart(cart_item, db_session: Session):
    item = md.ShoppingCart(user_id=cart_item.user_id, plate_id=cart_item.plate_id, plate_quantity=cart_item.plate_quantity)
    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)
    return item


# Retrieving all cart items added by the current user
def get_all_cart_items(user_id, db_session: Session):
    items = db_session.query(md.ShoppingCart).filter_by(user_id=user_id).all()
    return items


# Retrieving all plates, to display in the Shopping cart tab
def get_all_plates(user_id, db_session: Session):
    plates_in_cart = (
        db_session.query(md.Plate).join(md.ShoppingCart)
        .filter(md.ShoppingCart.user_id == user_id).all()
    )

    return plates_in_cart


def remove_plate_from_cart(plate_id, user_id, db_session: Session):
    cart_item_to_remove = db_session.query(md.ShoppingCart).filter(
        md.ShoppingCart.plate_id == plate_id, md.ShoppingCart.user_id == user_id
    ).first()
    db_session.delete(cart_item_to_remove)
    db_session.commit()
