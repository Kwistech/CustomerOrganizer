# Customer Organizer - Johnathon Kwisses
from cmd_functions import *


def main():
    """Switch for Customer Organizer program.

    The user input correlates to function calls within 'cmd_functions.py'. The function calls then call the various
    class instances based on what the user wants to do. Note: The user must type 'q' to quit the program.

    """
    while True:
        menu()
        cmd = input("> ").lower()

        if cmd == "q":
            break
        elif cmd == "help":
            help_menu()
        elif cmd == "totals":
            get_totals_customers_money()

        else:

            name = input("Customer's name: ").lower()

            if cmd == "new customer":
                new_customer(name)
            elif cmd == "customer info":
                customer_info(name)
            elif cmd == "customer notes":
                customer_notes(name)

            elif cmd == "money received":
                customer_money_received(name)
            elif cmd == "money not received":
                customer_money_not_received(name)

            elif cmd == "add money received":
                add_money_received(name)
            elif cmd == "sub money received":
                sub_money_received(name)

            elif cmd == "add money not received":
                add_money_not_received(name)
            elif cmd == "sub money not received":
                sub_from_money_not_received(name)

            elif cmd == "clear":
                clear(name)
            elif cmd == "clear add":
                clear_add(name)

            # Can be confusing; just remember what you want to do.
            elif cmd == "move new customer":
                old_customer_move(name)
            elif cmd == "move old customer":
                new_customer_move(name)

if __name__ == "__main__":
    main()
