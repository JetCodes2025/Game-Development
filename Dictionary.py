# students_details 
name = "abc"
age = 12
address = "123@anywhere"
marks = 480
is_passed = True
#data structure 
#list is mutable , non-homogeneous, and ordered sequence of items.
student_details = ["abc", 12, "123@anywhere", 480, True]
#real life example of lists is groccery list.
#dictionary is mutable
contacts = {
    "name":"Jane Doe",
    "number": 123456789,
    "age":23,
    "city":"New York"
} 
print(contacts)
#Accessing the value from the dictionary 
print(contacts['name'])
#get the list of keys 
print(contacts.keys())
#use of for loop 
for key in contacts:
    print(key,contacts[key])
#if condition to check whether a key exists or not in a dictionary 
if "country" in contacts:
    print(contacts["country"])
else: 
    print("key does not exists")
#as dictionary is mutable we can add key value pairs 
contacts["country"] = "Unites States"
print(contacts)

