#list: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True,"ball"]
print(mylist2)

#to get items from list using another variable
item = mylist2[-2]
print(item)

#useful metho to check if your index is in your list
for i in mylist: #1
    print(i)
print("\n")
if "apple" in mylist:#2
    print("yes")
else:
    print("NO")
# to check how many elements u have in your list you use the LEN()FUNCTION
print(len(mylist))
# to append another item to ur list u use the .append method
mylist.append("lemon",)
print(mylist)
#to insert an item to a particular index in the list we use the insert method
mylist.insert(1,"blueberry")
print(mylist)
# to remove an item from the list we use the pop method
