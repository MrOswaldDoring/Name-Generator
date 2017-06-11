import random

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"
user_name = ""
inputs = []
dx=dy=0

user_input_1 = input("How many letters would you like the name to be?: ")
user_input_2 = input("How many names would you like to generate?: ")

name_length = int(user_input_1)
num_of_names = int(user_input_2)

for num in range(name_length):
		inputs.append(input("Enter 'v' for vowels, 'c' for consonants, or enter your letter of choice: "))

def text_generator():
	global user_name

	for i in inputs:
		if i == 'v':
			user_name += random.choice(vowels)
		elif i == 'c':
			user_name += random.choice(consonants)
		else:
			user_name += i

	return user_name

for j in range(num_of_names):
	text_generator()
	print(user_name)
	user_name = ""

