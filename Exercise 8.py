print("---Welcome to Posh's Gift Shop---")
print("----Please Login into System----")
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "Thammanoon" and passwordInput == "6116" :
    print("Welcome!")
    print("---Total Goods List---")
    print(" 1. Floral Candle : 442 coins")
    print(" 2. Candy Bouquet : 554 coins")
    print(" 3. Cloche Hat    : 468 coins")
    print(" 4. Red Scarf     : 288 coins")
    print(" 5. Cotton Shirt  : 241 coins")
    GoodsNumber = int(input("Choose Goods Number :"))
    if GoodsNumber == 1:
        price = 442
    if GoodsNumber == 2:
        price = 554
    if GoodsNumber == 3:
        price = 468
    if GoodsNumber == 4:
        price = 288
    if GoodsNumber == 5:
        price = 241
    amount = int(input("Amount : "))
    sum = price * amount
    print("Total Price  :  ", sum,"coins")
    print("-------- THANK YOU --------")
else:
    print("Incorrect Username or password")
