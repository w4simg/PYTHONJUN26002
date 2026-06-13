#j

price = float(input("Enter the price of the product: "))
def calculate_discount(price):
    if price > 5000:
        discount = price * 0.10
    else:
        discount = 0
        print("No discount")

    print("Discount Amount: ₹", discount)

calculate_discount(price)