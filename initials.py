fullName = input("Hi! to see your initials enter your full name as \'first name\' \'second name\': ")
firstInitial = fullName[0]
secondIndex = fullName.find(' ')
secondInitial = fullName[secondIndex + 1]

print ("Your initial is \'%s %s\'" %(firstInitial,secondInitial))
