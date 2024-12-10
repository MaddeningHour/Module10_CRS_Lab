def myCheck():
    while True:
        myTotal = input("What is the total of your check? $: ").strip().replace(',', '')
        stars = ''
        myResult = ''

        if len(myTotal) < 10:
            stars = "*" * (10-len(myTotal))
        try:
            myTotal = float(myTotal)
            myResult += stars + f"{myTotal:,.2f}"
            return myResult

        except ValueError:
            print("Your check must be a valid number.")
            
        
print(f'${myCheck():>10}')