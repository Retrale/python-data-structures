def mid(x):
    word_length = len(x)
    middle_letter = ""
    if (word_length % 2) != 0:
        mid_point = int(((word_length/2) + 0.5)-1)
        middle_letter = x[mid_point]
        
        
    else:
        middle_letter=""
        
    return(middle_letter)

print(f"{mid('dragons').capitalize()} is the middle letter.")

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

#username = input("Please enter your username: ")

#display_invoice(username, 100.01, "01/02")


def  add(x, y):
    z = x + y
    return z

def  subtract(x, y):
    z = x - y
    return z

def  multiply(x, y):
    z = x * y
    return z

def  divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))


def create_name(first, last):
    
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("WILLIAM", "PLANT")
print(full_name)

fruits = ["apple", "orange", "banana", "coconut"]
for i in range(len(fruits)):
    print(fruits[i])
print(fruits[::-1])
print(fruits[::2])

for fruit in fruits:
    print(fruit)

#print(dir(fruits))

#print(help(fruits))
    
#print(len(fruits))
#print("apple" in fruits) returns a boolean
fruits[1] = "pineapple"    
for fruit in fruits:
    print(fruit)

fruits.append("sausage")
print(fruits)

fruits.remove("sausage")
print(fruits)

fruits.insert(0, "grape")
print(fruits)

#alphabetical sort
fruits.sort()
print(fruits)

#reverse order of list
fruits.reverse()
print(fruits)

#clears a list
#fruits.clear()
#print(fruits)

#prints index psoition
print(fruits.index("apple"))

print(fruits.count("apple"))

#sets
#unordered and immutable, but add/remove is okay, NO duplicates
fruits = {"apple", "orange", "banana", "coconut"}
print(fruits)

print(len(fruits))
print("pineapple" in fruits)
#print(fruits[0]) cannot use indexing on sets as the order changes

fruits.add("pineapple")
print(fruits)

fruits.remove("apple")
print(fruits)
fruits.pop()#removes whatever elemt is first, random with a set
print(fruits)

fruits.clear()
print(fruits)


#tuples - ordered and unchangeable duplicates are okay.
#faster than lists
fruits = ("apple", "orange", "banana", "coconut", "coconut")
print(fruits)

print(fruits.index("apple"))
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit)


#dictionary tutorial/hashmap
my_dict = {
    'first_name': "William",
    'surname': "Plant",
    'age': 23,
    'birth_year': 2000,
    'birth_month': "November",
    'day_born': "3rd"
}

print(f"{my_dict['first_name']} is {my_dict['age']} years old and he was born on the {my_dict['day_born']} of {my_dict['birth_month']} in the year {my_dict['birth_year']}.")

name_change = input("What is your new name? ")

my_dict["first_name"] = name_change

print(f"{my_dict['first_name']} is {my_dict['age']} years old and he was born on the {my_dict['day_born']} of {my_dict['birth_month']} in the year {my_dict['birth_year']}.")

#a function is a little worker, if that workers job is to make a sandiwch, by the time that function is run, it will return a sandwich

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict_values = my_dict.values()
print(my_dict_values)

class character:
    def __init__(self, name, size, age, race):
        self.name = name
        self.size = size
        self.age = age
        self.race = race
        
user = character("John", "Big", 15, "Dwarf")

print(user.race)