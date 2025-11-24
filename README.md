# Coffee Shop Management System - Phase 2

This repository contains the second iteration (Part 2) of the Coffee Shop Management System. It is a command-line interface (CLI) application written in Python that simulates a coffee shop ordering system.

This version incorporates specific modifications and improvements identified during the initial phase (Part 1). The code has been refined to enhance robustness, user experience, and adherence to Object-Oriented Programming (OOP) principles.

## Improvements from Phase 1

Following the analysis of the first version, the following enhancements have been implemented:

* **Robust Error Handling:** Integrated `try-except` blocks to manage invalid user inputs (e.g., non-integer menu selections or negative quantities) without crashing the program.
* **Membership Integration:** Added a dedicated logic to handle member status and apply automatic discounts.
* **Code Refactoring:** Improved the separation of concerns by organizing the code into distinct classes (`Client`, `Drink`, `CoffeeShop`) for better maintainability.
* **Detailed Receipt:** Enhanced the final output to provide a clear breakdown of the transaction, including discounts and change due.

## Features

* **Client Management:** Handles customer profiles including names and membership status.
* **Menu System:** Displays a dynamic list of beverages including local specialties (e.g., Cafe Touba) with pricing in FCFA.
* **Order Processing:** Calculates subtotals, applies the 10% member discount where applicable, and computes the total.
* **Payment Handling:** Manages cash payments, validates sufficiency of funds, and calculates change.

## Code Structure

The project is organized around three main classes:

1.  **Client:** Stores customer details and membership boolean.
2.  **Drink:** Defines beverage attributes (name and price).
3.  **CoffeeShop:** Contains the business logic, inventory list, and methods for interaction.

## Getting Started

### Prerequisites

* Python 3.x installed on your machine.

### Installation

1.  Clone the repository:
    git clone https://github.com/Akiraez33/coffee-shop-manager-v2.git

2.  Navigate to the project directory:
    cd coffee-shop-manager-v2

### Usage

Run the main script to start the application:

python main.py

Follow the on-screen prompts to enter customer details, select drinks, and process payments.

## Example Output

Welcome to Coffee Shop

First name: Moussa
Last name: Diop
Are you a member? (yes/no): yes

Hello Moussa Diop!

--- Menu ---
1. Lipton - 200 FCFA
2. Nescafe - 250 FCFA
...
8. Cafe Touba - 350 FCFA

Select drink number: 8
Quantity: 2

Cafe Touba x2
Member discount: -70 FCFA
Total: 630 FCFA

Payment: 1000

--- Receipt ---
Customer: Moussa Diop
Item: Cafe Touba x2
Discount: 70 FCFA
Paid: 1000 FCFA
Change: 370 FCFA
---------------

## Author

.BALIMA Hector Giscard 
.BAMOUNI Grace Marcella 
.COULIBALY Faez 
.KONDOMBO Josué 
.KONOMBO Madeleine 
.YOUGBARE Eunice Athalie Teega-Wendé

Project created for educational purposes, demonstrating the evolution of code through iterative improvements.# Coffee-management-2
