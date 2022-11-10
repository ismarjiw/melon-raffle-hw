"""Randomly pick customer and print customer info"""

# Add code starting here
from random import choice 
from customers import Customer

customer_file_path = 'customers.txt'

def get_customers_from_file(customer_file_path):
    """Read customer file and return list of customer objects.

    Read file at customer_file_path and create a customer object
    containing customer information.
    """

    customers = []

    customer_file = open(customer_file_path)

    # Process a file like:
    #
    #   customer-name | email | street | city | zipcode

    for line in customer_file:
        customer_data = line.strip().split("|")
        name, email, street, city, zipcode = customer_data

        new_customer = Customer(name, email, street, city, zipcode)
        customers.append(new_customer)

    return customers

def pick_random_customer(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")

get_customers_from_file(customer_file_path)
customers = get_customers_from_file(customer_file_path)
pick_random_customer(customers)

# Hint: remember to import any functions you need from
# other files or libraries
