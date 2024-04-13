-- Insert data into Administrative_Staff
INSERT INTO Administrative_Staff (Name, Role, ContactInformation) VALUES
('John Doe', 'Manager', 'john.doe@email.com'),
('Jane Smith', 'Receptionist', 'jane.smith@email.com'),
('Alice Johnson', 'Trainer Coordinator', 'alice.johnson@email.com'),
('Bob Williams', 'Maintenance Supervisor', 'bob.williams@email.com'),
('Eva Brown', 'Customer Service', 'eva.brown@email.com');

-- Insert data into Equipment
INSERT INTO Equipment (EquipmentName, Status) VALUES
('Treadmill', 'Available'),
('Dumbbell Set', 'In Use'),
('Rowing Machine', 'Maintenance'),
('Exercise Bike', 'Available'),
('Yoga Mats', 'Available'),
('Barbell', 'Available'),
('Lat Pulldown Machine', 'Available'),
('Calf Raise Machine', 'Available'),
('Squat Rack', 'Available');

-- Insert data into Member
INSERT INTO Member (Name, Email, Password, FitnessGoal, HealthMetrics, PaymentStatus) VALUES
('Saad Humayun', 'saad.humayun@email.com', 'password1', 'Lose weight', '25', 'Active'),
('Roshan Dewmina', 'roshan.dewmina@email.com', 'password2', 'Increase stamina', '20', 'Active'),
('Sahith Nulu', 'sahith.nulu@email.com', 'password3', 'Muscle gain', '18', 'Active'),
('Chenul Gomes', 'chenul.gomes@email.com', 'password4', 'Flexibility', '28', 'Pending'),
('Emily Wallis', 'emily.wallis@email.com', 'password5', 'General fitness', '19', 'Overdue');

-- Insert data into Trainer
INSERT INTO Trainer (Name, Specialization, AvailableTimes) VALUES
('Rachel Green', 'Yoga', '08:00-10:00'),
('Ross Geller', 'Weightlifting', '10:00-12:00'),
('Monica Geller', 'Aerobics', '12:00-14:00'),
('Joey Tribbiani', 'Personal Training', '14:00-16:00'),
('Chandler Bing', 'Crossfit', '16:00-18:00'),
('Chris Bumstead', 'Bodybuilding', '12:00-15:00'),
('Jamal Browner', 'Powerlifting', '15:00-18:00'),
('Sara Saffari', 'Bodybuilding', '10:00-12:00');

-- Insert data into Room
INSERT INTO Room (RoomName, Capacity, StaffID) VALUES
('Yoga Studio', 15, (SELECT StaffID FROM Administrative_Staff WHERE Name = 'John Doe')),
('Weight Room', 20, (SELECT StaffID FROM Administrative_Staff WHERE Name = 'Jane Smith')),
('Cardio Room', 10, (SELECT StaffID FROM Administrative_Staff WHERE Name = 'Alice Johnson')),
('Spin Studio', 5, (SELECT StaffID FROM Administrative_Staff WHERE Name = 'Bob Williams')),
('General Gym', 25, (SELECT StaffID FROM Administrative_Staff WHERE Name = 'Eva Brown'));

-- Insert data into Fitness_Class
INSERT INTO Fitness_Class (ClassName, Schedule, RoomID, TrainerID) VALUES
('Morning Yoga', '09:00', (SELECT RoomID FROM Room WHERE RoomName = 'Yoga Studio'), (SELECT TrainerID FROM Trainer WHERE Name = 'Rachel Green')),
('Weight Training', '11:00', (SELECT RoomID FROM Room WHERE RoomName = 'Weight Room'), (SELECT TrainerID FROM Trainer WHERE Name = 'Ross Geller')),
('High Aerobics', '13:00', (SELECT RoomID FROM Room WHERE RoomName = 'Cardio Room'), (SELECT TrainerID FROM Trainer WHERE Name = 'Monica Geller')),
('Personal Coaching', '15:00', (SELECT RoomID FROM Room WHERE RoomName = 'Spin Studio'), (SELECT TrainerID FROM Trainer WHERE Name = 'Joey Tribbiani')),
('Evening Crossfit', '17:00', (SELECT RoomID FROM Room WHERE RoomName = 'General Gym'), (SELECT TrainerID FROM Trainer WHERE Name = 'Chandler Bing'));

-- Insert data into Training_Session
INSERT INTO Training_Session (Date, Time, MemberID, TrainerID) VALUES
('2024-04-01', '09:00', (SELECT MemberID FROM Member WHERE Name = 'Saad Humayun'), (SELECT TrainerID FROM Trainer WHERE Name = 'Rachel Green')),
('2024-04-02', '11:00', (SELECT MemberID FROM Member WHERE Name = 'Roshan Dewmina'), (SELECT TrainerID FROM Trainer WHERE Name = 'Ross Geller')),
('2024-04-03', '13:00', (SELECT MemberID FROM Member WHERE Name = 'Sahith Nulu'), (SELECT TrainerID FROM Trainer WHERE Name = 'Monica Geller')),
('2024-04-04', '15:00', (SELECT MemberID FROM Member WHERE Name = 'Chenul Gomes'), (SELECT TrainerID FROM Trainer WHERE Name = 'Joey Tribbiani')),
('2024-04-05', '17:00', (SELECT MemberID FROM Member WHERE Name = 'Emily Wallis'), (SELECT TrainerID FROM Trainer WHERE Name = 'Chandler Bing'));

-- Insert data into Registers
INSERT INTO Registers (MemberID, ClassID, GroupName) VALUES
((SELECT MemberID FROM Member WHERE Name = 'Saad Humayun'), (SELECT ClassID FROM Fitness_Class WHERE ClassName = 'Morning Yoga'), 'Group A'),
((SELECT MemberID FROM Member WHERE Name = 'Roshan Dewmina'), (SELECT ClassID FROM Fitness_Class WHERE ClassName = 'Weight Training'), 'Group B'),
((SELECT MemberID FROM Member WHERE Name = 'Sahith Nulu'), (SELECT ClassID FROM Fitness_Class WHERE ClassName = 'High Aerobics'), 'Group C'),
((SELECT MemberID FROM Member WHERE Name = 'Chenul Gomes'), (SELECT ClassID FROM Fitness_Class WHERE ClassName = 'Personal Coaching'), 'Group D'),
((SELECT MemberID FROM Member WHERE Name = 'Emily Wallis'), (SELECT ClassID FROM Fitness_Class WHERE ClassName = 'Evening Crossfit'), 'Group E');

-- Insert data into Fi_Me (Fitness Class to Member)
INSERT INTO Fi_Me (ClassID, MemberID) VALUES
((SELECT ClassID FROM Fitness_Class WHERE ClassName = 'Morning Yoga'), (SELECT MemberID FROM Member WHERE Name = 'Saad Humayun')),
((SELECT ClassID FROM Fitness_Class WHERE ClassName = 'Weight Training'), (SELECT MemberID FROM Member WHERE Name = 'Roshan Dewmina')),
((SELECT ClassID FROM Fitness_Class WHERE ClassName = 'High Aerobics'), (SELECT MemberID FROM Member WHERE Name = 'Sahith Nulu')),
((SELECT ClassID FROM Fitness_Class WHERE ClassName = 'Personal Coaching'), (SELECT MemberID FROM Member WHERE Name = 'Chenul Gomes')),
((SELECT ClassID FROM Fitness_Class WHERE ClassName = 'Evening Crossfit'), (SELECT MemberID FROM Member WHERE Name = 'Emily Wallis'));

-- Insert data into Eq_As (Equipment to Administrative Staff)
INSERT INTO Eq_As (EquipmentID, StaffID) VALUES
((SELECT EquipmentID FROM Equipment WHERE EquipmentName = 'Treadmill'), (SELECT StaffID FROM Administrative_Staff WHERE Name = 'John Doe')),
((SELECT EquipmentID FROM Equipment WHERE EquipmentName = 'Dumbbell Set'), (SELECT StaffID FROM Administrative_Staff WHERE Name = 'Jane Smith')),
((SELECT EquipmentID FROM Equipment WHERE EquipmentName = 'Rowing Machine'), (SELECT StaffID FROM Administrative_Staff WHERE Name = 'Alice Johnson')),
((SELECT EquipmentID FROM Equipment WHERE EquipmentName = 'Exercise Bike'), (SELECT StaffID FROM Administrative_Staff WHERE Name = 'Bob Williams')),
((SELECT EquipmentID FROM Equipment WHERE EquipmentName = 'Yoga Mats'), (SELECT StaffID FROM Administrative_Staff WHERE Name = 'Eva Brown'));
