import time
import sys
#These are the required modules


skull = r"""
       ______
     .-'      '-.
    /            \
   |,  .-.  .-.  ,|
   | )(_o/  \o_)( |
   |/     /\     \|
   (_     ^^     _)
    \__|IIIIII|__/
     | \IIIIII/ |
     \          /
      `--------`
"""

print(skull)


print("\nBLOOD & POWDER: BUILDUP")
print(" The Prequel to Blood & Powder")
print("  ALPHA EDITION [DEV ONLY]")
print("   This edition may be published alongside the official release version..")
print("    !!Please check out my other works like Dragon Breath Roulette!!")
print("May Eric Harris and Dylan Klebolds rest in peace...")


game = input("START GAME? Y/N: ").upper()
if game == "Y":
	print("STARTING GAME...")
elif game == "N":
	print("COME BACK WHEN YOU ARE READY, DUMB FUCK")
	sys.exit()
elif game not in ["Y", "N"]:
	print("STARTING GAME ANYWAYS, NUMBNUTS.")


#---START OF CHOICE SET 1: INDUCTION---
while True:
	print("\n'Yo, bro! You good? Blanked out there, for a second'")
	time.sleep(0.5); print("1. Say 'Yeah. Day dreamed a bit'")
	time.sleep(0.5); print("2. Say 'No...'")
	time.sleep(0.5); print("3. Say nothing")
	choice1 = input("INPUT: ").upper()

	if choice1 == "1":
		print("Alright.. Anything you want to talk about? Y/N")
		inchoice1 = input("[INPUT] ").upper()
		if inchoice1 == "Y":
			print("[YOU] I have been struggling.. Honestly do not know what to do")
			break
		elif inchoice1 == "N":
			print("[YOU] No, thank you, though. You were always nice to me")
			break
		elif inchoice1 not in ["Y", "N"]:
				print("Make a choice when you are ready...")

	elif choice1 == "2":
		print("'Oh... Okay..'")
		break

	elif choice1 == "3":
		print("'Something definetly is wrong... You never ignore me..'")
		break

	elif choice1 not in ["1", "2", "3"]:
		print("Relaunch the game when you are READY? WHY ARE YOU NOT READY IF YOU LAUNCHED THE GAME?????????????")
		print("BE FUCKING READY NEXT TIME " * 5)
		break
#---END OF CHOICE SET 1---


#--START OF CHOICE SET 2: REASON---
while True:
	print("\nDay at school goes by slowly. Menalina High School... School of hell..")
	print("1. Eat in the cafeteria")
	print("2. Eat at the staircase")
	print("3. Don't eat today")
	choice2 = input("INPUT: ").upper()

	if choice2 == "1":
		print("You get your food and sit down at a table. Your friend, Dylan, sits down with you. As you have a conversation a person behind you taps your head hard with a plastic luch tray. You look back and see it is Daniel... 'Dammit, can you stop, Daniel' Dylan says, speaking up to defend you.. Daniel chuckles but walks off.... He backed off.. for now")
		break

	if choice2 == "2":
		print("You go to the staircase, eating your food, Peyton walks by, she waves at you. You wave back but her boyfriend glares at you.. Dylan comes up to you. 'Daniel bothering you?' [Y/N]")
		inchoice2 = input("[INPUT] ").upper()
		if inchoice2 == "Y":
			print("'That damn bastard... One day he'll get what is coming to him...'")
			break
		if inchoice2 == "N":
			print("'You sure..? Alright, I will take your word for it.. Just let me know if he bothers you, bro..'")
			break
		if inchoice not in ["Y", "N"]:
			print("MAKE A CHOICE, BITCH.")

	if choice2 == "3":
		print("While hungry, you don't eat, not willing to take the abuse from other students.. You walk upstairs to your next class ahead of schedule..")
		break
#---END OF CHOICE SET 2---


#---START OF CHOICE SET 3: HOME---
while True:
	print("\nIt is the end of the day. Do you and Dylan go to your house? [Y/N]")
	choice3 = input("INPUT: ").upper()

	if choice3 == "Y":
		print("'Thanks for letting me come over, Mrs. Harris... Yo bro, want to order some food? I will pay' [Y/N]")
		inchoice3 = input("[INPUT] ").upper()
		if inchoice3 == "Y":
			print("[YOU] Sure. Thanks for paying. I'll get next time... 'Alright. Only chinese and the pizza place is open..")
			print("1. Chinese")
			print("2. Pizza")
			dchoice3 = input("[[INPUT]] ")
			if dchoice3 == "1":
				print("'Chinese it is!'")
			if dchoice3 == "2":
				print("[YOU] Pizza does sound good right about now")
			if dchoice3 not in ["1", "2"]:
				print("FINE, SKIP DIALOGUE [WHICH IS THE GAME ITSELF DUMBASS]")
		if inchoice3 == "N":
			print("'Alright, but I am hungry. Care if I get a snack?'")
		break
	if choice3 == "N":
		print("You and Dylan goes to the park... Next day arrives quickly")
		break
#---END OF CHOICE SET 3---


#--START OF CHOICE SET 4: RISE---
while True:
	print("\nYou and Dylan is in the basement. Playing pool... 'How many rounds should we get from the seller? Since the guns are for the range, we should not need much, right?'")
	print("1. Single Box [CRINGE]")
	print("2. A few Boxes")
	print("3. Enough for a massacre")
	choice4 = input("INPUT: ").upper()

	if choice4 == "1":
		print("[YOU] A single box should be fine. Can't over-do it, ya'know?")
		break

	if choice4 == "2":
		print("[YOU] Just a few. Enough to last a while..")
		break

	if choice4 == "3":
		print("'And how much exactly is that?")
		numchoice4 = input("[INPUT NUMBER] ")
		print(f"Alright, {numchoice4} it is, then'")
		break
#---END OF CHOICE SET 4---


#---START OF CHOICE SET 5: DELIVERY---
while True:
	print("\nDelivery arrives.. Looking at the stuff in your room, you are feeling quite satisfied. You and Dylan goes to the range, what to practice first?")
	print("1. AIM")
	print("2. Firing under timers")
	print("3. Nothing for today")
	choice5 = input("INPUT: ").upper()

	if choice5 == "1":
		print("'Aim is very important.... Alright, hop to, I guess..'")
		break

	if choice5 == "2":
		print("Timed firing, perfect, no sarcasm, we do need to practice that!")
		break

	if choice5 == "3":
		print("'Really? After waiting so long of waiting for these guns and ammunition?' [Y/N]")
		inchoice5 = input("[INPUT] ").upper()

		if inchoice5 == "Y":
			print("[YOU] Yeah, not feelung so well..")
			break
		if inchoice5 == "N":
			print("[YOU] I change my mind, let's get to practicing our aim for today.")
			break
#---END OF CHOICE SET 5---


#---START OF CHOICE SET 6: DESECRATION---
while True:
	print("Menalina. Menalina. MEnalina. MENalina. MENAlina. MENALina. MENALIna. MENALINa. MENALINA MELNILA")
	print("1. OPEn fIRE")
	print("2222 WArtvh Thekm BKLEED")
	print("DyLSAN MYURDER THGENM ALL")
	choice6 = input("InRHGJ: ").upper()

	if choice6 == "1":
		print("FIRE FIRE FIRE FIRE " * 5)
		inchoice = input("[BlOD] ").upper()
		if inchoice == "BLOOD":
			print("BLOOD BLOOD BLOOD BLOOD BLOOD")
			break

	if choice6 == "2":
		print("THEY BLEED THEY BLEED THEY BNLLEEDD")
		break

	if choice6 == "3":
		print("DYLAN FIRE FIRE DDLLYYAANN FFIIRREE DDDLLLYYYAAANNN FFFIIIRRREEE")
		break
#--END OF CHOICE SET 6---