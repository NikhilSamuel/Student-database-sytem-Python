from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import apply as apply
import mysql.connector
import backendProject
from tkinter import ttk


#Main Window select the user type and login
class Interface:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("750x550+0+0")
        self.root.title("Welcome to the Login Page")
        self.root.configure()
        self.root.resizable(0, 0)

        self.login = backendProject.Login()

        myimage = ImageTk.PhotoImage(Image.open("login.png"))
        image = Label(self.root, relief=RIDGE, width=375, height=550, image=myimage)
        image.place(x=0, y=0)

        frame = Frame(self.root, relief=RIDGE, width=375, height=550, bg='thistle1')
        frame.place(x=375, y=0)

        welcomeLabel = Label(frame, bg='thistle1', text="Login in to", font=("arial", 18, "bold"), fg='black')
        welcomeLabel.place(x=20, y=120)
        welcomeLabel2 = Label(frame, bg='thistle1', text="DATABASE", font=("Verdana", 25, "bold"), fg='brown1')
        welcomeLabel2.place(x=155, y=113)

        typeLabel = Label(frame, text="User Type:", fg='black', bg='thistle1', font=("Verdana", 13))
        typeLabel.place(x=50, y=240)

        options = ["Admin", "Professor", "Student"]

        self.var = StringVar()
        self.var.set("select user")
        self.name = StringVar()
        self.password = StringVar()

        typeMenu = apply.apply(OptionMenu, (frame, self.var) + tuple(options))
        typeMenu.place(x=160, y=240)
        typeMenu.configure(bg='tomato2', fg='black')

        nameLabel = Label(frame, text="Username:", fg='black', bg='thistle1', font=("verdana", 13))
        nameLabel.place(x=50, y=290)

        self.nameEntry = Entry(frame, bg='thistle1', textvariable=self.name, fg='black', font=("arial", 13), width=30)
        self.nameEntry.place(x=50, y=320)

        passwordLabel = Label(frame, text="Password:", fg='black', bg='thistle1', font=("Verdana", 13))
        passwordLabel.place(x=50, y=360)

        self.passwordEntry = Entry(frame, bg='thistle1', textvariable=self.password, fg='black', font=("arial", 13),
                                   show="*", width=30)
        self.passwordEntry.place(x=50, y=390)

        submit = Button(frame, text='LOGIN', bd=1, bg='tomato2', fg='black', relief=SUNKEN,
                        font=("MS Sans Serif", 14, "bold"), command=self.submit)
        submit.place(x=80, y=470)

        quitButton = Button(frame, text='QUIT', bd=1, bg='AntiqueWhite3', fg='black', relief=SUNKEN,
                            font=("MS Sans Serif", 14, "bold"), command=self.exit)
        quitButton.place(x=180, y=470)

        mainloop()


#quit button function

    def exit(self):
        msgbox = messagebox.askyesno("Exit", "Do you want to exit?")
        if msgbox > 0:
            self.root.destroy()
            return


#submit button function
    def submit(self):
        type = self.var.get()
        username = self.name.get()
        password = self.password.get()
        null = ""


#user type and credentials validation
        if (type == "Admin"):
            if username == null:
                messagebox.showerror("Alert", "Please enter your username!")
            elif password == null:
                messagebox.showerror("Alert", "Please enter your Password!")
            elif(username=="Ahmad" and password=="Ahmad"):
                messagebox.showinfo("Welcome", "Welcome " + str(self.name.get()))
                self.adminAction()

            else:
                row = self.login.loginValidation(self.name.get())
                if (username == row[1] and password == row[2]):
                    messagebox.showinfo("Welcome", "Welcome " + str(self.name.get()))
                    self.adminAction()
                else:
                    messagebox.showerror("error", "Incorrect Username or Password")

        elif (type == "Professor"):
            if username == null:
                messagebox.showinfo("Alert", "Please enter your username!")
            elif password == null:
                messagebox.showinfo("Alert", "Please enter your Password!")
            else:
                row = self.login.loginValidation(self.name.get())
                if (username == row[1] and password == row[2]):
                    messagebox.showinfo("Welcome", "Welcome " + str(self.name.get()))
                    self.professorAction()
                else:
                    messagebox.showerror("Failed", "Incorrect Username or Password")

        elif (type == "Student"):
            if username == null:
                messagebox.showerror("Alert", "Please enter your username!")
            elif password == null:
                messagebox.showerror("Alert", "Please enter your Password!")
            else:
                row = self.login.loginValidation(self.name.get())
                if (username == row[1] and password == row[2]):
                    messagebox.showinfo("Welcome", "Welcome " + str(self.name.get()))
                    self.studentAction()
                else:
                    messagebox.showerror('Failed', "Incorrect Username or Password")
        else:
            messagebox.showerror("Error", "Please select the user type!")


# function to call the admin window and close the main window
    def adminAction(self):
        self.root.destroy()
        adminWindow = AdminWindow()

    # function to call the professor window and close the main window
    def professorAction(self):
        self.root.destroy()
        professorwindow = ProfessorWindow()

    # function to call the student window and close the main window
    def studentAction(self):
        self.root.destroy()
        studentWindow = StudentWindow()

# Admin window

class AdminWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("650x650+0+0")
        self.root.configure(relief=RIDGE, bg='SteelBlue4')
        self.root.title("Welcome Admin")
        self.root.resizable(0, 0)
        frame = Frame(self.root, height=400, relief=RIDGE, width=400, bd=3, bg='steel blue')
        frame.place(x=30, y=150)

        adminLabel = Label(self.root, text="Welcome Admin", fg='white', bg='SteelBlue4', bd=2, font=("Helvetica", 15))
        adminLabel.place(x=30, y=50)

        label = Label(self.root, text="Click on buttons below to Add or Update data!!", fg='black', bg='SteelBlue4',
                      bd=2, font=("arial", 12))
        label.place(x=30, y=120)

        label = Label(self.root, text="Powered by python", fg='white', bg='SteelBlue4',
                      font=("arial", 12))
        label.place(x=500, y=630)

        gridFrame = Frame(frame, bg='steel blue', relief=RIDGE)
        gridFrame.pack(fill=BOTH, expand=1)

        studentButton = Button(gridFrame, relief=RIDGE, text="STUDENTS", bg='steel blue', font=("Verdana", 20, "bold"),
                               fg='white', height=2,
                               width=30, command=self.adminstudent)
        professorButton = Button(gridFrame, relief=RIDGE, text="PROFESSORS", bg='steel blue',
                                 font=("Verdana", 20, "bold"), fg='white', height=2,
                                 width=30, command=self.adminprofessor)
        upButton = Button(gridFrame, relief=RIDGE, text="USER NAME & PASSWORDS", font=("Verdana", 20, "bold"),
                          bg='steel blue', fg='white', height=2,
                          width=30, command=self.adminup)
        gradeButton = Button(gridFrame, relief=RIDGE, text="GRADES", bg='steel blue', font=("Verdana", 20, "bold"),
                             fg='white', height=2, width=30,
                             command=self.admingrade)
        courseButton = Button(gridFrame, relief=RIDGE, text="COURSES", bg='steel blue', font=("Verdana", 20, "bold"),
                              fg='white', height=2, width=30,
                              command=self.admincourse)

        studentButton.grid(row=0, column=0)
        professorButton.grid(row=1, column=0)
        upButton.grid(row=2, column=0, )
        gradeButton.grid(row=3, column=0)
        courseButton.grid(row=4, column=0)

        self.root.mainloop()

#function to call Student detail window for admin
    def adminstudent(self):
        self.root.destroy()
        adminstudent = AdminWindowStudent()

    #function to call professor detail window for admin
    def adminprofessor(self):
        self.root.destroy()
        adminprofessor = AdminWindowProfessor()

    #function to call admin window to add user credentials
    def adminup(self):
        self.root.destroy()
        adminup = AdminWindowUP()

    #function to call admin window to add the grades
    def admingrade(self):
        self.root.destroy()
        admingrade = AdminWindowGrades()

    def admincourse(self):
        self.root.destroy()
        admincourse = AdminWindowCourse()

#student window to view the grades.

class StudentWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x620+0+0")
        self.root.title("Results Archive")
        self.root.configure(relief=RIDGE, bg='steel blue')
        self.root.resizable(0, 0)

        self.result = backendProject.StudentGrades()
        self.Name = StringVar()

        topFrame = Frame(self.root, bg='SteelBlue4', height=120, width=1000)
        topFrame.place(x=0, y=0)

        univLabel = Label(topFrame, bg='SteelBlue4', text="JAWAN UNIVERSITY", font=("Verdana", 26, "bold"),
                          fg='black')
        univLabel.place(x=18, y=32)

        entryFrame = Frame(self.root, bg='steel blue', height=430, width=390)
        entryFrame.place(x=10, y=130)

        welcomelabel = Label(entryFrame, text="Welcome,", bg="steel blue", font=("arial", 14, "bold"))
        welcomelabel.place(x=10, y=25)

        label = Label(entryFrame, text="Enter your name below to get results!", bg="steel blue",
                      font=("arial", 12, "bold"))
        label.place(x=10, y=70)

        nameLabel = Label(entryFrame, bg="steel blue", text="Enter name:", font=("arial", 14, "bold"))
        nameLabel.place(x=11, y=165)

        self.nameEntry = Entry(entryFrame, font=("arial", 14, "bold"), textvariable=self.Name, relief=RIDGE, bd=2)
        self.nameEntry.place(x=136, y=167)

        submitButton = Button(entryFrame, text="Submit", bd=1, bg="SteelBlue4", relief=GROOVE, font=("Verdana", 14),
                              command=self.getResults)
        submitButton.place(x=130, y=215)

        resultFrame = Frame(self.root, bg='dark sea green')
        resultFrame.place(x=410, y=130, height=430, width=580)

        self.scrollbar = Scrollbar(resultFrame, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.resultlist = ttk.Treeview(resultFrame, columns=("coursename", "mark", "grade"),
                                       yscrollcommand=self.scrollbar.set)
        self.resultlist.heading("coursename", text="Course", anchor='center', )
        self.resultlist.heading("mark", text="GPA", anchor='center')
        self.resultlist.heading("grade", text="Grade", anchor='center')
        self.resultlist['show'] = 'headings'

        self.resultlist.column("coursename", width=100, anchor='center')
        self.resultlist.column("mark", width=50, anchor='center')
        self.resultlist.column("grade", width=50, anchor='center')
        self.resultlist.pack(fill=BOTH, expand=1)

        self.scrollbar.config(command=self.resultlist.yview, bg='gray')

        bottomFrame = Frame(self.root, bg='SteelBlue4', height=50, width=1000)
        bottomFrame.place(x=0, y=570)

        label = Label(bottomFrame, text="Powered by JAWAN", fg='black', bg="SteelBlue4",
                      font=("Helvetica", 12, "bold"))
        label.place(x=820, y=25)

        self.root.mainloop()

    def getResults(self):
        info = self.Name.get()
        null = ""
        self.resultlist.delete(*self.resultlist.get_children())
        if (info != null):
            for row in self.result.viewGradeData(self.Name.get()):
                self.resultlist.insert('', END, values=(row[5], row[6], row[7]))

#professor window to add student data.

class ProfessorWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1105x639+0+0")
        self.root.configure(relief=RIDGE, bg='SteelBlue4', bd=3)
        self.root.title("Professor-->Update Data")
        self.root.resizable(0, 0)

        self.prof = backendProject.Grades()
        self.prof.databaseCreation()

        self.prof.GradeData()

        updateLabelFrame = Frame(self.root, bg='SteelBlue4', height=40, width=1090, relief=RIDGE, bd=1)
        updateLabelFrame.place(x=5, y=5)

        updateLabel = Label(updateLabelFrame, fg='white', bg='Steelblue4', text="GRADE DATABASE",
                            font=("arial", 17, "bold"))
        updateLabel.place(x=370, y=5)

        frame = Frame(self.root, height='490', width='400', relief=RIDGE, bg='steel blue', bd=1)
        frame.place(x=5, y=50)

        entrylabel = Label(frame, text="ENTER DATA", fg='white', bg='steel blue', font=("arial", 15))
        entrylabel.place(x=80, y=15)

        self.profID = StringVar()
        self.profName = StringVar()
        self.stdID = StringVar()
        self.stdName = StringVar()
        self.CourseID = StringVar()
        self.Coursename = StringVar()
        self.Mark = StringVar()
        self.Grade = StringVar()

        self.Searchby = StringVar()
        self.SearchEntry = StringVar()

        self.Searchby.set("Select")

        self.profidLabel = Label(frame, text="Professor Id", fg='white', bg='steel blue',
                                 font=("Helvetica", 13, "bold"))
        self.profidLabel.place(x=10, y=80)

        self.profnameLabel = Label(frame, text="Professor Name", fg='white', bg='steel blue',
                                   font=("Helvetica", 13, "bold"))
        self.profnameLabel.place(x=10, y=130)

        self.stdidLabel = Label(frame, text="Student Id", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.stdidLabel.place(x=10, y=180)

        self.stdnameLabel = Label(frame, text="Student Name", fg='white', bg='steel blue',
                                  font=("Helvetica", 13, "bold"))
        self.stdnameLabel.place(x=10, y=230)

        self.courseidLabel = Label(frame, text="Course ID", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.courseidLabel.place(x=10, y=280)

        self.coursenameLabel = Label(frame, text="Course Name", fg='white', bg='steel blue',
                                     font=("Helvetica", 13, "bold"))
        self.coursenameLabel.place(x=10, y=330)

        self.markLabel = Label(frame, text="Course GPA", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.markLabel.place(x=10, y=380)

        self.gradeLabel = Label(frame, text="Course Grade", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.gradeLabel.place(x=10, y=430)

        self.txtprofidEntry = Entry(frame, fg='black', bd=2, textvariable=self.profID, font=("sans serif", 13, "bold"))
        self.txtprofidEntry.place(x=200, y=80)

        self.txtprofnameEntry = Entry(frame, fg='black', bd=2, textvariable=self.profName,
                                      font=("sans serif", 13, "bold"))
        self.txtprofnameEntry.place(x=200, y=130)

        self.txtstudidEntry = Entry(frame, fg='black', bd=2, textvariable=self.stdID, font=("sans serif", 13, "bold"))
        self.txtstudidEntry.place(x=200, y=180)

        self.txtstudnameEntry = Entry(frame, fg='black', bd=2, textvariable=self.stdName,
                                      font=("sans serif", 13, "bold"))
        self.txtstudnameEntry.place(x=200, y=230)

        self.txtcourseidEntry = Entry(frame, fg='black', bd=2, textvariable=self.CourseID,
                                      font=("sans serif", 13, "bold"))
        self.txtcourseidEntry.place(x=200, y=280)

        self.txtcourseEntry = Entry(frame, fg='black', bd=2, textvariable=self.Coursename,
                                    font=("sans serif", 13, "bold"))
        self.txtcourseEntry.place(x=200, y=330)

        self.txtmarkEntry = Entry(frame, fg='black', font=("sans serif", 13, "bold"), bd=2, textvariable=self.Mark)
        self.txtmarkEntry.place(x=200, y=380)

        self.txtgradeEntry = Entry(frame, fg='black', bd=2, textvariable=self.Grade, font=("sans serif", 13, "bold"))
        self.txtgradeEntry.place(x=200, y=430)

        searchFrame = Frame(self.root, width=682, height='490', bg='steel blue', relief=RIDGE, bd=1)
        searchFrame.place(x=410, y=50)

        searchCombo = ttk.Combobox(searchFrame, textvariable=self.Searchby, width=8, font=('arial', 13))
        searchCombo['values'] = ("profID", "profName", "StudID", "StudName", "CourseID", "CourseName", "Grade")
        searchCombo.place(x=20, y=23)

        searchEntry = Entry(searchFrame, textvariable=self.SearchEntry, width=20, font=("arial", 14), bd=2)
        searchEntry.place(x=133, y=22)

        searchButton = Button(searchFrame, bd=2, bg='steel blue', fg='black', activebackground='steel blue',
                              relief=RIDGE, text="Search", \
                              font=("arial", 13, "bold"), command=self.searchData)
        searchButton.place(x=365, y=20)

        ShowButton = Button(searchFrame, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                            text="Show All", font=("arial", 13, "bold"),
                            relief=FLAT, command=self.displayData)
        ShowButton.place(x=455, y=20)

        buttonfframe = Frame(self.root, bg='steel blue', height=79, bd=1, width=1085, relief=RIDGE)
        buttonfframe.place(x=6, y=546)

        addButton = Button(buttonfframe, bd=2, bg='lavender', activebackground='steel blue', fg='black', text="Add",
                           font=("arial", 13, "bold"), \
                           relief=FLAT, command=self.addData)
        addButton.place(x=265, y=20)

        deleteButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                              text="Delete", font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.deleteData)
        deleteButton.place(x=350, y=20)

        clearButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue', text="Clear",
                             font=("arial", 13, "bold"),
                             relief=FLAT, command=self.clearData)
        clearButton.place(x=450, y=20)

        updateButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Update",
                              activebackground='steel blue', font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.updateData)
        updateButton.place(x=550, y=20)

        exitButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Exit", font=("arial", 13, "bold"),
                            activebackground='steel blue', \
                            relief=FLAT, command=self.root.destroy)
        exitButton.place(x=650, y=20)

        resultFrame = Frame(searchFrame, relief=RIDGE, bg='steel blue')
        resultFrame.place(x=15, y=80, height=400, width=650)

        self.scrollbarx = Scrollbar(resultFrame, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(resultFrame, orient=VERTICAL)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.scrollbary.pack(side=RIGHT, fill=Y)

        self.gradelist = ttk.Treeview(resultFrame, columns=(
        "profID", "profName", "stdID", "stdName", "courseID", "courseName", "mark", "grade"), \
                                      xscrollcommand=self.scrollbarx.set, yscrollcommand=self.scrollbary.set)
        self.gradelist.bind("<ButtonRelease-1>", self.selectCursor)
        self.scrollbarx.config(command=self.gradelist.xview, bg='grey')
        self.scrollbary.config(command=self.gradelist.yview, bg='grey', activebackground='gray45')
        self.gradelist.heading("profID", text="Professor ID", anchor="center")
        self.gradelist.heading("profName", text="Professor Name", anchor="center")
        self.gradelist.heading("stdID", text="Student ID", anchor="center")
        self.gradelist.heading("stdName", text="Student Name", anchor="center")
        self.gradelist.heading("courseID", text="Course ID", anchor="center")
        self.gradelist.heading("courseName", text="Course Name", anchor="center")
        self.gradelist.heading("mark", text="GPA", anchor="center")
        self.gradelist.heading("grade", text="Grade", anchor="center")
        self.gradelist['show'] = 'headings'

        self.gradelist.column("profID", width=100, anchor="center")
        self.gradelist.column("profName", width=100, anchor="center")
        self.gradelist.column("stdID", width=100, anchor="center")
        self.gradelist.column("stdName", width=100, anchor="center")
        self.gradelist.column("courseID", width=100, anchor="center")
        self.gradelist.column("courseName", width=100, anchor="center")
        self.gradelist.column("mark", width=100, anchor="center")
        self.gradelist.column("grade", width=100, anchor="center")

        self.gradelist.pack(fill=BOTH, expand=1)
        self.gradelist.bind("<ButtonRelease-1>", self.selectCursor)
        self.displayData()
        self.root.mainloop()

    def clearData(self):
        self.txtprofidEntry.delete(0, END)
        self.txtprofnameEntry.delete(0, END)
        self.txtstudidEntry.delete(0, END)
        self.txtstudnameEntry.delete(0, END)
        self.txtcourseidEntry.delete(0, END)
        self.txtcourseEntry.delete(0, END)
        self.txtmarkEntry.delete(0, END)
        self.txtgradeEntry.delete(0, END)

    def addData(self):
        if (len(self.profID.get()) != 0 or len(self.stdID.get()) != 0 or len(self.Coursename.get()) != 0 or len(
                self.Mark.get()) != 0 or len(self.Grade.get()) != 0):
            if ((float(self.Mark.get()) >= 0 and float(self.Mark.get()) <= 100) and self.Grade.get() != ""):
                self.prof.addGradeData(self.profID.get(), self.profName.get(), self.stdID.get(), self.stdName.get(),
                                       self.CourseID.get(), self.Coursename.get(), \
                                       self.Mark.get(), self.Grade.get())
                self.clearData()
                messagebox.showinfo("success", "data added successfully")
                self.displayData()
            else:
                messagebox.showerror("Error", "Please check the grade you have entered")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def displayData(self):
        self.gradelist.delete(*self.gradelist.get_children())
        for row in self.prof.viewGradeData():
            self.gradelist.insert('', END, values=row)

    def selectCursor(self, event):
        global info
        selection = self.gradelist.focus()
        information = self.gradelist.item(selection)
        info = information['values']

        self.txtprofidEntry.delete(0, END)
        self.txtprofidEntry.insert(END, info[0])
        self.txtprofnameEntry.delete(0, END)
        self.txtprofnameEntry.insert(END, info[1])
        self.txtstudidEntry.delete(0, END)
        self.txtstudidEntry.insert(END, info[2])
        self.txtstudnameEntry.delete(0, END)
        self.txtstudnameEntry.insert(END, info[3])
        self.txtcourseidEntry.delete(0, END)
        self.txtcourseidEntry.insert(END, info[4])
        self.txtcourseEntry.delete(0, END)
        self.txtcourseEntry.insert(END, info[5])
        self.txtmarkEntry.delete(0, END)
        self.txtmarkEntry.insert(END, info[6])
        self.txtgradeEntry.delete(0, END)
        self.txtgradeEntry.insert(END, info[7])

    def deleteData(self):
        if (len(self.profID.get()) != 0):
            self.prof.deleteGradeData(info[0],info[2])
            self.clearData()
            messagebox.showinfo("success", "data deleted successfully")
            self.displayData()

    def searchData(self):
        self.gradelist.delete(*self.gradelist.get_children())
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute(
                "SELECT * FROM GRADES WHERE " + str(self.Searchby.get()) + "= '" + str(self.SearchEntry.get()) + "'")
            rows = mycursor.fetchall()
            for row in rows:
                self.gradelist.insert('', END, values=row)
            connector.close()
        except:
            messagebox.showerror("error", "Cant search data,Please try again!")
            connector.close()

    def updateData(self):
        if (len(self.profID.get()) != 0 or len(self.stdID.get()) != 0 or len(self.Coursename.get()) != 0 or len(
                self.Mark.get()) != 0 or len(self.Grade.get()) != 0):
            self.prof.deleteGradeData(info[0],info[2])

        if (len(self.profID.get()) != 0 or len(self.stdID.get()) != 0 or len(self.Coursename.get()) != 0 or len(
                self.Mark.get()) != 0 or len(self.Grade.get()) != 0):

            self.prof.addGradeData(self.profID.get(), self.profName.get(), self.stdID.get(), self.stdName.get(), \
                                   self.CourseID.get(), self.Coursename.get(), self.Mark.get(), self.Grade.get())
            self.clearData()
            messagebox.showinfo("success", "data updated successfully")
            self.displayData()
        else:
            messagebox.showerror("Required", "All fields are required!!")

#admin window to update student data

class AdminWindowStudent:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1105x639+0+0")
        self.root.configure(relief=RIDGE, bg='SteelBlue4', bd=3)
        self.root.resizable(0, 0)
        self.root.title("Admin-->Students")

        # creating object for student class to add student data ,calling the functions to create database and student table.

        self.stud = backendProject.Student()
        self.stud.databaseCreation()
        self.stud.StudentData()

        updateLabelFrame = Frame(self.root, bg='SteelBlue4', height=40, width=1090, relief=RIDGE, bd=1)
        updateLabelFrame.place(x=5, y=5)

        gobackButton = Button(updateLabelFrame, bd=1, bg='lavender', fg='black', activebackground='SteelBlue4', \
                              relief=RIDGE, text="Go back", font=("arial", 13, "bold"), command=self.returnAction)
        gobackButton.place(x=10, y=4)

        updateLabel = Label(updateLabelFrame, fg='white', bg='Steelblue4', text="STUDENT DATABASE",
                            font=("arial", 17, "bold"))
        updateLabel.place(x=370, y=5)

        frame = Frame(self.root, height='490', width='400', relief=RIDGE, bg='steel blue', bd=1)
        frame.place(x=5, y=50)

        entrylabel = Label(frame, text="ENTER DATA", fg='white', bg='steel blue', font=("arial", 15))
        entrylabel.place(x=80, y=15)

        self.stdID = StringVar()
        self.firstName = StringVar()
        self.lastName = StringVar()
        self.Email = StringVar()
        self.Gender = StringVar()
        self.Age = StringVar()
        self.Course = StringVar()
        self.Searchby = StringVar()
        self.SearchEntry = StringVar()

        self.Searchby.set("Select")

        self.idLabel = Label(frame, text="Student id", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.idLabel.place(x=10, y=80)

        self.firstnameLabel = Label(frame, text="Student First name", fg='white', bg='steel blue',
                                    font=("Helvetica", 13, "bold"))
        self.firstnameLabel.place(x=10, y=130)

        self.lastnameLabel = Label(frame, text="Student Last name", fg='white', bg='steel blue',
                                   font=("Helvetica", 13, "bold"))
        self.lastnameLabel.place(x=10, y=180)

        self.emailLabel = Label(frame, text="Student Email", fg='white', bg='steel blue',
                                font=("Helvetica", 13, "bold"))
        self.emailLabel.place(x=10, y=230)

        self.ageLabel = Label(frame, text="Student Age", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.ageLabel.place(x=10, y=280)

        self.genderLabel = Label(frame, text="Student Gender", bg='steel blue', fg='white',
                                 font=("Helvetica", 13, "bold"))
        self.genderLabel.place(x=10, y=330)

        self.courseLabel = Label(frame, text="Student Course", bg='steel blue', fg='white',
                                 font=("Helvetica", 13, "bold"))
        self.courseLabel.place(x=10, y=380)

        self.txtidEntry = Entry(frame, fg='black', bd=2, textvariable=self.stdID, font=("sans serif", 13, "bold"))
        self.txtidEntry.place(x=200, y=80)

        self.txtfirstnameEntry = Entry(frame, fg='black', bd=2, textvariable=self.firstName,
                                       font=("sans serif", 13, "bold"))
        self.txtfirstnameEntry.place(x=200, y=130)

        self.txtlastnameEntry = Entry(frame, fg='black', bd=2, textvariable=self.lastName,
                                      font=("sans serif", 13, "bold"))
        self.txtlastnameEntry.place(x=200, y=180)

        self.txtemailEntry = Entry(frame, fg='black', font=("sans serif", 13, "bold"), bd=2, textvariable=self.Email)
        self.txtemailEntry.place(x=200, y=230)

        self.txtageEntry = Entry(frame, fg='black', bd=2, textvariable=self.Age, font=("sans serif", 13, "bold"))
        self.txtageEntry.place(x=200, y=280)

        self.txtgenderEntry = Entry(frame, fg='black', bd=2, textvariable=self.Gender, font=("sans serif", 13, "bold"))
        self.txtgenderEntry.place(x=200, y=330)

        self.txtcourseEntry = Entry(frame, fg='black', bd=2, textvariable=self.Course, font=("sans serif", 13, "bold"))
        self.txtcourseEntry.place(x=200, y=380)

        searchFrame = Frame(self.root, width=682, height='490', bg='steel blue', relief=RIDGE, bd=1)
        searchFrame.place(x=410, y=50)

        searchCombo = ttk.Combobox(searchFrame, textvariable=self.Searchby, width=8, font=('arial', 13))
        searchCombo['values'] = ("StdID", "FirstName", "LastName", "Age", "Gender", "Course")
        searchCombo.place(x=20, y=23)

        searchEntry = Entry(searchFrame, textvariable=self.SearchEntry, width=20, font=("arial", 14), bd=2)
        searchEntry.place(x=133, y=22)

        searchButton = Button(searchFrame, bd=2, bg='steel blue', fg='black', activebackground='steel blue',
                              relief=RIDGE, text="Search", \
                              font=("arial", 13, "bold"), command=self.searchData)
        searchButton.place(x=365, y=20)

        ShowButton = Button(searchFrame, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                            text="Show All", font=("arial", 13, "bold"),
                            relief=FLAT, command=self.displayData)
        ShowButton.place(x=455, y=20)

        buttonfframe = Frame(self.root, bg='steel blue', height=79, bd=1, width=1085, relief=RIDGE)
        buttonfframe.place(x=6, y=546)

        addButton = Button(buttonfframe, bd=2, bg='lavender', activebackground='steel blue', fg='black', text="Add",font=("arial", 13, "bold"), \
                           relief=FLAT, command=self.addData)
        addButton.place(x=265, y=20)

        deleteButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                              text="Delete", font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.deleteData)
        deleteButton.place(x=350, y=20)

        clearButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue', text="Clear",
                             font=("arial", 13, "bold"),
                             relief=FLAT, command=self.clearData)
        clearButton.place(x=450, y=20)

        updateButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Update",
                              activebackground='steel blue', font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.updateData)
        updateButton.place(x=550, y=20)

        exitButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Exit", font=("arial", 13, "bold"),
                            activebackground='steel blue', \
                            relief=FLAT, command=self.root.destroy)
        exitButton.place(x=650, y=20)

        resultFrame = Frame(searchFrame, relief=RIDGE, bg='steel blue')
        resultFrame.place(x=15, y=80, height=400, width=650)

        #adding scrollbar to the UI

        self.scrollbarx = Scrollbar(resultFrame, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(resultFrame, orient=VERTICAL)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.scrollbary.pack(side=RIGHT, fill=Y)

        #Adding Treeview widget to the UI

        self.studentlist = ttk.Treeview(resultFrame,columns=("stdID", "Firstname", "Lastname", "Email", "Age", "Gender", "Course"), \
                                        xscrollcommand=self.scrollbarx.set, yscrollcommand=self.scrollbary.set)
        self.studentlist.bind("<ButtonRelease-1>", self.selectCursor)
        self.scrollbarx.config(command=self.studentlist.xview, bg='grey')
        self.scrollbary.config(command=self.studentlist.yview, bg='grey', activebackground='gray45')
        self.studentlist.heading("stdID", text="id", anchor="center")
        self.studentlist.heading("Firstname", text="Firstname", anchor="center")
        self.studentlist.heading("Lastname", text="Lastname", anchor="center")
        self.studentlist.heading("Email", text="Email", anchor="center")
        self.studentlist.heading("Age", text="Age", anchor="center")
        self.studentlist.heading("Gender", text="Gender", anchor="center")
        self.studentlist.heading("Course", text="Course", anchor="center")
        self.studentlist['show'] = 'headings'

        self.studentlist.column("stdID", width=150, anchor="center")
        self.studentlist.column("Firstname", width=150, anchor="center")
        self.studentlist.column("Lastname", width=150, anchor="center")
        self.studentlist.column("Email", width=250, anchor="center")
        self.studentlist.column("Age", width=150, anchor="center")
        self.studentlist.column("Gender", width=150, anchor="center")
        self.studentlist.column("Course", width=150, anchor="center")

        self.studentlist.pack(fill=BOTH, expand=1)

        #Event handling

        self.studentlist.bind("<ButtonRelease-1>", self.selectCursor)
        self.displayData()
        self.root.mainloop()

    def returnAction(self):
        exit = messagebox.askyesno("GO BACK", "Confirm if you want to go previous window")
        if exit > 0:
            self.root.destroy()
            admin = AdminWindow()
            return

    #function to clear the entry fields

    def clearData(self):
        self.txtidEntry.delete(0, END)
        self.txtfirstnameEntry.delete(0, END)
        self.txtlastnameEntry.delete(0, END)
        self.txtemailEntry.delete(0, END)
        self.txtageEntry.delete(0, END)
        self.txtgenderEntry.delete(0, END)
        self.txtcourseEntry.delete(0, END)

    #function to add data to the database

    def addData(self):
        if (len(self.stdID.get()) != 0):
            self.stud.addStdData(self.stdID.get(), self.firstName.get(), self.lastName.get(), self.Email.get(),
                                 self.Age.get(), \
                                 self.Gender.get(), self.Course.get())
            self.clearData()
            self.displayData()
            messagebox.showinfo("success", "Data added successfully")
        else:
            messagebox.showerror("Student Id Required", "Please enter student ID")

    #function to display data in the UI

    def displayData(self):
        self.studentlist.delete(*self.studentlist.get_children())
        for row in self.stud.viewStdData():
            self.studentlist.insert('', END, values=row)

    #function to handle a click event in the treeview widget

    def selectCursor(self, event):
        global info
        selection = self.studentlist.focus()
        information = self.studentlist.item(selection)
        info = information['values']

        self.txtidEntry.delete(0, END)
        self.txtidEntry.insert(END, info[0])
        self.txtfirstnameEntry.delete(0, END)
        self.txtfirstnameEntry.insert(END, info[1])
        self.txtlastnameEntry.delete(0, END)
        self.txtlastnameEntry.insert(END, info[2])
        self.txtemailEntry.delete(0, END)
        self.txtemailEntry.insert(END, info[3])
        self.txtageEntry.delete(0, END)
        self.txtageEntry.insert(END, info[4])
        self.txtgenderEntry.delete(0, END)
        self.txtgenderEntry.insert(END, info[5])
        self.txtcourseEntry.delete(0, END)
        self.txtcourseEntry.insert(END, info[6])

    #function to delete data from the database

    def deleteData(self):
        if (len(self.stdID.get()) != 0):
            self.stud.deleteStdData(info[0])
            self.clearData()
            self.displayData()
            messagebox.showinfo("success", "Data deleted Successfully!")

    #function to sort data in the UI according to the user needs.

    def searchData(self):
        self.studentlist.delete(*self.studentlist.get_children())
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute(
                "SELECT * FROM student WHERE " + str(self.Searchby.get()) + "= '" + str(self.SearchEntry.get()) + "'")
            rows = mycursor.fetchall()
            for row in rows:
                self.studentlist.insert('', END, values=row)
            connector.close()
        except exception:
            connector.close()

    #function to update the data.

    def updateData(self):
        if (len(self.stdID.get()) != 0):
            self.stud.deleteStdData(info[0])
        if (len(self.stdID.get()) != 0):
            self.stud.addStdData(self.stdID.get(), self.firstName.get(), self.lastName.get(), self.Email.get(), \
                                 self.Age.get(), self.Gender.get(), self.Course.get())
            self.clearData()
            self.displayData()
            messagebox.showinfo("success", "Data updated successfully")
        else:
            messagebox.showerror("Student Id Required", "Please enter student ID")

#admin window to update professor data

class AdminWindowProfessor:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1105x639+0+0")
        self.root.configure(relief=RIDGE, bg='SteelBlue4', bd=3)
        self.root.resizable(0, 0)
        self.root.title("Admin-->Professor")

        self.prof = backendProject.Professor()
        self.prof.databaseCreation()
        self.prof.ProfessorData()

        updateLabelFrame = Frame(self.root, bg='SteelBlue4', height=40, width=1090, relief=RIDGE, bd=1)
        updateLabelFrame.place(x=5, y=5)

        gobackButton = Button(updateLabelFrame, bd=1, bg='lavender', fg='black', activebackground='SteelBlue4', \
                              relief=RIDGE, text="Go back", font=("arial", 13, "bold"), command=self.returnAction)
        gobackButton.place(x=10, y=4)

        updateLabel = Label(updateLabelFrame, fg='white', bg='Steelblue4', text="PROFESSOR DATABASE",
                            font=("arial", 17, "bold"))
        updateLabel.place(x=370, y=5)

        frame = Frame(self.root, height='490', width='400', relief=RIDGE, bg='steel blue', bd=1)
        frame.place(x=5, y=50)

        entrylabel = Label(frame, text="ENTER DATA", fg='white', bg='steel blue', font=("arial", 15))
        entrylabel.place(x=80, y=15)

        self.profID = StringVar()
        self.firstName = StringVar()
        self.lastName = StringVar()
        self.Email = StringVar()
        self.Gender = StringVar()
        self.Age = StringVar()
        self.Mobile = StringVar()
        self.Searchby = StringVar()
        self.SearchEntry = StringVar()

        self.Searchby.set("Select")

        self.idLabel = Label(frame, text="Professor id", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.idLabel.place(x=10, y=80)

        self.firstnameLabel = Label(frame, text="Professor First name", fg='white', bg='steel blue',
                                    font=("Helvetica", 13, "bold"))
        self.firstnameLabel.place(x=10, y=130)

        self.lastnameLabel = Label(frame, text="Professor Last name", fg='white', bg='steel blue',
                                   font=("Helvetica", 13, "bold"))
        self.lastnameLabel.place(x=10, y=180)

        self.emailLabel = Label(frame, text="Professor Email", fg='white', bg='steel blue',
                                font=("Helvetica", 13, "bold"))
        self.emailLabel.place(x=10, y=230)

        self.ageLabel = Label(frame, text="Professor Age", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.ageLabel.place(x=10, y=280)

        self.genderLabel = Label(frame, text="Professor Gender", bg='steel blue', fg='white',
                                 font=("Helvetica", 13, "bold"))
        self.genderLabel.place(x=10, y=330)

        self.mobileLabel = Label(frame, text="Professor Mobile", bg='steel blue', fg='white',
                                 font=("Helvetica", 13, "bold"))
        self.mobileLabel.place(x=10, y=380)

        self.txtidEntry = Entry(frame, fg='black', bd=2, textvariable=self.profID, font=("sans serif", 13, "bold"))
        self.txtidEntry.place(x=200, y=80)

        self.txtfirstnameEntry = Entry(frame, fg='black', bd=2, textvariable=self.firstName,
                                       font=("sans serif", 13, "bold"))
        self.txtfirstnameEntry.place(x=200, y=130)

        self.txtlastnameEntry = Entry(frame, fg='black', bd=2, textvariable=self.lastName,
                                      font=("sans serif", 13, "bold"))
        self.txtlastnameEntry.place(x=200, y=180)

        self.txtemailEntry = Entry(frame, fg='black', font=("sans serif", 13, "bold"), bd=2, textvariable=self.Email)
        self.txtemailEntry.place(x=200, y=230)

        self.txtageEntry = Entry(frame, fg='black', bd=2, textvariable=self.Age, font=("sans serif", 13, "bold"))
        self.txtageEntry.place(x=200, y=280)

        self.txtgenderEntry = Entry(frame, fg='black', bd=2, textvariable=self.Gender, font=("sans serif", 13, "bold"))
        self.txtgenderEntry.place(x=200, y=330)

        self.txtmobileEntry = Entry(frame, fg='black', bd=2, textvariable=self.Mobile, font=("sans serif", 13, "bold"))
        self.txtmobileEntry.place(x=200, y=380)

        searchFrame = Frame(self.root, width=682, height='490', bg='steel blue', relief=RIDGE, bd=1)
        searchFrame.place(x=410, y=50)

        searchCombo = ttk.Combobox(searchFrame, textvariable=self.Searchby, width=8, font=('arial', 13))
        searchCombo['values'] = ("profID", "FirstName", "LastName", "Age", "Gender")
        searchCombo.place(x=20, y=23)

        searchEntry = Entry(searchFrame, textvariable=self.SearchEntry, width=20, font=("arial", 14), bd=2)
        searchEntry.place(x=133, y=22)

        searchButton = Button(searchFrame, bd=2, bg='steel blue', fg='black', activebackground='steel blue',
                              relief=RIDGE, text="Search", \
                              font=("arial", 13, "bold"), command=self.searchData)
        searchButton.place(x=365, y=20)

        ShowButton = Button(searchFrame, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                            text="Show All", font=("arial", 13, "bold"),
                            relief=FLAT, command=self.displayData)
        ShowButton.place(x=455, y=20)

        buttonfframe = Frame(self.root, bg='steel blue', height=79, bd=1, width=1085, relief=RIDGE)
        buttonfframe.place(x=6, y=546)

        addButton = Button(buttonfframe, bd=2, bg='lavender', activebackground='steel blue', fg='black', text="Add",
                           font=("arial", 13, "bold"), \
                           relief=FLAT, command=self.addData)
        addButton.place(x=265, y=20)

        deleteButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                              text="Delete", font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.deleteData)
        deleteButton.place(x=350, y=20)

        clearButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue', text="Clear",
                             font=("arial", 13, "bold"),
                             relief=FLAT, command=self.clearData)
        clearButton.place(x=450, y=20)

        updateButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Update",
                              activebackground='steel blue', font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.updateData)
        updateButton.place(x=550, y=20)

        exitButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Exit", font=("arial", 13, "bold"),
                            activebackground='steel blue', \
                            relief=FLAT, command=self.root.destroy)
        exitButton.place(x=650, y=20)

        resultFrame = Frame(searchFrame, relief=RIDGE, bg='steel blue')
        resultFrame.place(x=15, y=80, height=400, width=650)

        self.scrollbarx = Scrollbar(resultFrame, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(resultFrame, orient=VERTICAL)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.scrollbary.pack(side=RIGHT, fill=Y)

        self.proflist = ttk.Treeview(resultFrame,
                                     columns=("profID", "Firstname", "Lastname", "Email", "Age", "Gender", "Mobile"), \
                                     xscrollcommand=self.scrollbarx.set, yscrollcommand=self.scrollbary.set)
        self.proflist.bind("<ButtonRelease-1>", self.selectCursor)
        self.scrollbarx.config(command=self.proflist.xview, bg='grey')
        self.scrollbary.config(command=self.proflist.yview, bg='grey', activebackground='gray45')
        self.proflist.heading("profID", text="profID", anchor="center")
        self.proflist.heading("Firstname", text="Firstname", anchor="center")
        self.proflist.heading("Lastname", text="Lastname", anchor="center")
        self.proflist.heading("Email", text="Email", anchor="center")
        self.proflist.heading("Age", text="Age", anchor="center")
        self.proflist.heading("Gender", text="Gender", anchor="center")
        self.proflist.heading("Mobile", text="Mobile", anchor="center")
        self.proflist['show'] = 'headings'

        self.proflist.column("profID", width=150, anchor="center")
        self.proflist.column("Firstname", width=150, anchor="center")
        self.proflist.column("Lastname", width=150, anchor="center")
        self.proflist.column("Email", width=250, anchor="center")
        self.proflist.column("Age", width=150, anchor="center")
        self.proflist.column("Gender", width=150, anchor="center")
        self.proflist.column("Mobile", width=150, anchor="center")

        self.proflist.pack(fill=BOTH, expand=1)
        self.proflist.bind("<ButtonRelease-1>", self.selectCursor)
        self.displayData()
        self.root.mainloop()

    def returnAction(self):
        exit = messagebox.askyesno("GO BACK", "Confirm if you want to go previous window")
        if exit > 0:
            self.root.destroy()
            admin = AdminWindow()
            return

    def clearData(self):
        self.txtidEntry.delete(0, END)
        self.txtfirstnameEntry.delete(0, END)
        self.txtlastnameEntry.delete(0, END)
        self.txtemailEntry.delete(0, END)
        self.txtageEntry.delete(0, END)
        self.txtgenderEntry.delete(0, END)
        self.txtmobileEntry.delete(0, END)

    def addData(self):
        if (len(self.profID.get()) != 0):
            self.prof.addProfData(self.profID.get(), self.firstName.get(), self.lastName.get(), self.Email.get(),
                                  self.Age.get(), \
                                  self.Gender.get(), self.Mobile.get())
            self.clearData()
            messagebox.showinfo("success", "Data added successfully")
            self.displayData()
        else:
            messagebox.showerror("Professor Id Required", "Please enter Professor ID")

    def displayData(self):
        self.proflist.delete(*self.proflist.get_children())
        for row in self.prof.viewProfData():
            self.proflist.insert('', END, values=row)

    def selectCursor(self, event):
        global info
        selection = self.proflist.focus()
        information = self.proflist.item(selection)
        info = information['values']

        self.txtidEntry.delete(0, END)
        self.txtidEntry.insert(END, info[0])
        self.txtfirstnameEntry.delete(0, END)
        self.txtfirstnameEntry.insert(END, info[1])
        self.txtlastnameEntry.delete(0, END)
        self.txtlastnameEntry.insert(END, info[2])
        self.txtemailEntry.delete(0, END)
        self.txtemailEntry.insert(END, info[3])
        self.txtageEntry.delete(0, END)
        self.txtageEntry.insert(END, info[4])
        self.txtgenderEntry.delete(0, END)
        self.txtgenderEntry.insert(END, info[5])
        self.txtmobileEntry.delete(0, END)
        self.txtmobileEntry.insert(END, info[6])

    def deleteData(self):
        if (len(self.profID.get()) != 0):
            self.prof.deleteProfData(info[0])
            self.clearData()
            messagebox.showinfo("success", "Data deleted successfully")
            self.displayData()

    def searchData(self):
        self.proflist.delete(*self.proflist.get_children())
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute(
                "SELECT * FROM PROFESSOR WHERE " + str(self.Searchby.get()) + "= '" + str(self.SearchEntry.get()) + "'")
            rows = mycursor.fetchall()
            for row in rows:
                self.proflist.insert('', END, values=row)
            connector.close()
        except:
            messagebox.showerror("Error", "Please search again!")
            connector.close()

    def updateData(self):
        if (len(self.profID.get()) != 0):
            self.prof.deleteProfData(info[0])
        if (len(self.profID.get()) != 0):
            self.prof.addProfData(self.profID.get(), self.firstName.get(), self.lastName.get(), self.Email.get(), \
                                  self.Age.get(), self.Gender.get(), self.Mobile.get())
            self.clearData()
            messagebox.showinfo("success", "Data updated successfully")
            self.displayData()
        else:
            messagebox.showerror("Professor Id Required", "Please enter professor ID")

#admin window to update grades

class AdminWindowGrades:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1105x639+0+0")
        self.root.configure(relief=RIDGE, bg='SteelBlue4', bd=3)
        self.root.title("Admin-->Grades")
        self.root.resizable(0, 0)

        self.grade = backendProject.Grades()
        self.grade.databaseCreation()
        self.grade.GradeData()

        updateLabelFrame = Frame(self.root, bg='SteelBlue4', height=40, width=1090, relief=RIDGE, bd=1)
        updateLabelFrame.place(x=5, y=5)

        gobackButton = Button(updateLabelFrame, bd=1, bg='lavender', fg='black', activebackground='SteelBlue4', \
                              relief=RIDGE, text="Go back", font=("arial", 13, "bold"), command=self.returnAction)
        gobackButton.place(x=10, y=4)

        updateLabel = Label(updateLabelFrame, fg='white', bg='Steelblue4', text="GRADE DATABASE",
                            font=("arial", 17, "bold"))
        updateLabel.place(x=370, y=5)

        frame = Frame(self.root, height='490', width='400', relief=RIDGE, bg='steel blue', bd=1)
        frame.place(x=5, y=50)

        entrylabel = Label(frame, text="ENTER DATA", fg='white', bg='steel blue', font=("arial", 15))
        entrylabel.place(x=80, y=15)

        self.profID = StringVar()
        self.profName = StringVar()
        self.stdID = StringVar()
        self.stdName = StringVar()
        self.CourseID = StringVar()
        self.Coursename = StringVar()
        self.Mark = StringVar()
        self.Grade = StringVar()

        self.Searchby = StringVar()
        self.SearchEntry = StringVar()

        self.Searchby.set("Select")

        self.profidLabel = Label(frame, text="Professor Id", fg='white', bg='steel blue',
                                 font=("Helvetica", 13, "bold"))
        self.profidLabel.place(x=10, y=80)

        self.profnameLabel = Label(frame, text="Professor Name", fg='white', bg='steel blue',
                                   font=("Helvetica", 13, "bold"))
        self.profnameLabel.place(x=10, y=130)

        self.stdidLabel = Label(frame, text="Student Id", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.stdidLabel.place(x=10, y=180)

        self.stdnameLabel = Label(frame, text="Student Name", fg='white', bg='steel blue',
                                  font=("Helvetica", 13, "bold"))
        self.stdnameLabel.place(x=10, y=230)

        self.courseidLabel = Label(frame, text="Course ID", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.courseidLabel.place(x=10, y=280)

        self.coursenameLabel = Label(frame, text="Course Name", fg='white', bg='steel blue',
                                     font=("Helvetica", 13, "bold"))
        self.coursenameLabel.place(x=10, y=330)

        self.markLabel = Label(frame, text="Course GPA", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.markLabel.place(x=10, y=380)

        self.gradeLabel = Label(frame, text="Course Grade", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.gradeLabel.place(x=10, y=430)

        self.txtprofidEntry = Entry(frame, fg='black', bd=2, textvariable=self.profID, font=("sans serif", 13, "bold"))
        self.txtprofidEntry.place(x=200, y=80)

        self.txtprofnameEntry = Entry(frame, fg='black', bd=2, textvariable=self.profName,
                                      font=("sans serif", 13, "bold"))
        self.txtprofnameEntry.place(x=200, y=130)

        self.txtstudidEntry = Entry(frame, fg='black', bd=2, textvariable=self.stdID, font=("sans serif", 13, "bold"))
        self.txtstudidEntry.place(x=200, y=180)

        self.txtstudnameEntry = Entry(frame, fg='black', bd=2, textvariable=self.stdName,
                                      font=("sans serif", 13, "bold"))
        self.txtstudnameEntry.place(x=200, y=230)

        self.txtcourseidEntry = Entry(frame, fg='black', bd=2, textvariable=self.CourseID,
                                      font=("sans serif", 13, "bold"))
        self.txtcourseidEntry.place(x=200, y=280)

        self.txtcourseEntry = Entry(frame, fg='black', bd=2, textvariable=self.Coursename,
                                    font=("sans serif", 13, "bold"))
        self.txtcourseEntry.place(x=200, y=330)

        self.txtmarkEntry = Entry(frame, fg='black', font=("sans serif", 13, "bold"), bd=2, textvariable=self.Mark)
        self.txtmarkEntry.place(x=200, y=380)

        self.txtgradeEntry = Entry(frame, fg='black', bd=2, textvariable=self.Grade, font=("sans serif", 13, "bold"))
        self.txtgradeEntry.place(x=200, y=430)

        searchFrame = Frame(self.root, width=682, height='490', bg='steel blue', relief=RIDGE, bd=1)
        searchFrame.place(x=410, y=50)

        searchCombo = ttk.Combobox(searchFrame, textvariable=self.Searchby, width=8, font=('arial', 13))
        searchCombo['values'] = ("profID", "profName", "StudID", "StudName", "CourseID", "CourseName", "Grade")
        searchCombo.place(x=20, y=23)

        searchEntry = Entry(searchFrame, textvariable=self.SearchEntry, width=20, font=("arial", 14), bd=2)
        searchEntry.place(x=133, y=22)

        searchButton = Button(searchFrame, bd=2, bg='steel blue', fg='black', activebackground='steel blue',
                              relief=RIDGE, text="Search", \
                              font=("arial", 13, "bold"), command=self.searchData)
        searchButton.place(x=365, y=20)

        ShowButton = Button(searchFrame, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                            text="Show All", font=("arial", 13, "bold"),
                            relief=FLAT, command=self.displayData)
        ShowButton.place(x=455, y=20)

        buttonfframe = Frame(self.root, bg='steel blue', height=79, bd=1, width=1085, relief=RIDGE)
        buttonfframe.place(x=6, y=546)

        addButton = Button(buttonfframe, bd=2, bg='lavender', activebackground='steel blue', fg='black', text="Add",
                           font=("arial", 13, "bold"), \
                           relief=FLAT, command=self.addData)
        addButton.place(x=265, y=20)

        deleteButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                              text="Delete", font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.deleteData)
        deleteButton.place(x=350, y=20)

        clearButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue', text="Clear",
                             font=("arial", 13, "bold"),
                             relief=FLAT, command=self.clearData)
        clearButton.place(x=450, y=20)

        updateButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Update",
                              activebackground='steel blue', font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.updateData)
        updateButton.place(x=550, y=20)

        exitButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Exit", font=("arial", 13, "bold"),
                            activebackground='steel blue', \
                            relief=FLAT, command=self.root.destroy)
        exitButton.place(x=650, y=20)

        resultFrame = Frame(searchFrame, relief=RIDGE, bg='steel blue')
        resultFrame.place(x=15, y=80, height=400, width=650)

        self.scrollbarx = Scrollbar(resultFrame, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(resultFrame, orient=VERTICAL)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.scrollbary.pack(side=RIGHT, fill=Y)

        self.gradelist = ttk.Treeview(resultFrame, columns=(
        "profID", "profName", "stdID", "stdName", "courseID", "courseName", "mark", "grade"), \
                                      xscrollcommand=self.scrollbarx.set, yscrollcommand=self.scrollbary.set)
        self.gradelist.bind("<ButtonRelease-1>", self.selectCursor)
        self.scrollbarx.config(command=self.gradelist.xview, bg='grey')
        self.scrollbary.config(command=self.gradelist.yview, bg='grey', activebackground='gray45')
        self.gradelist.heading("profID", text="Professor ID", anchor="center")
        self.gradelist.heading("profName", text="Professor Name", anchor="center")
        self.gradelist.heading("stdID", text="Student ID", anchor="center")
        self.gradelist.heading("stdName", text="Student Name", anchor="center")
        self.gradelist.heading("courseID", text="Course ID", anchor="center")
        self.gradelist.heading("courseName", text="Course Name", anchor="center")
        self.gradelist.heading("mark", text="GPA", anchor="center")
        self.gradelist.heading("grade", text="Grade", anchor="center")
        self.gradelist['show'] = 'headings'

        self.gradelist.column("profID", width=150, anchor="center")
        self.gradelist.column("profName", width=150, anchor="center")
        self.gradelist.column("stdID", width=150, anchor="center")
        self.gradelist.column("stdName", width=150, anchor="center")
        self.gradelist.column("courseID", width=150, anchor="center")
        self.gradelist.column("courseName", width=150, anchor="center")
        self.gradelist.column("mark", width=150, anchor="center")
        self.gradelist.column("grade", width=150, anchor="center")

        self.gradelist.pack(fill=BOTH, expand=1)
        self.gradelist.bind("<ButtonRelease-1>", self.selectCursor)
        self.displayData()
        self.root.mainloop()

    def returnAction(self):
        exit = messagebox.askyesno("GO BACK", "Confirm if you want to go previous window")
        if exit > 0:
            self.root.destroy()
            admin = AdminWindow()
            return

    def clearData(self):
        self.txtprofidEntry.delete(0, END)
        self.txtprofnameEntry.delete(0, END)
        self.txtstudidEntry.delete(0, END)
        self.txtstudnameEntry.delete(0, END)
        self.txtcourseidEntry.delete(0, END)
        self.txtcourseEntry.delete(0, END)
        self.txtmarkEntry.delete(0, END)
        self.txtgradeEntry.delete(0, END)

    def addData(self):
        if (len(self.profID.get()) != 0 or len(self.stdID.get()) != 0 or len(self.Coursename.get()) != 0 or len(
                self.Mark.get()) != 0 or len(self.Grade.get()) != 0):
            if ((float(self.Mark.get()) >= 0 and float(self.Mark.get()) <= 100) and self.Grade.get() != ""):
                self.grade.addGradeData(self.profID.get(), self.profName.get(), self.stdID.get(), self.stdName.get(),
                                        self.CourseID.get(), self.Coursename.get(), \
                                        self.Mark.get(), self.Grade.get())
                self.clearData()
                self.displayData()
            else:
                messagebox.showerror("Error", "Please check the grade you have entered")
        else:
            messagebox.showerror("Error", "All fields are required!")

    def displayData(self):
        self.gradelist.delete(*self.gradelist.get_children())
        for row in self.grade.viewGradeData():
            self.gradelist.insert('', END, values=row)

    def selectCursor(self, event):
        global info
        selection = self.gradelist.focus()
        information = self.gradelist.item(selection)
        info = information['values']

        self.txtprofidEntry.delete(0, END)
        self.txtprofidEntry.insert(END, info[0])
        self.txtprofnameEntry.delete(0, END)
        self.txtprofnameEntry.insert(END, info[1])
        self.txtstudidEntry.delete(0, END)
        self.txtstudidEntry.insert(END, info[2])
        self.txtstudnameEntry.delete(0, END)
        self.txtstudnameEntry.insert(END, info[3])
        self.txtcourseidEntry.delete(0, END)
        self.txtcourseidEntry.insert(END, info[4])
        self.txtcourseEntry.delete(0, END)
        self.txtcourseEntry.insert(END, info[5])
        self.txtmarkEntry.delete(0, END)
        self.txtmarkEntry.insert(END, info[6])
        self.txtgradeEntry.delete(0, END)
        self.txtgradeEntry.insert(END, info[7])

    def deleteData(self):
        if (len(self.profID.get()) != 0):
            self.grade.deleteGradeData(info[0],info[2])
            self.clearData()
            messagebox.showinfo("success", "data deleted successfully")
            self.displayData()

    def searchData(self):
        self.gradelist.delete(*self.gradelist.get_children())
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute(
                "SELECT * FROM GRADES WHERE " + str(self.Searchby.get()) + "= '" + str(self.SearchEntry.get()) + "'")
            rows = mycursor.fetchall()
            for row in rows:
                self.gradelist.insert('', END, values=row)
            connector.close()
        except:
            messagebox.showerror("error", "Cant search data,Please try again!")
            connector.close()

    def updateData(self):
        if (len(self.profID.get()) != 0 or len(self.stdID.get()) != 0 or len(self.Coursename.get()) != 0 or len(
                self.Mark.get()) != 0 or len(self.Grade.get()) != 0):
            self.grade.deleteGradeData(info[0],info[2])

        if (len(self.profID.get()) != 0 or len(self.stdID.get()) != 0 or len(self.Coursename.get()) != 0 or len(
                self.Mark.get()) != 0 or len(self.Grade.get()) != 0):

            self.grade.addGradeData(self.profID.get(), self.profName.get(), self.stdID.get(), self.stdName.get(),
                                    self.CourseID.get(), \
                                    self.Coursename.get(), self.Mark.get(), self.Grade.get())
            self.clearData()
            messagebox.showinfo("success", "data updated successfully")
            self.displayData()
        else:
            messagebox.showerror("Required", "All fields are required!!")

#admin window to add user credentials.

class AdminWindowUP:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1105x639+0+0")
        self.root.configure(relief=RIDGE, bg='SteelBlue4', bd=3)
        self.root.title("Admin-->Username Password")
        self.root.resizable(0, 0)

        self.up = backendProject.UsernamePassword()
        self.up.databaseCreation()
        self.up.upData()

        updateLabelFrame = Frame(self.root, bg='SteelBlue4', height=40, width=1090, relief=RIDGE, bd=1)
        updateLabelFrame.place(x=5, y=5)

        gobackButton = Button(updateLabelFrame, bd=1, bg='lavender', fg='black', activebackground='SteelBlue4', \
                              relief=RIDGE, text="Go back", font=("arial", 13, "bold"), command=self.returnAction)
        gobackButton.place(x=10, y=4)

        updateLabel = Label(updateLabelFrame, fg='white', bg='Steelblue4', text="VALIDATION DATABASE",
                            font=("arial", 17, "bold"))
        updateLabel.place(x=370, y=5)

        frame = Frame(self.root, height='490', width='400', relief=RIDGE, bg='steel blue', bd=1)
        frame.place(x=5, y=50)

        entrylabel = Label(frame, text="ENTER DATA", fg='white', bg='steel blue', font=("arial", 15))
        entrylabel.place(x=80, y=15)

        self.Usertype = StringVar()
        self.Username = StringVar()
        self.Password = StringVar()

        self.Searchby = StringVar()
        self.SearchEntry = StringVar()

        self.Usertype.set("select")
        self.Searchby.set("Select")

        self.usertypeLabel = Label(frame, text="Usertype", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.usertypeLabel.place(x=10, y=80)

        self.usernameLabel = Label(frame, text="Username", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.usernameLabel.place(x=10, y=130)

        self.passwordLabel = Label(frame, text="Password", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.passwordLabel.place(x=10, y=180)

        self.usertypeEntry = ttk.Combobox(frame, textvariable=self.Usertype, width=8, font=("sans serif", 13),
                                          state='readonly')
        self.usertypeEntry['values'] = ("Admin", "Professor", "Student")
        self.usertypeEntry.place(x=200, y=80)

        self.usernameEntry = Entry(frame, fg='black', bd=2, textvariable=self.Username, font=("sans serif", 13, "bold"))
        self.usernameEntry.place(x=200, y=130)

        self.passwordEntry = Entry(frame, bd=2, textvariable=self.Password, font=("sans serif", 13, "bold"))
        self.passwordEntry.place(x=200, y=180)

        searchFrame = Frame(self.root, width=682, height='490', bg='steel blue', relief=RIDGE, bd=1)
        searchFrame.place(x=410, y=50)

        searchCombo = ttk.Combobox(searchFrame, textvariable=self.Searchby, width=8, font=('arial', 13),
                                   state='readonly')
        searchCombo['values'] = ("Usertype", "Username", "Password")
        searchCombo.place(x=20, y=23)

        searchEntry = Entry(searchFrame, textvariable=self.SearchEntry, width=20, font=("arial", 14), bd=2)
        searchEntry.place(x=133, y=22)

        searchButton = Button(searchFrame, bd=2, bg='steel blue', fg='black', activebackground='steel blue',
                              relief=RIDGE, text="Search", \
                              font=("arial", 13, "bold"), command=self.searchData)
        searchButton.place(x=365, y=20)

        ShowButton = Button(searchFrame, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                            text="Show All", font=("arial", 13, "bold"),
                            relief=FLAT, command=self.displayData)
        ShowButton.place(x=455, y=20)

        buttonfframe = Frame(self.root, bg='steel blue', height=79, bd=1, width=1085, relief=RIDGE)
        buttonfframe.place(x=6, y=546)

        addButton = Button(buttonfframe, bd=2, bg='lavender', activebackground='steel blue', fg='black', text="Add",
                           font=("arial", 13, "bold"), \
                           relief=FLAT, command=self.addData)
        addButton.place(x=265, y=20)

        deleteButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                              text="Delete", font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.deleteData)
        deleteButton.place(x=350, y=20)

        clearButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue', text="Clear",
                             font=("arial", 13, "bold"),
                             relief=FLAT, command=self.clearData)
        clearButton.place(x=450, y=20)

        updateButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Update",
                              activebackground='steel blue', font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.updateData)
        updateButton.place(x=550, y=20)

        exitButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Exit", font=("arial", 13, "bold"),
                            activebackground='steel blue', \
                            relief=FLAT, command=self.root.destroy)
        exitButton.place(x=650, y=20)

        resultFrame = Frame(searchFrame, relief=RIDGE, bg='steel blue')
        resultFrame.place(x=15, y=80, height=400, width=650)

        self.scrollbarx = Scrollbar(resultFrame, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(resultFrame, orient=VERTICAL)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.scrollbary.pack(side=RIGHT, fill=Y)

        self.uplist = ttk.Treeview(resultFrame, columns=("Usertype", "Username", "Password"), \
                                   xscrollcommand=self.scrollbarx.set, yscrollcommand=self.scrollbary.set)
        self.uplist.bind("<ButtonRelease-1>", self.selectCursor)
        self.scrollbarx.config(command=self.uplist.xview, bg='grey')
        self.scrollbary.config(command=self.uplist.yview, bg='grey', activebackground='gray45')
        self.uplist.heading("Usertype", text="Usertype", anchor="center")
        self.uplist.heading("Username", text="Username", anchor="center")
        self.uplist.heading("Password", text="Password", anchor="center")
        self.uplist['show'] = 'headings'

        self.uplist.column("Usertype", width=150, anchor="center")
        self.uplist.column("Username", width=150, anchor="center")
        self.uplist.column("Password", width=150, anchor="center")

        self.uplist.pack(fill=BOTH, expand=1)
        self.uplist.bind("<ButtonRelease-1>", self.selectCursor)
        self.displayData()
        self.root.mainloop()

    def returnAction(self):
        exit = messagebox.askyesno("GO BACK", "Confirm if you want to go previous window")
        if exit > 0:
            self.root.destroy()
            admin = AdminWindow()
            return

    def clearData(self):
        self.usertypeEntry.delete(0, END)
        self.usernameEntry.delete(0, END)
        self.passwordEntry.delete(0, END)

    def addData(self):
        if (len(self.usertypeEntry.get()) != 0 or len(self.usernameEntry.get()) != 0 or len(
                self.passwordEntry.get()) != 0):

            self.up.addUPData(self.usertypeEntry.get(), self.usernameEntry.get(), self.passwordEntry.get())
            self.clearData()
            messagebox.showinfo("success", "data added successfully")
            self.displayData()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def displayData(self):
        self.uplist.delete(*self.uplist.get_children())
        for row in self.up.viewUPData():
            self.uplist.insert('', END, values=row)

    def selectCursor(self, event):
        global info
        selection = self.uplist.focus()
        information = self.uplist.item(selection)
        info = information['values']

        self.Usertype.set("select")
        self.usernameEntry.delete(0, END)
        self.usernameEntry.insert(END, info[1])
        self.passwordEntry.delete(0, END)
        self.passwordEntry.insert(END, info[2])

    def deleteData(self):
        if (len(self.Username.get()) != 0):
            self.up.deleteUPData(info[1])
            self.clearData()
            messagebox.showinfo("success", "data deleted successfully")
            self.displayData()

    def searchData(self):
        self.uplist.delete(*self.uplist.get_children())
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute("SELECT * FROM USERNAMEPASSWORD WHERE " + str(self.Searchby.get()) + "= '" + str(
                self.SearchEntry.get()) + "'")
            rows = mycursor.fetchall()
            for row in rows:
                self.uplist.insert('', END, values=row)
            connector.close()
        except exception:
            messagebox.showerror("error", "Cant search data,Please try again!")
            connector.close()

    def updateData(self):
        if (len(self.Usertype.get()) != 0 or len(self.Username.get()) != 0 or len(self.Password.get()) != 0):
            self.up.deleteUPData(info[0])

        if (len(self.Usertype.get()) != 0 or len(self.Username.get()) != 0 or len(self.Password.get()) != 0):

            self.up.addUPData(self.Usertype.get(), self.Username.get(), self.Password.get())
            self.clearData()
            messagebox.showinfo("success", "data updated successfully")
            self.displayData()
        else:
            messagebox.showerror("Required", "All fields are required!!")

#admin window to add course data

class AdminWindowCourse:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1105x639+0+0")
        self.root.configure(relief=RIDGE, bg='SteelBlue4', bd=3)
        self.root.title("Admin-->Courses")
        self.root.resizable(0, 0)

        self.course = backendProject.Courses()
        self.course.databaseCreation()
        self.course.courseData()

        updateLabelFrame = Frame(self.root, bg='SteelBlue4', height=40, width=1090, relief=RIDGE, bd=1)
        updateLabelFrame.place(x=5, y=5)

        gobackButton = Button(updateLabelFrame, bd=1, bg='lavender', fg='black', activebackground='SteelBlue4', \
                              relief=RIDGE, text="Go back", font=("arial", 13, "bold"), command=self.returnAction)
        gobackButton.place(x=10, y=4)

        updateLabel = Label(updateLabelFrame, fg='white', bg='Steelblue4', text="COURSE DATABASE",
                            font=("arial", 17, "bold"))
        updateLabel.place(x=370, y=5)

        frame = Frame(self.root, height='490', width='400', relief=RIDGE, bg='steel blue', bd=1)
        frame.place(x=5, y=50)

        entrylabel = Label(frame, text="ENTER DATA", fg='white', bg='steel blue', font=("arial", 15))
        entrylabel.place(x=80, y=15)

        self.CourseID = StringVar()
        self.Coursename = StringVar()
        self.ProfID = StringVar()
        self.ProfName = StringVar()
        self.No_of_students = StringVar
        self.Duration = StringVar

        self.Searchby = StringVar()
        self.SearchEntry = StringVar()

        self.Searchby.set("Select")

        self.courseidLabel = Label(frame, text="Course ID", fg='white', bg='steel blue', font=("Helvetica", 13, "bold"))
        self.courseidLabel.place(x=10, y=80)

        self.coursenameLabel = Label(frame, text="Course Name", fg='white', bg='steel blue',
                                     font=("Helvetica", 13, "bold"))
        self.coursenameLabel.place(x=10, y=130)

        self.profidLabel = Label(frame, text="Professor ID", fg='white', bg='steel blue',
                                 font=("Helvetica", 13, "bold"))
        self.profidLabel.place(x=10, y=180)

        self.profnameLabel = Label(frame, text="Professor Name", fg='white', bg='steel blue',
                                   font=("Helvetica", 13, "bold"))
        self.profnameLabel.place(x=10, y=230)

        self.No_of_studentsLabel = Label(frame, text="Total Students", fg='white', bg='steel blue',
                                         font=("Helvetica", 13, "bold"))
        self.No_of_studentsLabel.place(x=10, y=280)

        self.durationLabel = Label(frame, text="Duration", fg='white', bg='steel blue',
                                   font=("Helvetica", 13, "bold"))
        self.durationLabel.place(x=10, y=330)

        self.courseidEntry = Entry(frame, textvariable=self.CourseID, fg='black', bd=2, font=("sans serif", 13, "bold"))
        self.courseidEntry.place(x=200, y=80)

        self.coursenameEntry = Entry(frame, textvariable=self.Coursename, bd=2, fg='black',
                                     font=("sans serif", 13, "bold"))
        self.coursenameEntry.place(x=200, y=130)

        self.profidEntry = Entry(frame, fg='black', bd=2, textvariable=self.ProfID, font=("sans serif", 13, "bold"))
        self.profidEntry.place(x=200, y=180)

        self.profnameEntry = Entry(frame, bd=2, textvariable=self.ProfName, font=("sans serif", 13, "bold"))
        self.profnameEntry.place(x=200, y=230)

        self.no_of_Entry = Entry(frame, bd=2, textvariable=self.No_of_students, font=("sans serif", 13, "bold"))
        self.no_of_Entry.place(x=200, y=280)

        self.durationEntry = Entry(frame, bd=2, textvariable=self.Duration, font=("sans serif", 13, "bold"))
        self.durationEntry.place(x=200, y=330)

        searchFrame = Frame(self.root, width=682, height='490', bg='steel blue', relief=RIDGE, bd=1)
        searchFrame.place(x=410, y=50)

        searchCombo = ttk.Combobox(searchFrame, textvariable=self.Searchby, width=8, font=('arial', 13),
                                   state='readonly')
        searchCombo['values'] = ("CourseID", "CourseName", "ProfID", "Profname", "Duration")
        searchCombo.place(x=20, y=23)

        searchEntry = Entry(searchFrame, textvariable=self.SearchEntry, width=20, font=("arial", 14), bd=2)
        searchEntry.place(x=133, y=22)

        searchButton = Button(searchFrame, bd=2, bg='steel blue', fg='black', activebackground='steel blue',
                              relief=RIDGE, text="Search", \
                              font=("arial", 13, "bold"), command=self.searchData)
        searchButton.place(x=365, y=20)

        ShowButton = Button(searchFrame, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                            text="Show All", font=("arial", 13, "bold"),
                            relief=FLAT, command=self.displayData)
        ShowButton.place(x=455, y=20)

        buttonfframe = Frame(self.root, bg='steel blue', height=79, bd=1, width=1085, relief=RIDGE)
        buttonfframe.place(x=6, y=546)

        addButton = Button(buttonfframe, bd=2, bg='lavender', activebackground='steel blue', fg='black', text="Add",
                           font=("arial", 13, "bold"), \
                           relief=FLAT, command=self.addData)
        addButton.place(x=265, y=20)

        deleteButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue',
                              text="Delete", font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.deleteData)
        deleteButton.place(x=350, y=20)

        clearButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', activebackground='steel blue', text="Clear",
                             font=("arial", 13, "bold"),
                             relief=FLAT, command=self.clearData)
        clearButton.place(x=450, y=20)

        updateButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Update",
                              activebackground='steel blue', font=("arial", 13, "bold"), \
                              relief=FLAT, command=self.updateData)
        updateButton.place(x=550, y=20)

        exitButton = Button(buttonfframe, bd=2, bg='lavender', fg='black', text="Exit", font=("arial", 13, "bold"),
                            activebackground='steel blue', \
                            relief=FLAT, command=self.root.destroy)
        exitButton.place(x=650, y=20)

        resultFrame = Frame(searchFrame, relief=RIDGE, bg='steel blue')
        resultFrame.place(x=15, y=80, height=400, width=650)

        self.scrollbarx = Scrollbar(resultFrame, orient=HORIZONTAL)
        self.scrollbary = Scrollbar(resultFrame, orient=VERTICAL)
        self.scrollbarx.pack(side=BOTTOM, fill=X)
        self.scrollbary.pack(side=RIGHT, fill=Y)

        self.courselist = ttk.Treeview(resultFrame, columns=(
        "CourseID", "Coursename", "ProfID", "Profname", "nostudents", "Duration"), \
                                       xscrollcommand=self.scrollbarx.set, yscrollcommand=self.scrollbary.set)
        self.courselist.bind("<ButtonRelease-1>", self.selectCursor)
        self.scrollbarx.config(command=self.courselist.xview, bg='grey')
        self.scrollbary.config(command=self.courselist.yview, bg='grey', activebackground='gray45')
        self.courselist.heading("CourseID", text="Course ID", anchor="center")
        self.courselist.heading("Coursename", text="Course name", anchor="center")
        self.courselist.heading("ProfID", text="Professor ID", anchor="center")
        self.courselist.heading("Profname", text="Professor Name", anchor="center")
        self.courselist.heading("nostudents", text="Total Students", anchor="center")
        self.courselist.heading("Duration", text="Duration", anchor="center")
        self.courselist['show'] = 'headings'

        self.courselist.column("CourseID", width=150, anchor="center")
        self.courselist.column("Coursename", width=150, anchor="center")
        self.courselist.column("ProfID", width=150, anchor="center")
        self.courselist.column("Profname", width=150, anchor="center")
        self.courselist.column("nostudents", width=150, anchor="center")
        self.courselist.column("Duration", width=150, anchor="center")

        self.courselist.pack(fill=BOTH, expand=1)
        self.courselist.bind("<ButtonRelease-1>", self.selectCursor)
        self.displayData()
        self.root.mainloop()

    def returnAction(self):
        exit = messagebox.askyesno("GO BACK", "Confirm if you want to go previous window")
        if exit > 0:
            self.root.destroy()
            admin = AdminWindow()
            return

    def clearData(self):
        self.courseidEntry.delete(0, END)
        self.coursenameEntry.delete(0, END)
        self.profidEntry.delete(0, END)
        self.profnameEntry.delete(0, END)
        self.no_of_Entry.delete(0, END)
        self.durationEntry.delete(0, END)

    def addData(self):
        if (len(self.courseidEntry.get()) != 0):
            self.course.addCourseData(self.courseidEntry.get(), self.coursenameEntry.get(), self.profidEntry.get(),
                                      self.profnameEntry.get(), self.no_of_Entry.get(), \
                                      self.durationEntry.get())
            self.clearData()
            messagebox.showinfo("success", "data added successfully")
            self.displayData()
        else:
            messagebox.showerror("Error", "Please enter Course ID")

    def displayData(self):
        self.courselist.delete(*self.courselist.get_children())
        for row in self.course.viewCourseData():
            self.courselist.insert('', END, values=row)

    def selectCursor(self, event):
        global info
        selection = self.courselist.focus()
        information = self.courselist.item(selection)
        info = information['values']

        self.courseidEntry.delete(0, END)
        self.courseidEntry.insert(0, info[0])
        self.coursenameEntry.delete(0, END)
        self.coursenameEntry.insert(END, info[1])
        self.profidEntry.delete(0, END)
        self.profidEntry.insert(END, info[2])
        self.profnameEntry.delete(0, END)
        self.profnameEntry.insert(END, info[3])
        self.no_of_Entry.delete(0, END)
        self.no_of_Entry.insert(END, info[4])
        self.durationEntry.delete(0, END)
        self.durationEntry.insert(END, info[5])

    def deleteData(self):
        if (len(self.CourseID.get()) != 0):
            self.course.deleteCourseData(info[0])
            self.clearData()
            messagebox.showinfo("success", "data deleted successfully")
            self.displayData()

    def searchData(self):
        self.courselist.delete(*self.courselist.get_children())
        connector = mysql.connector.connect(
            host="localhost",
            user="Nikhil",
            passwd="Nikhil",
            database="projectdatabase"
        )
        mycursor = connector.cursor()
        try:
            mycursor.execute(
                "SELECT * FROM COURSES WHERE " + str(self.Searchby.get()) + "= '" + str(self.SearchEntry.get()) + "'")
            rows = mycursor.fetchall()
            for row in rows:
                self.courselist.insert('', END, values=row)
            connector.close()
        except exception:
            messagebox.showerror("error", "Cant search data,Please try again!")
            connector.close()

    def updateData(self):
        if (len(self.CourseID.get()) != 0):
            self.course.deleteCourseData(info[0])

        if (len(self.CourseID.get()) != 0):

            self.course.addCourseData(self.courseidEntry.get(), self.coursenameEntry.get(), self.profidEntry.get(),
                                      self.profnameEntry.get(), \
                                      self.no_of_Entry.get(), self.durationEntry.get())
            self.clearData()
            messagebox.showinfo("success", "data updated successfully")
            self.displayData()
        else:
            messagebox.showerror("Required", "All fields are required!!")

#creating object of the class and calling the class
iface = Interface()
