choice = input("You have found an old laptop! What do you do with this laptop? (open it, leave it): ")
if choice == "leave it":
    print("The laptop transforms into a 13 foot tall monster and stomps on you!")
else:
    print("You open the laptop and an old version of internet explorer pops up.")
    choice2 = input("There is a bookmark labled 'RESTRICTED INFORMATION' Do you want to click it? (click it, no): ")
    if choice2 == "no":
        print("You close Internet Explorer and instead, you play 3d pinball!")
    else:
            print("You hear a knock at the door.")
