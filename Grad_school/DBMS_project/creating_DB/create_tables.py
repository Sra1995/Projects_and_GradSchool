


import mysql.connector

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(
    host="",                                                    # Hostname of the MySQL server
    user="",                                                           # Username to connect to the MySQL server
    passwd="",                                                        # Password to connect to the MySQL server
    database="" 
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

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
class RowInserter():

    def get_player_id_highest(self):
        """
        Executes a procedure call rather than a standard query.
        """
        global _PROC_GET_PLAYER_ID_HIGHEST
        return self.db.execute_proc_call(_PROC_GET_PLAYER_ID_HIGHEST)

    def delete_row_player(self, player_id):
        global _DELETE_ROW_PLAYER
        self.db.execute_query(_DELETE_ROW_PLAYER, (player_id, ))

    def update_row_player(self, attribute, value, player_id):
        global _UPDATE_ROW_PLAYER
        # because MySQL implements every possible method of wasting my time
        # for no reason. why can't I just put a ? where I want in a prepared
        # statement?
        update_row = _UPDATE_ROW_PLAYER.replace("$", attribute)
        print(update_row)
        self.db.execute_query(update_row, (value, player_id))

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


# Insert at least 5 rows into the tables

# Insert into administrator table
admin_data = [(1,), (2,), (3,), (4,), (5,)]
cursor.executemany(_INSERT_TABLE_ADMIN, admin_data)


# Insert into cartel table
cartel_data = [(1, 'Red Phoenix'), (2, 'Golden Tigers'), (3, 'Silver Falcons'), (4, 'Emerald Serpents'), (5, 'Sapphire Wolves')]
cursor.executemany(_INSERT_TABLE_CARTEL, cartel_data)

# Insert into player table
player_data = [(1, 'John Doe', 1000, 1, 1, 1, 1, 1, 1),
               (2, 'Jane Smith', 2000, 2, 2, 2, 2, 2, 2),
               (3, 'Michael Johnson', 3000, 3, 3, 3, 3, 3, 3),
               (4, 'Emily Davis', 4000, 4, 4, 4, 4, 4, 4),
               (5, 'David Wilson', 5000, 5, 5, 5, 5, 5, 5)]
cursor.executemany(_INSERT_TABLE_PLAYER, player_data)

# Insert into chat_message table
chat_message_data = [(1, 'Hello, how are you?', 1, 2, None),
                     (2, 'Hi, I\'m doing great!', 2, 1, None),
                     (3, 'What are you up to?', 1, 3, None),
                     (4, 'Just working on a project', 3, 1, None),
                     (5, 'Nice to meet you!', 2, 3, None)]
cursor.executemany(_INSERT_TABLE_CHAT_MESSAGE, chat_message_data)

# Insert into planet table
planet_data = [(1, 'Earth', 'Sol System', 1),
               (2, 'Mars', 'Sol System', 2),
               (3, 'Alpha Centauri', 'Alpha Centauri System', 3),
               (4, 'Proxima b', 'Alpha Centauri System', 4),
               (5, 'Pandora', 'Pandora System', 5)]
cursor.executemany(_INSERT_TABLE_PLANET, planet_data)

# Commit the changes and close the cursor and connection
cnx.commit()
cursor.close()
cnx.close()

