
# Health and Fitness Club Management System - Project Report

## Table of Contents
- [Introduction](#introduction)
- [Conceptual Design](#conceptual-design)
- [Relational Schemas](#relational-schemas)
- [Data Definition Language (DDL)](#data-definition-language-ddl)
- [Data Manipulation Language (DML)](#data-manipulation-language-dml)
- [Implementation](#implementation)
- [Bonus Features (Optional)](#bonus-features-optional)
- [GitHub Repository](#github-repository)
- [Conclusion](#conclusion)

## Introduction
Briefly introduce the purpose of this report, the scope of the project, and the main functionalities of the Health and Fitness Club Management System.

## Conceptual Design
### ER Diagrams
- Insert the ER diagrams created by the team member responsible.
- Describe each entity and relationship.
- Discuss the assumptions made regarding cardinalities and participation types.
  
### Assumptions
- List any assumptions made during the design phase.

## Relational Schemas
### Reduction to Relation Schemas
- Provide the relational schema diagrams and explain how the ER components were mapped to tables.
- Mention who was responsible for this part of the project.

## Data Definition Language (DDL)
### File Overview
- Explain what is included in the DDL file (e.g., table creation, constraints).
- This section is managed by the team member assigned to DDL.
- Provide a link to the GitHub location where the DDL file can be accessed.

## Data Manipulation Language (DML)
### Sample Data Insertion
- Discuss the DML file and the sample data it includes for each table.
- This section is managed by the team member assigned to DML.
- Provide a link to the GitHub location where the DML file can be accessed.

## Implementation

FLOW OF THE PROGRAM
The application is a Command Line Interface made in python

LOGIN/REGISTER INTERFACE

Login or Register: Upon starting the program, the user is prompted to either login or register as a member, trainer, or administrator.
If logging in:
    - Members input their email and password.
        - Example member login to test: email: , password: 
    - Trainers input their trainer ID.
        - Example trainer login to test: trainerID: 1
    - Administrators input their staff ID.
        - Example admin login to test: StaffID: 1
If registering:
    - Users provide necessary details like name, email, password, fitness goals, and health metrics.
    - Example information: 
        - Name: saad
        - email: saad@email.com
        - password: passwordsaad
        - fitness goals: gain muscle
        - health metrics: Excellent

MEMBER INTERFACE

After successful login or registration, members are presented with a dashboard where they can:
    - Update profile information
    - View profile information.
    - Manage schedules:
        - NOTE: While entering information for date, write it in the form YYYY-MM-DD (Eg. 2024-01-01)
        - NOTE: While entering information for time, write it in the form HH::MM (Eg. 19:00)
        - Schedule personal training sessions.
        - Schedule group fitness classes.
        - Reschedule or cancel sessions.
    - View upcoming schedules.
    - BONUS: Members can view recommended classes based on availability.

-----------------------------------------------------------------------------------------------------------------

TRAINER INTERFACE

Trainers have access to functionalities to:
    - Update availability.
        (i) NOTE: While entering information for availability, write it in the form HH:MM - HH:MM (Eg. 10:00 - 15:00)
    - View member profiles.
        (i) Search for a member based on the name
    - View trainer schedules.

-----------------------------------------------------------------------------------------------------------------

ADMIN INTERFACE

Administrators can:
    - Manage room bookings:
        - Update room information.
        - Update room for fitness classes.
        - Delete reservations for fitness classes.
    - View room bookings.
    - View room information.
    - Update equipment status.
    - Monitor equipment status.
    - Manage group fitness class schedules:
        - Add, update, or cancel group fitness classes.
        - Update training sessions.
        - Cancel training sessions.
    - View all classes.
    - Handle billing: Update payment status for members.

-----------------------------------------------------------------------------------------------------------------

## Bonus Features
- Discuss any additional features that were implemented to enhance the system.
- Explain the innovative aspects and the effort involved.


