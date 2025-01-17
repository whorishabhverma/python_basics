# Class Employee:
class Employee:
    def __init__(self,name,employee_id):
        if not name:
            raise ValueError("name can not be empty")
        if not isinstance(employee_id,int):
            raise ValueError("id should be integer")
        self.name = name
        self.employee_id = employee_id
    def get_employee_info(self):
        return f"employee's name : {self.name} and employee_id : {self.employee_id}"
        
class Department:
    def __init__(self,department_name):
        if not department_name:
            raise ValueError("department_name can not be empty")
        self.department_name = department_name
    
    def get_department_info(self):
        return f"department name : {self.department_name}"

class Manager(Employee,Department):
    def __init__(self,name,employee_id,department_name,level):
        Employee.__init__(self,name,employee_id)
        Department.__init__(self,department_name)
        if not level:
            raise ValueError("level can not be empty")
        self.level = level
        
    def get_manager_info(self):
        return f"{Employee.get_employee_info(self)}, {Department.get_department_info(self)} and level : {self.level}"

def main():
    try:
        manager = Manager("manager_bhaalu",1,"software","manager")
        print(manager.get_manager_info())
    except ValueError as e:
        print(f"error: {e}")
if __name__ == "__main__":
    main()


