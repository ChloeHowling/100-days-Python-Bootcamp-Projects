# FileNotFound


# KeyError
# a_dictionary = {'key':'value'}
# value = a_dictionary["what the heck"]

# IndexError
# fruit_List = ["Apple, "Orange", "Pear"]
# print(fruit_List[3])

# TypeError
# text = "abc"
# print(text + 5)

# try:
#     # Something that might cause an exception
# except:
#     # Do this is there was an exception
# else:
#     # Do this if there was no exception
# finally:
#     # Do this regardless of exception

# raise KeyError("This is an error that I made up")


height = float(input("Height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)


