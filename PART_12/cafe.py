menu = ["Starters", "Mains", "Desserts", "Drinks"]

stock = { 
    "Starters": 10, 
    "Mains": 30,
    "Desserts": 5,
    "Drinks": 20
}

price = { 
    "Starters": 50, 
    "Mains": 150,
    "Desserts": 60,
    "Drinks": 45
}

total_stock = 0

for item in menu: 
    total_stock += stock[item] * price[item]
    print(f"Total worth of {item} is R{price[item]*stock[item]} ")


print("-------------------------------")
print(f"Total value of stock: R{total_stock}")