import random as r
End='**********************************************'
print("Welcome to Snake Water Gun Game!")
while True:
    print("Enter 1 for Snake ,\nEnter 2 for Water,\nEnter 3 for Gun:")
    user_input=input("Enter your Option: ")

    if user_input=='1':
        print("Snake\nvs")
    elif user_input=='2':
        print("Water\nvs")
    elif user_input=='3':
        print("Gun\nvs")
    else:
        print("Invalid Input")
        print("Enter 1 for Snake ,\nEnter 2 for Water,\nEnter 3 for Gun:")
        user_input=input("Enter your Option: ")


    options=["Snake","Water","Gun"]
    computer_option=r.choice(options)
    print(f"Computer chose:{computer_option}")

    if user_input =='1' and computer_option=="Snake":#snake vs snake
        print('Snake vs Snake:No point')
        continue
    elif user_input =='2' and computer_option=="Snake":#Water vs Snake
        print("Water vs Snake:Computer Point\nSnake drank Water")
        continue
    elif user_input =='3' and computer_option=="Snake":#Gun vs Snake
        print("Gun vs Snake:Player Point\nGun shoots Snake")
        continue

    if user_input =='1' and computer_option=="Water" :#snake vs water
        print('Snake vs Water:Player point\nSnake drank water')
        continue
    elif user_input =='2' and computer_option=="Water":#Water vs Water
        print("Water vs Water:No point")
        continue
    elif user_input =='3' and computer_option=="Water":#Gun vs Water
        print("Gun vs Water:Computer Point\nGun drowned in Water")
        continue
    if user_input =='1' and computer_option=="Gun" :#snake vs Gun
        print('Snake vs Gun:Computer point\n Gun shoots Snake')
        continue
    elif user_input =='2' and computer_option=="Gun":#Water vs Gun
        print("Water vs Gun:Player Point\nGun drowned in water")
        continue
    elif user_input =='3' and computer_option=="Gun":#Gun vs Gun
        print("Gun vs Gun:No Point")
        continue
    End='**********************************************'
    print(End)  


