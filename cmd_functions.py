import json
import os
import shutil
import datetime
from customer_class import Customer


def menu():
    """Prints the design for the main() menu screen."""
    welcome_title = "\n\nWelcome to Customer Organizer!\n"
    divider = "-" * len(welcome_title)
    question = "\nWhat would you like to do today?"
    hint = "\n[Enter 'help' for more info]"

    print(welcome_title + divider + question + hint)


def help_menu():
    """Displays help menu; text from help.txt in root directory."""
    f = open("help.txt")
    lines = f.readlines()
    print()

    for line in lines:
        print(line.strip("\n"))


def new_customer(name):
    """Defines the attributes of the new customer and creates a customer.json file.

     The customer file will be created in the customer_files directory.

     Args:
         name (str): Customers name; used for reading from and writing to their files.

    """
    address = input("New customer's address? ").lower()
    phone_number = input("New customer's phone number? ")

    customer = Customer(name=name, address=address, phone_number=phone_number)

    for char in name:
        if char == " ":
            name = name.replace(" ", "_")

    try:
        os.mkdir("./customer_files/{}".format(name))
        f_json = open("customer_files/{0}/{0}.json".format(name), "w")
        json.dump(vars(customer), f_json, indent=4)
        f_json.close()

        f_txt = open("customer_files/{0}/{0}_log.txt".format(name), "w")
        f_txt.write("Customer: {}\n\n".format(name))
        f_txt.close()

        update_log(name, "Added new customer")
        print("\nAdded {} and files to customer_files directory".format(name))
    except (FileExistsError, FileNotFoundError):
        print("\nERROR!")


def customer_info(name):
    """Prints a customers information in a nice format.

    Args:
         name (str): Customers name; used for reading their files.

    """
    for char in name:
        if char == " ":
            name = name.replace(" ", "_")

    try:
        f = open("customer_files/{0}/{0}.json".format(name))
        customer = json.load(f)
        f.close()
        print(Customer(name=customer["name"], address=customer["address"], phone_number=customer["phone_number"],
                       money_received=customer["money_received"], money_not_received=customer["money_not_received"]))
    except FileNotFoundError:
        print("\nERROR: Customer doesn't exist!")


def customer_money_received(name):
    """Prints the total amount of money received by this customer.

    Args:
         name (str): Customers name; used for reading their files.

    """
    try:
        f = open("customer_files/{0}/{0}.json".format(name))
        customer = json.load(f)
        f.close()

        customer = Customer(name=customer["name"], money_received=customer["money_received"]).total_money_received()
        print(customer)
    except FileNotFoundError:
        print("\nERROR: Customer doesn't exist!")


def customer_money_not_received(name):
    """Prints the total amount of money NOT received by this customer.

    Args:
         name (str): Customers name; used for reading their files.

    """
    try:
        f = open("customer_files/{0}/{0}.json".format(name))
        customer = json.load(f)
        f.close()

        customer = Customer(name=customer["name"], money_received=customer["money_not_received"])\
            .total_money_not_received()
        print(customer)
    except FileNotFoundError:
        print("\nERROR: Customer doesn't exist!")


def customer_notes(name):
    """Prints the customers notes via class Customer().

    Args:
         name (str): Customers name; used for reading their files.

    """
    try:
        f = open("customer_files/{0}/{0}.json".format(name))
        customer = json.load(f)
        f.close()

        customer = Customer(name=customer["name"], notes=customer["notes"]).get_notes()
        print(customer)
    except FileNotFoundError:
        print("\nERROR: Customer doesn't exist!")


def add_money_received(name):
    """Adds money to customers money_received attribute.

    Args:
         name (str): Customers name; used for reading from and writing to their files.

    """
    money = input("Money to add to money received: ")

    try:
        f = open("customer_files/{0}/{0}.json".format(name))
        customer = json.load(f)
        f.close()

        f = open("customer_files/{0}/{0}.json".format(name), "w")
        customer["money_received"] += float(money)
        json.dump(customer, f, indent=4)
        f.close()

        Customer(name=customer["name"]).add_to_money_received(money=money)
        update_log(name, "Added ${} to money_received".format(money))
        print("\nAdded ${} to money_received!".format(money))
    except FileNotFoundError:
        print("\nERROR: Customer doesn't exist!")


def sub_money_received(name):
    """Subtracts money from customers money_received attribute.

    Args:
         name (str): Customers name; used for reading from and writing to their files.

    """
    money = input("Money to subtract from money received: ")

    try:
        f = open("customer_files/{0}/{0}.json".format(name))
        customer = json.load(f)
        f.close()

        f = open("customer_files/{0}/{0}.json".format(name), "w")
        customer["money_received"] -= float(money)
        json.dump(customer, f, indent=4)
        f.close()

        Customer(name=customer["name"]).sub_from_money_received(money=money)
        update_log(name, "Subtracted ${} from money_received".format(money))
        print("\nSubtracted ${} from money_received!".format(money))
    except FileNotFoundError:
        print("\nERROR: Customer doesn't exist!")


def add_money_not_received(name):
    """Adds money to customers money_not_received attribute.

    Args:
         name (str): Customers name; used for reading from and writing to their files.

    """
    money = input("Money to add to money not received: ")

    try:
        f = open("customer_files/{0}/{0}.json".format(name))
        customer = json.load(f)
        f.close()

        f = open("customer_files/{0}/{0}.json".format(name), "w")
        customer["money_not_received"] += float(money)
        json.dump(customer, f, indent=4)
        f.close()

        Customer(name=customer["name"]).add_to_money_not_received(money=money)
        update_log(name, "Added ${} to money_not_received".format(money))
        print("\nAdded ${} to money_not_received!".format(money))
    except FileNotFoundError:
        print("\nERROR: Customer doesn't exist!")


def sub_from_money_not_received(name):
    """Subtracts money from customers money_not_received attribute.

    Args:
         name (str): Customers name; used for reading from and writing to their files.

    """
    money = input("Money to subtract from money not received: ")

    try:
        f = open("customer_files/{0}/{0}.json".format(name))
        customer = json.load(f)
        f.close()

        f = open("customer_files/{0}/{0}.json".format(name), "w")
        customer["money_not_received"] -= float(money)
        json.dump(customer, f, indent=4)
        f.close()

        Customer(name=customer["name"]).sub_from_money_not_received(money=money)
        update_log(name, "Subtracted ${} from money_not_received".format(money))
        print("\nSubtracted ${} from money_not_received!".format(money))
    except FileNotFoundError:
        print("\nERROR: Customer doesn't exist!")


def clear(name):
    """Sets customers money_not_received attribute to 0.

    Args:
         name (str): Customers name; used for reading from and writing to their files.

    """
    try:
        f = open("customer_files/{0}/{0}.json".format(name))
        customer = json.load(f)
        f.close()

        f = open("customer_files/{0}/{0}.json".format(name), "w")
        customer["money_not_received"] = 0
        json.dump(customer, f, indent=4)
        f.close()

        Customer(name=customer["name"]).sub_from_money_not_received(money=0)
        update_log(name, "Set money_not_received to 0")
        print("\nSet money_not_received to 0")
    except FileNotFoundError:
        print("\nERROR: Customer doesn't exist!")


def clear_add(name):
    """Transfers all of customers money_not_received to money_received.

    Args:
         name (str): Customers name; used for reading from and writing to their files.

    """
    try:
        f = open("customer_files/{0}/{0}.json".format(name))
        customer = json.load(f)
        f.close()

        f = open("customer_files/{0}/{0}.json".format(name), "w")
        update = "Transferred all of money_not_received (${}) to money_received".format(
                 customer["money_not_received"])
        customer["money_received"] += customer["money_not_received"]
        customer["money_not_received"] = 0
        json.dump(customer, f, indent=4)
        f.close()

        Customer(name=customer["name"]).sub_from_money_not_received(money=0)
        update_log(name, update)
        print("\n" + update)
    except FileNotFoundError:
        print("\nERROR: Customer doesn't exist!")


def update_log(name, update):
    """Writes updates to customers log .txt file.

    Args:
         name (str): Customers name; used for reading from and writing to their .txt log file.
         update (str): Update to to written to customers .txt log file.

    """
    f_txt = open("customer_files/{0}/{0}_log.txt".format(name), "a")
    now = datetime.datetime.now()
    date_format = "{Y}/{M}/{D} - ".format(Y=now.year, M=now.month, D=now.day)
    f_txt.write(date_format + update + "\n")
    f_txt.close()


def old_customer_move(name):
    """Moves customer directory in customer_files to old_customers directory in customer_files directory.

    old_customers directory will be created upon this function call.

    Args:
        name (str): Customers name; used for moving customers directory to old_customers directory.

    """
    try:
        os.makedirs("./customer_files/old_customers")
    except FileExistsError:
        pass

    update = "Moved all customer files to old_customer directory\n{}"
    update_log(name, update.format("-" * len(update)))

    shutil.move("./customer_files/{}".format(name), "./customer_files/old_customers/{}".format(name))
    print("\n" + update.strip("{}"))


def new_customer_move(name):
    """Moves customer directory in old_customers directory up one level to customer_files directory.

    Args:
        name (str): Customers name; used for moving customers directory up one level.

    """
    shutil.move("./customer_files/old_customers/{}".format(name), "./customer_files/{}".format(name))

    update = "Moved all old customer files to customer_files directory\n{}"
    update_log(name, update.format("-" * len(update)))
    print("\n" + update.strip("{}"))


def get_totals_customers_money():
    """Prints the grand total for money received and money not received from all customers."""
    total_money_received = 0
    total_money_not_received = 0

    for directory in os.listdir("./customer_files"):
        for file in os.listdir("./customer_files/{}".format(directory)):
            if ".json" in file:
                f = open("./customer_files/{}/{}".format(directory, file))
                customer = json.load(f)
                total_money_received += customer["money_received"]
                total_money_not_received += customer["money_not_received"]

    print_out = "\nTotal money received from all customers: ${}\nTotal money NOT received from all customers: ${}"
    print(print_out.format(total_money_received, total_money_not_received))
