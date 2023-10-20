from sqlalchemy.orm import Session
import server.models as md


def add_review(review_rating, db_session: Session):
    review = md.Review(
        user_id=review_rating.user_id,
        plate_id=review_rating.plate_id,
        rating=review_rating.rating,
        comment=review_rating.comment
    )
    db_session.add(review)
    db_session.commit()
    db_session.refresh(review)
    return review


def search_review(user_id, plate_id, db_session: Session):
    review = db_session.query(md.Review).filter_by(user_id=user_id, plate_id=plate_id).first()
    return True if review else False
