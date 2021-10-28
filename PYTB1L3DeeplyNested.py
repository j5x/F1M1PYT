# Ik heb honger en wil eten
# als er nog wat ligt in de koelkast eet ik dat
# Als ik geen geld heb ga ik gewoon koken

Hunger = True
Cooking = False
Fridge = False
Money = True

if Hunger == True and Cooking == False and Fridge == False and Money == True:
    print("[x] You ordered pizza.")
elif Hunger == True and Cooking == False and Fridge == True:
    print("[x] Er ligt nog een kiekje in de koelkast.")
elif Hunger == False:
    print("[x] You're not hungry.")
else:
    print("[x] You're broke, go cook food")