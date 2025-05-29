import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
    
circle1=Circle(2)  
print(circle1.perimeter());
print(circle1.area());

from datetime import date
class Person():
    def __init__(self,name,country,dateOfBirth):
        self.name=name
        self.country=country
        self.birth=dateOfBirth
    def age(self):
        today=date.today()
        return  today.year-self.birth
    
person1=Person('John','USA',2005)    
print(person1.age());

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        return self.num1/self.num2
    
number=Calculator(8,4)
print(number.add())   
print(number.sub())
print(number.multiply())
print(number.divide());

import math
class Shape:
    def area(self):
       raise NotImplementedError
    def calculate_perimeter(self):
        raise NotImplementedError
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius    
    def area(self):
        return math.pi*self.radius**2
    def perimeter(self):
        return 2*math.pi*self.radius
class Triangle(Shape):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3   
    def area(self):
        s=(self.side1+self.side2+self.side3)/2
        return  s * (s - self.side1) * (s - self.side2) * (s - self.side3)
    def perimeter(self):
        return self.side1+self.side2+self.side3
class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        self.side**2
    def perimeter(self):
        return 4*self.side;

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)  # This adds the item to the list
    
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return 'Stack is empty'
        
stack1=Stack()
stack1.push(10)    
print(stack1.pop())  
print(stack1.items)  
stack1.push(11)    
print(stack1.pop()) 
print(stack1.items)  
stack1.push('Ozoda') 
print(stack1.pop())
print(stack1.items) ;

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
       
        self.items.append(item)

    def dequeue(self):
     
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        
        return len(self.items) == 0

queue=Queue()       
queue.enqueue(10)
queue.enqueue(11)
print(queue.dequeue())
print(queue.dequeue())
print(queue.items)
print(queue.is_empty());

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with balance ${initial_balance}.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            if amount > 0:
                self.accounts[account_number] += amount
                print(f"Deposited ${amount} into account {account_number}.")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount > 0:
                if self.accounts[account_number] >= amount:
                    self.accounts[account_number] -= amount
                    print(f"Withdrew ${amount} from account {account_number}.")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account {account_number} balance: ${self.accounts[account_number]}")
        else:
            print("Account not found.")

if __name__ == "__main__":
    bank = Bank()
    bank.create_account("12345", 500)
    bank.deposit("12345", 200)
    bank.withdraw("12345", 100)
    bank.check_balance("12345")





        



