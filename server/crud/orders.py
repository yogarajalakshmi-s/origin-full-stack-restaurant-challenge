from sqlalchemy.orm import Session
from fastapi import HTTPException

import server.models as md


def get_orders(db_session: Session):
    orders = db_session.query(md.Order).filter_by().all()
    print(orders)
    return orders


def add_order(db_session: Session, cart_items):
    order = md.Order()
    # Add PlateOrder objects.

    for item in cart_items:
        plate_order = md.PlateOrder(
            plate_id=item.plate_id,
            order_id=order.order_id,
            quantity=item.plate_quantity
        )
        order.plates.append(plate_order)

    db_session.add(order)
    db_session.commit()
    db_session.refresh(order)

    return order
