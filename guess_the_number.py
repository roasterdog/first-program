import random

prompts = "\nEnter a number ranging from 1 to 100. \n(Enter 'q' to exit): "
list_of_numbers = list(range(1,101))

def generated_number(lists, prompt):
	while True:
		user_input = input(prompt)
		random_num = random.choice(lists)

		if user_input == 'q':
			break

		if not user_input.isdigit():
			print("Sorry, I do not understand that.")
			continue

		print(f"Number chosen by computer: {random_num}")

		if random_num == int(user_input):
			print("You got it correct!")

		else:
			print("Oops, you didn't get it right.")

generated_number(list_of_numbers, prompts.lower())