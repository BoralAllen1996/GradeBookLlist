#Using python list and its function for gradebook...
# Your code below: 
subjects = ["physics", "cslculus", "poetry", "history"]
grades = [98, 97, 85, 88]

#Adding subject..............
last_semester_gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
#gradebook.append(["computer science", 100])


#Adding subject.............
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88], ["computer science", 100]]
gradebook.append(["visual arts", 93])

# visual arts..
gradebook[4]

#Removing low grades...
gradebook.remove(["poetry", 85])

#Adding the passed subject on the list.....
gradebook.append(["pass", "poetry", 85])

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)

#End.............
