from todoapp import TodoApp

"""
To - do (por hacer)
es una aplicacion que permite crear tareas
    1 - lavar platos - done: false
    2 - sacar basura - done: false

    lista de tareas
        cada tarea seria un diccionario
            id - taskid
            title - el titulo de la tarea
            done - es un valor booleano que indica si
                    la tarea ya fue terminada
"""
# la vista

print("Inicio TodoApp: \n")

# vamos a crear una instancia de la clase TodoApp
todoAppObj = TodoApp()


def showAllTasks():
    taskList = todoAppObj.getAllTasks()
    print("\n")
    if len(taskList) > 0:
        for task in taskList:
            print(task)
        print("\n")
    else:
        print("\n**no hay tareas por el momento**\n")


def createNewTask():
    print("** crear una nueva tarea **\n")
    title = input("title: ")
    todoAppObj.addNewTask(title)
    showAllTasks()


def modifyTask():
    print("** modificar la tarea ** \n")
    # solicitar al usuario el id de la tarea a modificar
    taskId = int(input("taskId: "))
    # cuando lo tenemos necesitamos la tarea (diccionario)
    currentTask = todoAppObj.getTaskById(taskId)
    # le vamos a imprimir el antiguo titulo
    print(f"old title: {currentTask['title']}")
    # con un input recibimos el nuevo titulo
    newTitle = input("new title: ")
    # enviamos la nueva informacion a ser modificada a la clase
    updateSuccess = todoAppObj.updateTask(taskId, newTitle)
    # regresamos si lo logramos
    print(f"task updated: {updateSuccess}\n")


def markTaskAsDone():
    print("** marcar la tarea como termianda ** \n")
    taskId = int(input("taskId: "))
    updateSuccess = todoAppObj.updateTaskAsDone(taskId)
    print(f"task updated: {updateSuccess}")


def deleteTask():
    pass


while True:
    print("Menu: \n")
    print("(0) salir")
    print("(1) ver todas las tareas")
    print("(2) crear una nueva tarea")
    print("(3) modificar una tarea - titulo")
    print("(4) finalizar una tarea")
    print("(5) eliminar una tarea \n")
    option = int(input("opcion: "))

    if option == 0:
        print("termino TodoApp\n")
        break
    elif option == 1:
        showAllTasks()
    elif option == 2:
        createNewTask()
    elif option == 3:
        modifyTask()
    elif option == 4:
        markTaskAsDone()
