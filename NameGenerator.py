import random   
print ("welcome to a random name generator, please enter up to five names, and the program will randomly pick a name to be chosen\n") 
NumberNames= int(raw_input("How many names would you like to enter?- "))
if NumberNames== 1:
	 print("Cannot randomly generate names from one name")
if NumberNames== 2:
	print("Please enter your two names\n")
	names = [str(raw_input("Name1- ")),str(raw_input("Name2- "))]
	generate1= (random.choice(names))
	print(generate1)
	print("\n Thanks for playing")
if NumberNames == 3:
	print("please enter your three names")
	names2 = [str(raw_input("Name1- ")),str(raw_input("Name2- ")),str(raw_input("Name3- "))]
	generate2= (random.choice(names2))
	print(generate2)
	draw1= str(raw_input("would you like to draw again?-"))
	if (draw1== "yes"):
		names2.remove(generate2)
		generate22=(random.choice(names2))
		print(generate22)
		print("\n Thanks for Playing!")
if NumberNames== 4:
	print("Please enter your four names")
	names3=[str(raw_input("Name1- ")),str(raw_input("Name2- ")), str(raw_input("Name3- ")), str(raw_input("Name4- "))]
	generate3= (random.choice(names3))
	print(generate3)
	draw2= str(raw_input("Would you like to draw again?-"))
	if (draw2== "yes"):
		names3.remove(generate3)
		generate33= (random.choice(names3))
		print(generate33)
		draw22= str(raw_input("Would you like to draw again?-"))
		if(draw22== "yes"):
			names3.remove(generate33)
			generate333= (random.choice(names3))
			print(generate333)
			print("\n Thanks for Playing!")

