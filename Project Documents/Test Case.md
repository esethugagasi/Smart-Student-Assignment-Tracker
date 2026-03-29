Test Cases – Smart Student Assignment Tracker

1. Functional Test Cases

| Test ID | Req ID | Description       | Steps                   | Expected Result  | Actual Result | Status |
| ------- | ------ | ----------------- | ----------------------- | ---------------- | ------------- | ------ |
| TC-01   | FR1    | Register account  | Enter email/password    | Account created  | TBD           | TBD    |
| TC-02   | FR2    | Login             | Enter valid credentials | Login successful | TBD           | TBD    |
| TC-03   | FR4    | Create module     | Add module              | Module appears   | TBD           | TBD    |
| TC-04   | FR7    | Create assignment | Add assignment          | Assignment saved | TBD           | TBD    |
| TC-05   | FR8    | Set deadline      | Select date             | Date saved       | TBD           | TBD    |
| TC-06   | FR9    | Update status     | Mark complete           | Status updated   | TBD           | TBD    |
| TC-07   | FR11   | View dashboard    | Open dashboard          | Data displayed   | TBD           | TBD    |
| TC-08   | FR12   | Notifications     | Trigger reminder        | Email sent       | TBD           | TBD    |

2. Non-Functional Test Cases

Performance Test
Simulate 1000 users accessing dashboard
Expected: Response time ≤ 3 seconds

Security Test
Attempt login with invalid credentials
Expected: Access denied and logged

