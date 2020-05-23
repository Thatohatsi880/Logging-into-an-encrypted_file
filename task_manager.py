from datetime import date # imports date to take into time
import datetime
# opens both the files
user_file = open("user.txt","r+")
tasks_file = open("tasks.txt","r+")

userList = []

# Replaces the new line function
login = True
while login:
    userName = input("Username: ")
    userPassword = input("Password: ")
    for userLogin in user_file:
        userList = userLogin.split(", ")
        if userList[0] == userName and userPassword ==  userList[1].replace("\n",""):
            login = False 
            break
    if login: #If the user entered credetials which are not found in 
       print("wrong credentials") 

#A function for registering a user.
#If the user input by the user is already registered, return a message and close the text file.
def r(newUsername, newPasword):
    user = open("user.txt","r")
    if newUsername in user.read():
        return "Username already exists"
        user_file.close()
    #If its not, and the confirm password is equal to the new password, register the user, and return the name and password.
    elif newPassword == confirmPassword:
        user = open("user.txt","a")
        return f"\n{newUsername}, {newPassword}"

#A function that adds a task to the tasks.txt text file.
def add_task(taskUsername, taskTitle, taskDescription, taskDuedate):
    todayDate = date.today() # takes in the computers current date
    taskCurentDate = todayDate.strftime("%d %b %Y")
    taskComplete = "No" #for every completed task to be added
    tasks = open("tasks.txt","a")
    return f"\n{taskUsername}, {taskTitle}, {taskDescription}, {taskDuedate}, {taskComplete}"

        
def view_all() : # function enables the user to view all their tasks
    for taskline in tasks_file:
       splittaskline = taskline.split(", ")
       taskView = splittaskline[1]
       AssignView = splittaskline[0]
       taskDescriptionView = splittaskline[2]
       dateAssignView = splittaskline[3]
       DueDateView = splittaskline[4] 
       CompleteView = splittaskline[5]   
       return f"Task: {taskView} \nAssigned to: {AssignView} \nTask Description:{taskDescriptionView}\nDate assigned: {dateAssignView}\nDuedate: {DueDateView} \nTask Complete: {CompleteView}"      

def  main(): # enables the user to view more details on a certain task of their choice
    tasks = open("tasks.txt","r+")
    count = 0
    for taskline in tasks:
        splitTask = taskline.split(", ")
        if splitTask[0] == userName:
            count += 1
            newtask = f"{count}: {taskline}"
            print(newtask)
        viewTask = input("Enter a specific task number you want to view: ")#Declares the user to enter the number of tasks that they wish to view
        splitTask = newtask.split(": ")
        print(splitTask)
        if viewTask == splitTask[0]:
            print (splitTask[1])
        changeTask = input("Do you want to mark the tsk as {complete} or {edit} the task? ")
        edittask = splitTask[1].rstrip("\n").split(", ")
        print(edittask)
        if changeTask.lower()=="complete":
            edittask[5].replace("No", "Yes")
            print(edittask)

if userName == "admin":
   print("\nPlease select one of the following options: \nr - register user \na - add tasks \nva - view all tasks \nvm - view my tasks \ngr - generate reports \nds - display statistics \ne - exit") 
   option = input("\nYour option: ")
#Else if the user is not "admin" options will appear.
else:
    print("\nPlease select one of the following options: \na - add tasks \nva - view all tasks \nvm - view my tasks \ne - exit")                                                                                                                                                                                                                                                                         
    option = input("\nYour option: ")

#If the user is "admin" and chooses 'r' to register a user, the user will be prompted for a new username and password.
if option.lower() == "r" and userName == "admin":
    newUserName = input("New username: ")
    newPassword = input("New password: ")
    confirmPassword = input("Confirm password: ")

    print(r(newUserName, newPassword))
    user_file.write(r(newUserName, newPassword)) 
#displays function for add_task
elif option.lower() == "a":
    taskUsername = input("Username: ")
    taskTitle = input("Title: ")
    taskDescr = input("Task Description: ")
    taskDuedate = input("Due Date (dd-mmm-yyyy): ")
    #The data about the the new task will be printed to the task.txt textfile.
    print(add_task(taskUsername,taskTitle,taskDescr,taskDuedate))
    tasks_file.write(add_task(taskUsername,taskTitle,taskDescr,taskDuedate))

elif option.lower() == "va":
    print(view_all())

#If the user chooses vm, to only view tasks assigned the the user who logged in, def viw_mine will be returned.
elif option.lower() == "vm": 
    print(main())              
#displays the function for gr
if option.lower()== "gr":
    task_Overview = open ("task_overview","w")
    user_Overview = open ("user_overview", "w")
    today = date.today()
    countTasks = 0
    countComplete = 0
    countinComplete = 0
    countCompleteOverdue = 0
    countUsers = 0
    countUserTask= 0
    countUserComplete = 0
    countUserinComplete = 0
    countUserCompleteOverdue = 0

# opens both the textfiles (task and user)
    tasks_file = open("tasks.txt","r")
    user_file = open("user.txt","r")
    
    for taskslines in tasks_file:
        countTasks += 1
        splitLines = taskslines.split(",")
        completeTask = splitLines[5].replace("\n","")
        overDueDate = today.strftime("%d %b %Y")
        dateObject = datetime.datetime.strptime(overDueDate, "%d %b %Y")
        overDueObject = datetime.datetime.strptime(splitLines[4], "%d %b %Y")
        
        #print(splitLines[4] + " and " + overDueDate)
        if completeTask == "No":
            countinComplete += 1
        elif completeTask == "Yes":
            countComplete += 1
# splits the lines 
        if completeTask == "No" and splitLines[4] < overDueDate:
            countCompleteOverdue += 1
#if task is complete
        elif completeTask == "Yes":
            countComplete += 1
# if task is complete and overdue
        if completeTask == "No" and overDueObject < dateObject:
            countOverdue += 1
#prints out percentage for both incomplete and incomplete overdue
        inCompletepercentage = (countinComplete/countTasks) * 100
        overDuepercentage = (countOverdue/countTasks) * 100
#Prints out for the task_overview textfile
    task_Overview.write(f"Total number of tasks: {countTasks}") 
    task_Overview.write(f"\nTotal number of uncompleted tasks: {countinComplete}")
    task_Overview.write(f"\nTotal number of completed tasks: {countComplete}")
    task_Overview.write(f"\nTotal number of uncomplete and overdue tasks: {countCompleteOverdue}")
    task_Overview.write(f"\nPercentage of uncomplete tasks: {inCompletepercentage:.2f}%")
    task_Overview.write(f"\nPercentage of tasks that are overdue: {overDuepercentage:.2f}%")
   #prints all for the user_Overviewfile
    user_Overview.write(f"The total number of users: {countUsers}")
    user_Overview.write(f"\nThe total number of tasks: {countTasks}")
    user_Overview.write(f"\nThe total number of tasks assigned: {countUserTask}")
    #print(f"The percentage of the total number of tasks assigned to user: {userTaskpercentage:.2f}")
    #print(f"The percentage of tasks assigned to the user and completed: {userCompletepercentage:.2f}")
    #print(f"The percentage of tasks assigned to the user and incomplete: {userinCompletepercentage:.2f}")
    #print(f"The percentage of tasks assigned to the user, incomplete and are overdue: {userinCompleteOverduepercentage:.2f}")

#If the user chooses ds, print out all the information task_overview and user_overview text files on the screen.
if option.lower() == "ds":
    task_Overview = open("task_overview.txt", "r")
    user_Overview = open("user_overview.txt", "r")
    
    print(f"\nReports generated from task_overview.txt")
    for task_OverviewLine in task_Overview:
        print(task_OverviewLine)
    #prints the task overview file
    print(f"\nReports generated from user_overview.txt")
    for user_OverviewLine in user_Overview:
        print(user_OverviewLine)
# prints the user task overview file

    task_Overview.close()
    user_Overview.close()

#Close all the text files.            
user_file.close()                                                                                                                                                                                                                                                                                                                                                                                                                                       
tasks_file.close()                         
