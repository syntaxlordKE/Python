# This function calculates a discounted price
# I f the discount percentage is 20% or higher, it applies the discount
# Otherwise, it returns the original price

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying adiscount.

    args: 
    price (float): The original price of item
    discount_percent (float): The discount percentage.

    returns:
    Float: The final price after the discount or the original price if the disount is less than 20%
    """
    # lets check if discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price
    
# Use try-except block to handle potential errors from user input
try:
    original_price = float(input("Enter the original price of item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    final_price = calculate_discount(original_price, discount_percent)

    # lets check if discount was applied
    if final_price < original_price:
        print(f"A discount of {discount_percent: .2f}% was apllied.")
        print(f"The final price is: Ksh.{final_price:.2f}")
    else:
        print("The discount was less than 20%, so no discount was applied.")
        print(f"The original price is: Ksh.{original_price:.2f}")
except ValueError:
    print("Invalid input: PLease enter a valid number for the price and discount")