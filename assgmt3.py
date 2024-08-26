#1. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
            self.items[item_name]['price'] = price 
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}
    
    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if self.items[item_name]['quantity'] > quantity:
                self.items[item_name]['quantity'] -= quantity
            else:
                del self.items[item_name]
        else:
            print(f"Item '{item_name}' not found in the cart.")
    
    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item['price'] * item['quantity']
        return total
    
    def __str__(self):
        return "\n".join([f"{item_name}: ${details['price']} x {details['quantity']}" for item_name, details in self.items.items()])

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item('Apple', 0.99, 3)
    cart.add_item('Milk', 1.49, 2)
    cart.add_item('Bread', 2.49)

    print("Shopping Cart:")
    print(cart)

    print("\nTotal Price:", cart.calculate_total())

    cart.remove_item('Apple', 1)
    print("\nAfter removing 1 Apple:")
    print(cart)

    print("\nTotal Price:", cart.calculate_total())



#2. Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.


class Bank:
 def __init__(self):
  self.balance = 0
print("The Account is created")

def deposit(self):
 amount = float(input("Enter the amount to be deposited: "))

 self.balance += amount
 print("Deposit is successful and the balance in the account is {:.2f}" % self.balance)

def withdraw(self):
 amount = float(input("Enter the amount to be withdrawn: "))
 if self.balance >= amount:
  self.balance -= amount

  print("The withdrawal is successful and the balance is {:.2f}" % self.balance)

 else:
  print("Insufficient Balance")

def enquire(self):
 print("Balance in the account is {:.2f}" % self.balance)

acct = Bank()

acct.deposit()
acct.withdraw()
acct.enquire()


