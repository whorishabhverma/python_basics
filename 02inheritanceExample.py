class Person:
    def __init__(self,name,age):
        if not name:
            raise ValueError("name can not be empty")
        if not isinstance(age,int) or age <= 0:
            raise ValueError("age must be a positive integer")
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"name is {self.name} and age is  {self.age} "
    

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        if not student_id:
            raise ValueError("Student ID cannot be empty.")
        self.student_id = student_id
    
    def display_info(self):
        return f"{super().display_info()} and student id is {self.student_id} "
    
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        if not subject:
            raise ValueError("Subject cannot be empty.")
        self.subject = subject
    
    def display_info(self):
        return f"{super().display_info()} and subject is {self.subject} "
 
 
def main():
    try:
        # Creating objects
        student = Student("Rishabh", 21, "CA080")
        teacher = Teacher("Akshay Saini",12, "JavaScript")

        # Displaying information
        print(student.display_info())
        print(teacher.display_info())
    except ValueError as e:
        print(f"Error: {e}")


# Run the program
if __name__ == "__main__":
    main()
 
 
 


        