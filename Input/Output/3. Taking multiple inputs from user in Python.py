# Python programm showing how to 
# multiple input using split

# taking two inputs at a time 
    # The first methode
x, y = input("Enter three values:").split()
print("Number of boys: ", x)
print("Number of girsl: ", y)
print()

    # The second methode
x, y = [int(x) for x in input("Enter three values: ").split()]
print("First Number is: ", x)
print("Sescond Number is : ", y)
print()


# taking three inputs at a time
    # The first methode
x, y, z = input("Enter three values: ").split()
print("Number of boys is: ", x)
print("Number of girls is: ", y)
print("Number of students is: ", z)
print()

    # The second methode
x, y, z = [int(x) for x in input("Enter three values: ").split()]
print("The Number is: ", x)
print("The Second Nuber is: ", y)
print("The third Number is: ", z)
print()


# taking two inputs at a time
    # The first methode 
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}" .format(a, b))
print()

    # The second methode
a, b = [int(x) for x in input("Enter two valuses: ").split()]
print("First Number is {}, and the second number is: {}".format(a, b))
print()


# taking multiple inputs at a time
# and type casting using list() function
    # The first methode 
b = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", b)

    # The second methode
b = [int(x) for x in input("Enter mutiple values: ").split()]
print("Number of list is: ", b)

# taking mutiple inputs at a time separated by comma
# muss man comma schreiben
x = [int(x) for x in input("Enter multiple value: ").split(",")]
print("Number of list is: ", x)
