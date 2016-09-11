print "You want a burrito. Do you go into Taco Bell or the local authentic Mexican place?"

choice = raw_input("> ")

if choice == "1":
	print "The kid at the counter is greasy and high. What do you do?"
	print "1. Stay and order your burrito."
	print "2. Leave and go to the local authentic place."

	decision = raw_input("> ")

	if decision == "1":
		print "OK, that's your decision, however unwise."
		print "Do you want a beef, chicken, or veggie burrito?"

		burrito = raw_input("> ")

		if burrito == "beef":
			print "Great choice. The beef is only 6 days old. You probably won't get dysentary. \nUnfortunately for you, the greasy, high \nburrito guy fills you burrito \nin sections by width rather than length. What do you do?"
			print "1. Yell at the greasy burrito maker that you are not a fucking pellican \nand can't eat a burrito lengthwise."
			print "2. Push the greasy burrito maker to see if he is, in fact, a goddamn mop \nwith a hat that spilled some shit into a burrito."
			print "3. Ask the greasy, high burrito maker for a hit to make your wade through \nthe river of cilantro more endurable."

			reaction = raw_input("> ")

			if reaction == "1":
				print "Great choice. Now make a burrito hat for the burrito maker out of the \nburritobomination you were handed."
			elif reaction == "2":
				print "Your instinct was correct. Check the place for a live, human burrito \nmaker and request a new burrito."
			elif reaction == "3":
				print "At least the burrito maker was smart enough to buy dank. You eat your \nburrito like corn on the cob and go on with your day."
			else:
				print "All I'm going to say is that murder is illegal in all 50 states."

		elif burrito == "chicken":
			print "Yeesh, sorry. Say goodbye to your friends, family, and pets."
		else:
			print "Good decision, sincerely. You will most likely not die on this Taco Bell trip."

	elif decision == "2":
		print "Much better decision. Enjoy your delicious burrito."
	else:
		"Go for pizza."

elif choice == "2":
	print "Enjoy your fabulous, authentic burrito."

else:
	print "I guess you aren't that hungry after all."


