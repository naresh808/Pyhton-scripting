'''
#we can declare variable in a single line also
x=3;y=5.7;lang_name="pyhton scriting"
'''
x=3
y=5.7
lang_name="pyhotn scripting"
print(x,y,lang_name)
print("it will print out as per varible order in format")
print("{} {} {}".format(x,y,lang_name))  #it will print out as per varible order in format


print("will give output in line by line")


print("{} \n{} \n{}".format(x,y,lang_name)) #will give output in line by line


print("{} {} {}".format(y,x,lang_name)) #it will print out as per varible order in format


print(f"x value is:{x} The y value is:{y} The language is:{lang_name}")


print(f"x value is:{x} \nThe y value is:{y} \nThe language is:{lang_name}")

#To print out as per out requirement way then we can store that way in variable and we can call it
my_req_output=f"x value is:{x} \nThe y value is:{y} \nThe language is:{lang_name}"
print(my_req_output)
