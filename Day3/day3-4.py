threshold_height = 120
customer_height = int(input("Enter your height in cm: "))
if customer_height >= threshold_height:
    customer_age = int(input("Enter your age: "))
    if customer_age < 12:
        ticket_price = 5
    elif customer_age <= 18:
        ticket_price = 7
    elif customer_age >= 45 and customer_age <= 55:
        ticket_price = 0
        print("You get a free ticket!")
    else:
        ticket_price = 50
    wants_photos = input("You can ride the roller coaster!\nDo you also want photos? \nReply Y for Yes or N for No: ")
    if wants_photos == "Y":
        ticket_price += 3
    elif wants_photos == "N":
        ticket_price += 0
    print(f"Your ticket price is {ticket_price} pounds")
else:
    print("Sorry, you are not tall enough to ride the roller coaster.")