import mysql
import mysql.connector
from tkinter import messagebox

#class to create the student table and make updations
class Student:

    #function to create the database

    def databaseCreation(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("CREATE DATABASE IF NOT EXISTS PROJECTDATABASE")
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("Database Error", "Error occured during DATABASE creation")
            connector.rollback()
            connector.close()

    #function to create the student table

    def StudentData(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("CREATE TABLE IF NOT EXISTS student(StdID VARCHAR(20) PRIMARY KEY Not Null,FirstName VARCHAR(50),\
                                LastName VARCHAR(50),Email VARCHAR(50),Age INTEGER(10),Gender VARCHAR(20),Course VARCHAR(20))")
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("Database Error","Error occured during table creation",e )
            connector.rollback()
            connector.close()

    #function to add data to the student table

    def addStdData(self,studid,fname,lname,email,age,gender,course):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("INSERT INTO student(StdID,FirstName,LAstName,Email,Age,Gender,Course) VALUES('%s','%s','%s','%s','%s','%s','%s')"\
                             %(studid,fname,lname,email,age,gender,course))
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("Error","Data already exists!")

    #function to view data stored in the student table

    def viewStdData(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("SELECT * FROM student")
            rows = mycursor.fetchall()
            connector.close()
            return rows
        except:
            connector.rollback()
            connector.close()

    #function to delete student data

    def deleteStdData(self,stdid):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("DELETE FROM STUDENT WHERE StdID='%s'"%(stdid))
            connector.commit()
            connector.close()
        except:
            connector.rollback()
            connector.close()
            messagebox.showerror("error","Data cannot be deleted!")

#class to create the student table and make updations
class Professor:

    def databaseCreation(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("CREATE DATABASE IF NOT EXISTS PROJECTDATABASE")
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("Database Error", "Error occured during DATABASE creation")
            connector.rollback()
            connector.close()

    def ProfessorData(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("CREATE TABLE IF NOT EXISTS professor(profID VARCHAR(20) PRIMARY KEY Not Null,FirstName VARCHAR(50),\
                                LastName VARCHAR(50),Email VARCHAR(50),Age INTEGER(10),Gender VARCHAR(20),Mobile VARCHAR(20))")
            connector.commit()
            connector.close()
        except Error as e:
            messagebox.showerror("Database Error","Error occured during table creation",e )
            connector.rollback()
            connector.close()

    def addProfData(self,profid,fname,lname,email,age,gender,mobile):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("INSERT INTO PROFESSOR(profID,FirstName,LAstName,Email,Age,Gender,Mobile)  VALUES('%s','%s','%s','%s','%s','%s','%s')"\
                             %(profid,fname,lname,email,age,gender,mobile))
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("error","Please try again!")
            connector.close()


    def viewProfData(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("SELECT * FROM professor")
            rows = mycursor.fetchall()
            connector.close()
            return rows
        except Error as e:
            connector.rollback()
            connector.close()

    def deleteProfData(self,profid):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("DELETE FROM PROFESSOR WHERE profID='%s'"%(profid))
            connector.commit()
            connector.close()
        except Error as e:
            connector.rollback()
            connector.close()
            messagebox.showerror("error","Please try again!")

#class to create the grades table and make updations
class Grades:

    def databaseCreation(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("CREATE DATABASE IF NOT EXISTS PROJECTDATABASE")
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("Database Error", "Error occured during DATABASE creation")
            connector.rollback()
            connector.close()

    def GradeData(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("CREATE TABLE IF NOT EXISTS grades(profID VARCHAR(20) Not Null,profName varchar(20),StudID VARCHAR(20),StudName varchar(20),\
                                            CourseID varchar(20) primary key, CourseName VARCHAR(50),Mark INT(10),Grade CHAR(10))")
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("Database Error", "Error occured during table creation")
            connector.rollback()
            connector.close()

    def addGradeData(self, profid,profname,studid,studname,courseid, course, mark, grade):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("INSERT INTO GRADES(profID,profName,StudID,StudName,CourseID,CourseName,Mark,Grade)  VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"\
                         %(profid,profname, studid,studname,courseid,course, mark, grade))
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("error","Please try again!")
            connector.close()

    def viewGradeData(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("SELECT * FROM grades")
            rows = mycursor.fetchall()
            connector.close()
            return rows
        except:
            connector.rollback()
            connector.close()

    def deleteGradeData(self, profid,studid):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("DELETE FROM GRADES WHERE profID='%s' AND StudID='%s' " % (profid,studid))
            connector.commit()
            connector.close()
        except:
            connector.rollback()
            connector.close()
            messagebox.showerror("error","Please try again!")

#class to add user credentials and to make updations
class UsernamePassword:
    def databaseCreation(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("CREATE DATABASE IF NOT EXISTS PROJECTDATABASE")
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("Database Error", "Error occured during DATABASE creation")
            connector.rollback()
            connector.close()

    def upData(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("CREATE TABLE IF NOT EXISTS USERNAMEPASSWORD (Usertype VARCHAR(20) Not Null,Username VARCHAR(20) PRIMARY KEY,\
                                            Password VARCHAR(50))")
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("Database Error", "Error occured during table creation")
            connector.rollback()
            connector.close()

    def addUPData(self,usertype,username,password):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("INSERT INTO USERNAMEPASSWORD(Usertype,Username,Password)  VALUES('%s','%s','%s')"\
                         %(usertype,username,password))
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("error","Please try again!")
            connector.rollback()
            connector.close()

    def viewUPData(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("SELECT * FROM USERNAMEPASSWORD")
            rows = mycursor.fetchall()
            connector.close()
            return rows
        except Error as e:
            connector.rollback()
            connector.close()

    def deleteUPData(self,username):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("DELETE FROM USERNAMEPASSWORD WHERE Username='%s'" %(username))
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("error","Please try again")
            connector.rollback()
            connector.close()

#class to create the course table and make updations
class Courses:
    def databaseCreation(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("CREATE DATABASE IF NOT EXISTS PROJECTDATABASE")
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("Database Error", "Error occured during DATABASE creation")
            connector.rollback()
            connector.close()

    def courseData(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("CREATE TABLE IF NOT EXISTS COURSES (CourseID VARCHAR(20) Not Null primary key,CourseName VARCHAR(20),\
                             ProfID VARCHAR(20),Profname VARCHAR(20),No_of_Students VARCHAR(10),Duration VARCHAR(20))")
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("Database Error", "Error occured during table creation")
            connector.rollback()
            connector.close()

    def addCourseData(self,cid,cname,pid,pname,nofstudents,duration):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("INSERT INTO COURSES(CourseID,CourseName,ProfID,Profname,No_of_Students,Duration)  VALUES('%s','%s','%s','%s','%s','%s')"\
                         %(cid,cname,pid,pname,nofstudents,duration))
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("error","Please try again!")
            connector.close()

    def viewCourseData(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("SELECT * FROM COURSES")
            rows = mycursor.fetchall()
            connector.close()
            return rows
        except:
            connector.rollback()
            connector.close()

    def deleteCourseData(self,cid):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("DELETE FROM COURSES WHERE CourseID='%s'" %(cid))
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("error","Please try again!")
            connector.rollback()
            connector.close()

#class for sorting student grades
class StudentGrades:

    def databaseCreation(self):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("CREATE DATABASE IF NOT EXISTS PROJECTDATABASE")
            connector.commit()
            connector.close()
        except:
            messagebox.showerror("Database Error", "Error occured during DATABASE creation")
            connector.rollback()
            connector.close()

    def viewGradeData(self,name):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("SELECT * FROM grades where StudName='%s'"%(name))
            rows = mycursor.fetchall()
            connector.close()
            return rows
        except:
            messagebox.showerror("Error","Please try again.")
            connector.rollback()
            connector.close()

#class for sorting user login credentials
class Login:
    def loginValidation(self,name):
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("SELECT * FROM USERNAMEPASSWORD where Username='%s'"%(name))
            row=mycursor.fetchone()
            connector.close()
            return row
        except:
            messagebox.showerror("Error","Login Error,Please try again.")





