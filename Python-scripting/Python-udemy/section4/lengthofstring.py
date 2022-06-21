my_fav_scripting="python tutorials"
my_str_leng=len(my_fav_scripting)
print(f'Length of a given string is : {my_str_leng}')
print(f'Length of a given string call via direct variable: {len(my_fav_scripting)}')
print(my_fav_scripting[-1])
print(my_fav_scripting[-16:-5])




print("below statement won't work because index starting values always has to start with low values")
print(my_fav_scripting[-5:-16])

