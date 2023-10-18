from sqlalchemy.orm import Session
import server.models as md


# Adding item to the cart
def add_item_to_cart(cart_item, db_session: Session):
    item = md.ShoppingCart(user_id=cart_item.user_id, plate_id=cart_item.plate_id, plate_quantity=cart_item.plate_quantity)
    db_session.add(item)
    db_session.commit()
    db_session.refresh(item)
    return item


# Retrieving all dishes added to the Shopping cart by the current user
def get_all_cart_items(user_id, db_session: Session):
    items = db_session.query(md.ShoppingCart).filter_by(user_id=user_id).all()
    return items
