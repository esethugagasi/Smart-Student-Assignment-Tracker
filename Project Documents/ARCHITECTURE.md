Smart Student Assignment Tracker 
Architecture
1.	Project Title
Smart Student Assignment Tracker

2.	Domain
Education Technology

3.	Problem statement
Students are struggling to coordinate assignments across numerous modules. Deadlines might be missed due to poor organization or a lack of awareness of future obligations. Existing methods are frequently fragmented or not purposefully intended for academic task management.

The suggested solution solves this challenge by offering a single platform for students to track assignments, manage modules, and receive notifications about upcoming deadlines.

4.	Individual Scope
The scope of this project is limited to a system for students to organize academic assignments and track their progress. The system will enable basic user authentication, module management, assignment tracking, and dashboard reporting.
The project is feasible for a single developer because the system focuses solely on key functions and avoids extensive integration or support.

5.	C4 Architecture	model
The system architecture follows the C4 model, which describes software architecture at various levels of abstraction.

The following diagrams are included:
•	System Context Diagram.
•	Container Diagram
•	Component Diagram.
 

5.1.	System Context Diagram
The System Context Diagram shows the main system, its primary user, and the external systems it interacts with.

Flowchart 
•	Students are primary users who manage modules and assignments.
•	Smart Student Assignment Tracker is a centralized solution for organizing assignments, deadlines, and progress.
•	EmailService [Email Notification Service\nAn external service that sends deadline reminders]

 Student Creates account, logs in, controls assignments, and views dashboard| System sends reminder notifications. EmailService

5.2.	Container Diagram
    Please find it in C:\Users\eseth\OneDrive\Books\Software\Smart-Student-Assignment-Tracker\Project Documents\ContainerDiagram.uxf
5.3.	Component Diagram
    Please find it in C:\Users\eseth\OneDrive\Books\Software\Smart-Student-Assignment-Tracker\Project Documents\ComponentDiagram.uxf
 

6.	End-to-End workflow
The architecture enables the following end-to-end process:
•	The student launches the web app.
•	The student registers or logs into the system.
•	The front end submits authentication requests to the backend API.
•	The backend checks credentials and stores/retrieves user data from the database.
•	The interface allows the student to create modules and assignments.
•	The backend database contains modules and assignment records.
•	The dashboard pulls assignment data and shows future, completed, and overdue assignments.
•	The reminder service tracks upcoming deadlines.
•	The notification service provides deadline reminders via the email provider.

7.	The architectural benefits
This architecture provides the following benefits:

•	Clear separation of roles.
•	Easy maintenance and testing
•	Improved scalability for future developments.
•	Strong alignment to software engineering is best practice.
•	Clear visibility of system components from beginning to end.

8.	Future improvements
Potential future upgrades include:

•	Mobile application container.
•	Push notification support.
•	Calendar integration
•	The analytics and reporting module
•	Multi-user collaboration support
