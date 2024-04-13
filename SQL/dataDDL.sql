-- Table creation for 'Member'
CREATE TABLE Member (
    MemberID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    FitnessGoal TEXT,
    HealthMetrics TEXT,
    PaymentStatus TEXT
);

-- Table creation for 'Trainer'
CREATE TABLE Trainer (
    TrainerID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Specialization TEXT,
    AvailableTimes TEXT
);

-- Table creation for 'Training Session'
CREATE TABLE Training_Session (
    SessionID SERIAL PRIMARY KEY,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    MemberID INT REFERENCES Member(MemberID),
    TrainerID INT REFERENCES Trainer(TrainerID)
);

-- Table creation for 'Administrative Staff'
CREATE TABLE Administrative_Staff (
    StaffID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Role VARCHAR(255) NOT NULL,
    ContactInformation TEXT
);


-- Table creation for 'Room'
CREATE TABLE Room (
    RoomID SERIAL PRIMARY KEY,
    RoomName VARCHAR(255) NOT NULL,
    Capacity INT CHECK (Capacity > 0),
    StaffID INT,
    FOREIGN KEY (StaffID) REFERENCES Administrative_Staff(StaffID)
);

-- Table creation for 'Fitness Class'
CREATE TABLE Fitness_Class (
    ClassID SERIAL PRIMARY KEY,
    ClassName VARCHAR(255) NOT NULL,
    Schedule TIME NOT NULL,
    RoomID INT,
    TrainerID INT REFERENCES Trainer(TrainerID),
    FOREIGN KEY (RoomID) REFERENCES Room(RoomID)
);

-- Table creation for 'Registers' (to hold registrations of members to fitness classes)
CREATE TABLE Registers (
    MemberID INT,
    ClassID INT,
    GroupName VARCHAR(255),
    PRIMARY KEY (MemberID, ClassID),
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
    FOREIGN KEY (ClassID) REFERENCES Fitness_Class(ClassID)
);


-- Table creation for 'Equipment'
CREATE TABLE Equipment (
    EquipmentID SERIAL PRIMARY KEY,
    EquipmentName VARCHAR(255) NOT NULL,
    Status VARCHAR(50) CHECK (Status IN ('Available', 'In Use', 'Maintenance'))
);


-- Intermediary table for 'Fi_Me' (Fitness Class to Member)
CREATE TABLE Fi_Me (
    ClassID INT REFERENCES Fitness_Class(ClassID),
    MemberID INT REFERENCES Member(MemberID),
    PRIMARY KEY (ClassID, MemberID)
);

-- Intermediary table for 'Eq_As' (Equipment to Administrative Staff)
CREATE TABLE Eq_As (
    EquipmentID INT REFERENCES Equipment(EquipmentID),
    StaffID INT REFERENCES Administrative_Staff(StaffID),
    PRIMARY KEY (EquipmentID, StaffID)
);
