Reflection – Assignment 8

One of the main challenges in this assignment was determining the appropriate level of detail for state and activity diagrams. Too much detail made diagrams complex and difficult to read, while too little detail reduced their usefulness in representing system behavior.

Another challenge was aligning diagrams with previous assignments. Each state and activity needed to correspond to functional requirements and user stories, requiring careful cross-checking to maintain consistency.

Distinguishing between state diagrams and activity diagrams was also important. State diagrams focus on how an object changes over time, while activity diagrams focus on the sequence of actions in a process. Understanding this difference helped in modeling the system more effectively.

Additionally, modeling workflows such as notifications required thinking about system automation and background processes, which are not always visible to users.

Overall, this assignment improved understanding of dynamic system behavior and highlighted the importance of visual modeling in software design.


State Diagram
-------------

State diagram models the lifecycle of an assignment.
- The assignment starts in the Created state.
- It moves to Pending once saved.
- The student progresses it to In Progress and Completed.
- If deadlines are missed, it transitions to Overdue.
- After submission, it is graded.

Traceability
- FR: Create assignment -> Created
- FR: Update status -> In Progress / Completed
- FR: Deadline tracking -> Overdue
- US-04: Create assignment
- US-05: Set deadline


Notification Workflow
----------------------

Activity diagram models the automated notification process.
- The system checks assignment deadlines.
- If a deadline is approaching, the notification service generates reminders.
- The email service sends notifications to the user.
- The system updates notification status after sending.

Stakeholder Alignment
- Addresses student need for reminders (US-08)
- Supports functional requirement for notifications (FR-08)

Key Features
- Decision node ensures notifications are only sent when necessary
- Swimlanes separate system responsibilities
- Workflow includes external service interaction (Email Service)


