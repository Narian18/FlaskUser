from typing import Optional

from flask_login import UserMixin
from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash

from backend.models.mixins import NamedMixin
from backend.common.db import db


class User(UserMixin, NamedMixin, db.Model):
    __tablename__ = 'users'     # the DBMS will almost definitely have its own 'user' table
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    email: Mapped[str] = mapped_column(String(256), index=True, unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(256), nullable=False)

    @classmethod
    def get_by_email(cls, email: str):
        stmt = select(cls).where(cls.email == email)
        return db.session.scalars(stmt).first()

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.name}>'
