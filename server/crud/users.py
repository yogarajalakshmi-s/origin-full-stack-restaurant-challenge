from sqlalchemy.orm import Session
import server.models as md


# Adding new use to the DB
def add_new_user(db_user, db_session: Session):
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    return db_user


# Get a user by their email
def get_user_by_email(email, db_session: Session):
    user = db_session.query(md.User).filter_by(email=email).first()
    return user
