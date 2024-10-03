-- File: hw3_part3.sql

-- 1. Each table should have at least one row of data.
--2. Statements should be ordered so that none of the relational constraints are invalidated.  Please contact me if this is not possible (e.g. a circular dependency).


-- 1. Administrator Table
INSERT INTO Administrator (AdminID) VALUES (1);

-- 2. Cartel Table
INSERT INTO Cartel (CartelID, CartelName, MessageBoard) VALUES (1, 'Galactic', 'Welcome to our cartel!');

-- 3. Orders Table
INSERT INTO Orders (OrderID, OrderStatus, OrderDate) VALUES (1, 'Pending', '2024-03-08 10:00:00');

-- 4. Player Table
INSERT INTO Player (PlayerID, PlayerName, Resources, PlayerMoney, Tech_level, Hull_level, Weapon_tech, Mining_level, Factory_level, CartelID) 
VALUES (1, 'JohnDoe', 1000, 5000, 50, 60, 70, 80, 90, 1);

-- 5. Planet Table
INSERT INTO Planet (PlanetID, PlanetName, PlayerID) VALUES (1, 'Mars', 1);

-- 6. PrivateMessageSystem Table
INSERT INTO PrivateMessageSystem (MessageID, SenderID, ReceiverID, PM_Message) VALUES (1, 1, 2, 'Hello, how are you?');

-- 7. ChatSystem Table
INSERT INTO ChatSystem (ChatID, CartelID, Chat_Message, Chat_Date) VALUES (1, 1, 'Chat message', '2024-03-08 10:30:00');

-- 8. Overseen_by Table
INSERT INTO Overseen_by (AdminID, PlayerID) VALUES (1, 1);

-- 9. Factory Table
INSERT INTO Factory (FactoryID, Baubles, Resources, PlanetID) VALUES (1, 50, 200, 1);

-- 10. Mine Table
INSERT INTO Mine (MineID, Resources, PlanetID) VALUES (1, 100, 1);

-- 11. Shipyard Table
INSERT INTO Shipyard (ShipyardID, Ships, Resources, PlanetID) VALUES (1, 10, 500, 1);

-- 12. ResearchCenter Table
INSERT INTO ResearchCenter (ResearchCenterID, ResearchType, Resources, PlanetID) VALUES (1, 'Physics', 1000, 1);

-- 13. Fleet Table
INSERT INTO Fleet (FleetID, PlayerID) VALUES (1, 1);

-- 14. FleetOrders Table
INSERT INTO FleetOrders (FleetID, OrderID) VALUES (1, 1);

-- 15. Ship Table
INSERT INTO Ship (ShipID, FleetID, PlayerID, Weapons, Speed, ShipType, Capacity, Resources) 
VALUES (1, 1, 1, 10, 100, 'Explorer', 200, 500);
