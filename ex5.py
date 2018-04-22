my_name = 'Rick J. Aquilia'
my_age = 29 #True Story
my_height = 75 #inches
my_weight = 215
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'
my_joke = "Haha, that's not heavy actually"

#The 'f' allows you to import variables within the braces in the code
#Similar to print("Let's talk about", my_name)
#Think of it as python within a string

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall")
print(f"He's {my_weight} pounds heavy")
print(my_joke)
print(f"He's got {my_eyes} eyes and {my_hair} hair")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

#This line is tricky, try to get it exactly right
#What we're doing here is performing a mathematical calculation using variables
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
