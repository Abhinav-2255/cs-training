def vending_machine(capacity, stock):
    while True:
        n = int(input("How many bottles of pepsi would you like? "))
        if n <= stock:
            stock -= n
            for i in range(n):
                print("Take your pepsi")
        else:
            for i in range(stock):
                print("Take your pepsi")
            print("Out of stock")
            stock = 0
        print("Happy drinks")

# Example usage
vending_machine(200, 70)

