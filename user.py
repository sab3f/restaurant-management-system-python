from abc import ABC
from orders import Order
class User(ABC):
    def __init__(self,name,phone,mail,address):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.address = address

class Customer(User):
    def __init__(self, name, phone, mail, address):
        super().__init__(name, phone, mail, address)
        self.cart = Order()

    def view_menu(self,restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self,restaurant,item_name,quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print('Item quantity exceeded!')
            else:    
              item.quantity = quantity
              self.cart.add_item(item)
        else:
            print('Item not available')

    def view_cart(self):
        print('**View Cart**')
        print('Name\tPrice\tQuantity')
        for item,quantity in self.cart.items.items():
         print(f'{item.name}\t{item.price}\t{quantity}')
        print(f'Total Price : {self.cart.total_price()}')

    def pay_bill(self):
        print(f'{self.cart.total_price()} paid successfully')
        self.cart.clear()    

class Employee(User):
    def __init__(self, name, phone, mail, address,age,designation,salary):
        super().__init__(name, phone, mail, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, mail, address):
        super().__init__(name, phone, mail, address)
        

    def add_employee(self,Restaurant,employee):
       Restaurant.add_employee(employee)
       print(f'{employee} is added !!')

    def view_employee(self,Restaurant):
        Restaurant.view_employee()

    def add_item(self,Restaurant,item):
        Restaurant.menu.add_menu(item)  
    
    def delete_item(self,Restaurant,item):
        Restaurant.menu.remove_item(item)  

    def view_menu(self,restaurant):
        restaurant.menu.show_menu()    