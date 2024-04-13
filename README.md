*READ THIS TO UNDERSTAND HOW TO USE THE PROGRAM*

FLOW OF THE PROGRAM
The application is a Command Line Interface made in python. You can run the program by running ./main.py in the terminal.

LOGIN/REGISTER INTERFACE

Login or Register: Upon starting the program, the user is prompted to either login or register as a member, trainer, or administrator.
If logging in:
    (1) Members input their email and password.
        (i) Example member login to test: email: sahith.nulu@email.com, password: password3
    (2) Trainers input their trainer ID.
        (i) Example trainer login to test: trainerID: 1
    (3) Administrators input their staff ID.
        (i) Example admin login to test: StaffID: 1
If registering:
    (1) Users provide necessary details like name, email, password, fitness goals, and health metrics.
    (2) Example information: 
        (i) Name: saad
        (ii) email: saad@email.com
        (iii) password: passwordsaad
        (iv) fitness goals: gain muscle
        (v) health metrics: Excellent

-----------------------------------------------------------------------------------------------------------------

MEMBER INTERFACE

After successful login or registration, members are presented with a dashboard where they can:
    (1) Update profile information
    (2) View profile information.
    (3) Manage schedules:
        (i) NOTE: While entering information for date, write it in the form YYYY-MM-DD (Eg. 2024-01-01)
        (ii) NOTE: While entering information for time, write it in the form HH::MM (Eg. 19:00)
        (iii) Schedule personal training sessions.
        (iv) Schedule group fitness classes.
        (v) Reschedule or cancel sessions.
    (4) View upcoming schedules.
    (5) BONUS: Members can view recommended classes based on availability.

-----------------------------------------------------------------------------------------------------------------

TRAINER INTERFACE

Trainers have access to functionalities to:
    (1) Update availability.
        (i) NOTE: While entering information for availability, write it in the form HH:MM - HH:MM (Eg. 10:00 - 15:00)
    (2) View member profiles.
        (i) Search for a member based on the name
    (3) View trainer schedules.

-----------------------------------------------------------------------------------------------------------------

ADMIN INTERFACE

Administrators can:
    (1) Manage room bookings:
        (i) Update room information.
        (ii)Update room for fitness classes.
        (iii) Delete reservations for fitness classes.
    (1) View room bookings.
    (2) View room information.
    (3) Update equipment status.
    (4) Monitor equipment status.
    (5) Manage group fitness class schedules:
        (i) Add, update, or cancel group fitness classes.
        (ii) Update training sessions.
        (iii) Cancel training sessions.
    (6) View all classes.
    (7) Handle billing: Update payment status for members.

-----------------------------------------------------------------------------------------------------------------

## Bonus Features
- Discuss any additional features that were implemented to enhance the system.
- Explain the innovative aspects and the effort involved.


