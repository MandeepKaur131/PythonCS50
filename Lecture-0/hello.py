# print("What's your name? ")
# input is used for inputs from users
"""
Multiline comment!
"""
name = input("What's your name? ").strip().title()

# Rempve whitespace from str
# name = name.strip().title()

print("hello, " + name)
print("how are you,", name)

# the optional parameter you can pass
# end="\n" default
# sep=" " to decide how the text will be separated
print("hello, ", end="")
print(name, end="\n")

# format string
print(f"hello, {name}")