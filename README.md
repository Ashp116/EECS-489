<img src="others/images/umich-cse-logo-white.png" alt="drawing" width="450"/>

# EECS 489: Computer Networks (Winter 2026)  

[[_TOC_]]

## Logistics 
 
- Instructor: [Muhammad Shahbaz](https://web.eecs.umich.edu/~msbaz)
- Student Instructors: 
  - [Wonbin Jin](https://www.linkedin.com/in/wonbinjin/), GSI
  - [Madison Heyer](https://www.linkedin.com/in/madison-heyer-910237220/), GSI
  - [Arnav Shah](https://www.linkedin.com/in/arnavs25/), GSI
  - [Lance Ying](https://www.linkedin.com/in/lanceying/), IA
- Lecture time: **MW 1:30-3:00pm**
- Location: [LCSIB 1365](https://maps.app.goo.gl/Nz6mhERDhVUSRS2X7)
- Credit Hours: 4.00
- Course discussion and announcements: [Campuswire](https://campuswire.com/c/G875C9A30)
- Development environment: [AWS Academy](https://awsacademy.instructure.com/courses/151633)
- Exam submission: [Gradescope](https://www.gradescope.com/courses/1206766)
- Office hours: [Calendar](https://campuswire.com/c/calendar)
- Lecture and Discussion Slides: [Google Drive](https://drive.google.com/drive/folders/1fZcK_Xw-4bJ_YaCD81XjHtGBvE5wvDZ6)
- Discussion sections
  - (011) Friday 9:30am-10:30am, GGBL 2147, Wonbin Jin
  - (012) Thursday 4:30-5:30pm, FXB 1024, Arnav Shah
  - (013) Friday 12:30-1:30pm, EECS 1311, Madison Heyer

> **Note:** Visit [Canvas](https://umich.instructure.com/courses/818453) for instructions on joining [Campuswire](https://campuswire.com/c/G875C9A30), [Gradescope](https://www.gradescope.com/courses/1206766), and [AWS Academy](https://awsacademy.instructure.com/courses/151633).

#### Suggesting edits to the course page and more ...

We strongly welcome any changes, updates, or corrections to the course page or assignments or else that you may have. Please submit them using the [GitLab merge request workflow](https://docs.gitlab.com/ee/development/contributing/merge_request_workflow.html).

## Course Description

EECS 489 is an undergraduate-level course in Computer Networks at the University of Michigan. In this course, we will explore the underlying principles and design decisions that have enabled the Internet to (inter)connect billions of people and trillions of things on and off this planet. We will study the pros and cons of the current Internet design, ranging from classical problems (e.g., packet switching, routing, naming, transport, and congestion control) to emerging and future trends, like data centers, software-defined networking (SDN), programmable data planes, and network function virtualization (NFV), to name a few.

The goals for this course are:

- To become familiar with the classical and emerging problems in networking and their solutions.
- To learn what is the state-of-the-art in networking research: network architecture, protocols, and systems.
- To gain experience with network programming using industry-standard and state-of-the-art networking platforms.

# Course Syllabus and Schedule

> **Notes:** 
> - This syllabus and schedule are preliminary and subject to change.
> - Everything is due at 11:59 PM (Eastern) on the given day.
> - Abbreviations refer to the following:
>   - PD: Peterson/Davie 
>   - KR: Kurose/Ross

| Date    | Topics  | Notes | Readings |
| :------ | :------ | :------  | :------ |
| **Week 1** | **Course Overview** | | |
| Wed <br> Jan 07 | Introduction ([ppt](https://drive.google.com/file/d/1BHkOV02QfuHHvOLZ_NyRPm888gy1cBo5/view)) | | |
| **Week 2** | **History of the Internet** | | |
| Mon <br> Jan 12 | A Brief History of the Internet ([ppt](https://drive.google.com/file/d/1S-oV_BZwsnvSMfIWXvgodAiZ-WpXEeK-/view)) | | &bull; [Leiner et al. (1999). A Brief History of the Internet](https://gitlab.com/umich-eecs489/winter-2026/public/-/raw/main/readings/brief-history.pdf) (Optional) |
| Wed <br> Jan 14 | [AWS Academy](https://awsacademy.instructure.com/courses/151633) and [Assignment 0](assignments) Walkthrough | | |
| **Week 3** | **Network Building Blocks** | | |
| Mon <br> Jan 19 | *Martin Luther King, Jr. Day* <br> No Class | | |
| Wed <br> Jan 21 | Layering and Protocols ([ppt](https://drive.google.com/file/d/15UlLcYifhMxbJjs1ZtOHYm10iY4x8zme/view?usp=sharing)) | | &bull; [End-to-End Arguments](https://gitlab.com/umich-eecs489/winter-2026/public/-/raw/main/readings/e2eArgument84.pdf) <br/> &bull; PD: [1.3 (Architecture)](https://book.systemsapproach.org/foundation/architecture.html) |
| Fri <br> Jan 23 | | &bull; [Quiz 1](https://www.gradescope.com/courses/1206766/assignments/7521648) `due Jan 26` | |
| **Week 4** |**The Network API** | | |
| Mon <br> Jan 26 | Sockets: The Network Interface ([ppt](https://drive.google.com/file/d/1nRLC7BpptxV92dk6XnLkPsfwzH7atzBs/view?usp=sharing)) | &bull; [Demo](demos/sockets) <br> &bull; [Assignment 1](assignments/assignment1) `due Feb 09` | &bull; PD: [1.4 (Software)](https://book.systemsapproach.org/foundation/software.html) <br> &bull; [Beej's Guide](http://beej.us/guide/bgnet/) (Optional) |
| Wed <br> Jan 28 | Transport: Process-to-Process Communication ([ppt](https://drive.google.com/file/d/1u9hlNUOYL_2sGnq3EuahwqXNBInSgvv9/view?usp=sharing)) | | &bull; PD: [2.5 (Reliable Transmission)](https://book.systemsapproach.org/direct/reliable.html) <br> &bull; PD: [5.1 - 5.2 (UDP, TCP)](https://book.systemsapproach.org/e2e.html) |
| **Week 5** | **Local Area Networks** | | |
| Mon <br> Feb 02 | | | |
| Wed <br> Feb 04 | | | |
| **Week 6** | **Network Addressing and Configuration** | | |
| Mon <br> Feb 09 | | | |
| Wed <br> Feb 11 | | | |
| **Week 7** | **Process-to-Process Communication**| | |
| Mon <br> Feb 16 | | | |
| Wed <br> Feb 18 | | | |
| **Week 8** | **Software-Defined Networks and Data Centers**| | |
| Mon <br> Feb 23 | | | |
| Wed <br> Feb 25 | | | |
| **Week 9** | **Wide Area Networks** | | |
| Mon <br> Mar 09 | | | |
| Wed <br> Mar 11 | | | |
| **Week 10** | **Programmable Networks (and Network Data Planes)** | | |
| Mon <br> Mar 16 | | | |
| Wed <br> Mar 18 | | | |
| **Week 11** | **Resource Allocation** | | |
| Mon <br> Mar 23 | | | |
| Wed <br> Mar 25 | | | |
| **Week 12** | **Network Applications** | | |
| Mon <br> Mar 30 | | | |
| Wed <br> Apr 01 | | | |
| **Week 13** | **TBD** | | |
| Mon <br> Apr 06 | | | |
| Wed <br> Apr 08 | | | |
| **Week 14** | **TBD** | | |
| Mon <br> Apr 13 | | | |
| Wed <br> Apr 15 | | | |
| **Week 15** | **TBD** | | |
| Mon <br> Apr 20 | | | |
| Tue <br> Apr 21 | | | |
| **Week 16** | **Exam Week** | | |

## Prerequisites

Students must have completed [EECS 281](https://eecs281staff.github.io/eecs281.org/) (Data Structures and Algorithms) and [EECS 370](https://eecs370.github.io/) (Introduction to Computer Organization) before enrolling in this course.

While EECS 482 is not required, students are expected to have strong proficiency in C/C++ programming and familiarity with Unix-based operating systems.

## Recommended Textbooks
- Computer Networks: A Systems Approach by L. Peterson and B. Davie ([Online Version](https://book.systemsapproach.org/index.html))
- Computer Networking: A Top-Down Approach by J. Kurose and K. Ross (7th or earlier edition)

> Other optional but interesting resources: [Software-Defined Networks: A Systems Approach](https://sdn.systemsapproach.org/index.html), [5G Mobile Networks: A Systems Approach](https://5g.systemsapproach.org/index.html) [Sytems Approach - Blog](https://www.systemsapproach.org/blog), [TCP Congestion Control: A Systems Approach](https://tcpcc.systemsapproach.org/index.html), [Operating an Edge Cloud: A Systems Approach](https://ops.systemsapproach.org), and [Network Algorithmics: An Interdisciplinary Approach to Designing Fast Networked Devices](https://umich.skillport.com/skillportfe/main.action?assetid=RW$89427:_ss_book:166141#summary/BOOKS/RW$89427:_ss_book:166141)


## Programming Assignments

- [Assignment 0](assignments) `not graded`
- [Assignment 1](assignments/assignment1) `due Feb 09`
- [Assignment 2]() `due TBD`
- [Assignment 3]() `due TBD`
- [Assignment 4]() `due TBD`

## Quizzes

- [Quiz 1](https://www.gradescope.com/courses/1206766/assignments/7521648) `due Jan 26`
- [Quiz 2]() `due TBD`
- [Quiz 3]() `due TBD`
- [Quiz 4]() `due TBD`
- [Quiz 5]() `due TBD`

> **Format:** take home, open book

## Midterm and Final Exams
There will be one midterm and a final exam based on course content (lectures, discussions, and assignments).

- Midterm Exam `on Feb 25 (during class)` 
- Final Exam `on TBD`

> **Format:** in class, closed book

## Grading

- Class participation: 5%
- Programming assignments: 45%
- Quizzes: 10%
- Midterm exam: 20%
- Final exam: 20%
- Extra credit: 2%

## Policies

### Late submission

- Grace period: 24 hours for the entire semester.
- After the grace period, 25% off for every 24 hours late, rounded up.

If you have extenuating circumstances that result in an assignment being late, please let us know about them as soon as possible.

### Academic Integrity & Honor Code

We will follow U-M Engineering's academic policies throughout this course unless stated otherwise (see [U-M Engineering's Academic Policies](https://bulletin.engin.umich.edu/rules/)). You are responsible for adhering to these policies and upholding the Honor Code.

## Acknowledgements

This class borrows inspiration from several incredible sources.
- The lecture slides' material is partially adapted from my Ph.D. advisors, Jen Rexford's [COS 461](https://www.cs.princeton.edu/courses/archive/fall20/cos461) class and Nick Feamster's [COS 461](https://www.cs.princeton.edu/courses/archive/spring19/cos461/) class at Princeton.
