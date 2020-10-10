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
        return len(self.taskList)

    def getTaskById(self, taskId):
        # un for para navegar las tareas en la lista
        for task in self.taskList:
            # si el taskid es el del diccionario
            if task["id"] == taskId:
                # retornamos el diccionario
                return task

    def updateTask(self, taskId, newTitle):
        # un for para navegar las tareas en la lista
        for task in self.taskList:
            # si el taskid es el del diccionario
            if task["id"] == taskId:
                # la actualizacion con el nuevo titulo
                task["title"] = newTitle
                return True
        return False

    def updateTaskAsDone(self, taskId):
        for task in self.taskList:
            if task["id"] == taskId:
                task["done"] = True
                return True
        return False

    def deleteTaskById(self, taskId):
        for task in self.taskList:
            if task["id"] == taskId:
                self.taskList.remove(task)
                return True
        return False
