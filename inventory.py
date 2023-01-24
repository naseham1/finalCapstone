# Create a class called shoes and define specified attributes
class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        pass
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    # Create a function to return the cost of the shoes
    def get_cost(self):
        pass
        print("The cost of the product is", {self.cost})
    
    # Create a function to return the quantity of the shoes
    def get_quantity(self):
        pass
        print("The quantity of the shoes are", {self.quantity})
    
    #  Create astring representation of the class
    def __str__(self):
        pass
        trainer_details = (f"Country, code, product, cost and quantity respectively ({self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity})")
        print(trainer_details)

shoe_list = [] # List of objects of shoes
inventory_list = [] # List of inventory
f = open('inventory.txt', 'r+')

# Create a function to read the inventory.txt file
def read_shoes_data():
    try:
        f.read()
        for lines in f:
            strip_lines = lines.strip('\n')
            split_lines = strip_lines.split(',')
            inventory_list.append(split_lines)
        # Create a shoes object the data from the inventory list and append this object into the shoes list
        for i in range(1, len(inventory_list)):
            shoe = inventory_list[i]
            shoes = Shoes(shoe[0], shoe[1], shoe[2], shoe[3], int(shoe[4]))
            shoe_list.append(shoes)
    except FileNotFoundError as error:
            print("Sorry, this file cannot be found")

# Create a function a capture new data about shoes
def capture_shoes():
        pass
        new_country = input("country: ")
        new_code = input("code: ")
        new_product = input("product: ")
        new_cost = input("cost: ")
        new_quantity = input("quantity: ")
        # Create a object called new_shoe which includes the user input
        new_shoe = Shoes(new_country, new_code, new_product, new_cost, new_quantity)
        # Add the new_shoe object to the shoe_list
        shoe_list.append(new_shoe)
        f.write(f"{new_country},{new_code},{new_product},{new_cost},{new_quantity}")

# Create a function to print all of the data from the shoes list
def view_all():
    # Create lists of each dataset
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    # Create a for loop to input and print all of the information and from the shoe list 
    for lines in shoe_list:
        country.append(lines.get_country())
        code.append(lines.get_code())
        product.append(lines.get_cost())
        cost.append(lines.get_cost())
        quantity.append(lines.get_quantity())
    print(country, code, product, cost, quantity)

# Create a function to enable the user to restock an item
def re_stock():
    restock = []
    country = []
    code = []
    product = []
    cost = []
    quantity = []
    # identify the shoe object with the lowest quantity and idenify the shoes that need to be restocked
    shoe_list.sort(key=lambda x:x.quantity)
    for i in range(1,6):
        restock.append(shoe_list[i])
    for line in restock:
        country.append(line.get_country())
        code.append(line.get_code())
        product.append(line.get_product())
        cost.append(line.get_cost())
        quantity.append(line.get_quantity())
        # Ask the user to state the product and quanity of the product they would like to restock
        input_item = int(input("State the product you would like to restock: "))
        input_quantity = int(input("How many more would you like to add? "))
        shoe_list[input_item].set_quantity(input_quantity)
        # Print this new quanity in the file
        updated_quantity = " "
        for item in shoe_list:
            updated_quantity += (f"{item.get_country()},{item.get_code()},{item.get_product()},{item.get_cost()},{item.get_quantity()}")
            f.write(updated_quantity)
            f.close()

# Create a function to enable a user to search for a shoe 
def search_shoe():
    pass
    # Request the user to input the code
    find_shoe = input("Enter the shoe code you are looking for: ")
    for line in shoe_list:
        if line.get_code() == find_shoe:
            print({line})
# Create a function to enable to user to identify the value of the shoe and print the value
def value_per_item():
    for line in shoe_list:
        value = int(line.get_cost()) * int(line.get_quantity())
        print(f"Code: {line.get_code()}, Value: {value}")

# Create a function to determine the shoe with the highest quantity
def highest_qty():
    # Determine the product with the highest quantity
    print(max(shoe_list, key=lambda item: item.quantity))
    # Print that this shoe is on sale
    print("This shoe is currently on sale")


#==========Main Menu=============
# Create a main menu for all of the functions above
def main_menu():
    while True:
        menu = int(input('''\n
            Please select an option from the menu:
            1. Capture shoes
            2. View all shoes
            3. Restock a shoe
            4. Search for a shoe
            5. View the value of the shoe
            6. View the shoes on sale
            \n'''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            re_stock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()

        elif menu == 6:
            highest_qty()