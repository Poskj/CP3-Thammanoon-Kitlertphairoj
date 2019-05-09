print("---Welcome to Posh Shop---")
print("--Please Login into System--")
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "Thammanoon" and passwordInput == "6116" :
    print("Welcome!")
    print("---Total Goods List---")
    print(" 1. Bacon        : 50  coins")
    print(" 2. Blue Sweater : 208 coins")
    print(" 3. Potato       : 36  coins")
    print(" 4. Caramel Apple: 255 coins")
    print(" 5. Olive        : 82  coins")
    GoodsNumber = int(input("Choose Goods Number :"))
    if GoodsNumber == 1:
        price = 50
    if GoodsNumber == 2:
        price = 208
    if GoodsNumber == 3:
        price = 36
    if GoodsNumber == 4:
        price = 255
    if GoodsNumber == 5:
        price = 82
    amount = int(input("Amount : "))
    sum = price * amount
    print("Total Price  :  ", sum,"coins")
    print("-------- THANK YOU --------")
else:
    print("Incorrect Username or password")
