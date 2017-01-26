import sys

if  (len(sys.argv)) >=2:
    for arg in sys.argv[1:]:
        print("fizz buzz counting up to {}".format(arg))
    for number in range(1,int(arg)):
        if number % 3 == 0 and number % 5 == 0:
            print("fizz buzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)
#now I am going to repeat the whole loop; but there must be a way to insert one value into the end of the range if input at command line,
#and insert another value if input as my_input, without having to re-write the loop but  using a different variable. 
else:
    my_input = input("Enter a number:")
    print("fizz buzz counting up to {}".format(my_input))
    for number in range(1,int(my_input)):
        if number % 3 == 0 and number % 5 == 0:
            print("fizz buzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number) 
        
    



    
    
