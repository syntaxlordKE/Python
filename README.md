# Week 2 Assignment - Python List Operations

This program demonstrates basic **list operations** in Python, including `append`, `insert`, `extend`, `pop`, `sort`, and `index`.

It builds a list step by step and shows the results after each operation.

---

## 📌 Features

The program performs the following steps:

1. **Create an empty list** called `my_list`.
2. **Append** the elements `10, 20, 30, 40` to the list.
3. **Insert** the value `15` at the second position (index `1`).
4. **Extend** the list with another list: `[50, 60, 70]`.
5. **Remove** the last element from the list using `pop()`.
6. **Sort** the list in ascending order.
7. **Find and print** the index of the value `30`.

---

# Week 3 Assignment - Control Flows and Functions in Python

This program demonstrates the use of **control flows** (`if`, `else`, `try-except`) and **functions** in Python.  
It calculates the final price of an item based on the discount percentage provided by the user.

---

## 📌 Features

1. Defines a function `calculate_discount(price, discount_percent)`:
   - If the discount is **20% or higher**, the discount is applied.
   - If the discount is **less than 20%**, the original price is returned.

2. Uses a **try-except block** to handle invalid user input (e.g., non-numeric values).

3. Provides clear user feedback:
   - Displays the applied discount percentage and the final price (if applicable).
   - Informs the user if no discount was applied.

---

# Week 4 Assignment - File Read & Write Challenge & Error Handling Lab

This program demonstrates **file handling** in Python by reading from a file, modifying its contents, and writing the modified version to a new file.  
It also includes **error handling** to manage cases where the file doesn’t exist or can’t be accessed.

---

## 📌 Features

1. Prompts the user to **enter a filename** to read.  
2. Attempts to **open and read** the file content safely.  
3. **Modifies** the file’s content (e.g., converts all text to uppercase).  
4. **Writes** the modified content to a new file named `modified_<original_filename>`.  
5. Handles common file-related errors:
   - `FileNotFoundError` – when the file doesn’t exist.  
   - `PermissionError` – when the user lacks read/write permissions.  
   - Any other unexpected error is caught and displayed gracefully.


---

# Week 5 Assignment - Object-Oriented Programming (OOP) in Python

This week explores **Object-Oriented Programming (OOP)** concepts such as **classes**, **objects**, **constructors**, **encapsulation**, **inheritance**, and **polymorphism**.

---

## 🏗️ Assignment 1: Design Your Own Class  
**File:** `smartphone_oop_inheritance.py`

This program defines a `Smartphone` class that inherits from a parent `Device` class.  
It demonstrates **encapsulation** using private attributes and **inheritance** through class extension.

### 📌 Features
1. `Device` (Parent Class) – stores general device info (brand, model).  
2. `Smartphone` (Child Class) – adds attributes like `storage` and `battery`.  
3. Implements **encapsulation** using private attributes and getters/setters.  
4. Demonstrates real-world behavior with methods like `charge()` and `specs()`.  
5. Uses a constructor (`__init__`) to initialize objects with unique values.

---

## 🎭 Activity 2: Polymorphism Challenge  
**File:** `vehicle_polymorphism_demo.py`

This program demonstrates **polymorphism** using different vehicle classes that all share the same method name (`move()`), but perform different actions.

### 📌 Features
1. Defines classes `Car`, `Plane`, and `Boat`.  
2. Each class implements its own version of `move()`.  
3. Demonstrates **polymorphism** by calling `move()` on different objects in a loop.  
4. Showcases flexibility and extensibility of OOP design.

### 🖥️ Example Output


---

## 🧪 Example Usage


