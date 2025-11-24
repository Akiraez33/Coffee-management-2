class Client:
    def __init__(self, name, surname, is_member=False):
        self.name = name
        self.surname = surname
        self.is_member = is_member
    
    def full_name(self):
        return f"{self.name} {self.surname}"


class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class CoffeeShop:
    def __init__(self):
        self.drinks = [
            Drink("Lipton", 200),
            Drink("Nescafé", 250),
            Drink("Milk", 150),
            Drink("Chocolate Coffee", 300),
            Drink("Cappuccino", 500),
            Drink("Espresso", 400),
            Drink("Latte", 550),
            Drink("Café Touba", 350)
        ]
        self.member_discount = 0.10
    
    def show_menu(self):
        print("\n--- Menu ---")
        for i, drink in enumerate(self.drinks, 1):
            print(f"{i}. {drink.name} - {drink.price} FCFA")
    
    def get_drink(self, num):
        if 1 <= num <= len(self.drinks):
            return self.drinks[num - 1]
        return None
    
    def calculate_price(self, drink, qty, is_member):
        total = drink.price * qty
        discount = 0
        
        if is_member:
            discount = total * self.member_discount
            total -= discount
        
        return total, discount


def main():
    print("Welcome to Coffee Shop\n")
    
    name = input("First name: ")
    surname = input("Last name: ")
    member = input("Are you a member? (yes/no): ").lower() == "yes"
    
    client = Client(name, surname, member)
    shop = CoffeeShop()
    
    print(f"\nHello {client.full_name()}!")
    
    while True:
        shop.show_menu()
        
        try:
            choice = int(input("\nSelect drink number: "))
            drink = shop.get_drink(choice)
            if not drink:
                print("Invalid selection")
                continue
        except ValueError:
            print("Please enter a number")
            continue
        
        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Must be at least 1")
                continue
        except ValueError:
            print("Please enter a valid quantity")
            continue
        
        total, discount = shop.calculate_price(drink, quantity, client.is_member)
        
        print(f"\n{drink.name} x{quantity}")
        if discount > 0:
            print(f"Member discount: -{discount:.0f} FCFA")
        print(f"Total: {total:.0f} FCFA")
        
        while True:
            try:
                payment = float(input("Payment: "))
                if payment < total:
                    print(f"Not enough. Need {total - payment:.0f} more")
                    continue
                break
            except ValueError:
                print("Invalid amount")
        
        change = payment - total
        
        print(f"\n--- Receipt ---")
        print(f"Customer: {client.full_name()}")
        print(f"Item: {drink.name} x{quantity}")
        if discount > 0:
            print(f"Discount: {discount:.0f} FCFA")
        print(f"Paid: {payment:.0f} FCFA")
        print(f"Change: {change:.0f} FCFA")
        print("---------------\n")
        
        again = input("Another order? (yes/no): ").lower()
        if again != "yes":
            break
    
    print("\nThanks for visiting!")


if __name__ == "__main__":
    main()