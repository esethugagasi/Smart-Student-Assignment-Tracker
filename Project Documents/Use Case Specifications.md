Use Case 1: Register Account

Actor: Student
Precondition: User is not registered
Postcondition: Account created

Basic Flow:
User enters email and password
System validates input
System creates account

Alternative Flow:
Invalid email → error message displayed

Use Case 2: Login

Actor: Student
Precondition: Account exists
Postcondition: User logged in

Basic Flow:
User enters credentials
System verifies credentials
Access granted

Alternative Flow:
Incorrect password → access denied


Use Case 3: Create Module

Actor: Student
Precondition: User logged in
Postcondition: Module saved

Basic Flow:
User enters module name
System saves module


Use Case 4: Create Assignment

Actor: Student
Precondition: Module exists
Postcondition: Assignment created

Basic Flow:
User enters assignment details
System saves assignment


Use Case 5: Set Deadline

Actor: Student
Precondition: Assignment exists
Postcondition: Deadline recorded

Basic Flow:
User selects date
System stores deadline


Use Case 6: View Dashboard

Actor: Student
Precondition: User logged in
Postcondition: Dashboard displayed

Basic Flow:
System retrieves assignments
Displays upcoming and overdue tasks


Use Case 7: Update Assignment Status

Actor: Student
Precondition: Assignment exists
Postcondition: Status updated

Basic Flow:
User selects status
System updates record


Use Case 8: Receive Notifications

Actor: Student
Precondition: Assignment has deadline
Postcondition: Notification sent

Basic Flow:
System checks deadlines
Sends reminder via email

Alternative Flow:
Email fails → retry mechanism triggered