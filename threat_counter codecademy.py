starting_money = 100
starting_num_items = 10
item_price = 4

# Your code here
def buy_items(money, threats_number, threats_price):
  num_bought = 0
  while money >= threats_price and threats_number > 0:
    money -= threats_price
    threats_number -= 1
    num_bought += 1
  return num_bought

total = buy_items(starting_money, starting_num_items, item_price)
print("You were able to buy " + str(total) + " items.")
  
# For testing purposes
total_1 = buy_items(100, 10, 4)
print("Test 1: " + str(total_1))
total_2 = buy_items(10, 10, 4)
print("Test 2: " + str(total_2))