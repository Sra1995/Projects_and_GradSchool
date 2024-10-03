-- 1. Administrator Table
CREATE TABLE Administrator (
    AdminID INT PRIMARY KEY
);

-- 2. Cartel Table
CREATE TABLE Cartel (
    CartelID INT PRIMARY KEY,
    CartelName VARCHAR(255) NOT NULL,
    MessageBoard VARCHAR(255) NOT NULL
);

-- 3. Orders Table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    OrderStatus VARCHAR(255),
    OrderDate DATETIME
);

-- 4. Player Table
CREATE TABLE Player (
    PlayerID INT PRIMARY KEY,
    PlayerName VARCHAR(255) NOT NULL,
    Resources INT,
    PlayerMoney INT,
    Tech_level INT CHECK (Tech_level <= 100),
    Hull_level INT CHECK (Hull_level <= 100),
    Weapon_tech INT CHECK (Weapon_tech <= 100),
    Mining_level INT CHECK (Mining_level <= 100),
    Factory_level INT CHECK (Factory_level <= 100),
    CartelID INT FOREIGN KEY REFERENCES Cartel(CartelID)
);

-- 5. Planet Table
CREATE TABLE Planet (
    PlanetID INT PRIMARY KEY,
    PlanetName VARCHAR(255) NOT NULL,
    PlayerID INT FOREIGN KEY REFERENCES Player(PlayerID)
);

-- 6. PrivateMessageSystem Table
CREATE TABLE PrivateMessageSystem (
    MessageID INT PRIMARY KEY,
    SenderID INT,
    ReceiverID INT,
    PM_Message VARCHAR(255) NOT NULL,
    FOREIGN KEY (SenderID) REFERENCES Player(PlayerID),
    FOREIGN KEY (ReceiverID) REFERENCES Player(PlayerID)
);

-- 7. ChatSystem Table
CREATE TABLE ChatSystem (
    ChatID INT PRIMARY KEY,
    CartelID INT,
    Chat_Message VARCHAR(255) NOT NULL,
    Chat_Date DATETIME,
    FOREIGN KEY (CartelID) REFERENCES Cartel(CartelID)
);

-- 8. Overseen_by Table
CREATE TABLE Overseen_by (
    AdminID INT,
    PlayerID INT,
    PRIMARY KEY (AdminID, CartelID),
    FOREIGN KEY (AdminID) REFERENCES Administrator(AdminID),
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID)
);

-- 9. Factory Table
CREATE TABLE Factory (
    FactoryID INT PRIMARY KEY,
    Baubles INT,
    Resources INT,
    PlanetID INT FOREIGN KEY REFERENCES Planet(PlanetID)
);

-- 10. Mine Table
CREATE TABLE Mine (
    MineID INT PRIMARY KEY,
    Resources INT,
    PlanetID INT FOREIGN KEY REFERENCES Planet(PlanetID)
);

-- 11. Shipyard Table
CREATE TABLE Shipyard (
    ShipyardID INT PRIMARY KEY,
    Ships INT,
    Resources INT,
    PlanetID INT FOREIGN KEY REFERENCES Planet(PlanetID)
);

-- 12. ResearchCenter Table
CREATE TABLE ResearchCenter (
    ResearchCenterID INT PRIMARY KEY,
    ResearchType VARCHAR(255), -- Physics, energy, etc but it can be null when the center just got built
    Resources INT,
    PlanetID INT FOREIGN KEY REFERENCES Planet(PlanetID)
);

-- 13. Fleet Table
CREATE TABLE Fleet (
    FleetID INT PRIMARY KEY,
    PlayerID INT,
    FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID)
);

-- 14. FleetOrders Table
CREATE TABLE FleetOrders (
    FleetID INT,
    OrderID INT,
    PRIMARY KEY (FleetID, OrderID),
    FOREIGN KEY (FleetID) REFERENCES Fleet(FleetID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

-- 15. Ship Table
CREATE TABLE Ship (
    ShipID INT PRIMARY KEY,
    FleetID INT FOREIGN KEY REFERENCES Fleet(FleetID),
    PlayerID INT FOREIGN KEY REFERENCES Player(PlayerID),
    Weapons INT,
    Speed INT,
    ShipType VARCHAR(255) NOT NULL,
    Capacity INT,
    Resources INT
);






-- Constraints Adding

-- 1. Administrator Table
ALTER TABLE Administrator
ADD CONSTRAINT PK_Administrator PRIMARY KEY (AdminID);

-- 2. Cartel Table
ALTER TABLE Cartel
ADD CONSTRAINT PK_Cartel PRIMARY KEY (CartelID);

-- 3. Orders Table
ALTER TABLE Orders
ADD CONSTRAINT PK_Orders PRIMARY KEY (OrderID),
ADD CONSTRAINT FK_Orders_Fleet FOREIGN KEY (FleetID) REFERENCES Fleet(FleetID) ON DELETE CASCADE,
ADD CONSTRAINT FK_Orders_Order FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE;

-- 4. Player Table
ALTER TABLE Player
ADD CONSTRAINT PK_Player PRIMARY KEY (PlayerID),
ADD CONSTRAINT FK_Player_Cartel FOREIGN KEY (CartelID) REFERENCES Cartel(CartelID) ON DELETE CASCADE;

-- 5. Planet Table
ALTER TABLE Planet
ADD CONSTRAINT PK_Planet PRIMARY KEY (PlanetID),
ADD CONSTRAINT FK_Planet_Player FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID) ON DELETE CASCADE;

-- 6. PrivateMessageSystem Table
ALTER TABLE PrivateMessageSystem
ADD CONSTRAINT PK_PrivateMessageSystem PRIMARY KEY (MessageID),
ADD CONSTRAINT FK_PMS_Sender FOREIGN KEY (SenderID) REFERENCES Player(PlayerID) ON DELETE CASCADE,
ADD CONSTRAINT FK_PMS_Receiver FOREIGN KEY (ReceiverID) REFERENCES Player(PlayerID) ON DELETE CASCADE;

-- 7. ChatSystem Table
ALTER TABLE ChatSystem
ADD CONSTRAINT PK_ChatSystem PRIMARY KEY (ChatID),
ADD CONSTRAINT FK_ChatSystem_Cartel FOREIGN KEY (CartelID) REFERENCES Cartel(CartelID) ON DELETE CASCADE;

-- 8. Overseen_by Table
ALTER TABLE Overseen_by
ADD CONSTRAINT PK_Overseen_by PRIMARY KEY (AdminID, PlayerID),
ADD CONSTRAINT FK_Overseen_by_Admin FOREIGN KEY (AdminID) REFERENCES Administrator(AdminID) ON DELETE CASCADE,
ADD CONSTRAINT FK_Overseen_by_Player FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID) ON DELETE CASCADE;

-- 9. Factory Table
ALTER TABLE Factory
ADD CONSTRAINT PK_Factory PRIMARY KEY (FactoryID),
ADD CONSTRAINT FK_Factory_Planet FOREIGN KEY (PlanetID) REFERENCES Planet(PlanetID) ON DELETE CASCADE;

-- 10. Mine Table
ALTER TABLE Mine
ADD CONSTRAINT PK_Mine PRIMARY KEY (MineID),
ADD CONSTRAINT FK_Mine_Planet FOREIGN KEY (PlanetID) REFERENCES Planet(PlanetID) ON DELETE CASCADE;

-- 11. Shipyard Table
ALTER TABLE Shipyard
ADD CONSTRAINT PK_Shipyard PRIMARY KEY (ShipyardID),
ADD CONSTRAINT FK_Shipyard_Planet FOREIGN KEY (PlanetID) REFERENCES Planet(PlanetID) ON DELETE CASCADE;

-- 12. ResearchCenter Table
ALTER TABLE ResearchCenter
ADD CONSTRAINT PK_ResearchCenter PRIMARY KEY (ResearchCenterID),
ADD CONSTRAINT FK_ResearchCenter_Planet FOREIGN KEY (PlanetID) REFERENCES Planet(PlanetID) ON DELETE CASCADE;

-- 13. Fleet Table
ALTER TABLE Fleet
ADD CONSTRAINT PK_Fleet PRIMARY KEY (FleetID),
ADD CONSTRAINT FK_Fleet_Player FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID) ON DELETE CASCADE;

-- 14. FleetOrders Table
ALTER TABLE FleetOrders
ADD CONSTRAINT PK_FleetOrders PRIMARY KEY (FleetID, OrderID),
ADD CONSTRAINT FK_FleetOrders_Fleet FOREIGN KEY (FleetID) REFERENCES Fleet(FleetID) ON DELETE CASCADE,
ADD CONSTRAINT FK_FleetOrders_Order FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE;

-- 15. Ship Table
ALTER TABLE Ship
ADD CONSTRAINT PK_Ship PRIMARY KEY (ShipID),
ADD CONSTRAINT FK_Ship_Fleet FOREIGN KEY (FleetID) REFERENCES Fleet(FleetID) ON DELETE CASCADE,
ADD CONSTRAINT FK_Ship_Player FOREIGN KEY (PlayerID) REFERENCES Player(PlayerID) ON DELETE CASCADE;



