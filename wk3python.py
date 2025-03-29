# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
def sumOfList(x):
    total_sum = 0
    for i in x:
        total_sum += i  # Accumulate sum
    print("Sum of list:", total_sum)

myList = []
print("Enter a list of 4 integers:")

for _ in range(4):  # Loop 4 times
    num = int(input())  # Take input and convert to integer
    myList.append(num)  # Append to list

print("Your list:", myList)
sumOfList(myList)  # Call the function with the list


# Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
myBooks = ("Atomic Habits","Beef","Lower","Phone Booth","Beyond Zero")
for i in myBooks:
    print(i)
    i =+1
# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
a = input("What's your name?")
b = int(input("What' your age?"))
c = input("What's your favourite color?")

bio = {"name":a,"age":b,"color":c}
print(bio)
# Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
def setsdisplay(a,b):
    print(str("the sets are, set1:"+a+ "set2:"+b))
int1 = set()
int2 = set()
print("Enter 4 numbers for set one:")
for i in range(4):
    num1 = int(input())
    int1.add(num1)
print("For set 2 please 😘")
for j in range(4):
    num2 = int(input())
    int2.add(num2)
setsdisplay(int1,int2)
# Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

breakfast = ["milk","cookies","biscuit","eggs"]
odd_num = []
char_count = 0
for i in breakfast:
    print(i)
    char_count = 0#resets the character count to zero otherwise it will just register "cookies only"
    for j in range(len(i)) :
        addition += 1
       
    if addition%2 !=0:
        odd_num.append(i)
print("The list with items of odd numbbers are:", odd_num)