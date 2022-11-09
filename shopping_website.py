#This code doesn't apply to DRY method, I will eventually repair this.
print("Welcome to our shopping site!")
for_while = True
shopping_cost = 0
items_in_shopping_cart = 5
def unknown_command():
    print("I don't understand this command! \n")



    





while for_while == True:
    choice = input("Choose a section you are intresed in \n Sections avilable: \n T-shirts \n Hoodies \n Trousers \n Shoes \n Shopping cart \n")
    while choice.lower() == 'hoodies':
        hoodies_choice = input("\n Hoodies currently avilable: \n Black hoodie-30$ \n Green hoodie-30$ \n Gucci hoodie-200$ \n Adidas hoodie-60$ \n Type 'BACK' to comeback to main site. \n")
        if hoodies_choice.lower() == 'black':
            yes_no = input("Are you sure You want to add black hoodie to your shopping cart? Yes/No\n")
            if yes_no.lower() == 'no':
                print("Ok, let's comeback to the hoodie section.")
            while yes_no.lower() == 'yes':
                amountt = input("How many piecies of clothing would You like to buy?\n")
                if amountt.isdigit():
                    shopping_cost += 30 * int(amountt)
                    print(f"\n{shopping_cost}$ has been added to your total cost!\n")
                    break
                else:
                    unknown_command()
        elif hoodies_choice.lower() == 'green':
            yes_no = input("Are you sure You want to add green hoodie to your shopping cart? Yes/No\n")
            if yes_no.lower() == 'no':
                print("Ok, let's comeback to the hoodie section.")
            while yes_no.lower() == 'yes':
                amountt = input("How many piecies of clothing would You like to buy?\n")
                if amountt.isdigit():
                    shopping_cost += 30 * int(amountt)
                    print(f"\n{shopping_cost}$ has been added to your total cost!\n")
                    break
                else:
                    unknown_command()
        elif hoodies_choice.lower() == 'gucci':
            yes_no = input("Are you sure You want to add Gucci hoodie to your shopping cart? Yes/No\n")
            if yes_no.lower() == 'no':
                print("Ok, let's comeback to the hoodie section.")
            while yes_no.lower() == 'yes':
                amountt = input("How many piecies of clothing would You like to buy?\n")
                if amountt.isdigit():
                    shopping_cost += 200 * int(amountt)
                    print(f"\n{shopping_cost}$ has been added to your total cost!\n")
                    break
                else:
                    unknown_command
        elif hoodies_choice.lower() == 'adidas':
            yes_no = input("Are you sure You want to add Adidas hoodie to your shopping cart? Yes/No\n")
            if yes_no.lower() == 'no':
                print("Ok, let's comeback to the t-shirt section.")
            if yes_no.lower() == 'yes':
                amountt = input("How many piecies of clothing would You like to buy?\n")
                if amountt.isdigit():
                    shopping_cost += 60 * int(amountt)
                    print(f"\n{shopping_cost}$ has been added to your total cost!\n")
                    break
                else:
                    unknown_command
        elif hoodies_choice.lower() == 'back':
            break
        else:
            unknown_command()
    while choice.lower() == 'tshirts':
        tshirt_choice = input("T-shirts currently avilable: \n Black t-shirt-10$ \n Green t-shirt-10$ \n Gucci t-shirt-100$ \n Adidas t-shirt-40$ \n Type 'BACK' to comeback to main site. \n")
        if tshirt_choice.lower() == 'black':
            yes_no = input("Are you sure You want to add black t-shirt to your shopping cart? Yes/No")
            if yes_no.lower() == 'no':
                print("Ok, let's comeback to the t-shirt section.")
            while yes_no.lower() == 'yes':
                amountt = input("How many piecies of clothing would You like to buy?\n")
                if amountt.isdigit():
                    shopping_cost += 10 * int(amountt)
                    print(f"\n{shopping_cost}$ has been added to your total cost!\n")
                    break
                else:
                    unknown_command()
        elif tshirt_choice.lower() == 'green':
            yes_no = input("Are you sure You want to add green t-shirt to your shopping cart? Yes/No")
            if yes_no.lower() == 'no':
                print("Ok, let's comeback to the t-shirt section.")
            while yes_no.lower() == 'yes':
                amountt = input("How many piecies of clothing would You like to buy?\n")
                if amountt.isdigit():
                    shopping_cost += 10 * int(amountt)
                    print(f"\n{shopping_cost}$ has been added to your total cost!\n")
                    break
                else:
                    unknown_command()
        elif tshirt_choice.lower() == 'gucci':
            yes_no = input("Are you sure You want to add Gucci t-shirt to your shopping cart? Yes/No")
            if yes_no.lower() == 'no':
                print("Ok, let's comeback to the t-shirt section.")
            while yes_no.lower() == 'yes':
                amountt = input("How many piecies of clothing would You like to buy?\n")
                if amountt.isdigit():
                    shopping_cost += 100 * int(amountt)
                    print(f"\n{shopping_cost}$ has been added to your total cost!\n")
                    break
                else:
                    unknown_command
        elif tshirt_choice.lower() == 'adidas':
            yes_no = input("Are you sure You want to add Adidas t-shirt to your shopping cart? Yes/No")
            if yes_no.lower() == 'no':
                print("Ok, let's comeback to the t-shirt section.")
            if yes_no.lower() == 'yes':
                amountt = input("How many piecies of clothing would You like to buy?\n")
                if amountt.isdigit():
                    shopping_cost += 60 * int(amountt)
                    print(f"\n{shopping_cost}$ has been added to your total cost!\n")
                    break
                else:
                    unknown_command
        elif tshirt_choice.lower() == 'back':
            break
        else:
            unknown_command()  
    while choice.lower() == 'Shopping cart':
        print()
