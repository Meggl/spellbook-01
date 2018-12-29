import spellbook-01_character
def main():
    spellbook-01_character.IntEx()
    nameList, characterCount = spellbook-01_character.ReadProfiles()
    profileChoice = spellbook-01_character.PickProfile(nameList, characterCount)
    if profileChoice == 0:
        charInfo = spellbook-01_character.CreateProfile()
        spellbook-01_character.DisplayCreateProfile(charInfo)
        counter = spellbook-01_character.AskEditProfile()
        while counter != 0:
            charInfo = spellbook-01_character.EditProfile(counter, charInfo)
            spellbook-01_character.DisplayCreateProfile(charInfo)
            counter = spellbook-01_character.AskEditProfile()
        spellbook-01_character.SaveClose(charInfo)

    else:
        #Go to B
        pass

main()
