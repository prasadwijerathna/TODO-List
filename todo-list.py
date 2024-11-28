tasks=[]

def addTask():
    task=input("please enter task :")
    tasks.append(task)
    print(f"task '{task}' added to the list")
    
    
def listTasks():
    if not tasks:
      print("the are no tasks currently")
    else:
      print("current tasks")
      for index,task in enumerate(tasks):
          print(f"task #{index}.{task}")
          
          
def deleteTask():
    listTasks()
    try:
      taskToDelete=int(input("enter"))
      if taskToDelete>=0 and taskToDelete <len(tasks):
        tasks.pop(taskToDelete)
        print("Task {taskToDelete} has been removed")
      else:
        print("task")
    except:
        print("invalid output")
    

print("welcome todo list app")
while True:
    print("please select one of following")
    
    choice=input("what would you like to do  :")
    if(choice== "1"):
        addTask()
    elif(choice== "2"):
        deleteTask()
    elif (choice== "3"):
       listTasks() 
    elif(choice== "4"):
        break
    else:
        print("invalid input")
        
 
