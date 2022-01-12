age = int ( input ("How old are you?\n") )

decades = age // 10 # // whole number division
years = age % 10 # the remainder

print("You are " + str(decades) + " decades and " + str(years) + " years old.")