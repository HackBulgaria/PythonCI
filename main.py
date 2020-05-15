from project.models import User

from project.database import Session, Base, engine

Base.metadata.create_all(engine)

user = User(name='ed')

session = Session()
session.add(user)
session.commit()

session = Session()
fetched = session.query(User).order_by(User.id.desc()).first()

print(fetched.id)
