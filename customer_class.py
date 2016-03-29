class Customer(object):
    """Creates Customer object and handles most of the methods used for the program."""

    def __init__(self, name="", address="", phone_number="", money_received=0, money_not_received=0, notes=[]):
        self.name = name
        self.address = address
        self.phone_number = phone_number

        self.money_received = money_received
        self.money_not_received = money_not_received

        self.notes = notes

    def __str__(self):
        info = "\nName: {}\nAddress: {}\nPhone Number: {}\n\n" \
               "Total Money Received: ${}\nMoney Not Received: ${}\n\nNotes: {}"
        return info.format(self.name.title(), self.address.title(), self.phone_number,
                           self.money_received, self.money_not_received, self.notes)

    def total_money_received(self):
        """Prints the total amount of money received from the customer.

        Return:
            str: Prints formatted string.

        """
        print_out = "\nMoney Received from {} - ${}".format(self.name.title(), self.money_received)
        return print_out

    def total_money_not_received(self):
        """Prints the total amount of money not received from the customer.

        Return:
            str: Prints formatted string.

        """
        print_out = "\nMoney Not Received from {} - ${}".format(self.name.title(), self.money_not_received)
        return print_out

    def get_notes(self):
        """Prints the customers notes added by user.

        Return:
            list: Contains all notes for this customer.
            None: If there are no notes.

        """
        if self.notes:
            return self.notes
        else:
            return "\nNo notes for {}".format(self.name)

    def add_to_money_received(self, money):
        """Adds money to the total amount of money received from the customer.

        Args:
            money (int): Money to be added to self.money_received.

        """
        try:
            money = float(money)
            self.money_received += money
        except ValueError:
            print("\nERROR!")

    def sub_from_money_received(self, money):
        """Subtracts money from the total amount of money received from the customer.

        Args:
            money (int): Money to be subtracted from self.money_received.

        """
        try:
            money = float(money)
            self.money_received -= money
        except ValueError:
            print("\nERROR!")

    def add_to_money_not_received(self, money):
        """Adds money to the total amount of money NOT received from the customer.

        Args:
            money (int): Money to be added to self.money__not_received.

        """
        try:
            money = float(money)
            self.money_not_received += money
        except ValueError:
            print("ERROR!")

    def sub_from_money_not_received(self, money):
        """Subtracts money from the total amount of money NOT received from the customer.

        Args:
            money (int): Money to be subtracted from self.money__not_received.

        """
        try:
            money = float(money)
            self.money_not_received -= money
        except ValueError:
            print("ERROR!")
