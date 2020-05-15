from project.services import create_user, get_last_user

from project.database import Base, engine

Base.metadata.create_all(engine)

create_user(name='ed')
user = get_last_user()

print(user)
