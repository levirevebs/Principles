feet = int(input("How tall are you in feet?"))
inches = int(input("How many inches are you tall (minus feet)"))
totalinches = feet * 12 + inches
totalmeters = totalinches * 0.0254
print("Your height in meters is", totalmeters)