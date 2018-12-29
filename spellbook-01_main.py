import Spellbook03_character
def main():
    Spellbook03_character.IntEx()
    nameList, characterCount = Spellbook03_character.ReadProfiles()
    profileChoice = Spellbook03_character.PickProfile(nameList, characterCount)
    if profileChoice == 0:
        charInfo = Spellbook03_character.CreateProfile()
        Spellbook03_character.DisplayCreateProfile(charInfo)
        counter = Spellbook03_character.AskEditProfile()
        while counter != 0:
            charInfo = Spellbook03_character.EditProfile(counter, charInfo)
            Spellbook03_character.DisplayCreateProfile(charInfo)
            counter = Spellbook03_character.AskEditProfile()
        Spellbook03_character.SaveClose(charInfo)

    else:
        #Go to B
        pass

main()
