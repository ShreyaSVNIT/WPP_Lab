num = eval(input("Enter the number of products: "))
product = {}
for i in range(num) :
    name = input(f'Enter product name {i + 1}: ')
    price = eval(input(f'Enter product {i + 1} price: '))
    product[name] = price

flag = 0
for i in range(num) :
    prod = input("Enter product name you want: ")
    if prod in product:
        print(f"The price of this product is {product[prod]}")
        flag = 1

if flag == 0 : 
    print("Sorry, the product is not there.")
