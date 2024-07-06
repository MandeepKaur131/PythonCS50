# def to define functions

# def hello(to="world") :
#     print("hello,", to)

# hello()
# name = input("What's your name? ")

# hello(name)

# print(name)
# In python, you need to define the fuctions before they get called.
# which means you'll define them at the top which doesn't
# let your code flow logically
# so you can use the following approach with main

def main() :
    name = input("What's your name? ")
    hello(name)

def hello(to="world") :
    print("hello,", to)


main()