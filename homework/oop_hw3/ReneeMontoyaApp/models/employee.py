from framework.models import Model


class Employee(Model):
    file = "employees.json"

    def __init__(self, id, name, email, department_type, department_id):
        self.id = id
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id

    @classmethod
    def search_email(cls, email):
        for dict in cls.get_all():
            if dict.email == email:
                return dict
        print("Not found email")
