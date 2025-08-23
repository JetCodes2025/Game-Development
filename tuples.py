my_tuple=("apples","banana","cherry",89.9,True,45)
print(my_tuple)

Stud_details =("Jane",12)
#packing
address=('225', "buckfield Shelters","New York", '234523')
for i in address:
    print(i , end=" ")
#unpacking
house_no, apartment_name,city, pin = address
print()
print("House No:" , house_no)
print("Apartment Name: ", apartment_name)
print("City:", city)
print("Pin Code: ", pin)

#tuples can be created without using parentheses
my_tuple1= "apples","banana","cherry",89.9,True,45
print(my_tuple1)
# nested tuple 
n_tuple=("mouse",(1,2,3),['a','b','c'])
print(n_tuple)

#nested index 
print(n_tuple[2][1]) 
print(n_tuple[1][1])

#slicing in the tuple 
vowels_tuple=('a','e','i','o','u')
print(vowels_tuple[1])
print(vowels_tuple[1:4])
print(vowels_tuple[3:])
vowels_tuple=('a','b',[1,2,3]) #tuples can be reassigned.
print(vowels_tuple)



