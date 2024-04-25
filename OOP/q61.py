from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department
    
    @abstractmethod
    def calculate_pay(self):
        pass
    
    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)
        print("Pay:", self.calculate_pay())

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, department, monthly_salary):
        super().__init__(name, emp_id, department)
        self.monthly_salary = monthly_salary
    
    def calculate_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, department, hours_worked, hourly_rate):
        super().__init__(name, emp_id, department)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    
    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate

class FreelanceEmployee(Employee):
    def __init__(self, name, emp_id, department, projects_completed, rate_per_project):
        super().__init__(name, emp_id, department)
        self.projects_completed = projects_completed
        self.rate_per_project = rate_per_project
    
    def calculate_pay(self):
        return self.projects_completed * self.rate_per_project

# Example usage:
full_time_emp = FullTimeEmployee("Rajesh Kumar", "FT001", "IT", 5000)
part_time_emp = PartTimeEmployee("Priya Sharma", "PT001", "HR", 20, 25)
freelance_emp = FreelanceEmployee("Amit Patel", "FL001", "Marketing", 10, 100)

print("Full-Time Employee Details:")
full_time_emp.display_details()
print()

print("Part-Time Employee Details:")
part_time_emp.display_details()
print()

print("Freelance Employee Details:")
freelance_emp.display_details()
