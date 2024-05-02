# Get user input for grocery store items
def get_user_items_input():
    while True:
        try:
            user_items = int(input("Enter the numbers of items you want to buy: "))
            return user_items
        except ValueError:
            print("Please enter a valid number")
            user_items = int(input("Enter the numbers of items you want to buy: "))

# print("type of user_items", type(user_items))


# !!! try at home !!!
# print("get_user_items_input: ", get_user_items_input())


user_items = get_user_items_input()
total_price = 0
# Get user input for grocery store items' prices
for i in range(user_items):

    item_price = float(input("Enter the price of item #{}: ".format(i+1)))
    total_price = total_price + item_price


# Calculate the total price of the items and print it
print("Total price of the items is: ", total_price)




