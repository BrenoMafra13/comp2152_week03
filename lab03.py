import random
# Dice options using list() and range()
diceOptions = list(range(1, 7))

# Weapons Array
weapons = ["Fist","Knife","Club","Gun","Bomb","Nuclear bomb"]

# Displa available weapons
print("Available weapons: ", ', '.join(weapons))

def get_combat_strength(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <=value <= 6:
                return value
            else:
                print("Please enter a number between 1 and 6")
        except ValueError:
            print("Please enter a number between 1 and 6")

combatStrenght = get_combat_strength("Enter your combat strength (1-6): ")
mCombatStrenght = get_combat_strength("Enter monster combat strength( 1-6): ")

for j in range (1,21,2):
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    heroWeapon = weapons[heroRoll-1]
    monsterWeapon = weapons[monsterRoll-1]

    heroTotal = heroRoll + combatStrenght
    monsterTotal = monsterRoll + mCombatStrenght

    print(f"Round {j}:")
    print(f"Hero rolled a {heroRoll} and used {heroWeapon}")
    print(f"Monster rolled a {monsterRoll} and used {monsterWeapon}")

    if heroTotal > monsterTotal:
        print("Hero wins!")
    elif heroTotal < monsterTotal:
        print("Monster wins!")
    else:
        print("It's a tie!")

if j != 11:
    print("Battle concluded after 20 rounds!")