from db_controller import DBController

db_controller = DBController()

foods = db_controller.get_all_foods()
print(foods)

db_controller.insert_food("Bananas")

foods = db_controller.get_all_foods()
print(foods)
