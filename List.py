#Managing a large amount of data using "List" to keep track of said values.
friend = ["Uzoma", "Chibu", "Bryan"] #Square brackets = to listed items.
            
print(friend[0]) # Access elements based off of there index.
print(friend[1])

print(friend[-1]) #Access index elements with negative number.

print(friend[1:3]) #Access specific elements.

friend = ["Adamma", "Obi", "Scott"]
friend[1] = "Mike" #Modify values even with those in list.
print(friend[1])

#/br Above infomration is seperate!!!!!

#List Funcitons
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Uzoma", "Chibu", "Adamma", "Mom"]
friends.extend(lucky_numbers) #Adds the list together
friends.append("Creed") #Adds string onto end of the list
friends.insert(1, "Kelly") #Replaces the value based on index value
#friends.remove("Uzoma") removes an element from list
#friends.clear removes all the elements in the list
#friends.pop() removes the last element in the list
#lucky_numbers.sort() sorts the elements in ascending order
#lucky_numbers.reverse() reverse the elements in ascending order
friends2 = friends.copy()
print(friends2)

print(friends.index("Chibu")) #Tells you if the element is in the list.
#print(friends.count()) tells you how many of that element is in the list
#