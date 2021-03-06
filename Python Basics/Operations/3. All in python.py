class learn:
    # This code explains how can we
    # use 'any' function on list
    list1 = []
    list2 = []

    # Index ranges from 1 to 10 to multiply
    for i in range(1,11):
        list1.append(4*i)

    # Index to access the list2 is from 0 to 9
    for i in range(0,10):
        list2.append(list1[i]%5==0)

    print('See whether at least one number is divisible by 5 in list 1=>')
    print(any(list2))

    # Python code to demonstrate working of
    # add(), sub(), mul()

    # importing operator module
    import operator

    # Initializing variables
    a = 4
    b = 3

    # using add() to add two numbers
    print ("The addition of numbers is :",end="")
    print (operator.add(a, b))

    # using sub() to subtract two numbers
    print ("The difference of numbers is :",end="")
    print (operator.sub(a, b))

    # using mul() to multiply two numbers
    print ("The product of numbers is :",end="")
    print (operator.mul(a, b))

    # Python code to demonstrate working of
    # truediv(), floordiv(), pow(), mod()

    # importing operator module
    import operator

    # Initializing variables
    a = 5
    b = 2

    # using truediv() to divide two numbers
    print ("The true division of numbers is : ",end="")
    print (operator.truediv(a,b))

    # using floordiv() to divide two numbers
    print ("The floor division of numbers is : ",end="")
    print (operator.floordiv(a,b))

    # using pow() to exponentiate two numbers
    print ("The exponentiation of numbers is : ",end="")
    print (operator.pow(a,b))

    # using mod() to take modulus of two numbers
    print ("The modulus of numbers is : ",end="")
    print (operator.mod(a,b))

    # Python code to demonstrate working of
    # lt(), le() and eq()

    # importing operator module
    import operator

    # Initializing variables
    a = 3
    b = 3

    # using lt() to check if a is less than b
    if(operator.lt(a,b)):
        print ("3 is less than 3")
    else : print ("3 is not less than 3")

    # using le() to check if a is less than or equal to b
    if(operator.le(a,b)):
        print ("3 is less than or equal to 3")
    else : print ("3 is not less than or equal to 3")

    # using eq() to check if a is equal to b
    if (operator.eq(a,b)):
        print ("3 is equal to 3")
    else : print ("3 is not equal to 3")


    # Python code to demonstrate working of
    # gt(), ge() and ne()

    # importing operator module
    import operator

    # Initializing variables
    a = 4
    b = 3

    # using gt() to check if a is greater than b
    if (operator.gt(a,b)):
        print ("4 is greater than 3")
    else : print ("4 is not greater than 3")

    # using ge() to check if a is greater than or equal to b
    if (operator.ge(a,b)):
        print ("4 is greater than or equal to 3")
    else : print ("4 is not greater than or equal to 3")

    # using ne() to check if a is not equal to b
    if (operator.ne(a,b)):
        print ("4 is not equal to 3")
    else : print ("4 is equal to 3")


