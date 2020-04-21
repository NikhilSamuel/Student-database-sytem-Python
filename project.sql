-- creating the project database and using it
create database projectdatabase;
use projectdatabase;

-- creating the student table
create table student(StdID VARCHAR(20) PRIMARY KEY Not Null,
FirstName VARCHAR(50),
LastName VARCHAR(50),
Email VARCHAR(50),
Age INTEGER(10),
Gender VARCHAR(20),
Course VARCHAR(20));

-- inserting into the student table
insert into student values("C0761036", "Fahim", "Shariff", "C0761036@mylambton.ca", 23, "Male", "CSAT");
insert into student values("C0765028", "Nikhil", "Samuel", "C0765028@mylambton.ca", 23, "Male", "CSAT");
insert into student values("C0765139", "Jude", "Tacwel", "C0765139@mylambton.ca", 24, "Male", "CSAT");


-- creating the professor table
create table professor(profID VARCHAR(20) PRIMARY KEY Not Null,
FirstName VARCHAR(50),
LastName VARCHAR(50),
Email VARCHAR(50),
Age INTEGER(10),
Gender VARCHAR(20),
Mobile VARCHAR(20));

-- inserting into the professor table
insert into professor values("P001", "Ahmad", "Alhamad", "P001@mylambton.ca", 50, "Male", "6478981234");
insert into professor values("P002", "Javeria", "Aamir", "P002@mylambton.ca", 45, "Female", "647888222");
insert into professor values("P003", "Peter", "Sigurdson", "P003@mylambton.ca", 60, "Male", "647777777");


-- creating the grade table
create table grades(profID VARCHAR(20) Not Null,
profName varchar(20),
StudID VARCHAR(20),
StudName varchar(20),
CourseID varchar(20) primary key,
CourseName VARCHAR(50),
Mark INT(10),
Grade CHAR(10));

-- inserting into the professor table
insert into grades values("P001", "Ahmad Alhamad", "C0761036", "Fahim Shariff", "CSAT01", "Python", 80, "A");
insert into grades values("P002", "Javeria Aamir", "C0765028", "Nikhil Samuel", "CSAT02", "Java", 90, "A");
insert into grades values("P003", "Peter Sigurdson", "C0765139", "Jude Tacwel", "CSAT03", "C#", 80, "A");


-- creating the username and password table
create table USERNAMEPASSWORD (Usertype VARCHAR(20) Not Null,
Username VARCHAR(20) PRIMARY KEY,
Password VARCHAR(50));

-- inserting into the username and password table
insert into USERNAMEPASSWORD values("Admin", "Admin1", "Admin1");
insert into USERNAMEPASSWORD values("Professor", "Professor1", "Professor1");
insert into USERNAMEPASSWORD values("Student", "Student1", "Student1");


-- creating the course table
create table COURSES (CourseID VARCHAR(20) Not Null primary key,
CourseName VARCHAR(20),
ProfID VARCHAR(20),
Profname VARCHAR(20),
No_of_Students VARCHAR(10),
Duration VARCHAR(20));

-- inserting into the course table
insert into COURSES values("CSAT01", "Python","P001", "Ahmad Alhamad", "30", "16 Weeks");
insert into COURSES values("CSAT02", "Java","P002", "Javeria Aamir", "32", "16 Weeks");
insert into COURSES values("CSAT03", "C#","P003", "Peter Sigurdson", "34", "16 Weeks");



