#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// This program will generate a .sql file which can be used as DML (use this for testing efficiency)

#define MAX_RECORDS 1000000  // Adjust this for number of records wanted 
#define MAX_TRAINERS (MAX_RECORDS / 10)
#define MAX_ADMIN (MAX_RECORDS / 100)
#define MAX_EQUIPMENT (MAX_RECORDS / 50)
#define MAX_ROOMS (MAX_RECORDS / 100)
#define MAX_CLASSES (MAX_RECORDS / 50)
#define BUFFER_SIZE 255

void random_string(char *str, int length) {
    char charset[] = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    while (length-- > 0) {
        size_t index = (double) rand() / RAND_MAX * (sizeof charset - 1);
        *str++ = charset[index];
    }
    *str = '\0';
}

void unique_email(char *email, int id) {
    sprintf(email, "%d_user@example.com", id); 
}

void random_date(char *date) {
    sprintf(date, "%d-%02d-%02d", rand() % 5 + 2020, rand() % 12 + 1, rand() % 28 + 1);
}

void random_time(char *time) {
    sprintf(time, "%02d:%02d", rand() % 24, rand() % 60);
}

int main() {
    srand(time(NULL));  

    FILE *fp = fopen("dml_script.sql", "w");
    if (fp == NULL) {
        printf("Failed to open file\n");
        return -1;
    }

    char name[BUFFER_SIZE], email[BUFFER_SIZE], date[BUFFER_SIZE], time[BUFFER_SIZE];
    int i;

    // Administrative Staff
    for (i = 1; i <= MAX_ADMIN; i++) {
        random_string(name, 10);
        unique_email(email, i);
        fprintf(fp, "INSERT INTO Administrative_Staff (Name, Role, ContactInformation) VALUES ('%s', 'Role_%d', '%s');\n", name, i, email);
    }

    // Equipment
    for (i = 1; i <= MAX_EQUIPMENT; i++) {
        random_string(name, 10);
        const char* status[] = {"Available", "In Use", "Maintenance"};
        int rand_status = rand() % 3;
        fprintf(fp, "INSERT INTO Equipment (EquipmentName, Status) VALUES ('%s', '%s');\n", name, status[rand_status]);
    }

    // Members
    for (i = 1; i <= MAX_RECORDS; i++) {
        random_string(name, 10);
        unique_email(email, i);
        fprintf(fp, "INSERT INTO Member (Name, Email, Password, FitnessGoal, HealthMetrics, PaymentStatus) VALUES ('%s', '%s', 'password%d', 'Goal_%d', 'Metrics_%d', 'Active');\n", name, email, i, i, i);
    }

    // Trainers
    for (i = 1; i <= MAX_TRAINERS; i++) {
        random_string(name, 10);
        random_time(time);
        fprintf(fp, "INSERT INTO Trainer (Name, Specialization, AvailableTimes) VALUES ('%s', 'Specialization_%d', '%s');\n", name, i, time);
    }

    // Rooms
    for (i = 1; i <= MAX_ROOMS; i++) {
        random_string(name, 10);
        fprintf(fp, "INSERT INTO Room (RoomName, Capacity, StaffID) VALUES ('%s', %d, %d);\n", name, rand() % 100 + 1, rand() % MAX_ADMIN + 1);
    }

    // Fitness Classes
    for (i = 1; i <= MAX_CLASSES; i++) {
        random_string(name, 10);
        random_time(time);
        fprintf(fp, "INSERT INTO Fitness_Class (ClassName, Schedule, RoomID, TrainerID) VALUES ('%s', '%s', %d, %d);\n", name, time, rand() % MAX_ROOMS + 1, rand() % MAX_TRAINERS + 1);
    }

    // Training Sessions
    for (i = 1; i <= MAX_RECORDS / 5; i++) {
        random_date(date);
        random_time(time);
        fprintf(fp, "INSERT INTO Training_Session (Date, Time, MemberID, TrainerID) VALUES ('%s', '%s', %d, %d);\n", date, time, rand() % MAX_RECORDS + 1, rand() % MAX_TRAINERS + 1);
    }

    // Registers
    for (i = 1; i <= MAX_RECORDS / 3; i++) {
        fprintf(fp, "INSERT INTO Registers (MemberID, ClassID, GroupName) VALUES (%d, %d, 'Group_%d');\n", rand() % MAX_RECORDS + 1, rand() % MAX_CLASSES + 1, i);
    }

    // Fi_Me (Fitness Class to Member)
    for (i = 1; i <= MAX_RECORDS / 5; i++) {
        fprintf(fp, "INSERT INTO Fi_Me (ClassID, MemberID) VALUES (%d, %d);\n", rand() % MAX_CLASSES + 1, rand() % MAX_RECORDS + 1);
    }

    // Eq_As (Equipment to Administrative Staff)
    for (i = 1; i <= MAX_EQUIPMENT / 2; i++) { 
        fprintf(fp, "INSERT INTO Eq_As (EquipmentID, StaffID) VALUES (%d, %d);\n", rand() % MAX_EQUIPMENT + 1, rand() % MAX_ADMIN + 1);
    }

    fclose(fp);
    printf("DML script generated successfully.\n");

    return 0;
}
