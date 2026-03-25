import time
import sys
#The required module[s]

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
print("  BETA EDITION [DEV ONLY]")
print("   This edition may be published alongside the official release version..")
print("    !!Please check out my other works like Dragon Breath Roulette!!")
print("May Eric Harris and Dylan Klebolds rest in peace...")
#Introduction

char_set = "CHARACTERS: Dylan, Maxwell, Charlie, Angela, Principle Wells, Roman"
#Variables go here


print("\n\n!!Press 'S' to start or 'E' to exit!! [CHAR ti print names of characters]")
start = input("C: ").upper()

if start == "CHAR":
	print(char_set)

if start == "S":
	print("ENJOY...")
if start == "E":
	print("RETURN WHEN YOU ARE READY, TRUTH-SEEKER.")
	sys.exit()
if start not in ["S", "E", "CHAR"]:
	print("NOT A CHOICE, RESTART THE PROGRAM AND MAKE A CHOICE")
	sys.exit()


#---START OF CHOICE 1: BEGINNING---
while True:
	print("\nDylan: Yo, you good? blacked out there for a second...")
	time.sleep(1); print("1. Yes")
	time.sleep(1.5); print("2. No")
	time.sleep(2); print("[Ignore] Dylan")
	choice = input("INPUT: ").upper()

	if choice == "1":
		print("\n[YOU] Yeah, I am good, thanks for asking... Are you?")
		print("Dylan: Actually a pretty good day so far... These pricks are ignoring us...")
		break

	if choice == "2":
		print("Want to talk about it? [Y/N]")
		inchoice = input("[CHOICE] ").upper()

		if inchoice == "Y":
			print("[YOU] We are getting botheres every single fucking day over nothing. How can you be okay?")
			print("Dylan: Use the chances where they are not to have a good time. Come on, schools over anyways...")
			break

		if inchoice == "N":
			print("Dylan: Well, if you do... let me know... Come on, schools over..")
			break

		if inchoice not in ["Y", "N"]:
			print("Dylan: ...Ignore me then...")

	if choice == "IGNORE":
		print("Dylan: That bad? Damn, man... Alright, schools over, we can go somewhere, have us a good time, cheer you up... Though I wish these bastards would leave us alone... Your own family picks on you and you don't see nothing wrong with that.... Guess it's kind of the same with mine, my family ignores me and considers my brother better...")
		break

	if choice not in ["1", "2", "IGNORE"]:
		print("Not making a choice means you lose out on dialogue... which is the whole game... WHOLE...")
#---END OF CHOICE 1---
