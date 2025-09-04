# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price   


# Asking user to enter the original price and the discount percentage
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Printing the final price
final_price = calculate_discount(price, discount_percent)

# Printing results
if discount_percent >= 20:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Original price: {price}")