my_str=""
my_new_str=" "
print(f'{bool(my_str)}\n {bool(my_new_str)}')
my_fav_scripting="Pyhton"
print(f'{my_fav_scripting}')
print(my_fav_scripting)

print("Index class statred")
print(my_fav_scripting[0])
print(my_fav_scripting[5])
print(my_fav_scripting[-1])
print(my_fav_scripting[0:5])
print(my_fav_scripting[0:])
str_0_4=my_fav_scripting[0:5]
print(str_0_4)
print(my_fav_scripting[:5])
print(my_fav_scripting[2:4])
print("we can delete complete string but not a part of string")
del my_fav_scripting
my_fav_scripting="pyhton tutorials"
print(my_fav_scripting)
print(" we can not delete part of string")
del my_fav_scripting[1]


