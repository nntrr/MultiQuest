import time

def start_game():
    print("""
                                    WELCOME !! to MultiQuest: Tales of Adventure 
                                    Where you are the hero, the man of the hour. 
                                    
This is a text based adventure game where you are given options (yes or no) which will decide your fate, the story of your life.
This storys has been taken from my favourite movies and characters. """)

    choice = input("Choose your hero's name: ")

    print(f"\nAh, {choice}! You embark on an extraordinary journey across different worlds, where your choices shape the course of destiny.")
    time.sleep(2)
    print("Armed with the Space Stone, you have the power to traverse various dimensions and join iconic heroes in their battles.")
    time.sleep(2)
    print("Your adventure begins now. The fate of these worlds lies in your hands.")

    start_journey()

def start_journey():
    print("\nYou find yourself standing before the mighty Space Stone.")
    time.sleep(2)
    print("This powerful artifact grants you control over space, enabling you to travel to different realms.")
    time.sleep(2)
    choice = input("Are you ready to embark on a grand adventure? (yes / no): ")

    if choice.lower() == "yes":
        print("\nBrave and ready, you activate the Space Stone, feeling its energy course through you.")
        time.sleep(2)
        print("You can now travel to different worlds and make a difference.")
        time.sleep(2)
        choose_world()

    elif choice.lower() == "no":
        print("\nTake your time, hero. When you're ready, return and we shall begin your journey.")
        time.sleep(2)
        print("Remember, the call to adventure awaits.")
        time.sleep(2)
        start_journey()

    else:
        print("\nInvalid choice. Try again.")
        start_journey()

def choose_world():
    print("\nThe universe presents you with six distinct paths: the Wizarding World, the World of Superheroes, the realm of Mutants, the ancient realm of Middle-earth, the dreamscape of Inception, and the high seas of Pirates of the Caribbean.")
    time.sleep(2)
    choice = input("Where would you like to go? (wizarding / superheroes / mutants / middle-earth / inception / pirates): please type the whole word")

    if choice.lower() == "wizarding":
        print("\nYou step through a magical portal and find yourself in the enchanting Wizarding World.")
        time.sleep(2)
        print("Here, you can choose to join the fight against dark forces or explore the magical world on your own.")
        time.sleep(2)
        harry_potter_story()

    elif choice.lower() == "superheroes":
        print("\nYou step through a cosmic portal and find yourself in a world teeming with superheroes.")
        time.sleep(2)
        print("Here, you have the opportunity to team up with iconic heroes against formidable foes.")
        time.sleep(2)
        superhero_story()

    elif choice.lower() == "mutants":
        print("\nYou pass through a dimensional rift and find yourself in a world where mutants with extraordinary powers exist.")
        time.sleep(2)
        print("Here, you can choose to join the X-Men and fight for the peaceful coexistence of mutants and humans.")
        time.sleep(2)
        xmen_story()

    elif choice.lower() == "middle-earth":
        print("\nYou step into the ancient realm of Middle-earth, a world of magic, courage, and destiny.")
        time.sleep(2)
        print("Here, you can choose to join the quest to destroy the One Ring or forge your own path.")
        time.sleep(2)
        lotr_story()

    elif choice.lower() == "inception":
        print("\nYou enter the dreamscape of Inception, where reality and imagination intertwine.")
        time.sleep(2)
        print("Here, you can choose to be a skilled dream extractor or explore the depths of the human mind.")
        time.sleep(2)
        inception_story()

    elif choice.lower() == "pirates":
        print("\nYou set sail on the high seas of Pirates of the Caribbean, a world of swashbuckling adventure.")
        time.sleep(2)
        print("Here, you can choose to become a daring pirate captain or uncover the secrets of cursed treasure.")
        time.sleep(2)
        pirates_story()

    else:
        print("\nInvalid choice. Try again.")
        choose_world()

def harry_potter_story():
    print("\nIn the Wizarding World, you find yourself at Hogwarts School of Witchcraft and Wizardry.")
    time.sleep(2)
    print("As you explore, you encounter fellow witches and wizards who seek your help in the fight against dark forces.")
    time.sleep(2)
    choice = input("Will you join the Order of the Phoenix and confront the dark wizard? (yes / no): ")

    if choice.lower() == "yes":
        print("\nYou join the Order of the Phoenix, training alongside Harry Potter and his allies.")
        time.sleep(2)
        print("Together, you face dangerous quests and work towards defeating the dark forces.")
        time.sleep(2)
        final_battle("Voldemort", "wizarding")

    elif choice.lower() == "no":
        print("\nYou decide to follow your own path, venturing through the magical world and forging your own destiny.")
        time.sleep(2)
        print("With your unique skills and alliances, you uncover secrets and make a lasting impact.")
        time.sleep(2)
        final_battle("Voldemort", "wizarding")

    else:
        print("\nInvalid choice. Try again.")
        harry_potter_story()

def superhero_story():
    print("\nIn the world of superheroes, you find yourself in a bustling metropolis where heroes protect the innocent.")
    time.sleep(2)
    print("As you explore, you encounter renowned heroes such as Iron Man, Superman, and Batman.")
    time.sleep(2)
    choice = input("Which hero would you like to team up with? (iron man / superman / batman): ")

    if choice.lower() == "iron man":
        print("\nYou join forces with Iron Man to investigate a technological mystery.")
        time.sleep(2)
        print("Together, you unravel a villain's plot, showcasing your expertise in technology and heroics.")
        time.sleep(2)
        final_battle("Ultron", "superheroes")

    elif choice.lower() == "superman":
        print("\nYou team up with Superman to face the formidable threat of Darkseid.")
        time.sleep(2)
        print("Together, you soar through the skies, unleashing your powers for the greater good.")
        time.sleep(2)
        final_battle("Darkseid", "superheroes")

    elif choice.lower() == "batman":
        print("\nYou collaborate with Batman to stop the cunning plans of the Joker.")
        time.sleep(2)
        print("Together, you navigate the shadows and confront the chaos in Gotham City.")
        time.sleep(2)
        final_battle("Joker", "superheroes")

    else:
        print("\nInvalid choice. Try again.")
        superhero_story()

def xmen_story():
    print("\nIn the realm of mutants, you find yourself at the X-Mansion, a haven for mutants.")
    time.sleep(2)
    print("As you explore, you encounter the X-Men, a team dedicated to maintaining peace between mutants and humans.")
    time.sleep(2)
    choice = input("Will you join the X-Men in their quest for coexistence? (yes / no): ")

    if choice.lower() == "yes":
        print("\nYou join the X-Men, training under Professor Xavier and honing your mutant abilities.")
        time.sleep(2)
        print("Together, you face challenges, battling against prejudice and dangerous adversaries.")
        time.sleep(2)
        final_battle("Magneto", "mutants")

    elif choice.lower() == "no":
        print("\nYou decide to take a different path, venturing through the world of mutants as a lone hero.")
        time.sleep(2)
        print("With your unique powers and principles, you make your mark on the mutant world.")
        time.sleep(2)
        final_battle("Magneto", "mutants")

    else:
        print("\nInvalid choice. Try again.")
        xmen_story()

def lotr_story():
    print("\nIn the ancient realm of Middle-earth, you find yourself amid a grand quest.")
    time.sleep(2)
    print("As you explore, you encounter brave companions who seek to destroy the One Ring.")
    time.sleep(2)
    choice = input("Will you join the Fellowship of the Ring to save Middle-earth? (yes / no): ")

    if choice.lower() == "yes":
        print("\nYou join the Fellowship of the Ring, embarking on a perilous journey.")
        time.sleep(2)
        print("Together, you face fearsome creatures and the forces of darkness.")
        time.sleep(2)
        final_battle("Sauron", "middle-earth")

    elif choice.lower() == "no":
        print("\nYou decide to take a different path, venturing through the vast landscapes of Middle-earth.")
        time.sleep(2)
        print("With your unique skills and alliances, you leave an indelible mark on the realm.")
        time.sleep(2)
        final_battle("Sauron", "middle-earth")

    else:
        print("\nInvalid choice. Try again.")
        lotr_story()

def inception_story():
    print("\nIn the dreamscape of Inception, you unlock the potential of the human mind.")
    time.sleep(2)
    print("As you delve into dreams within dreams, you can choose to be a skilled dream extractor or an enigmatic architect.")
    time.sleep(2)
    choice = input("What role will you take in this dreamscape? (extractor / architect): ")

    if choice.lower() == "extractor":
        print("\nYou become a skilled dream extractor, adept at navigating the subconscious.")
        time.sleep(2)
        print("With your unique talents, you uncover hidden truths and secrets buried in the human mind.")
        time.sleep(2)
        final_battle("Cobb's subconscious", "dreams")

    elif choice.lower() == "architect":
        print("\nYou assume the role of an enigmatic architect, capable of shaping dream worlds.")
        time.sleep(2)
        print("With your imagination, you craft awe-inspiring dreamscapes and explore the depths of human consciousness.")
        time.sleep(2)
        final_battle("Subconscious constructs", "dreams")

    else:
        print("\nInvalid choice. Try again.")
        inception_story()

def pirates_story():
    print("\nOn the high seas of Pirates of the Caribbean, you find yourself amidst a world of piracy and cursed treasure.")
    time.sleep(2)
    print("As you explore, you encounter legendary pirates and mystical artifacts.")
    time.sleep(2)
    choice = input("Will you become a daring pirate captain or uncover the secrets of cursed treasure? (pirate / treasure): ")

    if choice.lower() == "pirate":
        print("\nYou embrace the life of a daring pirate captain, sailing the seas and seeking adventure.")
        time.sleep(2)
        print("With your cunning and charisma, you leave a mark on the pirate world and carve out your own legend.")
        time.sleep(2)
        final_battle("Davy Jones", "pirates")

    elif choice.lower() == "treasure":
        print("\nYou embark on a quest to uncover the secrets of cursed treasure and its enigmatic curse.")
        time.sleep(2)
        print("With your bravery and resourcefulness, you delve into mysteries that span the ages.")
        time.sleep(2)
        final_battle("Curse of the Aztec Gold", "pirates")

    else:
        print("\nInvalid choice. Try again.")
        pirates_story()

def final_battle(enemy, world):
    print(f"\nPrepare yourself for the ultimate showdown against {enemy}!")
    time.sleep(2)
    choice = input("Are you ready to face your enemy? (yes / no): ")

    if choice.lower() == "yes":
        print("\nYou enter the battle with unwavering determination, summoning all your powers and skills.")
        time.sleep(2)
        print("In an epic clash, you face off against your enemy, unleashing your full potential.")
        time.sleep(2)
        victory(world)

    elif choice.lower() == "no":
        print("\nYou take a moment to gather your strength, knowing that the final battle awaits.")
        time.sleep(2)
        print("When you're ready, return and face your enemy with renewed determination.")
        time.sleep(2)
        final_battle(enemy, world)

    else:
        print("\nInvalid choice. Try again.")
        final_battle(enemy, world)

def victory(world):
    if world == "wizarding":
        print("\nWith a final surge of power, you emerge victorious, defeating Lord Voldemort.")
        time.sleep(2)
        print("The Wizarding World celebrates your triumph, and peace is restored.")
    elif world == "superheroes":
        print("\nWith a final surge of power, you emerge victorious, defeating the formidable enemy.")
        time.sleep(2)
        print("The city rejoices in your triumph, and your heroic deeds become the stuff of legends.")
    elif world == "mutants":
        print("\nWith a final surge of power, you emerge victorious, bringing peace and unity to mutantkind.")
        time.sleep(2)
        print("Mutants and humans learn to coexist, paving the way for a brighter future.")
    elif world == "middle-earth":
        print("\nWith a final surge of power, you emerge victorious, vanquishing the darkness.")
        time.sleep(2)
        print("The realms of Middle-earth are forever grateful for your bravery and heroism.")
    elif world == "dreams":
        print("\nWith a final surge of power, you emerge victorious, unlocking the secrets of the human mind.")
        time.sleep(2)
        print("The dreamscape is forever changed, and the power of inception lies in your hands.")
    elif world == "pirates":
        print("\nWith a final surge of power, you emerge victorious, claiming the treasures and defeating your foes.")
        time.sleep(2)
        print("The high seas of Pirates of the Caribbean will forever remember your daring escapades.")

    time.sleep(2)
    choice = input("Would you like to explore another world? (yes / no): ")

    if choice.lower() == "yes":
        choose_world()
    elif choice.lower() == "no":
        print("\nThank you for embarking on this grand adventure with us.")
        time.sleep(2)
        print("Your journey may end here, but your legend will live on in these worlds you been.")
    else:
        print("\nInvalid choice. Try again.")
        victory(world)

start_game()
