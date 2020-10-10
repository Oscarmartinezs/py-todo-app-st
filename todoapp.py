# la logica
class TodoApp:
    # es el que se ocupa para inicializar la clase
    # y crear las variables o usar los metodos que
    # dejaran la clase lista para
    def __init__(self):
        self.taskList = []
        self.idCounter = 0

    def addNewTask(self, taskTitle):
        # aumentar el contador en 1
        self.idCounter += 1
        # obtner ese numero
        taskId = self.idCounter
        # luego vamos a crear el diccionario
        taskDict = {"id": taskId, "title": taskTitle, "done": False}
        # luego lo agregamos a la lista de tareas
        self.taskList.append(taskDict)

    def getAllTasks(self):
        return self.taskList

    def numberOfTasks(self):
        pass

    def getTaskById(self, taskId):
        pass

    def updateTask(self, taskId, newTitle):
        pass

    def updateTaskAsDone(self, taskId):
        pass

    def deleteTaskById(self, taskId):
        pass
