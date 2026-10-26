class Employee:
    def __init__(self):
        print("Employee Created")
    def __del__(self):
        print("Employee Destroyed!")    

def create_object():
    print("Making Object............")
    obj = Employee()
    print("Function End.............")
    return obj




obj = create_object()
print("Program End...............")

        

































    