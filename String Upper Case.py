class IOString():
    def __init__(self):
       self.str1 = ""
    def Get_String(self):
        self.str1 = input("Enter a String")
    def print_String(self):
        print("Result is :", self.str1.upper())  




str = IOString()


str.Get_String()
str.print_String()