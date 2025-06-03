#program to create a pangram checker.
#approach 1 check for vowels
input_string = input("Enter the string to be checked: ")
vowels = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
for vowel in input_string:
    if vowel in vowels:
        vowels[vowel] +=1
print(vowels)
#approach 2 checking for all alphabets 
input_str =  input("Enter the string to be checked: ")
vowels_List = ['a','e','i','o','u']
vowels = {}
for c in input_str:
    if c in vowels_List:
        if c in vowels:
            vowels[c] += 1
        else: 
            vowels[c] =1
print(vowels)

