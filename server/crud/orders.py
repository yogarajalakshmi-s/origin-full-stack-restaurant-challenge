from sqlalchemy.orm import Session
from fastapi import HTTPException

import server.models as md


def get_orders(user_id: int, db_session: Session):
    orders = (
        db_session.query(md.Order)
        .join(md.PlateOrder)
        .filter(md.PlateOrder.user_id == user_id)
        .order_by(md.Order.order_time.asc())
        .all()
    )
    return orders


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


def check_order(user_id: int, plate_id: int, db_session: Session):
    order = db_session.query(md.PlateOrder).filter_by(
        user_id=user_id, plate_id=plate_id).first()

    return True if order else False
