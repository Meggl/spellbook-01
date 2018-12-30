import spellbook_01_character
def main():
    spellbook_01_character.IntEx()
    nameList, characterCount, chDataGnameList, chDataGtypeList, infoCount = spellbook_01_character.ReadProfiles()
    profileChoice = spellbook_01_character.PickProfile(nameList, characterCount)
    if profileChoice == 0:
        charInfo = spellbook_01_character.CreateProfile()
        spellbook_01_character.DisplayCreateProfile(charInfo)
        counter = spellbook_01_character.AskEditProfile()
        while counter != 0:
            charInfo = spellbook_01_character.EditProfile(counter, charInfo)
            spellbook_01_character.DisplayCreateProfile(charInfo)
            counter = spellbook_01_character.AskEditProfile()
        spellbook_01_character.SaveClose(charInfo)

    else:
        #Go to B
        pass

main()
