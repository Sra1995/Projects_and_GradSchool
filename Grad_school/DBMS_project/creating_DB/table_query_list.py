

from enum import Enum


_CREATE_TABLE_ADMIN = """
CREATE TABLE administrator (
    id			TINYINT UNSIGNED			NOT NULL,
    CONSTRAINT ad_pk
PRIMARY KEY (id)
)
"""

_CREATE_TABLE_CARTEL = """
CREATE TABLE cartel (
    id			SMALLINT UNSIGNED		NOT NULL,
    cartel_name	VARCHAR(30)			NOT NULL,
    CONSTRAINT ca_pk
        PRIMARY KEY (id)
)
"""

_CREATE_TABLE_PLAYER = """
CREATE TABLE player (
    id			INT UNSIGNED			NOT NULL,
    player_name	VARCHAR(20)			NOT NULL,
    money			INT UNSIGNED			NOT NULL,
    engines_rl		TINYINT UNSIGNED			NOT NULL	DEFAULT 1,
    mining_rl		TINYINT UNSIGNED			NOT NULL	DEFAULT 1,
    factory_rl		TINYINT UNSIGNED			NOT NULL	DEFAULT 1,
    hull_rl		TINYINT UNSIGNED			NOT NULL	DEFAULT 1,
    weapons_rl		TINYINT UNSIGNED			NOT NULL	DEFAULT 1,
    cartel_id		SMALLINT UNSIGNED,
    CONSTRAINT pl_pk
        PRIMARY KEY (id),
    CONSTRAINT pl_ca_fk
        FOREIGN KEY (cartel_id)
        REFERENCES cartel(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_CHAT_MESSAGE = """
CREATE TABLE chat_message (
    id			BIGINT UNSIGNED			NOT NULL,
    contents		VARCHAR(200)			NOT NULL,
    sender		INT UNSIGNED,
    receiver_player	INT UNSIGNED			DEFAULT NULL,
    receiver_cartel	SMALLINT UNSIGNED			DEFAULT NULL,
    CONSTRAINT ch_pk
PRIMARY KEY (id),
    CONSTRAINT ch_pl
FOREIGN KEY (sender)
REFERENCES player(id)
ON DELETE SET NULL
ON UPDATE CASCADE,
    CONSTRAINT ch_rep_fk
FOREIGN KEY (receiver_player)
REFERENCES player(id)
ON DELETE SET NULL
ON UPDATE CASCADE,
    CONSTRAINT ch_rec_fk
FOREIGN KEY (receiver_cartel)
REFERENCES cartel(id)
ON DELETE SET NULL
ON UPDATE CASCADE
)
"""

_CREATE_TABLE_PLANET = """
CREATE TABLE planet (
    id			BIGINT UNSIGNED 			NOT NULL,
    planet_name	VARCHAR(30)			NOT NULL,
    location		VARCHAR(30)			NOT NULL,
    owner			INT UNSIGNED,
    CONSTRAINT pt_pk
        PRIMARY KEY (id),
    CONSTRAINT pt_ow_fk
        FOREIGN KEY (owner)
        REFERENCES player(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_BUILDING = """
CREATE TABLE building (
    id			BIGINT UNSIGNED			NOT NULL,
    build_price	SMALLINT UNSIGNED		NOT NULL,
    maint_price	SMALLINT UNSIGNED		NOT NULL,
    owner			INT UNSIGNED,
    CONSTRAINT bu_pk
        PRIMARY KEY (id),
    CONSTRAINT bu_ow_fk
        FOREIGN KEY (owner)
        REFERENCES player(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_MINE = """
CREATE TABLE mine (
    id			BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT mi_pk
        PRIMARY KEY (id),
    CONSTRAINT mi_id_fk
        FOREIGN KEY (id)
        REFERENCES building(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_FACTORY = """
CREATE TABLE factory (
    id			BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT fa_pk
        PRIMARY KEY (id),
    CONSTRAINT fa_id_fk
        FOREIGN KEY (id)
        REFERENCES building(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_SHIPYARD = """
CREATE TABLE shipyard (
    id			BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT sy_pk
        PRIMARY KEY (id),
    CONSTRAINT sy_id_fk
        FOREIGN KEY (id)
        REFERENCES building(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_RESEARCH_LAB = """
CREATE TABLE research_lab (
    id			BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT rl_pk
        PRIMARY KEY (id),
    CONSTRAINT rl_id_fk
        FOREIGN KEY (id)
        REFERENCES building(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_RESOURCE = """
CREATE TABLE resource (
    id			BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT re_pk
        PRIMARY KEY (id)
)
"""

_CREATE_TABLE_RAW_RESOURCE = """
CREATE TABLE raw_resource (
    id			BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT ra_pk
        PRIMARY KEY (id),
    CONSTRAINT ra_fk
        FOREIGN KEY (id)
        REFERENCES resource(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_BAUBLE = """
CREATE TABLE bauble (
    id			BIGINT UNSIGNED			NOT NULL,
    base_value		SMALLINT UNSIGNED		NOT NULL,
    CONSTRAINT ba_pk
        PRIMARY KEY (id),
    CONSTRAINT ba_fk
        FOREIGN KEY (id)
        REFERENCES resource(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_MINE_PRODUCTION = """
CREATE TABLE mine_production (
    mine_id		BIGINT UNSIGNED			NOT NULL,
    resource_id	BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT mp_pk
        PRIMARY KEY (mine_id, resource_id),
    CONSTRAINT mp_mi_fk
        FOREIGN KEY (mine_id)
        REFERENCES mine(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT mp_re_fk
        FOREIGN KEY (resource_id)
        REFERENCES resource(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_FACTORY_PRODUCTION = """
CREATE TABLE factory_production (
    factory_id		BIGINT UNSIGNED			NOT NULL,
    resource_id	BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT fp_pk
        PRIMARY KEY (factory_id, resource_id),
    CONSTRAINT fp_fa_fk
        FOREIGN KEY (factory_id)
        REFERENCES factory(id)
ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fp_re_fk
        FOREIGN KEY (resource_id)
        REFERENCES resource(id)
ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_BUILDING_STORAGE = """
CREATE TABLE building_storage (
    building_id	BIGINT UNSIGNED			NOT NULL,
    resource_id	BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT bs_pk
        PRIMARY KEY (building_id, resource_id),
    CONSTRAINT bs_sh_fk
        FOREIGN KEY (building_id)
        REFERENCES building(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT bs_re_fk
        FOREIGN KEY (resource_id)
        REFERENCES resource(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_FLEET = """
CREATE TABLE fleet (
    number		SMALLINT UNSIGNED		NOT NULL,
    owner			INT UNSIGNED,
    current_turn	BIT					NOT NULL,
    turn_value		TINYINT UNSIGNED			NOT NULL,
    CONSTRAINT fl_pk
        PRIMARY KEY (number, owner),
    CONSTRAINT fl_ow_fk
        FOREIGN KEY (owner)
        REFERENCES player(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_SHIP = """
CREATE TABLE ship (
    id			BIGINT UNSIGNED			NOT NULL,
    ship_type		VARCHAR(16)			NOT NULL,
    max_resources	SMALLINT UNSIGNED		NOT NULL,
    max_weapons	SMALLINT UNSIGNED		NOT NULL,
    num_weapons	SMALLINT UNSIGNED		NOT NULL,
    owner			INT UNSIGNED,
    fleet			SMALLINT UNSIGNED		NOT NULL,
    CONSTRAINT sh_pk
        PRIMARY KEY (id),
    CONSTRAINT sh_ow_fk
        FOREIGN KEY (owner)
        REFERENCES fleet(owner)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT sh_fl_fk
        FOREIGN KEY (fleet)
        REFERENCES fleet(number)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_SHIP_STORAGE = """
CREATE TABLE ship_storage (
    ship_id		BIGINT UNSIGNED			NOT NULL,
    resource_id	BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT ss_pk
        PRIMARY KEY (ship_id, resource_id),
    CONSTRAINT ss_sh_fk
        FOREIGN KEY (ship_id)
        REFERENCES ship(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT ss_re_fk
        FOREIGN KEY (resource_id)
        REFERENCES resource(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_ORDER_GROUP = """
CREATE TABLE order_group (
    id			INT UNSIGNED			NOT NULL,
    repeat_amount	TINYINT UNSIGNED			NOT NULL,
    assn_flt_num	SMALLINT UNSIGNED			NOT NULL,
    assn_flt_owner	INT UNSIGNED,
    CONSTRAINT or_pk
        PRIMARY KEY (id),
    CONSTRAINT or_num_fk
        FOREIGN KEY (assn_flt_num)
        REFERENCES fleet(number)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT or_own_fk
        FOREIGN KEY (assn_flt_owner)
        REFERENCES fleet(owner)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_FLEET_ORDER = """
CREATE TABLE fleet_order (
    id			BIGINT UNSIGNED			NOT NULL,
    priority_num	TINYINT UNSIGNED			NOT NULL,
    order_group_id	INT UNSIGNED,
    CONSTRAINT fo_pk
        PRIMARY KEY (id),
    CONSTRAINT fo_og_fk
        FOREIGN KEY (order_group_id)
        REFERENCES order_group(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_MOVE_ORDER = """
CREATE TABLE move_order (
    id			BIGINT UNSIGNED			NOT NULL,
    location		VARCHAR(30)			NOT NULL,
    CONSTRAINT mo_pk
        PRIMARY KEY (id),
    CONSTRAINT mo_id_fk
        FOREIGN KEY (id)
        REFERENCES fleet_order(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_LOAD_ORDER = """
CREATE TABLE load_order (
    id			BIGINT UNSIGNED			NOT NULL,
    resource		BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT lo_ok
        PRIMARY KEY (id),
    CONSTRAINT lo_id_fk
        FOREIGN KEY (id)
        REFERENCES fleet_order(id),
    CONSTRAINT lo_re_fk
        FOREIGN KEY (resource)
        REFERENCES resource(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""

_CREATE_TABLE_UNLOAD_ORDER = """
CREATE TABLE unload_order (
    id			BIGINT UNSIGNED			NOT NULL,
    resource		BIGINT UNSIGNED			NOT NULL,
    CONSTRAINT uo_ok
        PRIMARY KEY (id),
    CONSTRAINT uo_id_fk
        FOREIGN KEY (id)
        REFERENCES fleet_order(id),
    CONSTRAINT uo_re_fk
        FOREIGN KEY (resource)
        REFERENCES resource(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)
"""


class TableCreateQuery(Enum):
    """
    Enum that stores all the create table queries.
    Stored as an enum because that makes it easy
    to iterate through all queries for initializing
    the database.
    """
    CREATE_TABLE_ADMIN = _CREATE_TABLE_ADMIN
    CREATE_TABLE_CARTEL = _CREATE_TABLE_CARTEL
    CREATE_TABLE_PLAYER = _CREATE_TABLE_PLAYER
    CREATE_TABLE_CHAT_MESSAGE = _CREATE_TABLE_CHAT_MESSAGE
    CREATE_TABLE_PLANET = _CREATE_TABLE_PLANET
    CREATE_TABLE_BUILDING = _CREATE_TABLE_BUILDING
    CREATE_TABLE_MINE = _CREATE_TABLE_MINE
    CREATE_TABLE_FACTORY = _CREATE_TABLE_FACTORY
    CREATE_TABLE_SHIPYARD = _CREATE_TABLE_SHIPYARD
    CREATE_TABLE_RESEARCH_LAB = _CREATE_TABLE_RESEARCH_LAB
    CREATE_TABLE_RESOURCE = _CREATE_TABLE_RESOURCE
    CREATE_TABLE_RAW_RESOURCE = _CREATE_TABLE_RAW_RESOURCE
    CREATE_TABLE_BAUBLE = _CREATE_TABLE_BAUBLE
    CREATE_TABLE_MINE_PRODUCTION = _CREATE_TABLE_MINE_PRODUCTION
    CREATE_TABLE_FACTORY_PRODUCTION = _CREATE_TABLE_FACTORY_PRODUCTION
    CREATE_TABLE_BUILDING_STORAGE = _CREATE_TABLE_BUILDING_STORAGE
    CREATE_TABLE_FLEET = _CREATE_TABLE_FLEET
    CREATE_TABLE_SHIP = _CREATE_TABLE_SHIP
    CREATE_TABLE_SHIP_STORAGE = _CREATE_TABLE_SHIP_STORAGE
    CREATE_TABLE_ORDER_GROUP = _CREATE_TABLE_ORDER_GROUP
    CREATE_TABLE_FLEET_ORDER = _CREATE_TABLE_FLEET_ORDER
    CREATE_TABLE_MOVE_ORDER = _CREATE_TABLE_MOVE_ORDER
    CREATE_TABLE_LOAD_ORDER = _CREATE_TABLE_LOAD_ORDER
    CREATE_TABLE_UNLOAD_ORDER = _CREATE_TABLE_UNLOAD_ORDER


class TableDropQuery(Enum):
    """
    Enum that stores all the drop table queries.
    Stored as an enum because that makes it easy
    to iterate through all queries for resetting
    the database during the initialization process.
    """
    DROP_TABLE_ADMIN = "DROP TABLE IF EXISTS administrator"
    DROP_TABLE_CARTEL = "DROP TABLE IF EXISTS cartel"
    DROP_TABLE_PLAYER = "DROP TABLE IF EXISTS player"
    DROP_TABLE_CHAT_MESSAGE = "DROP TABLE IF EXISTS chat_message"
    DROP_TABLE_PLANET = "DROP TABLE IF EXISTS planet"
    DROP_TABLE_BUILDING = "DROP TABLE IF EXISTS building"
    DROP_TABLE_MINE = "DROP TABLE IF EXISTS mine"
    DROP_TABLE_FACTORY = "DROP TABLE IF EXISTS factory"
    DROP_TABLE_SHIPYARD = "DROP TABLE IF EXISTS shipyard"
    DROP_TABLE_RESEARCH_LAB = "DROP TABLE IF EXISTS research_lab"
    DROP_TABLE_RESOURCE = "DROP TABLE IF EXISTS resource"
    DROP_TABLE_RAW_RESOURCE = "DROP TABLE IF EXISTS raw_resource"
    DROP_TABLE_BAUBLE = "DROP TABLE IF EXISTS bauble"
    DROP_TABLE_MINE_PRODUCTION = "DROP TABLE IF EXISTS mine_production"
    DROP_TABLE_FACTORY_PRODUCTION = "DROP TABLE IF EXISTS factory_production"
    DROP_TABLE_BUILDING_STORAGE = "DROP TABLE IF EXISTS building_storage"
    DROP_TABLE_FLEET = "DROP TABLE IF EXISTS fleet"
    DROP_TABLE_SHIP = "DROP TABLE IF EXISTS ship"
    DROP_TABLE_SHIP_STORAGE = "DROP TABLE IF EXISTS ship_storage"
    DROP_TABLE_ORDER_GROUP = "DROP TABLE IF EXISTS order_group"
    DROP_TABLE_FLEET_ORDER = "DROP TABLE IF EXISTS fleet_order"
    DROP_TABLE_MOVE_ORDER = "DROP TABLE IF EXISTS move_order"
    DROP_TABLE_LOAD_ORDER = "DROP TABLE IF EXISTS load_order"
    DROP_TABLE_UNLOAD_ORDER = "DROP TABLE IF EXISTS unload_order"
