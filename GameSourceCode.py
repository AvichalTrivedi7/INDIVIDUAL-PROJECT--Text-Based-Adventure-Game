import random
import os.path
import sys
import pickle

world_map = {
    "kingdom": {"north": "forest", "east": "armory", "west": "mountain","south": "ruins"},
    "mountain": {"east": "kingdom"},
    "armory": {"west": "kingdom"},
    "forest": {"south": "kingdom","north": "deepforest"},
    "deepforest": {"south":"forest"},
    "ruins": {"north": "kingdom","south": "castle"},
    "castle": {"north": "ruins"}
}

Equipments=[]
health=100
coins=0

file_exists=os.path.isfile("loadfile.dat")

def load():
    global coins, health, Equipments, name, location
    if file_exists:
        with open("loadfile.dat", "rb") as file:
            data = pickle.load(file)
        coins, health, Equipments, name = data
        print(f"Your data has been loaded {name}, coins={coins}, health={health}, Equipments={Equipments}.")
        location="kingdom"
        main_loop()
    else:
        location="kingdom"
        gamestartkingdom()

def save():
    global coins, health, Equipments, name
    s = [coins, health, Equipments, name]

    with open("loadfile.dat", "wb") as file:
        pickle.dump(s, file)
    print("Data Saved.")
   
def addtoEquipments(obj):
    global Equipments
    Equipments.append(obj)
    return Equipments
    
def printEquipments():
    global Equipments
    print("Following are your current Equipments:")
    for i in Equipments:
        print(i)
    
def gamestartkingdom():
    global health, name, coins
    print("Welcome, brave warrior! You have been chosen to embark on a perilous quest.\n")
    print("The world consists of 7 parts, Starting from KINGDOM, where your journey begins.")
    print("\n\nWORLD MAP----->\n")
    print("                DEEP FOREST")
    print("                     '")
    print("                     '")
    print("                     '")
    print("                   FOREST")
    print("                     '")
    print("                     '")
    print("                     '")
    print("MOUNTAINS- - - - -KINGDOM- - - - - ARMORY")
    print("                     '")
    print("                     '")
    print("                     '")
    print("                   RUINS")
    print("                     '")
    print("                     '")
    print("                     '")
    print("                  CASTLE")
    print("\n")
    print("You have four directions to go from the KINGDOM:\n")
    print("- Going north, you'll find the FOREST, and deeper north, the DEEP FOREST. But be careful, Haste might cause you harm.")
    print("- Going west you'll find the MOUNTAINS. Take actions meticulously.")
    print("- Going east you'll find the ARMORY. Here you find the equipments to gain strength.")
    print("- Going south you'll find the RUINS, and further south, is the CASTLE, Beware the deadly boss resides here.")
    print("You start with Hydro Sword, Hydro Armour")
    addtoEquipments("Hydro Sword")
    addtoEquipments("Hydro Armour")
    printEquipments()
    print(f"You start with {health} health.")
    print(f"You start with {coins} coins.")
    print("\nOnly the most powerful of warriors can reach the castle and defeat the fearsome boss.")
    print("Your journey begins now.")
    print("Gather coins from winning battles and finding easter eggs while roaming, purchase weapons and armour, and prepare for the battles ahead.")
    name=input("\nWhat is your name brave adventurer?\n")
    print(f"Very well, {name}, May luck be with you.\n")
    kingdom()

def kingdom():
    global health
    print("You are at the peaceful kingdom.")
    print("Kingdom is a checkpoint, You have 100 health.")
    health=100
    main_loop()
    
def mountain():
    print("You stand at the foot of a towering mountain, its peak shrouded in mist.")
    main_loop()
    
def forest():
    print("You find yourself in a dense, ancient forest, filled with the sounds of nature.")
    main_loop()
    
def deepforest():
    print("You venture into a dark, mysterious forest, where strange creatures lurk in the shadows.")
    main_loop()
    
def ruins():
    print("You explore the remnants of a long-lost civilization, overgrown with vines and moss.")
    main_loop()
    
def castle():
    print("You approach the ominous castle, its dark towers looming over the landscape. A sense of dread fills the air as you hear the distant echo of evil laughter.")
    main_loop()

def move(direction):
    global location
    new_location=world_map[location].get(direction)
    if new_location:
        location=new_location
        print(f"\nYou travel far towards the {direction} and eventually reach the {location}...\n.\n.\n.\n.")
        if location=="kingdom":
            kingdom()
        elif location=="mountain":
            mountain()
        elif location=="forest":
            forest()
        elif location=="deepforest":
            deepforest()
        elif location=="ruins":
            ruins()
        elif location=="castle":
            castle()
        elif location=="armory":
            armory()
    else:
        print("You can't go that way.")

def fight():
    global location
    if location=="kingdom":
        print("The kingdom is safe, there are no fights here. Move to other regions to battle.")
        
    elif location=="mountain":
        fight_choice=input("Who do you want to fight?\n1. Stone Golem.\n2. Frost Claw.\n3. To go back to roaming (1,2,3)")
        if fight_choice=="1":
            mountainStonegolem()
        elif fight_choice=="2":
            mountainFrostclaw()
        elif fight_choice=="3":
            roam()
        else:
            print("Please select one of the options.")
            fight()
            
    elif location=="forest":
        fight_choice=input("Who do you want to fight?\n1. Woodland Wraith.\n2. Forest Guardian.\n3. To go back to roaming (1,2,3)")
        if fight_choice=="1":
            forestWoodlandwraith()
        elif fight_choice=="2":
            forestForestguardian()
        elif fight_choice=="3":
            roam()
        else:
            print("Please select one of the options.")
            fight()
            
    elif location=="deepforest":
        fight_choice=input("Who do you want to fight?\n1. Thorned Beast.\n2. Fanged Demon.\n3. To go back to roaming (1,2,3)")
        if fight_choice=="1":
            deepforestThornedBeast()
        elif fight_choice=="2":
            deepforestFangedDemon()
        elif fight_choice=="3":
            roam()
        else:
            print("Please select one of the options.")
            fight()
            
    elif location=="ruins":
        fight_choice=input("Who do you want to fight?\n1. Necromancer.\n2. Revenant Knight.\n3. To go back to roaming (1,2,3)")
        if fight_choice=="1":
            ruinsNecromancer()
        elif fight_choice=="2":
            ruinsRevenantknight()
        elif fight_choice=="3":
            roam()
        else:
            print("Please select one of the options.")
            fight()
            
    elif location=="castle":
        fight_choice=input("Would you like to fight the boss? or would you like to go back to roaming? (1,2)\n")
        if fight_choice=="1":
            castleBoss()
        elif fight_choice=="2":
            roam()
        else:
            print("Please select one of the options.")
            fight()

def encounters():
    return random.choice(["You stumble upon a group of squirrels arguing about the best type of acorn. You try to mediate, but they just squabble louder.","A wise old owl hoots at you. It seems to be pondering the meaning of existence, or perhaps just hungry.","You encounter a particularly grumpy troll. He complains about the weather and the lack of good mud puddles.","You meet a curious child who asks you some questions. Their innocent wonder fills you with joy.","A kind old woman offers you a warm cup of tea and a comforting smile.","A playful puppy bounds up to you, wagging its tail and eager for a game of fetch.","You found a pretty flower that made your day.","A gentle breeze carries a sweet floral scent.","You find a lucky penny on the ground.","You notice a rainbow that arcs across the sky.","A bird sings a beautiful melody.","A squirrel playfully scampers up a tree.","You witness a breathtaking sunset.","You find a child laughing with pure joy.","You discover a hidden waterfall.","A friendly cat purrs contentedly looking at you.","A beautiful butterfly flutters by.","A starry night sky fills you with wonder.","A gentle breeze rustles through the leaves.","A peaceful moment of solitude to reflect and recharge."])
    
def roam():
    global coins
    way=input("\nWhere would you like to go? (forward, backward, left, right, exit_roaming): ")
    if way in ["forward", "backward", "left", "right"]:
        print(encounters())
        rng_reward=random.randint(1,11)
        if rng_reward==7:
            print("You have gained 5 coins!")
            coins+=5
        print("...........................................")
        roam()
    elif way=="exit_roaming":
        main_loop()
    else:
        print("Please refrain from going in any directions other than the provided ones.")
        roam()

def menu():
    global coins, Equipments, name
    menu_choice=input("Pick your choice: \n1.Save and Exit.\n2.View Equipments.\n3.Check Coins.\n4.View Powers and Abilities of your Equipments.\n5.Exit menu.\n")
    if menu_choice=="1":
        save()
        quit()
    elif menu_choice=="2":
        printEquipments()
    elif menu_choice=="3":
        print(f"You currently have {coins} coins.")
    elif menu_choice=="4":
        print(f"{name}'s Sword Attacks: ")
        print(f"Sword ---> {Equipments[0]}")
        displayAttacks()
        print(f"{name}'s Armour Abilities: ")
        print(f"Armour ---> {Equipments[1]}")
        displayAbilities(Equipments[1])
    elif menu_choice=="5":
        print("The menu is closed.\n")
        main_loop()
    else:
        print("Please select an option from the list provided.\n")
        menu()
    

def main_loop():
    while True:
        action = input("What do you want to do? (change_region, roam, fight, menu, quit): ")
        if action == "change_region":
            direction = input("Which direction? (north, south, east, west): ")
            move(direction)
        elif action == "roam":
            roam()
        elif action == "fight":
            fight()
        elif action=="menu":
            menu()
        elif action == "quit":
            quit()
        else:
            print("Invalid action.")


def slightdamageTaken():
    hurtslight=random.randint(1,3)
    return hurtslight
    
def damageTaken():
    global Equipments
    if Equipments[1]=="Hydro Armour":
        hurt=random.randint(4,6)
    elif Equipments[1]=="Pyro Armour":
        hurt=random.randint(2,4)
    elif Equipments[1]=="Shadow Armour":
        hurt=random.randint(1,2)
    return hurt


def damageGiven():
    global Equipments
    if Equipments[0]=="Hydro Sword":
        hurted=random.randint(6,16)
    elif Equipments[0]=="Pyro Sword":
        hurted=random.randint(16,22)
    elif Equipments[0]=="Shadow Sword":
        hurted=random.randint(22,27)
    rng=random.randint(1,7)
    if rng==5:
        return 0
    else:
        return hurted
    
def bossSkill():
    return random.choice(["Vicious slash","Crushing Blow","Dark Bolt","Soul Drain","Shadow Strike","Berserk Charge","Cleave","Dismantle"])

def mainAttacks(choice):
    global Equipments
    choices=["1","2","3","4"]
    if Equipments[0]=="Hydro Sword":
        atks=["Aqua Slash","Hydro Pulse","Water Prison","Hydro Wrath"]
    elif Equipments[0]=="Pyro Sword":
        atks=["Fire Blast","Inferno","Heat Wave","Incinerate"]
    elif Equipments[0]=="Shadow Sword":
        atks=["Corruption","Dark Pulse","Shadow Ball","Nightmare"]
    if choice in choices:
        return atks[int(choice)-1]
    else:
        return random.choice(atks)
        
def displayAttacks():
    for i in range(1,5):
        print(mainAttacks(str(i)))
    
def castleBoss():
    global health, Equipments, coins
    bossHealth=175
    print("Shadow Wraith has appeared….!")
    print("The Shadow Wraith, a malevolent entity born from the darkest depths of the spirit realm, looms before you. Its ethereal form, shrouded in perpetual shadow, exudes an aura of dread. Its piercing red eyes, devoid of empathy, promise a battle of epic proportions. As you draw your weapon, the Wraith lets out a chilling, otherworldly laugh, signaling the beginning of a relentless assault.\n")
    print("Tips: Try to atleast have a shadow sword and armour before battling the boss.")
    battle=input("Are you ready for a battle with him or would you run? (yes/no)\n")
    print("\n")
    print(f"Remember, Your {Equipments[0]} attacks are:")
    displayAttacks()
    print("\n")
    if battle=="yes":
        while health>1 and bossHealth>1:
            prevYou=health
            health-=damageTaken()+7
            print(f"~~Shadow Wraith has used his skill {bossSkill()}!")
            if health<1:
                gameover()
                break 
            print(f"Your Remaining health {prevYou}--->{health}\n")
            
            prevOpp=bossHealth
            attack=input("Your turn now, Choose your attack (1,2,3,4) or any key for random attack.\n")
            print(f"~~You have Striked using {mainAttacks(attack)},")
            bossHealth-=damageGiven()
            if bossHealth<1:
                print(f"You have emerged as victorious! Congratulations on finishing the game :)")
                print(f"You have gained 200 coins and regenerated back to 100 health")
                health=100
                coins+=500
                main_loop()
            if prevOpp==bossHealth:
                print("The enemy has dodged the Attack!")
            else:  
                print(f"Enemy's remaining health, {prevOpp}--->{bossHealth}")
            
            print("\n***************************************************************\n")
        
        
    else:
        health-=slightdamageTaken()
        print(f"You suffer a slight hit as you flee, you have {health} health left.")
        main_loop()

def quit():
    sys.exit()
    
def gameover():
    global coins, health, Equipments
    print("The light fades from your eyes as you slip into an eternal slumber...")
    print(f"The game has ended, {name}.")
    coins, health, Equipments=0,100,[]
    print("If you have previously saved data then you will automatically restart from that point.")
    restart=input("Would you like to restart? (yes/no)")
    if restart=="yes":
        load()
    else:
        quit()

def frostclawSkill():
    return random.choice(["Razor Tear","Icy Slash","Iceberg","Dash","Cold Punch","Blizzard","Frozen Breath","Avalanche"])


def mountainFrostclaw():
    global health, Equipments, coins
    monsHealth=120
    print("Frost Claw has appeared.....")
    print("He shouts, I'll tear you limb from limb!!\n")
    battle=input("Are you ready for a battle with him or would you run? (yes/no)\n")
    print("\n")
    print(f"Remember, Your {Equipments[0]} attacks are:")
    displayAttacks()
    print("\n")
    if battle=="yes":
        while health>1 and monsHealth>1:
            prevYou=health
            health-=damageTaken()+1
            print(f"~~Frost Claw has used his skill {frostclawSkill()}!")
            if health<1:
                gameover()
                break 
            print(f"Your Remaining health {prevYou}--->{health}\n")
            
            prevOpp=monsHealth
            attack=input("Your turn now, Choose your attack (1,2,3,4) or any key for random attack.\n")
            print(f"~~You have Striked using {mainAttacks(attack)},")
            monsHealth-=damageGiven()
            if monsHealth<1:
                print(f"You have emerged as victorious! Congratulations on winning the battle")
                print(f"You have gained 60 coins and regenerated back to 100 health")
                health=100
                coins+=60
                main_loop()
            if prevOpp==monsHealth:
                print("The enemy has dodged the Attack!")
            else:  
                print(f"Enemy's remaining health, {prevOpp}--->{monsHealth}")
            
            print("\n***************************************************************\n")
        
        
    else:
        health-=slightdamageTaken()
        print(f"You suffer a slight hit as you flee, you have {health} health left.")
        main_loop()

def stonegolemSkill():
    return random.choice(["Rock Slide","Ground Pound","Earthquake","Petrify","Boulder Toss","Rock Throw","Land Slide","Heavy Punch"])

def mountainStonegolem():
    global health, Equipments, coins
    monsHealth=110
    print("Stone Golem has appeared.....")
    print("He says, Your courage is admirable, but futile!\n")
    battle=input("Are you ready for a battle with him or would you run? (yes/no)\n")
    print("\n")
    print(f"Remember, Your {Equipments[0]} attacks are:")
    displayAttacks()
    print("\n")
    if battle=="yes":
        while health>1 and monsHealth>1:
            prevYou=health
            health-=damageTaken()+1
            print(f"~~Stone Golem has used his skill {stonegolemSkill()}!")
            if health<1:
                gameover()
                break 
            print(f"Your Remaining health {prevYou}--->{health}\n")
            
            prevOpp=monsHealth
            attack=input("Your turn now, Choose your attack (1,2,3,4) or any key for random attack.\n")
            print(f"~~You have Striked using {mainAttacks(attack)},")
            monsHealth-=damageGiven()
            if monsHealth<1:
                print(f"You have emerged as victorious! Congratulations on winning the battle")
                print(f"You have gained 50 coins and regenerated back to 100 health")
                health=100
                coins+=50
                main_loop()
            if prevOpp==monsHealth:
                print("The enemy has dodged the Attack!")
            else:  
                print(f"Enemy's remaining health, {prevOpp}--->{monsHealth}")
            
            print("\n***************************************************************\n")
        
        
    else:
        health-=slightdamageTaken()
        print(f"You suffer a slight hit as you flee, you have {health} health left.")
        main_loop()

def woodlandwraithSkill():
    return random.choice(["Nature's Claw","Woodland's Curse","Drain Life","Phantom Blades","Root Bind","Entangling Roots","Silent Step","Tentacle Doom"])

def forestWoodlandwraith():
    global health, Equipments, coins
    monsHealth=120
    print("Woodland Wraith has appeared.....")
    print("He roars, Feel the wrath of the nature!!\n")
    battle=input("Are you ready for a battle with him or would you run? (yes/no)\n")
    print("\n")
    print(f"Remember, Your {Equipments[0]} attacks are:")
    displayAttacks()
    print("\n")
    if battle=="yes":
        while health>1 and monsHealth>1:
            prevYou=health
            health-=damageTaken()+1
            print(f"~~Woodland Wraith has used his skill {woodlandwraithSkill()}!")
            if health<1:
                gameover()
                break 
            print(f"Your Remaining health {prevYou}--->{health}\n")
            
            prevOpp=monsHealth
            attack=input("Your turn now, Choose your attack (1,2,3,4) or any key for random attack.\n")
            print(f"~~You have Striked using {mainAttacks(attack)},")
            monsHealth-=damageGiven()
            if monsHealth<1:
                print(f"You have emerged as victorious! Congratulations on winning the battle")
                print(f"You have gained 60 coins and regenerated back to 100 health")
                health=100
                coins+=60
                main_loop()
            if prevOpp==monsHealth:
                print("The enemy has dodged the Attack!")
            else:  
                print(f"Enemy's remaining health, {prevOpp}--->{monsHealth}")
            
            print("\n***************************************************************\n")
        
        
    else:
        health-=slightdamageTaken()
        print(f"You suffer a slight hit as you flee, you have {health} health left.")
        main_loop()

def forestguardianSkill():
    return random.choice(["Forest's Fury","Vine Whip","Nature's Embrace","Earth Slam","Summon Spirits","Lunar Eclipse","Solar Flare","Wind Gust"])

def forestForestguardian():
    global health, Equipments, coins
    monsHealth=120
    print("Forest Guardian has appeared.....")
    print("He murmurs, You shall regret crossing these paths.\n")
    battle=input("Are you ready for a battle with him or would you run? (yes/no)\n")
    print("\n")
    print(f"Remember, Your {Equipments[0]} attacks are:")
    displayAttacks()
    print("\n")
    if battle=="yes":
        while health>1 and monsHealth>1:
            prevYou=health
            health-=damageTaken()+1
            print(f"~~Forest Guardian has used his skill {forestguardianSkill()}!")
            if health<1:
                gameover()
                break 
            print(f"Your Remaining health {prevYou}--->{health}\n")
            
            prevOpp=monsHealth
            attack=input("Your turn now, Choose your attack (1,2,3,4) or any key for random attack.\n")
            print(f"~~You have Striked using {mainAttacks(attack)},")
            monsHealth-=damageGiven()
            if monsHealth<1:
                print(f"You have emerged as victorious! Congratulations on winning the battle")
                print(f"You have gained 50 coins and regenerated back to 100 health")
                health=100
                coins+=50
                main_loop()
            if prevOpp==monsHealth:
                print("The enemy has dodged the Attack!")
            else:  
                print(f"Enemy's remaining health, {prevOpp}--->{monsHealth}")
            
            print("\n***************************************************************\n")
        
        
    else:
        health-=slightdamageTaken()
        print(f"You suffer a slight hit as you flee, you have {health} health left.")
        main_loop()

def thornedbeastSkill():
    return random.choice(["Ancient Roots","Poison Cloud","Root Grapple","Feral Charge","Thorned Swipe","Vine Lash","Extreme Whip","Phantom Image"])

def deepforestThornedBeast():
    global health, Equipments, coins
    monsHealth=150
    print("Thorned Beast has appeared.....")
    print("He exclaims, You dare trespass in my domain? Your blood shall nourish the roots of this ancient forest.\n")
    battle=input("Are you ready for a battle with him or would you run? (yes/no)\n")
    print("\n")
    print(f"Remember, Your {Equipments[0]} attacks are:")
    displayAttacks()
    print("\n")
    if battle=="yes":
        while health>1 and monsHealth>1:
            prevYou=health
            health-=damageTaken()+2
            print(f"~~Thorned Beast has used his skill {thornedbeastSkill()}!")
            if health<1:
                gameover()
                break 
            print(f"Your Remaining health {prevYou}--->{health}\n")
            
            prevOpp=monsHealth
            attack=input("Your turn now, Choose your attack (1,2,3,4) or any key for random attack.\n")
            print(f"~~You have Striked using {mainAttacks(attack)},")
            monsHealth-=damageGiven()
            if monsHealth<1:
                print(f"You have emerged as victorious! Congratulations on winning the battle")
                print(f"You have gained 70 coins and regenerated back to 100 health")
                health=100
                coins+=70
                main_loop()
            if prevOpp==monsHealth:
                print("The enemy has dodged the Attack!")
            else:  
                print(f"Enemy's remaining health, {prevOpp}--->{monsHealth}")
            
            print("\n***************************************************************\n")
        
        
    else:
        health-=slightdamageTaken()
        print(f"You suffer a slight hit as you flee, you have {health} health left.")
        main_loop()

def fangeddemonSkill():
    return random.choice(["Ferocious Bite","Claw Slash","Demonic Frenzy","HellFire","Fearsome Roar","Demonic Transformation","Shadow Nova","Corrupting Strike"])

def deepforestFangedDemon():
    global health, Equipments, coins
    monsHealth=150
    print("Fanged Demon has appeared.....")
    print("He utters, You have awakened a slumbering terror. Your blood will feed my hunger, mortal.\n")
    battle=input("Are you ready for a battle with him or would you run? (yes/no)\n")
    print("\n")
    print(f"Remember, Your {Equipments[0]} attacks are:")
    displayAttacks()
    print("\n")
    if battle=="yes":
        while health>1 and monsHealth>1:
            prevYou=health
            health-=damageTaken()+2
            print(f"~~Fanged Demon has used his skill {fangeddemonSkill()}!")
            if health<1:
                gameover()
                break 
            print(f"Your Remaining health {prevYou}--->{health}\n")
            
            prevOpp=monsHealth
            attack=input("Your turn now, Choose your attack (1,2,3,4) or any key for random attack.\n")
            print(f"~~You have Striked using {mainAttacks(attack)},")
            monsHealth-=damageGiven()
            if monsHealth<1:
                print(f"You have emerged as victorious! Congratulations on winning the battle")
                print(f"You have gained 70 coins and regenerated back to 100 health")
                health=100
                coins+=70
                main_loop()
            if prevOpp==monsHealth:
                print("The enemy has dodged the Attack!")
            else:  
                print(f"Enemy's remaining health, {prevOpp}--->{monsHealth}")
            
            print("\n***************************************************************\n")
        
        
    else:
        health-=slightdamageTaken()
        print(f"You suffer a slight hit as you flee, you have {health} health left.")
        main_loop()

def necromancerSkill():
    return random.choice(["Bone Spear","Dark Aura","Soul Siphon","Death Grip","Curse of Weakness","Black Touch","Death Ward","Blight"])

def ruinsNecromancer():
    global health, Equipments, coins
    monsHealth=140
    print("Necromancer has appeared.....")
    print("He whispers, Eternal darkness awaits you. I will purge this realm of your impurity.\n")
    battle=input("Are you ready for a battle with him or would you run? (yes/no)\n")
    print("\n")
    print(f"Remember, Your {Equipments[0]} attacks are:")
    displayAttacks()
    print("\n")
    if battle=="yes":
        while health>1 and monsHealth>1:
            prevYou=health
            health-=damageTaken()+1
            print(f"~~Necromancer has used his skill {necromancerSkill()}!")
            if health<1:
                gameover()
                break 
            print(f"Your Remaining health {prevYou}--->{health}\n")
            
            prevOpp=monsHealth
            attack=input("Your turn now, Choose your attack (1,2,3,4) or any key for random attack.\n")
            print(f"~~You have Striked using {mainAttacks(attack)},")
            monsHealth-=damageGiven()
            if monsHealth<1:
                print(f"You have emerged as victorious! Congratulations on winning the battle")
                print(f"You have gained 60 coins and regenerated back to 100 health")
                health=100
                coins+=60
                main_loop()
            if prevOpp==monsHealth:
                print("The enemy has dodged the Attack!")
            else:  
                print(f"Enemy's remaining health, {prevOpp}--->{monsHealth}")
            
            print("\n***************************************************************\n")
        
        
    else:
        health-=slightdamageTaken()
        print(f"You suffer a slight hit as you flee, you have {health} health left.")
        main_loop()

def revenantknightSkill():
    return random.choice(["Summon Undead","Apocalypse","Dystopian Domain","Soul Steal","Spectral Slash","Eternal Curse","Undying Rage","Black Hole"])

def ruinsRevenantknight():
    global health, Equipments, coins
    monsHealth=150
    print("Revenant Knight has appeared.....")
    print("He rumbled, My spirit is eternally tethered to these crumbling ruins, now you shall be one among my army of the undead...\n")
    battle=input("Are you ready for a battle with him or would you run? (yes/no)\n")
    print("\n")
    print(f"Remember, Your {Equipments[0]} attacks are:")
    displayAttacks()
    print("\n")
    if battle=="yes":
        while health>1 and monsHealth>1:
            prevYou=health
            health-=damageTaken()+2
            print(f"~~Revenant Knight has used his skill {revenantknightSkill()}!")
            if health<1:
                gameover()
                break 
            print(f"Your Remaining health {prevYou}--->{health}\n")
            
            prevOpp=monsHealth
            attack=input("Your turn now, Choose your attack (1,2,3,4) or any key for random attack.\n")
            print(f"~~You have Striked using {mainAttacks(attack)},")
            monsHealth-=damageGiven()
            if monsHealth<1:
                print(f"You have emerged as victorious! Congratulations on winning the battle")
                print(f"You have gained 80 coins and regenerated back to 100 health")
                health=100
                coins+=80
                main_loop()
            if prevOpp==monsHealth:
                print("The enemy has dodged the Attack!")
            else:  
                print(f"Enemy's remaining health, {prevOpp}--->{monsHealth}")
            
            print("\n***************************************************************\n")
        
        
    else:
        health-=slightdamageTaken()
        print(f"You suffer a slight hit as you flee, you have {health} health left.")
        main_loop()

def leaveorstay():
    global location
    los=input("Would you like to purchase more or exit the armory? (stay/exit)")
    if los=="stay":
        switch_armory()
    elif los=="exit":
        location="kingdom"
        kingdom()
    else:
        print("Invalid choice, please try again")
        leaveorstay()

def displayAbilities(arg):
    if arg=="Hydro Armour":
        print("Hydro Armour is the Initial armour, reduces damage decently.")
    if arg=="Pyro Armour":
        print("Pyro Armour reduces damage by 33%")
    if arg=="Shadow Armour":
        print("Shadow Armour reduces damage by 66%")

def switch_armory():
    global choose,coins,Equipments,store,location
    print("Choose\n1 to see available Weapons\n2 to see available Armour\n3 to exit the Armory\n")
    choose=input("Enter your choice:\n")
    if choose=="1":
        print(store.get("Sword"))
        purchase=input("What would you like to purchase? (P for Pyro, S for Shadow)\n")
        if purchase=="P" or purchase=="p":
            if coins>=250:
                coins-=250
                Equipments[0]="Pyro Sword"
                print("--You have successfully purchased Pyro Sword--")
                print(f"Your remaining coins are {coins}.")
                print(f"\nRemember, Your {Equipments[0]} attacks are:")
                displayAttacks()
            else:
                print("You don't have enough coins")
        elif purchase=="S" or purchase=="s":
            if coins>=1000:
                coins-=1000
                Equipments[0]="Shadow Sword"
                print("--You have successfully purchased Shadow Sword--")
                print(f"Your remaining coins are {coins}.")
                print(f"\nRemember, Your {Equipments[0]} attacks are:")
                displayAttacks()
            else:
                print("You don't have enough coins")
        else:
            print("Invalid choice, try again")
            switch_armory()
    elif choose=="2":
        print(store.get("Armour"))
        purchase=input("What would you like to purchase? (P for Pyro, S for Shadow)\n")
        if purchase=="P" or purchase=="p":
            if coins>=250:
                coins-=250
                Equipments[1]="Pyro Armour"
                print("--You have successfully purchased Pyro Armour--")
                print(f"Your remaining coins are {coins}.")
                print(f"\nRemember, Your {Equipments[1]} ability is:")
                displayAbilities("Pyro Armour")
            else:
                print("You don't have enough coins")
        elif purchase=="S" or purchase=="s":
            if coins>=1000:
                coins-=1000
                Equipments[1]="Shadow Armour"
                print("--You have successfully purchased Shadow Armour--")
                print(f"Your remaining coins are {coins}.")
                print(f"\nRemember, Your {Equipments[1]} ability is:")
                displayAbilities("Shadow Armour")
            else:
                print("You don't have enough coins")
        else:
            print("Invalid choice, try again")
            switch_armory()
    elif choose=="3":
        print("You have left the armory, and are returning back to the kingdom......\n")
        location="kingdom"
        kingdom()
    else:
        print("Invalid choice")
        switch_armory()
    leaveorstay()
            
def armory():
    global Equipments, coins, store
    store={"Armour":["Pyro Armour (250 coins)","Shadow Armour (1000 coins)"],"Sword":["Pyro Sword (250 coins)","Shadow Sword (1000 coins)"]}
    print("Welcome to the armory!")
    switch_armory()

load()









