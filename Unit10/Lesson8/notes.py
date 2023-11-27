thing = '0123456789'
#print(thing[5])

#print(thing[:5])

#text = "these are lowercase letters"
#text_cap = text.upper()
#print(text_cap)

user_number = input("Give me a number:")
if user_number.isnumeric():
    print('This is a good number!')
elif user_number[0] == "-" and user_number[1:].isnumeric:
        print('This is a negative number!')
else:
    print('This is a bad number! :', user_number)