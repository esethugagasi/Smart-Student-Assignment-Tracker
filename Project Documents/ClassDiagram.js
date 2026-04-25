
```mermaid
classDiagram

class Student {
  -studentId: String
  -name: String
  -email: String
  +register()
  +login()
}

class UserAccount {
  -userId: String
  -password: String
  -status: String
  +authenticate()
}

class Module {
  -moduleId: String
  -name: String
  +addAssignment()
}

class Assignment {
  -assignmentId: String
  -title: String
  -deadline: Date
  -status: String
  +create()
  +updateStatus()
}

class Deadline {
  -dueDate: Date
  -reminderDate: Date
  +setDeadline()
}

class Notification {
  -notificationId: String
  -message: String
  -status: String
  +send()
}

class Dashboard {
  -assignmentsList: List
  +display()
}

class Session {
  -sessionId: String
  -expiry: Date
  +start()
  +end()
}

%% Relationships

Student "1" -- "1" UserAccount : owns
Student "1" -- "1..*" Module : manages
Module "1" -- "0..*" Assignment : contains
Assignment "1" -- "1" Deadline : has
Assignment "1" -- "0..*" Notification : triggers
Student "1" -- "1" Dashboard : views
UserAccount "1" -- "0..1" Session : creates

```
