name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_in_cm = height / 0.39370  # centimeters
weight = 180 # lbs
weight_in_kg = weight / 2.2046 # kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches[{round(height_in_cm)} centimeters] tall.")
print(f"He's {weight} pounds[{round(weight_in_kg)} kilograms] heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
