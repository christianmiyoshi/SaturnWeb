from domain.models.person import Person

class Student(Person):
    def __init__(self, first_name, middle_name, last_name):
        super().__init__(first_name, middle_name, last_name)
        self.undergraduate_admissions = []

    def enroll_course(course_offering_id):
        return 
    
