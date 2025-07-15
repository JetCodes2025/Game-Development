#1D list 
fruits= ['apple','mango','banana','kiwi']
#2D list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
#number of rows 
print("number of rows :", len(matrix))
#number of columns 
print("number of columns:", len(matrix[0]))
#accessing the items in 1D list 
print(fruits[2])
#accessing the items in 2D list 
print(matrix[0][1])
#looping through the 1D list 
print("All the fruit names from the list: ")
for i in fruits:
    print(i)
#looping through 3D list  #nested loops a loop inside a loop
for i in range(0,len(matrix)):
    for j in range(0, len(matrix[0])):
        print(matrix[i][j],end= " ")
    print("\n")
# take an input for amtrix and print the elements.
rows = int(input("enter the number of rows: "))
columns = int(input("enter the number of columns: "))
Matrix = []
temp= []
for i in range(rows):
    
    for j in range(columns):
        x = int(input("Enter the elements in the matrix : "))
        temp.append(x)
print(temp)








