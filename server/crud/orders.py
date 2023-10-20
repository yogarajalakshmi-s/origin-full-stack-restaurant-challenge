from sqlalchemy.orm import Session
from fastapi import HTTPException

import server.models as md


def get_orders(user_id: int, db_session: Session):
    user = db_session.query(md.User).filter_by(id=user_id).first()
    order = list({plate_order.order for plate_order in user.plate_orders})
    return order


def add_order(db_session: Session, cart_items):
    order = md.Order()
    # Add PlateOrder objects.

    for item in cart_items:
        plate_order = md.PlateOrder(
            plate_id=item.plate_id,
            order_id=order.order_id,
            quantity=item.plate_quantity,
            user_id=item.user_id
        )
        order.plates.append(plate_order)

    db_session.add(order)
    db_session.commit()
    db_session.refresh(order)

    return order
