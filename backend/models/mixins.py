from sqlalchemy import select

from backend.models.types import ModelID
from backend.common.db import db


class IDMixin:
    id: ModelID

    @classmethod
    def get_by_id(cls, instance_id: str | ModelID) -> db.Model | None:
        stmt = select(cls).where(cls.id == instance_id)
        return db.session.scalars(stmt).first()


class NamedMixin(IDMixin):
    name: str

    @classmethod
    def get_by_name(cls, name: str) -> db.Model | None:
        stmt = select(cls).where(cls.name == name)
        return db.session.scalars(stmt).first()
