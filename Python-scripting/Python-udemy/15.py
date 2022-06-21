#simple addition
a=4
b=8
result=a+b
print(f'the addition of {a} and {b} is:{result}')

print("Till here we are fixing the variables but if we want to work with human choosen variable then follow below procedure")

#Random int variables
a=input("Enter a value: ")
b=input("Enter b value: ")
print(f'The value of a is : {a} and type is: {type(a)}')
print(f'The value of a is : {b} and type is: {type(b)}')
print("input command will always work as string data type to avoid that we have to use type casting")
x=input("Enter x: ")
type(x)
x=int(input("Enter x"))
print(type(x))
y=eval(input("Enter y:"))  #3.4
print(type(y))


#simple addition
a=eval(input("Enter a value: "))
b=eval(input("Enter b value: "))
result=a+b
print(f'the addition of {a} and {b} is:{result}')
print(f'The value of a is:{a} and {type(a)}')
print(f'The value of a is:{b} and {type(b)}')

print("Till here we are fixing the variables but if we want to work with human choosen variable then follow below procedure")

