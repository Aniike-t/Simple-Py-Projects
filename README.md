# Simple Python Projects
**Simple And Easy projects made using python and using python libraries such as matplotlib, flask, pickle, SqlAlchemy and others.**


## Contents
**1. Shop Management System (Commandline app)** <br>
**2. Blood Group Survey App (Flask WebApp)**

# 1. Desciription of Shop Management System (Commandline app)
This project is an inventory management system built with Python. It offers various features such as adding items to the inventory, updating quantities, making purchases, viewing inventory and costs, removing items, and checking transaction history. It also includes the ability to update item prices.

Example Usage Scenario:
Imagine you run a small convenience store, and you need a simple way to manage your store's inventory and transactions. You can use the "Shop Management System" to easily keep track of your stock and sales.

## Step-by-Step Explanation

We need the `matplotlib.pyplot` library for plotting the graph, the `pickle` library for saving and loading data, and the `os` library for deleting files.


The main menu is the core of the program. It presents the user with a list of options and waits for their input. The options are:
<b>
1. Add Item to inventory
2. Updating Quantities
3. Purchasing Item
4. Viewing Inventory and Costs
5. Remove Item
6. Transaction History And Graph
7. Updates Price
</b>

The user can select an option by entering the corresponding number. The program will then execute the selected option.

# 2. Blood Group Survey App (Flask WebApp)

This Flask application allows users to input their name, age, blood group, and quantity of blood they are willing to donate. 
The data is stored in a SQLite database. 
A notification is displayed to the user after they submit their response.

## Prerequisites

* Python 3.6 or later
* Flask
* SQLAlchemy
* plyer

## Installation

1. Clone this repository.

2. Create a SQLite database.
```
sqlite3 data.db
```

3. Run the application.
```
python run.py
```

## Usage

1. Open the application in a web browser.
```
http://127.0.0.1:5000/
```
2. Enter your name, age, blood group, and quantity of blood you are willing to donate.
3. Click the "Submit" button.
4. A notification will be displayed to you after your response is submitted.
5. The person donated blood can be recorded in the database and can be further used in data analysis and visualisation.
