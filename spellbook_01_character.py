# This program is meant to allow users to open a pre-existing character profile or create and save a new character profile.



"""
def CharProfileData():

    # name of data Group (ex: Ability Scores)
    # supposed data type for group
    # number of different data points in a group
    # Prompt (instructions) for input of data points
    # Name of data point

    # number of points of all data


    #

"""

# |A| MAIN WINDOW |A|
# |A1| describe what the program is !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def IntEx():
    print("This program is meant to allow you to open a pre-existing character profile or create and save a new character profile.")
    print("These are the character profiles you can choose from.")


# |A2|display the pre-existing character profile names
def  ReadProfiles():
    # |a2.1| Create empty lists to put the data of like type with each other (in order, of course)
    sb-01_character = open('sb_01_character.txt', 'r')

    nameList = []

    # |a2.2| create a counter that keeps track of how many character profiles there are
    characterCount = 0

	# |a2.3| create a list that notes the line number that starts each profile
    tableContents = [0]

	# |a2.4| create a 'list' that holds each line of the whole text document.
    content = sb-01_character.readlines()

	# |a2.5| Every time there is a sparator line the character Count will go up one, the particular number that the separator line is on will be marked under 'tableContents', and the following lines will be recorded in their respected lists.
    for line in range(len(content)):
        if content[line] == '--------------------\n':

			# |a2.5.1| the character Count will go up one
            characterCount += 1

			# |a2.5.2| the particular number that the separator line is on will be marked under 'tableContents'
            int(line)
            tableContents.append(line)

			# |a2.5.3| the following lines will be recorded in their respected lists.
            nameList.append(content[line+1])
        else:
            pass

	# |a2.6| Close document
    sb-01_character.close()

	# |a2.7| Return the lists, the tableContents, and the profile count.
    return nameList, characterCount

#|A3| *bc* Display the pre-existing character profiles and ]prompt the user to either select a pre-exising profile or create a new profile, and retrieve that input.
def PickProfile(nameList, characterCount):
	# |a3.1| Display the profiles that the user can choose from. [right now, choosing an already-made profile will lead to a temporary DEAD END]
    print("These are the profiles you may choose from:\n")
    print("``````````````````````````````````````````````````````\n")
    print("0. [Create New Character Profile]\n\n")
    for character in range(characterCount):
        print(character+1, ".", nameList[character], sep = "")
        print("\n")
        print("``````````````````````````````````````````````````````\n")

	# |a3.2| <Validation Loop> ask the user to select a profile or to create a new one
    while True:
        try:
            print("Select the profile by entering the profile's number. \nTo create a new character profile type '0' instead.")
            profileChoice = int(input("YOU:  "))
            # VALIDATION datatype
        except(typeError):
            again = input("Please type a valid digit to select the profile of your choosing.\nHit 'enter' to continue.")
            continue
        else:
			# VALIDATION range
            if profileChoice < 0 or profileChoice > characterCount:
                again = input("Please type a valid digit to select the profile of your choosing.\nHit 'enter' to continue.")
                continue
            else:
                break

	# |a3.3| return the user's choice
    return profileChoice


# |B| SELECT PRE-EXISTING PROFILE |B|
    # display deadend ~Terminate Program~



# |C| CREATE NEW PROFILE |C|
def CreateProfile():
	print("This is the Character Profile Creation section.\nPlease type in your character's information as prompted; you will have a chance to edit the information before saving.")
	# make an empty-ish list for the new information about to come in.
	charInfo = [""]

	# create a counter for the upcoming loop.
	counter = 1
	while counter <= 32:
		counter, charInput = PechangaMachine(counter)
		charInfo.append(charInput)
		counter += 1
	return charInfo



def PechangaMachine(counter):
	# create lists of prompts for the loop.
    prompts = ["", "Your character's full Name:", "Level:", "Strength Score:", "Dexterity Score:", "Constitution Score:", "Intelligence Score:", "Wisdom Score:", "Charisma Score:","Acrobatics Skill Proficiency:", "Animal Handling Skill Proficiency:", "Arcana Skill Proficiency:", "Athletics Skill Proficiency:", "Deception Skill Proficiency:", "History Skill Proficiency:", "Insight Skill Proficiency:", "Intimidation Skill Proficiency:", "Investigation Skill Proficiency:", "Medicine Skill Proficiency:", "Nature Skill Proficiency:", "Perception Skill Proficiency:", "Performance Skill Proficiency:", "Persuasion Skill Proficiency:", "Religion Skill Proficiency:", "Sleight of Hand Skill Proficiency:", "Stealth Skill Proficiency:", "Survival Skill Proficiency:", "Strength Saving Throw Proficiency:", "Dexterity Saving Throw Proficiency:", "Constitution Saving Throw Proficiency:", "Intelligence Saving Throw Proficiency:", "Wisdom Saving Throw Proficiency:", "Charisma Saving Throw Proficiency:"]
    promptSK = "Please type 'N' for 'no proficiencies', 'P' for 'proficiency', \n'F' for 'familiarity', or 'E' for 'expertise'."
    promptST = "Please type 'N' for 'no proficiencies' or 'P' for 'proficiency'."


	# Ask, Validate, Receive input
	#NAME
    if counter == 1:
        print(prompts[counter])
        charInput = input("YOU:   ")

    # LEVEL AND ABILITY SCORES
    elif counter >= 2 and counter <= 8:
        while True:
            try:
                print(prompts[counter])
                charInput = int(input("YOU:  "))
            except:
                again = input("Please type an integer. \nHit 'enter' to continue.")
                continue
            else:
                if charInput < 1 or charInput > 99:
                    again = input("Please type an integer between 1 and 99. \nHit 'enter' to continue.")
                    continue
                else:
                    break
    # nSKILLS
    elif counter >= 9 and counter <= 26:
        while True:
            print(promptSK)
            print(prompts[counter])
            charInput = input("YOU:  ")
            charInput.strip()
            if charInput != 'N' and charInput != 'n' and charInput != 'P' and charInput != 'p' and charInput != 'F' and charInput != 'f'and charInput != 'E' and charInput != 'e':
                again = input("Please type one of the letter options available.\nHit 'enter' to continue.")
                continue
            else:
                break
    # SAVING THROWS
    elif counter >= 27 and counter <= 32:
        while True:
            print(promptST)
            print(prompts[counter])
            charInput = input("YOU:  ")
            charInput.strip()
            if charInput != 'N' and charInput != 'n' and charInput != 'P' and charInput != 'p':
                again = input("Please type one of the letter options available.\nHit 'enter' to continue.")
                continue
            else:
                break
    else:
        print("Something went wrong: PechangaMachine Ask, Validate, Receive input")


    return counter, charInput


def DisplayCreateProfile(charInfo):
    print("\nHere is your character's information. Please review and decide if anything needs to be changed.")
    print("[1] Character Name:\t\t", charInfo[1],"\n[2] Level:\t\t\t", charInfo[2], "\n\nABILITY SCORES\n[3] Strength:\t", charInfo[3], "\t[4] Dexterity:\t", charInfo[4], "\t[5] Constitution:\t", charInfo[5], "\n[6] Intelligence:\t", charInfo[6], "\t[7] Wisdom:\t", charInfo[7], "\t[8] Charisma:\t", charInfo[8], "\n\nSKILLS\n[9] Acrobatics:\t\t", charInfo[9], "\n[10] Animal Handling:\t", charInfo[10],"\n[11] Arcana:\t\t", charInfo[11], "\n[12] Athletics:\t\t", charInfo[12], "\n[13] Deception:\t\t", charInfo[13], "\n[14] History:\t\t", charInfo[14], "\n[15] Insight:\t\t", charInfo[15], "\n[16] Intimidation:\t\t", charInfo[16], "\n[17] Investigation:\t\t", charInfo[17], "\n[18] Medicine:\t\t", charInfo[18], "\n[19] Nature:\t\t", charInfo[19], "\n[20] Perception:\t\t", charInfo[20], "\n[21] Performance:\t\t", charInfo[21], "\n[22] Persuasion:\t\t", charInfo[22], "\n[23] Religion:\t\t", charInfo[23], "\n[24] Sleight of Hand:\t", charInfo[24], "\n[25] Stealth:\t\t", charInfo[25], "\n[26] Survival:\t\t", charInfo[26], "\n\nSAVING THROW PROFICIENCY\n[27] Strength:\t", charInfo[27], "\t[28] Dexterity:\t", charInfo[28], "\t[29] Constitution:\t", charInfo[29], "\n[30] Intelligence:\t", charInfo[30], "\t[31] Wisdom:\t", charInfo[31], "\t[32] Charisma:\t", charInfo[32], "\n\n")


def AskEditProfile():
    print("If you wish to edit anything, please type the item's number.")
    while True:
        try:
            counter = int(input("YOU:  "))
        except:
            again = input("Please type an integer that is between 0 and 32.\nHit 'enter' to continue.")
            continue
        else:
            if counter > 32 or counter < 0:
                again = input("Please type an integer that is between 0 and 32.\nHit 'enter' to continue.")
                continue
            else:
                break
    return counter

def EditProfile(counter, charInfo):
    counter, charInput = PechangaMachine(counter)
    charInfo[counter] = charInput
    return charInfo

def SaveClose(charInfo):
    sb-01_character = open('sb_01_character.txt', 'a')
    sb-01_character.write('--------------------\n')
    for counter in range(len(charInfo)):
        if counter == 0:
            pass
        else:

            variable = str(charInfo[counter])
            # str(variable)
            variable += "\n"
            sb-01_character.write(variable)
    sb-01_character.write("")
    sb-01_character.close()
    print("Thank you.\n\nInformation was saved!")

# |D| CONFIRM ITEMS |D|
    # write the data into the text file
    # display to the user that the information was saved ~Terminate Program~

# |E| EDIT AN ITEM |E|
    # retrieve the user's character's data (One item) (using item's funciton)
    # display the user's character's data (All items)
    # |de|prompt the user to either edit an item or confirm all the items |de|

# NOTE: For C, we are collecting the data through a list and 'for' loop, then when we go down to E, that's when we'll use the functions.
