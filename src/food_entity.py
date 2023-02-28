from base_entity import BaseEntity
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class FoodEntity(BaseEntity):
    __tablename__ = "food"

    id: Mapped[int] = mapped_column(String(36), primary_key=True)
    name: Mapped[str]
