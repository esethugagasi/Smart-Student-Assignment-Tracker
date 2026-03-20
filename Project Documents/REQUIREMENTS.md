Smart Student Assignment Tracker System Requirements

1. Introduction

The Smart Student Assignment Tracker is a system designed to help students manage assignments, deadlines, and academic tasks efficiently. This document defines the functional and non-functional requirements of the system.

2. Functional Requirements

User Management

The system shall allow users to register an account.
    Acceptance: User account created with unique email validation.
The system shall allow users to log in securely.
    Acceptance: Valid login completes in ≤2 seconds.
The system shall allow users to log out.
    Acceptance: Session is terminated and user redirected.


Module Management

The system shall allow users to create modules.
    Acceptance: Module appears in dashboard immediately.
The system shall allow users to edit modules.
    Acceptance: Changes are saved and reflected instantly.
The system shall allow users to delete modules.
    Acceptance: Module and related assignments are removed.

Assignment Management
The system shall allow users to create assignments.
    Acceptance: Assignment is stored with title, module, and due date.
The system shall allow users to set assignment deadlines.
    Acceptance: Deadline is visible in dashboard.
The system shall allow users to update assignment status.
    Acceptance: Status changes (e.g., "Completed") are saved.
The system shall allow users to set assignment priority.
    Acceptance: Priority levels (Low, Medium, High) are displayed.

Dashboard & Notifications

The system shall display upcoming and overdue assignments.
    Acceptance: Dashboard updates in real-time.
The system shall send reminders for upcoming deadlines.
    Acceptance: Notifications are sent at least 24 hours before due date.

3. Non-Functional Requirements

Usability
The system shall provide an intuitive user interface.
The system shall be accessible via modern web browsers.

Deploy-ability
The system shall be deployable on Linux and Windows servers.
The system shall support cloud deployment.

Maintainability
The system shall follow modular architecture.
The system shall include developer documentation.

Scalability
The system shall support at least 1,000 concurrent users.

Security
User passwords shall be encrypted.
The system shall use secure authentication mechanisms.
Performance
The system shall respond to user actions within 2 seconds.
Dashboard data shall load within 3 seconds.

4. Traceability Overview

All requirements are directly linked to stakeholder needs such as:
Students → assignment tracking and reminders
Lecturers → reduced late submissions
IT staff → system reliability and performance

5. Conclusion
The defined requirements ensure the system is functional, secure, and scalable while addressing stakeholder concerns effectively.
