print("Mary had a little lamb.")
# You need a . before format for this to assign 'snow' to the brackets
# This tells python you want to run a command so the period is essential
print("Its fleece was white as {}".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)
# What'd that do
# It created 10 periods

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end
print(end1 + end2 + end3 + end4 + end5 + end6, end= ' ')
# If we remove the ,end = ' ' then it separates the value as such
# Cheese
# Burger
# If we keep it, it outputs 'Cheese Burger' so it's printing the
# following on the same line
print(end7 + end8 + end9 + end10 + end11 + end12)
