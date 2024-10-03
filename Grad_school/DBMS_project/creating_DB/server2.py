import socket
import mysql.connector
from mysql.connector import Error






_PROC_GET_PLAYER_ID_HIGHEST = """
get_highest_player_id
"""

_DELETE_ROW_PLAYER = """
DELETE FROM player WHERE id=?
"""

_UPDATE_ROW_PLAYER = """
UPDATE player SET $=? WHERE id=?
"""

_INSERT_TABLE_ADMIN = """
INSERT INTO administrator (id)
VALUES (?)
"""

_INSERT_TABLE_CARTEL = """
INSERT INTO cartel (id, cartel_name)
VALUES (?, ?)
"""

_INSERT_TABLE_PLAYER = """
INSERT INTO player (id, player_name, money, engines_rl, mining_rl, factory_rl, hull_rl, weapons_rl, cartel_id)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

_INSERT_TABLE_CHAT_MESSAGE = """
INSERT INTO chat_message (id, contents, sender, receiver_player, receiver_cartel)
VALUES (?, ?, ?, ?, ?)
"""

_INSERT_TABLE_PLANET = """
INSERT INTO planet (id, planet_name, location, owner)
VALUES (?, ?, ?, ?)
"""

_INSERT_TABLE_BUILDING = """
INSERT INTO building (id, build_price, maint_price, owner)
VALUES (?, ?, ?, ?)
"""

_INSERT_TABLE_MINE = """
INSERT INTO mine (id)
VALUES (?)
"""

_INSERT_TABLE_FACTORY = """
INSERT INTO factory (id)
VALUES (?)
"""

_INSERT_TABLE_SHIPYARD = """
INSERT INTO shipyard (id)
VALUES (?)
"""

_INSERT_TABLE_RESEARCH_LAB = """
INSERT INTO research_lab (id)
VALUES (?)
"""

_INSERT_TABLE_RESOURCE = """
INSERT INTO resource (id)
VALUES (?)
"""

_INSERT_TABLE_RAW_RESOURCE = """
INSERT INTO raw_resource (id)
VALUES (?)
"""

_INSERT_TABLE_BAUBLE = """
INSERT INTO bauble (id, base_value)
VALUES (?, ?)
"""

_INSERT_TABLE_MINE_PRODUCTION = """
INSERT INTO mine_production (mine_id, resource_id)
VALUES (?, ?)
"""

_INSERT_TABLE_FACTORY_PRODUCTION = """
INSERT INTO factory_production (factory_id, resource_id)
VALUES (?, ?)
"""

_INSERT_TABLE_BUILDING_STORAGE = """
INSERT INTO building_storage (building_id, resource_id)
VALUES (?, ?)
"""

_INSERT_TABLE_FLEET = """
INSERT INTO fleet (number, owner, current_turn, turn_value)
VALUES (?, ?, ?, ?)
"""

_INSERT_TABLE_SHIP = """
INSERT INTO ship (id, ship_type, max_resources, max_weapons, num_weapons, owner, fleet)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

_INSERT_TABLE_SHIP_STORAGE = """
INSERT INTO ship_storage (ship_id, resource_id)
VALUES (?, ?)
"""

_INSERT_TABLE_ORDER_GROUP = """
INSERT INTO order_group (id, repeat_amount, assn_flt_num, assn_flt_owner)
VALUES (?, ?, ?, ?)
"""

_INSERT_TABLE_FLEET_ORDER = """
INSERT INTO fleet_order (id, priority_num, order_group_id)
VALUES (?, ?, ?)
"""

_INSERT_TABLE_MOVE_ORDER = """
INSERT INTO move_order (id, location)
VALUES (?, ?)
"""

_INSERT_TABLE_LOAD_ORDER = """
INSERT INTO load_order (id, resource)
VALUES (?, ?)
"""

_INSERT_TABLE_UNLOAD_ORDER = """
INSERT INTO unload_order (id, resource)
VALUES (?, ?)
"""


class RowInserter:
    def __init__(self, db):
        self.db = db

    def get_highest_player_id(self):
        global _PROC_GET_PLAYER_ID_HIGHEST
        return self.db.execute_proc_call(_PROC_GET_PLAYER_ID_HIGHEST)

    def delete_row_player(self, player_id):
        global _DELETE_ROW_PLAYER
        self.db.execute_query(_DELETE_ROW_PLAYER, (player_id,))

    def update_row_player(self, attribute, value, player_id):
        global _UPDATE_ROW_PLAYER
        update_query = _UPDATE_ROW_PLAYER.replace("$", attribute)
        self.db.execute_query(update_query, (value, player_id))

    def insert_table_admin(self, admin_id: int):
        global _INSERT_TABLE_ADMIN
        self.db.execute_query(_INSERT_TABLE_ADMIN, (admin_id,))

    def insert_table_cartel(self, cartel_id: int, cartel_name: str):
        global _INSERT_TABLE_CARTEL
        self.db.execute_query(_INSERT_TABLE_CARTEL, (cartel_id, cartel_name))
    
    def insert_table_player(self, player_id: int, player_name: str, money: int, engines_rl: int, mining_rl: int, factory_rl: int, hull_rl: int, weapons_rl: int, cartel_id: int):
        global _INSERT_TABLE_PLAYER
        self.db.execute_query(_INSERT_TABLE_PLAYER, (player_id, player_name, money, engines_rl, mining_rl, factory_rl, hull_rl, weapons_rl, cartel_id))
    
    def insert_table_chat_message(self, message_id: int, contents: str, sender: int, receiver_player: int, receiver_cartel: int):
        global _INSERT_TABLE_CHAT_MESSAGE
        self.db.execute_query(_INSERT_TABLE_CHAT_MESSAGE, (message_id, contents, sender, receiver_player, receiver_cartel))
    
    def insert_table_planet(self, planet_id: int, planet_name: str, location: str, owner: int):
        global _INSERT_TABLE_PLANET
        self.db.execute_query(_INSERT_TABLE_PLANET, (planet_id, planet_name, location, owner))
    
    def insert_table_building(self, building_id: int, build_price: int, maint_price: int, owner: int):
        global _INSERT_TABLE_BUILDING
        self.db.execute_query(_INSERT_TABLE_BUILDING, (building_id, build_price, maint_price, owner))
    
    def insert_table_mine(self, mine_id: int):
        global _INSERT_TABLE_MINE
        self.db.execute_query(_INSERT_TABLE_MINE, (mine_id,))
    
    def insert_table_factory(self, factory_id: int):
        global _INSERT_TABLE_FACTORY
        self.db.execute_query(_INSERT_TABLE_FACTORY, (factory_id,))
    
    def insert_table_shipyard(self, shipyard_id: int):
        global _INSERT_TABLE_SHIPYARD
        self.db.execute_query(_INSERT_TABLE_SHIPYARD, (shipyard_id,))
    
    def insert_table_research_lab(self, research_lab_id: int):
        global _INSERT_TABLE_RESEARCH_LAB
        self.db.execute_query(_INSERT_TABLE_RESEARCH_LAB, (research_lab_id,))
    
    def insert_table_resource(self, resource_id: int):
        global _INSERT_TABLE_RESOURCE
        self.db.execute_query(_INSERT_TABLE_RESOURCE, (resource_id,))
    
    def insert_table_raw_resource(self, raw_resource_id: int):
        global _INSERT_TABLE_RAW_RESOURCE
        self.db.execute_query(_INSERT_TABLE_RAW_RESOURCE, (raw_resource_id,))
    
    def insert_table_bauble(self, bauble_id: int, base_value: int):
        global _INSERT_TABLE_BAUBLE
        self.db.execute_query(_INSERT_TABLE_BAUBLE, (bauble_id, base_value))
    
    def insert_table_mine_production(self, mine_id: int, resource_id: int):
        global _INSERT_TABLE_MINE_PRODUCTION
        self.db.execute_query(_INSERT_TABLE_MINE_PRODUCTION, (mine_id, resource_id))
    
    def insert_table_factory_production(self, factory_id: int, resource_id: int):
        global _INSERT_TABLE_FACTORY_PRODUCTION
        self.db.execute_query(_INSERT_TABLE_FACTORY_PRODUCTION, (factory_id, resource_id))
    
    def insert_table_building_storage(self, building_id: int, resource_id: int):
        global _INSERT_TABLE_BUILDING_STORAGE
        self.db.execute_query(_INSERT_TABLE_BUILDING_STORAGE, (building_id, resource_id))
    
    def insert_table_fleet(self, fleet_number: int, fleet_owner: int, current_turn: int, turn_value: int):
        global _INSERT_TABLE_FLEET
        self.db.execute_query(_INSERT_TABLE_FLEET, (fleet_number, fleet_owner, current_turn, turn_value))
    
    def insert_table_ship(self, ship_id: int, ship_type: str, max_resources: int, max_weapons: int, num_weapons: int, owner: int, fleet: int):
        global _INSERT_TABLE_SHIP
        self.db.execute_query(_INSERT_TABLE_SHIP, (ship_id, ship_type, max_resources, max_weapons, num_weapons, owner, fleet))
    
    def insert_table_ship_storage(self, ship_id: int, resource_id: int):
        global _INSERT_TABLE_SHIP_STORAGE
        self.db.execute_query(_INSERT_TABLE_SHIP_STORAGE, (ship_id, resource_id))
    
    def insert_table_order_group(self, order_group_id: int, repeat_amount: int, assn_flt_num: int, assn_flt_owner: int):
        global _INSERT_TABLE_ORDER_GROUP
        self.db.execute_query(_INSERT_TABLE_ORDER_GROUP, (order_group_id, repeat_amount, assn_flt_num, assn_flt_owner))
    
    def insert_table_fleet_order(self, fleet_order_id: int, priority_num: int, order_group_id: int):
        global _INSERT_TABLE_FLEET_ORDER
        self.db.execute_query(_INSERT_TABLE_FLEET_ORDER, (fleet_order_id, priority_num, order_group_id))
    
    def insert_table_move_order(self, move_order_id: int, location: str):
        global _INSERT_TABLE_MOVE_ORDER
        self.db.execute_query(_INSERT_TABLE_MOVE_ORDER, (move_order_id, location))
    
    def insert_table_load_order(self, load_order_id: int, resource: int):
        global _INSERT_TABLE_LOAD_ORDER
        self.db.execute_query(_INSERT_TABLE_LOAD_ORDER, (load_order_id, resource))
    
    def insert_table_unload_order(self, unload_order_id: int, resource: int):
        global _INSERT_TABLE_UNLOAD_ORDER
        self.db.execute_query(_INSERT_TABLE_UNLOAD_ORDER, (unload_order_id, resource))
    
    def update_table_admin(self, admin_id: int):
        global _UPDATE_TABLE_ADMIN
        self.db.execute_query(_UPDATE_TABLE_ADMIN, (admin_id,))
    
    def update_table_cartel(self, cartel_id: int, cartel_name: str):
        global _UPDATE_TABLE_CARTEL
        self.db.execute_query(_UPDATE_TABLE_CARTEL, (cartel_id, cartel_name))
    
    def update_table_player(self, player_id: int, player_name: str, money: int, engines_rl: int, mining_rl: int, factory_rl: int, hull_rl: int, weapons_rl: int, cartel_id: int):
        global _UPDATE_TABLE_PLAYER
        self.db.execute_query(_UPDATE_TABLE_PLAYER, (player_id, player_name, money, engines_rl, mining_rl, factory_rl, hull_rl, weapons_rl, cartel_id))
    
    def update_table_chat_message(self, message_id: int, contents: str, sender: int, receiver_player: int, receiver_cartel: int):
        global _UPDATE_TABLE_CHAT_MESSAGE
        self.db.execute_query(_UPDATE_TABLE_CHAT_MESSAGE, (message_id, contents, sender, receiver_player, receiver_cartel))
    
    def update_table_planet(self, planet_id: int, planet_name: str, location: str, owner: int):
        global _UPDATE_TABLE_PLANET
        self.db.execute_query(_UPDATE_TABLE_PLANET, (planet_id, planet_name, location, owner))
    
    def update_table_building(self, building_id: int, build_price: int, maint_price: int, owner: int):
        global _UPDATE_TABLE_BUILDING
        self.db.execute_query(_UPDATE_TABLE_BUILDING, (building_id, build_price, maint_price, owner))
    
    def update_table_mine(self, mine_id: int):
        global _UPDATE_TABLE_MINE
        self.db.execute_query(_UPDATE_TABLE_MINE, (mine_id,))
    
    def update_table_factory(self, factory_id: int):
        global _UPDATE_TABLE_FACTORY
        self.db.execute_query(_UPDATE_TABLE_FACTORY, (factory_id,))
    
    def update_table_shipyard(self, shipyard_id: int):
        global _UPDATE_TABLE_SHIPYARD
        self.db.execute_query(_UPDATE_TABLE_SHIPYARD, (shipyard_id,))
    
    def update_table_research_lab(self, research_lab_id: int):
        global _UPDATE_TABLE_RESEARCH_LAB
        self.db.execute_query(_UPDATE_TABLE_RESEARCH_LAB, (research_lab_id,))
    
    def update_table_resource(self, resource_id: int):
        global _UPDATE_TABLE_RESOURCE
        self.db.execute_query(_UPDATE_TABLE_RESOURCE, (resource_id,))
    
    def update_table_raw_resource(self, raw_resource_id: int):
        global _UPDATE_TABLE_RAW_RESOURCE
        self.db.execute_query(_UPDATE_TABLE_RAW_RESOURCE, (raw_resource_id,))
    
    def update_table_bauble(self, bauble_id: int, base_value: int):
        global _UPDATE_TABLE_BAUBLE
        self.db.execute_query(_UPDATE_TABLE_BAUBLE, (bauble_id, base_value))
    
    def update_table_mine_production(self, mine_id: int, resource_id: int):
        global _UPDATE_TABLE_MINE_PRODUCTION
        self.db.execute_query(_UPDATE_TABLE_MINE_PRODUCTION, (mine_id, resource_id))
    
    def update_table_factory_production(self, factory_id: int, resource_id: int):
        global _UPDATE_TABLE_FACTORY_PRODUCTION
        self.db.execute_query(_UPDATE_TABLE_FACTORY_PRODUCTION, (factory_id, resource_id))
    
    def update_table_building_storage(self, building_id: int, resource_id: int):
        global _UPDATE_TABLE_BUILDING_STORAGE
        self.db.execute_query(_UPDATE_TABLE_BUILDING_STORAGE, (building_id, resource_id))
    
    def update_table_fleet(self, fleet_number: int, fleet_owner: int, current_turn: int, turn_value: int):
        global _UPDATE_TABLE_FLEET
        self.db.execute_query(_UPDATE_TABLE_FLEET, (fleet_number, fleet_owner, current_turn, turn_value))
    
    def update_table_ship(self, ship_id: int, ship_type: str, max_resources: int, max_weapons: int, num_weapons: int, owner: int, fleet: int):
        global _UPDATE_TABLE_SHIP
        self.db.execute_query(_UPDATE_TABLE_SHIP, (ship_id, ship_type, max_resources, max_weapons, num_weapons, owner, fleet))
    
    def update_table_ship_storage(self, ship_id: int, resource_id: int):
        global _UPDATE_TABLE_SHIP_STORAGE
        self.db.execute_query(_UPDATE_TABLE_SHIP_STORAGE, (ship_id, resource_id))
    
    def update_table_order_group(self, order_group_id: int, repeat_amount: int, assn_flt_num: int, assn_flt_owner: int):
        global _UPDATE_TABLE_ORDER_GROUP
        self.db.execute_query(_UPDATE_TABLE_ORDER_GROUP, (order_group_id, repeat_amount, assn_flt_num, assn_flt_owner))
    
    def update_table_fleet_order(self, fleet_order_id: int, priority_num: int, order_group_id: int):
        global _UPDATE_TABLE_FLEET_ORDER
        self.db.execute_query(_UPDATE_TABLE_FLEET_ORDER, (fleet_order_id, priority_num, order_group_id))
    
    def update_table_move_order(self, move_order_id: int, location: str):
        global _UPDATE_TABLE_MOVE_ORDER
        self.db.execute_query(_UPDATE_TABLE_MOVE_ORDER, (move_order_id, location))
    
    def update_table_load_order(self, load_order_id: int, resource: int):
        global _UPDATE_TABLE_LOAD_ORDER
        self.db.execute_query(_UPDATE_TABLE_LOAD_ORDER, (load_order_id, resource))
    
    def update_table_unload_order(self, unload_order_id: int, resource: int):
        global _UPDATE_TABLE_UNLOAD_ORDER
        self.db.execute_query(_UPDATE_TABLE_UNLOAD_ORDER, (unload_order_id, resource))







def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="",
            user="",
            passwd="",
            database=""
        )
    except Error as e:
        print(f"Database connection error: {e}")
    return connection

# Instantiate RowInserter with the database connection object
row_inserter = RowInserter(create_connection())

def handle_request(request, connection):
    cursor = connection.cursor()
    try:
        cursor.execute(request)
        if cursor.description is not None:
            rows = cursor.fetchall()
            result = '\n'.join(map(str, rows))
            return result
        else:
            connection.commit()
            return "Success"
    except Error as e:
        return f"Database error: {e}"

def sanitize_input(input_str):
    sanitized_input = input_str.strip()
    return sanitized_input

def add_planet(request, connection):
    return row_inserter.add_planet(request)

def edit_planet(request, connection):
    return row_inserter.edit_planet(request)

def delete_planet(request, connection):
    return row_inserter.delete_planet(request)

def server_program():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serversocket.bind(('localhost', 8089))
        serversocket.listen(5)
        print("Server is listening on port 8089")
    except socket.error as e:
        print(f"Socket error: {e}")
        return

    while True:
        try:
            connection, address = serversocket.accept()
            print(f"Connection established with {address}")
            while True:
                buf = connection.recv(1024)
                if len(buf) > 0:
                    sanitized_request = sanitize_input(buf.decode())
                    response = handle_request(sanitized_request, create_connection())
                    connection.send(response.encode())
                else:
                    break
        except Error as e:
            print(f"Error: {e}")
            break
        except socket.error as e:
            print(f"Socket error: {e}")
            break

if __name__ == "__main__":
    server_program()
