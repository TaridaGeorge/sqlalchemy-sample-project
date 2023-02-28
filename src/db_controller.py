from sqlalchemy import create_engine, select, insert
from sqlalchemy.orm import Session
from base_entity import BaseEntity
from food_entity import FoodEntity
from uuid import uuid4


class DBController:
    def __init__(self) -> None:
        self.db_engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
        BaseEntity.metadata.create_all(self.db_engine)

    def get_all_foods(self):
        with Session(self.db_engine) as session:
            stmt = select(FoodEntity)
            return session.execute(stmt).fetchall()

    def insert_food(self, food_name: str):
        with Session(self.db_engine) as session:
            stmt = insert(FoodEntity).values(id=str(uuid4()), name=food_name)
            return session.execute(stmt)
