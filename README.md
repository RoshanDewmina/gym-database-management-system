# README - Program Usage Instructions

## IMPORTANT

### INSTRUCTIONS TO RUN THE PROGRAM
1. Download the code and the necessary SQL files to test.
2. Install `psycopg2` and `tabulate`:f
    ```bash
    pip3 install psycopg2-binary
    pip3 install tabulate
    ```
3. **ENSURE MODULES ARE INSTALLED IN THE SAME VERSION AS THE PYTHON PROGRAM YOU ARE USING** (If using Python 3, use `pip3`).
4. Update the database information to match with your database settings.
5. Run the program using:
    - **FOR MAC/Linux**: `bash python3 main.py`
    - **FOR Windows**: `bash python main.py`
6. You can use the example information given in this README to log in or make any changes.

### FLOW OF THE PROGRAM
The application is a Command Line Interface made in Python.

## DATABASE SETUP
To setup the database, run the `dataDDL.sql` file from the SQL folder in postgreSQL
After tables are created, run the `dataDML.sql` file from the SQL folder in postgreSQL

**IMPORTANT** 
    The `dataDML.sql` is the file that should be used to run and test the program
    If you would like to test the efficiency of the database, compile and run the `generateRandomData.c` function

        To compile: `bash gcc -o generateData generateRandomData.c`
        To run:     `bash ./generateData`


#### LOGIN/REGISTER INTERFACE
Upon starting the program, the user is prompted to either login or register as a member, trainer, or administrator.

**If logging in:**
- Members input their email and password.
    - Example member login to test: 
        - email: `sahith.nulu@email.com`
        - password: `password3`
- Trainers input their trainer ID.
    - Example trainer login to test: 
        - trainerID: `1`
- Administrators input their staff ID.
    - Example admin login to test: 
        - StaffID: `1`

**If registering:**
- Users provide necessary details like name, email, password, fitness goals, and health metrics.
    - Example information: 
        - Name: `saad`
        - Email: `saad@email.com`
        - Password: `passwordsaad`
        - Fitness goals: `gain muscle`
        - Health metrics: `25`

**Note** When selecting to update/delete elements using ID's, ensure those ID's exist (error handelling is implemented however)

### MEMBER INTERFACE
After successful login or registration, members are presented with a dashboard where they can:
1. Update profile information.
2. View profile information.
3. Manage schedules:
    - **NOTE:** While entering information for date, write it in the form `YYYY-MM-DD` (E.g., `2024-01-01`).
    - **NOTE:** While entering information for time, write it in the form `HH:MM` (E.g., `19:00`).
    - Schedule personal training sessions.
    - Schedule group fitness classes.
    - Reschedule or cancel sessions.
4. View upcoming schedules.
5. **BONUS:** Members can view recommended classes based on availability.

### TRAINER INTERFACE
Trainers have access to functionalities to:
1. Update availability.
    - **NOTE:** While entering information for availability, write it in the form `HH:MM - HH:MM` (E.g., `10:00 - 15:00`).
2. View member profiles.
    - Search for a member based on the name.
3. View trainer schedules.

### ADMIN INTERFACE
Administrators can:
1. Manage room bookings:
    - Update room information.
    - Update room for fitness classes.
    - Delete reservations for fitness classes.
2. View room bookings.
3. View room information.
4. Update equipment status.
5. Monitor equipment status.
6. Manage group fitness class schedules:
    - Add, update, or cancel group fitness classes.
    - Update training sessions.
    - Cancel training sessions.
7. View all classes.
8. Handle billing:
    - Update payment status for members.
