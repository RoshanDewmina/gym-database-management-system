#<----------------- DATABASE CONNECTION FUNCTIONS ----------------->

import psycopg2
from psycopg2 import Error
import random
from tabulate import tabulate

# Database connection parameters
DB_NAME = "#YOUR DATABASE NAME#"    
DB_USER = "#YOUR DATABASE USER#"
DB_PASSWORD = "#YOUR PASSWORD TO CONNECT TO DATABASE#"
DB_HOST = "localhost"
DB_PORT = "5432"

def connect():
    try:
        connection = psycopg2.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )
        return connection
    except Error as e:
        print("Error while connecting to PostgreSQL:", e)

#<----------------- MEMBER FUNCTIONS ----------------->

def displayMemberDashboard(name, memberID):
    menu = [
        "1. Update profile information",
        "2. View Profile Information",
        "3. Manage Schedules",
        "4. View Upcoming Schedules",
        "5. RECOMMENDED CLASSES!!!",
        "6. Logout"
    ]
    print(f"\nWelcome Member {name}!")
    print("\nWhat would you like to do?")
    print("\n".join(menu))
    choice = input("\nEnter your choice: ")
    if choice == "1":
        updateProfile(name, memberID)
    elif choice == "2":
        viewProfile(name, memberID)
    elif choice == "3":
        manageSchedules(name, memberID)
    elif choice == "4":
        viewSchedules(name, memberID)
    elif choice == "5":
        viewRecommendedClasses(name, memberID)
    elif choice == "6":
        main()
    else:
        print("\nInvalid choice. Please try again.\n")
        displayMemberDashboard(name, memberID)

def viewRecommendedClasses(name, memberID):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT ClassID FROM Fitness_Class;")
    possibleID = cursor.fetchall()
    randomIndex = random.randint(0, len(possibleID) - 1)
    if possibleID:
        cursor.execute("SELECT ClassName, Schedule, RoomID, TrainerID FROM Fitness_Class WHERE ClassID = %s;", (possibleID[randomIndex][0],))
        recommended = cursor.fetchone()
        print("Recommended class:")
        headers = ["Class Name", "Schedule", "Room ID", "Trainer ID"]
        print(tabulate([headers, recommended], headers="firstrow", tablefmt="grid"))
    else:
        print("No recommended classes.")
    cursor.close()
    connection.close()
    displayMemberDashboard(name, memberID)

def viewSchedules(name, memberID):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT SessionID, Date, Time, TrainerID FROM Training_Session WHERE MemberID = %s;", (memberID,))
    sessions = cursor.fetchall()
    if sessions:
        print("\nUpcoming Training sessions:")
        headers = ["Session ID", "Date", "Time", "Trainer ID"]
        print(tabulate([headers] + sessions, headers="firstrow", tablefmt="grid"))
    else:
        print("No upcoming Training sessions.")
    
    cursor.execute("""SELECT FC.ClassID, FC.ClassName, FC.Schedule, FC.RoomID, FC.TrainerID 
                      FROM Fitness_Class FC 
                      JOIN Registers R ON FC.ClassID = R.ClassID 
                      WHERE R.MemberID = %s;""", (memberID,))
    classes = cursor.fetchall()
    if classes:
        print("\nUpcoming Group Fitness Classes:")
        headers = ["Class ID", "Class Name", "Schedule", "Room ID", "Trainer ID"]
        print(tabulate([headers] + classes, headers="firstrow", tablefmt="grid"))
    else:
        print("No upcoming Group Fitness Classes.")
    cursor.close()
    connection.close()
    displayMemberDashboard(name, memberID)

def manageSchedules(name, memberID):
    menu = [
        "1. Schedule personal training session",
        "2. Schedule group fitness class",
        "3. Reschedule personal training session",
        "4. Cancel personal training session",
        "5. Cancel group fitness class"
    ]
    print("\nWhat would you like to do?")
    print("\n".join(menu))
    choice = input("Enter your choice: ")
    connection = connect()
    cursor = connection.cursor()
    if choice == "1":
        print("\nBelow are the available training sessions:")
        cursor.execute("""
            SELECT t.TrainerID, t.Name, t.Specialization, t.AvailableTimes
            FROM Trainer t
            LEFT JOIN Training_Session ts ON t.TrainerID = ts.TrainerID
            WHERE ts.TrainerID IS NULL;
        """)
        sessions = cursor.fetchall()
        if sessions:
            for session in sessions:
                print(session)
            trainerID = input("Enter ID of the trainer you want to schedule a session with: ")
            date = input("Enter date of session: ")
            time = input("Enter time of session: ")
            cursor.execute("INSERT INTO Training_Session (Date, Time, MemberID, TrainerID) VALUES (%s, %s, %s, %s);", (date, time, memberID, trainerID))
            connection.commit()
            print("Session scheduled successfully.")
        else:
            print("No trainers available.")
    elif choice == "2":
        groupName = input("Enter name of group (A/B/C): ")
        classID = input("Enter ID of class you want to register for: ")
        cursor.execute("SELECT ClassName, Schedule, RoomID, TrainerID FROM Fitness_Class WHERE ClassID = %s;", (classID,))
        fitnessClass = cursor.fetchone()
        if fitnessClass:
            headers = ["Class Name", "Schedule", "Room ID", "Trainer ID"]
            print(tabulate([headers, fitnessClass], headers="firstrow", tablefmt="grid"))
            cursor.execute("INSERT INTO Registers (MemberID, ClassID, GroupName) VALUES (%s, %s, %s);", (memberID, classID, groupName))
            connection.commit()
            print("Registration successful.")
    elif choice == "3":
        sessionID = input("Enter ID of session to be rescheduled: ")
        newDate = input("Enter new date: ")
        newTime = input("Enter new time: ")
        cursor.execute("UPDATE Training_Session SET Date = %s, Time = %s WHERE SessionID = %s;", (newDate, newTime, sessionID))
        connection.commit()
        print("Session rescheduled successfully.")
    elif choice == "4":
        sessionID = input("Enter ID of training session to be cancelled: ")
        cursor.execute("DELETE FROM Training_Session WHERE SessionID = %s;", (sessionID,))
        connection.commit()
        print("Session cancelled successfully.")
    elif choice == "5":
        classID = input("Enter ID of group fitness class to be cancelled: ")
        cursor.execute("DELETE FROM Registers WHERE ClassID = %s AND MemberID = %s;", (classID, memberID))
        connection.commit()
        print("Class registration cancelled successfully.")
    else:
        print("Invalid choice. Please try again.")
    cursor.close()
    connection.close()
    displayMemberDashboard(name, memberID)

def updateProfile(name, memberID):
    menu = [
        "1. Update name",
        "2. Update password",
        "3. Update email",
        "4. Update Goals",
        "5. Update Health Metrics"
    ]
    print("\nUpdate profile information:")
    print("\n".join(menu))
    choice = input("Enter your choice: ")
    connection = connect()
    cursor = connection.cursor()
    if choice == "1":
        newName = input("Enter updated name: ")
        cursor.execute("UPDATE Member SET Name = %s WHERE MemberID = %s;", (newName, memberID))
        connection.commit()
        print("Name updated successfully.")
    elif choice == "2":
        newPassword = input("Enter updated password: ")
        cursor.execute("UPDATE Member SET Password = %s WHERE MemberID = %s;", (newPassword, memberID))
        connection.commit()
        print("Password updated successfully.")
    elif choice == "3":
        newEmail = input("Enter updated email: ")
        cursor.execute("UPDATE Member SET Email = %s WHERE MemberID = %s;", (newEmail, memberID))
        connection.commit()
        print("Email updated successfully.")
    elif choice == "4":
        newGoals = input("Enter updated goals: ")
        cursor.execute("UPDATE Member SET FitnessGoal = %s WHERE MemberID = %s;", (newGoals, memberID))
        connection.commit()
        print("Goal updated successfully.")
    elif choice == "5":
        newMetrics = input("Enter updated health metrics: ")
        cursor.execute("UPDATE Member SET HealthMetrics = %s WHERE MemberID = %s;", (newMetrics, memberID))
        connection.commit()
        print("Health metrics updated successfully.")
    else:
        print("\nInvalid choice. Please try again.")
    cursor.close()
    connection.close()
    displayMemberDashboard(name, memberID)

def viewProfile(name, memberID):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT Name, Email, FitnessGoal, HealthMetrics FROM Member WHERE MemberID = %s;", (memberID,))
    member = cursor.fetchone()
    cursor.close()
    connection.close()
    if member:
        headers = ["Name", "Email", "Fitness Goals", "Health Metrics"]
        print(tabulate([headers, member], headers="firstrow", tablefmt="grid"))
    else:
        print("\nNo profile information found.")
    displayMemberDashboard(name, memberID)

#<----------------- TRAINER FUNCTIONS ----------------->

def displayTrainerDashboard(name, trainerID):
    menu = [
        "1. Update availability",
        "2. View member profiles",
        "3. View Trainer Schedules",
        "4. Logout"
    ]
    print(f"\nWelcome Trainer {name}!")
    print("\nWhat would you like to do?")
    print("\n".join(menu))
    choice = input("\nEnter your choice: ")
    if choice == "1":
        updateAvailability(name, trainerID)
    elif choice == "2":
        viewMemberProfiles(name, trainerID)
    elif choice == "3":
        viewTrainerSchedules(name, trainerID)
    elif choice == "4":
        main()
    else:
        print("\nInvalid choice. Please try again.")
        displayTrainerDashboard(name, trainerID)

def viewTrainerSchedules(name, trainerID):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT SessionID, Date, Time, MemberID FROM Training_Session WHERE TrainerID = %s;", (trainerID,))
    sessions = cursor.fetchall()
    if sessions:
        print("Upcoming Training sessions:")
        headers = ["Session ID", "Date", "Time", "Member ID"]
        print(tabulate([headers] + sessions, headers="firstrow", tablefmt="grid"))
    else:
        print("No upcoming Training sessions.")
    cursor.execute("SELECT ClassID, ClassName, Schedule, RoomID FROM Fitness_Class WHERE TrainerID = %s;", (trainerID,))
    classes = cursor.fetchall()
    if classes:
        print("Upcoming Group Fitness Classes:")
        headers = ["Class ID", "Class Name", "Schedule", "Room ID"]
        print(tabulate([headers] + classes, headers="firstrow", tablefmt="grid"))
    else:
        print("No upcoming Group Fitness Classes.")
    cursor.close()
    connection.close()
    displayTrainerDashboard(name, trainerID)

def updateAvailability(name, trainerID):
    availability = input("Enter your availability: ")
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("UPDATE Trainer SET AvailableTimes = %s WHERE TrainerID = %s;", (availability, trainerID))
    connection.commit()
    print("Availability updated successfully.")
    cursor.close()
    connection.close()
    displayTrainerDashboard(name, trainerID)

def viewMemberProfiles(name, trainerID):
    memberName = input("Enter name of member to be searched: ")
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT MemberID, Name, Email, FitnessGoal, HealthMetrics, PaymentStatus FROM Member where Name = %s;", (memberName,))
    members = cursor.fetchall()
    if members:
        headers = ["Member ID", "Name", "Email", "Fitness Goal", "Health Metrics", "Payment Status"]
        print(tabulate([headers] + members, headers="firstrow", tablefmt="grid"))
    else:
        print("Member not found.")
    cursor.close()
    connection.close()
    displayTrainerDashboard(name, trainerID)

#<----------------- ADMIN FUNCTIONS ----------------->

def displayAdminDashboard(name, staffID):
    menu = [
        "1. Manage room bookings",
        "2. View room bookings",
        "3. View room information",
        "4. Update equipment status",
        "5. Monitor equipment status",
        "6. Manage group fitness class schedules",
        "7. View all classes",
        "8. Billing",
        "9. Logout"
    ]
    print(f"\nWelcome Admin {name}!")
    print("\nWhat would you like to do?")
    print("\n".join(menu))
    choice = input("\nEnter your choice: ")
    if choice == "1":
        manageRoomBookings(name, staffID)
    elif choice == "2":
        viewRoomBookings(name, staffID)
    elif choice == "3":
        viewRoomInformation(name, staffID)
    elif choice == "4":
        manageEquipment(name, staffID)
    elif choice == "5":
        monitorEquipment(name, staffID)
    elif choice == "6":
        manageClassSchedules(name, staffID)
    elif choice == "7":
        viewAllClasses(name, staffID)
    elif choice == "8":
        billing(name, staffID)
    elif choice == "9":
        main()
    else:
        print("\nInvalid choice. Please try again.")
        displayAdminDashboard(name, staffID)

def viewAllClasses(name, staffID):
    print("\nWhich class would you like to view?")
    menu = [
        "1. Group Fitness Classes",
        "2. Personal Training Sessions"
    ]
    print("\n".join(menu))
    choice = input("\nEnter your choice: ")
    connection = connect()
    cursor = connection.cursor()
    if choice == "1":
        cursor.execute("SELECT * FROM Fitness_Class;")
        classes = cursor.fetchall()
        headers = ["Class ID", "Class Name", "Schedule", "Room ID", "Trainer ID"]
        print(tabulate([headers] + classes, headers="firstrow", tablefmt="grid"))
    elif choice == "2":
        cursor.execute("SELECT * FROM Training_Session;")
        sessions = cursor.fetchall()
        headers = ["Session ID", "Date", "Time", "Member ID", "Trainer ID"]
        print(tabulate([headers] + sessions, headers="firstrow", tablefmt="grid"))
    else:
        print("\nInvalid choice. Please try again.")
        viewAllClasses(name, staffID)
    cursor.close()
    connection.close()
    displayAdminDashboard(name, staffID)

def viewRoomBookings(name, staffID):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT ClassName, RoomID FROM Fitness_Class;")
    bookings = cursor.fetchall()
    if bookings:
        headers = ["Class Name", "Room ID"]
        print("Room bookings:")
        print(tabulate([headers] + bookings, headers="firstrow", tablefmt="grid"))
    else:
        print("No room bookings found.")
    cursor.close()
    connection.close()
    displayAdminDashboard(name, staffID)

def viewRoomInformation(name, staffID):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT RoomID, RoomName, Capacity, StaffID FROM Room;")
    rooms = cursor.fetchall()
    if rooms:
        headers = ["Room ID", "Room Name", "Capacity", "Staff ID"]
        print("Room information:")
        print(tabulate([headers] + rooms, headers="firstrow", tablefmt="grid"))
    else:
        print("No room information found.")
    cursor.close()
    connection.close()
    displayAdminDashboard(name, staffID)

def manageRoomBookings(name, staffID):
    menu = [
        "1. Update room information",
        "2. Update room for fitness classes",
        "3. Delete reservation for fitness class"
    ]
    print("\nWhat would you like to do?")
    print("\n".join(menu))
    choice = input("\nEnter your choice: ")
    connection = connect()
    cursor = connection.cursor()
    if choice == "1":
        roomID = input("Enter id of room to be updated: ")
        roomName = input("Enter updated name: ")
        cursor.execute("UPDATE Room SET RoomName = %s WHERE RoomID = %s;", (roomName, roomID))
        connection.commit()
        print("Room updated successfully.")
    elif choice == "2":
        classID = input("Enter id of fitness class to be updated: ")
        roomID = input("Enter new room ID: ")
        cursor.execute("UPDATE Fitness_Class SET RoomID = %s WHERE ClassID = %s;", (roomID, classID))
        connection.commit()
        print("Room updated successfully.")
    elif choice == "3":
        classID = input("Enter id of fitness class to be deleted: ")
        cursor.execute("DELETE FROM Fitness_Class WHERE ClassID = %s;", (classID,))
        connection.commit()
        print("Reservation for fitness class deleted successfully.")
    else:
        print("Invalid choice. Please try again.")
    cursor.close()
    connection.close()
    displayAdminDashboard(name, staffID)

def manageEquipment(name, staffID):
    connection = connect()
    cursor = connection.cursor()
    equipmentID = input("Enter id of equipment to be updated: ")
    status = input("Enter updated status: ")
    cursor.execute("UPDATE Equipment SET Status = %s WHERE EquipmentID = %s;", (status, equipmentID))
    connection.commit()
    print("Equipment status updated successfully.")
    cursor.close()
    connection.close()
    displayAdminDashboard(name, staffID)

def monitorEquipment(name, staffID):
    connection = connect()
    cursor = connection.cursor()
    equipmentID = input("Enter id of equipment to be monitored: ")
    cursor.execute("SELECT Status FROM Equipment WHERE EquipmentID = %s;", (equipmentID,))
    status = cursor.fetchone()
    if status:
        print(f"The status of equipment with id {equipmentID} is {status[0]}")
    else:
        print("Equipment not found.")
    cursor.close()
    connection.close()
    displayAdminDashboard(name, staffID)

def manageClassSchedules(name, staffID):
    menu = [
        "1. Add new group fitness class",
        "2. Update group fitness class",
        "3. Cancel group fitness class",
        "4. Update training session",
        "5. Cancel training session"
    ]
    print("\nWhat would you like to do?")
    print("\n".join(menu))
    choice = input("\nEnter your choice: ")
    connection = connect()
    cursor = connection.cursor()
    if choice == "1":
        className = input("Enter name of class: ")
        schedule = input("Enter schedule of class: ")
        roomID = input("Enter room ID for class: ")
        trainerID = input("Enter trainer ID for class: ")
        cursor.execute("INSERT INTO Fitness_Class (ClassName, Schedule, RoomID, TrainerID) VALUES (%s, %s, %s, %s);", (className, schedule, roomID, trainerID))
        connection.commit()
        print("Class added successfully.")
    elif choice == "2":
        classID = input("Enter id of class to be updated: ")
        newSchedule = input("Enter updated class schedule: ")
        cursor.execute("UPDATE Fitness_Class SET Schedule = %s WHERE ClassID = %s;", (newSchedule, classID))
        connection.commit()
        print("Class schedule updated successfully.")
    elif choice == "3":
        classID = input("Enter id of class to be deleted: ")
        cursor.execute("DELETE FROM Fi_Me WHERE ClassID = %s;", (classID,))
        cursor.execute("DELETE FROM Registers WHERE ClassID = %s;", (classID,))
        cursor.execute("DELETE FROM Fitness_Class WHERE ClassID = %s;", (classID,))
        connection.commit()
        print("Class deleted successfully.")
    elif choice == "4":
        sessionID = input("Enter id of session to be updated: ")
        newDate = input("Enter updated date: ")
        newTime = input("Enter updated time: ")
        cursor.execute("UPDATE Training_Session SET Date = %s, Time = %s WHERE SessionID = %s;", (newDate, newTime, sessionID))
        connection.commit()
        print("Session updated successfully.")
    elif choice == "5":
        sessionID = input("Enter id of session to be cancelled: ")
        cursor.execute("DELETE FROM Training_Session WHERE SessionID = %s;", (sessionID,))
        connection.commit()
        print("Session cancelled successfully.")
    else:
        print("Invalid choice. Please try again.")
    cursor.close()
    connection.close()
    displayAdminDashboard(name, staffID)

def billing(name, staffID):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT MemberID, Name, PaymentStatus FROM Member WHERE PaymentStatus IS NOT NULL;")
    members = cursor.fetchall()
    print("Current Billing Status:")
    headers = ["MemberID", "Name", "Payment Status"]
    print(tabulate([headers] + members, headers="firstrow", tablefmt="grid"))
    while True:
        update = input("Do you want to update a member's billing status? (yes/no): ")
        if update.lower() == 'yes':
            member_id = input("Enter the MemberID to update: ")
            new_status = input("Enter the new Payment Status (Paid/Pending/Overdue): ")
            cursor.execute("UPDATE Member SET PaymentStatus = %s WHERE MemberID = %s;", (new_status, member_id))
            connection.commit()
            print(f"Payment status updated for MemberID {member_id}.")
        elif update.lower() == 'no':
            break
        else:
            print("Invalid input, please type 'yes' or 'no'.")
    cursor.close()
    connection.close()
    displayAdminDashboard(name, staffID)

#<----------------- REGISTER FUNCTIONS ----------------->

def register():
    name = input("Enter Name: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    goals = input("Enter fitness goals: ")
    healthMetrics = input("Enter health metrics (BMI): ")
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Member (Name, Email, Password, FitnessGoal, HealthMetrics, PaymentStatus) VALUES (%s, %s, %s, %s, %s, 'Pending');", (name, email, password, goals, healthMetrics))
    cursor.execute("SELECT MemberID FROM Member WHERE Email = %s;", (email,))
    memberID = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    if memberID:
        print("\nUser registered successfully.")
        displayMemberDashboard(name, memberID[0])
    else:
        print("\nRegistration failed. Please try again.")
        register()

#<----------------- LOGIN FUNCTIONS ----------------->

def login():
    menu = [
        "1. Member",
        "2. Trainer",
        "3. Admin"
    ]
    print("\nWhat would you like to login as?")
    print("\n".join(menu))
    choice = input("\nEnter your choice: ")
    if choice == "1":
        Memberlogin()
    elif choice == "2":
        Trainerlogin()
    elif choice == "3":
        Adminlogin()
    else:
        print("\nInvalid choice. Please try again.")
        login()

def Memberlogin():
    email = input("Enter email: ")
    password = input("Enter password: ")
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT MemberID, Name FROM Member WHERE Email = %s AND Password = %s;", (email, password))
    member = cursor.fetchone()
    cursor.close()
    connection.close()
    if member:
        displayMemberDashboard(member[1], member[0])
    else:
        print("Invalid email or password. Please try again.")
        Memberlogin()

def Trainerlogin():
    trainerID = input("Enter trainer ID: ")
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT TrainerID, Name FROM Trainer WHERE TrainerID = %s;", (trainerID,))
    trainer = cursor.fetchone()
    cursor.close()
    connection.close()
    if trainer:
        displayTrainerDashboard(trainer[1], trainer[0])
    else:
        print("Invalid trainer ID. Please try again.")
        Trainerlogin()

def Adminlogin():
    staffID = input("Enter staff ID: ")
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("SELECT StaffID, Name FROM Administrative_Staff WHERE StaffID = %s;", (staffID,))
    admin = cursor.fetchone()
    cursor.close()
    connection.close()
    if admin:
        displayAdminDashboard(admin[1], admin[0])
    else:
        print("Invalid admin ID. Please try again.")
        Adminlogin()

#<----------------- MAIN FUNCTION ----------------->

def main():
    print("Welcome to Iron Pulse Gym Management System!\n")
    menu = [
        "1. Login",
        "2. Register",
        "3. Exit"
    ]
    print("\nWhat would you like to do?")
    print("\n".join(menu))
    choice = input("\nEnter your choice: ")
    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        print("Exiting the program.")
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()

#<----------------- APPLICATION STARTS HERE ----------------->

if __name__ == "__main__":
    main()
