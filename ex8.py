formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I made myself a snowball",
    "As perfect as can be",
    "I thought I'd keep it as a pet",
    "Or let it sleep with me"
))
