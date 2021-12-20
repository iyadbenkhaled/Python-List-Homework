a = 12
s = "hello"
try:
    print(a+s)
    
except TypeError:
    print("Ooops, looks like '{}' and '{}' cannot be added.".format(a, s))
finally:
    print("Exption handled succesfully :D")