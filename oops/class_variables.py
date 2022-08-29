
class Employee :  
    raise_percent = 1.04
    num_of_emp = 0

    def __init__(self , name , email , salary):
        self.name = name
        self.email = email
        self.salary = salary 
        Employee.num_of_emp += 1
       
    def get_name_and_email(self):
        print('{} -> {}'.format(self.name , self.email))
    
    def get_raise(self):
        print("Increamented salary for {} is {}".format( self.name, self.salary*self.raise_percent))
    
   

if __name__ == '__main__' : 
    emp1 = Employee('Divya' , 'dsrao0712@gmail.com' , 90000)
    emp2 = Employee('Chinnu' , 'chinnu@gmail.com' , 20000)

    emp1.get_name_and_email()
    emp2.get_name_and_email()

    emp1.raise_percent = 1.05

    emp1.get_raise()
    emp2.get_raise()

    print(Employee.num_of_emp)

    



        
        