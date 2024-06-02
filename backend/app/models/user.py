from sqlalchemy.orm import Mapped, mapped_column
from ..extensions import db

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(unique=False)
    def __init__(self, email, password):
        self.email = email
        self.password = password





