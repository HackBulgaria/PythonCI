from project.models import User
from project.database import session_scope


def create_user(name):
    with session_scope() as session:
        user = User(name=name)

        session.add(user)

        return user


def get_last_user():
    with session_scope() as session:
        fetched = session.query(User).order_by(User.id.desc()).first()

        return fetched
