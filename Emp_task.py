class Employee:
    def __init__(self, emp_id, first_name, last_name, address, designation, years_of_exp, salary):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.designation = designation
        self.years_of_exp = years_of_exp
        self.salary = salary

    def calculate_bonus(self, bonus_percentage):
        bonus_amount = (bonus_percentage / 100) * self.salary
        return bonus_amount

    def display_employee_info(self):
        return f"Employee Name: {self.emp_id} {self.first_name} {self.last_name} {self.address} {self.designation} {self.years_of_exp} {self.salary}"

def main():
    # employee records 
    employee_records = [
        {"Id": 1, "firstN": "Kiran", "lastN": "Girase", "Add": "Pune", "Desgn": "Manager", "yearsOfExp": 8, "salary": 90000},
        {"Id": 2, "firstN": "Ashitosh", "lastN": "Gilbile", "Add": "Mumbai", "Desgn": "Engineer", "yearsOfExp": (2.5), "salary": 36000},
        {"Id": 3, "firstN": "Vaibhav", "lastN": "Sutar", "Add": "Mumbai", "Desgn": "Senior_Engineer", "yearsOfExp": (5), "salary": 65000},
        {"Id": 4, "firstN": "Rutuja", "lastN": "Tardekar", "Add": "mumbai", "Desgn": "HR", "yearsOfExp": (1.5), "salary": 22000},
        {"Id": 5, "firstN": "Sushant", "lastN": "jadhav", "Add": "Gujrat", "Desgn": "Site_Engineer", "yearsOfExp": (5.2), "salary": 38000},
        {"Id": 6, "firstN": "Ashish", "lastN": "jadhav", "Add": "kolhapur", "Desgn": "Fire_Engineer", "yearsOfExp": (2.5), "salary": 26000},
        {"Id": 7,"firstN":  "Ravi",    "lastN": "Sutar",  "Add": "navi_Mumbai","Desgn": "carpenter", "yearsOfExp": (10.5), "salary": 42000},
              ]

    # for user use to enter bonus percentage and years of experience
    bonus_percentage = float(input("Enter bonus percentage: "))
    years_of_exp = int(input("Enter years of experience: "))

    # Iterate through the employee records
    for record in employee_records:
        employee = Employee(record["Id"], record["firstN"], record["lastN"], record["Add"], record["Desgn"], record["yearsOfExp"], record["salary"])
        
        # Check if employee meets the criteria for bonus based on years of experience
        if employee.years_of_exp >= years_of_exp: 
            bonus_amount = employee.calculate_bonus(bonus_percentage)
            print(employee.display_employee_info()) 
            print(f"Bonus Amount: ${bonus_amount:.2f}\n")
            print()

if __name__ == "__main__":
    main()