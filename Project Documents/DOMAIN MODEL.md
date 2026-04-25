Domain Model – Smart Student Assignment Tracker
-------------------------------------------------

Core Entities
-------------

| Entity       | Attributes                            | Methods                  | Relationships                   |
| ------------ | ------------------------------------- | ------------------------ | ------------------------------- |
| Student      | studentId, name, email                | register(), login()      | Creates Assignment, owns Module |
| Module       | moduleId, name                        | addAssignment()          | Contains Assignments            |
| Assignment   | assignmentId, title, deadline, status | create(), updateStatus() | Belongs to Module               |
| Deadline     | dueDate, reminderDate                 | setDeadline()            | Associated with Assignment      |
| Notification | notificationId, message, status       | send()                   | Linked to Assignment            |
| UserAccount  | userId, password, status              | authenticate()           | Belongs to Student              |
| Dashboard    | assignmentsList                       | display()                | Aggregates Assignments          |
| Session      | sessionId, expiry                     | start(), end()           | Linked to UserAccount           |


Key Business Rules
-------------------

A Student can have multiple modules
A Module can contain multiple assignments
Each Assignment has one deadline
Notifications are triggered based on deadlines
A user must be authenticated before accessing the dashboard