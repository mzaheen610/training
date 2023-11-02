class employees():
    def __init__(self) -> None:
        self.employees = set()

    def addEmployees(self):
        for i in range(5):
            newEmployee = input("Enter a name:")
            self.employees.add(newEmployee)

    def showEmployees(self):
        print(self.employees)
        for  empNo,emp in enumerate(self.employees):
            print("Employee" , empNo , ":" ,emp)

dbizEmployees = employees()
dbizEmployees.addEmployees()
dbizEmployees.showEmployees()

