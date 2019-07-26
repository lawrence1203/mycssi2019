
print("hello world!")

print("Bye world!")

num1 = int(raw_input("Enter number #1: "))
num2 = int(raw_input("Enter number #2: "))
total = num1 + num2
print("The sum is " + str(total))

num = int(raw_input("Enter a number: "))
if num > 0:
    print("That is a positive number!")
    print("It is greater than zero!")
elif num < 0:
    print("That's a negative number!")
else:
    print("Zero is neither positive nor negative!")


string = "hello there"
for letter in string:
    print(letter.upper())

for i in range(5):
    print(i)

x = 1
while x <= 5:
    print(x)
    x = x + 1


my_name = "Bob"
friend1 = "Alice"
friend2 = "John"
friend3 = "Mallory"

print(
"My bane is %s and my friends are %s, %s, and %s" %
(my_name, friend1, friend2, friend3)
)


def greetAgent(first_name, last_name):
    print("%s. %s %s." % (last_name, first_name, last_name))
greetAgent('James', 'Bond')


def findSum(number):
    sum = 0
    for i in range(number):
        sum = sum + 1
    return sum + number

print(findSum(10))
