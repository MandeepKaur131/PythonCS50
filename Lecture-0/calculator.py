# x = input("Enter value for x: ")
# y = input("Enter value for y: ")

# x = int(input("Enter value for x: "))
# y = int(input("Enter value for y: "))


# z = int(x) + int(y)
# print(x + y)

# print(int(input("Enter value for x: ")) + int(input("Enter value for y: ")))

# x = float(input("Enter value for x: "))
# y = float(input("Enter value for y: "))
# # print(f"{round(x + y, 2): ,}")
# print(f"{x + y: .2f}")

def main() :
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n) :
    return n * n

main()
