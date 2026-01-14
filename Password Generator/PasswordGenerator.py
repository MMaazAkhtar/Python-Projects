import random as r
import string as s

def generate_password():

    uppercase_alphabets = s.ascii_uppercase
    lowercase_alphabets = s.ascii_lowercase

    numbers=['0','1','2','3','4','5','6','7','8','9']
    special_characters=['@']
    upper_part=r.choice(uppercase_alphabets)
    alpha_part1=r.choice(lowercase_alphabets)
    alpha_part2=r.choice(lowercase_alphabets)
    alpha_part3=r.choice(lowercase_alphabets)
    alpha_part=alpha_part1+alpha_part2+alpha_part3
    special_part=r.choice(special_characters)
    number_part1=r.choice(numbers)
    number_part2=r.choice(numbers)
    number_part3=r.choice(numbers)

    number_part=number_part1+number_part2+number_part3
    password=upper_part+alpha_part+special_part+number_part

    return password



Header="*****Welcome to the Password Generator: *****"
print(Header.center(100))

user_input=input("Enter P to generate password or Q to quit: ")
user_input.lower()

if user_input == "q":
    quit()
elif user_input != "p":
    print("Invalid Input! ")
else:
    result=generate_password()
    print(result)

    

    
