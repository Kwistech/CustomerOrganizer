# CustomerOrganizer

Customer Organizer v.1.0

Customer Organizer is a program for Python 3 that stores customer information in a logical way.

##Installation

This program is not installed. It is run from the command line.

Fork the repository and clone it to your local drive.

From the program's root directory, run the following:

`python main.py`

##Upon First Run##

A new customer directory must be created. To do this, enter: 'new customer'

```
Welcome to Customer Organizer!
---------------------------------
What would you like to do today?
[Enter 'help' for more info]
> new customer
```

Give the program the information it asks and it will create a directory with the
customers name in the customer_files directory. In this directory will be two files
(ex. customer_name.json, customer_name_log.txt).

The .json file is the file in which the customers information will be stored.
The .txt file is a log of all the changes you have made to the .json file.

##Features

The program comes with the basic features needed to manage customers:

+ Add/Remove customers
+ Display customer information
+ Add/Subtract from customer pending/approved amounts
+ Move customer files based on active/inactive accounts

##Menu Commands

Below are the basic commands for the program (more info can be found in help.txt):

+ new customer
+ customer info
+ customer notes
+ money received
+ money not received
+ add money received
+ sub money received
+ add money not received
+ sub money not received
+ clear
+ clear add
+ move new customer
+ move old customer
