import random

hp = 50
npc_hp = 50
player_heal_potion = 3
enemy_heal_potion = 3

# Input action from player
def get_action():
    action = input("\nPress:" +
                    "\n(1) to attack" +
                    "\n(2) to block" +
                    "\n(3) to heal (+10 HP): 3 potions per level" +
                    "\nAction: ")
    print()
    return action

# Difficulty per level
def choose_npc_action(level): 
    if level == 1:
        return random.choice(['1', '2', '3'])
    elif level == 2:
        return random.choice(['1', '1', '1', '2', '2', '3', '3'])
    elif level == 3:  
        return random.choice(['1', '1', '1', '1', '2', '2', '2', '3', '3', '3'])

def start_game():
    print("Welcome to the Terminal Conquest RPG!" +
          "\nBy Aldrei Justin Santua" +
          "\nDeveloper: Here's max. 50 HP")

    while True:
        response = input("\nDo you accept (yes/no)? ").strip().lower()
        if response == "yes":
            print("\n+50 HP granted!")
            print("Great! Let's begin your adventure.")
            break
        elif response == "no":
            print("Maybe next time! See you, comrade.")
            exit()
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")
            
start_game()

class LevelOne:
    def start(self):
        global hp, npc_hp, player_heal_potion, enemy_heal_potion

        print("\nLevel 1: The Dark Forest")
        print("You find yourself in a dark forest. A wild goblin appears!")
        print("Your current damage ranges from 1 to 10. While the goblin's damage is between 1 to 5.")

        while hp > 0 and npc_hp > 0:

            action = get_action()
            npc_action = choose_npc_action(1)
            
            # Process player action
            if action == '1':
                damage = random.randint(1, 10)
                if npc_action == '2':
                    reduced_damage = max(1, int(damage * 0.6))
                    print(f"Player Action: You attack the goblin for {damage} damage!")
                    print(f"Enemy Action: The goblin blocks (-40% DMG)! Goblin HP: {npc_hp - reduced_damage}")
                    npc_hp -= reduced_damage
                else:
                    print(f"Player Action: You attack the goblin for {damage} damage! Goblin HP: {npc_hp - damage}")
                    npc_hp -= damage

            elif action == '2':
                if npc_action != '1':
                    print(f"Player Action: You are blocking!")

            elif action == '3':
                if player_heal_potion > 0:
                    if hp < 50:
                        heal = min(10, 50 - hp)
                        hp += heal
                        player_heal_potion -= 1
                        print(f"Player Action: You heal for {heal} HP! Your HP: {hp}. Potions left: {player_heal_potion}")
                    else:
                        print("Your HP is already full!")
                else:
                    print("No healing potions left!")

            # Process enemy action
            if npc_action == '1':
                damage = random.randint(1, 5)
                if action == '2':
                    reduced_damage = max(1, int(damage * 0.6))
                    print(f"Enemy Action: The goblin attacks you for {damage} damage!")
                    print(f"Player Action: You block (-40% DMG)! Your HP: {hp - reduced_damage}")
                    hp -= reduced_damage
                else:
                    print(f"Enemy Action: The goblin attacks you for {damage} damage! Your HP: {hp - damage}")
                    hp -= damage

            elif npc_action == '2':
                if action != '1':
                    print(f"Enemy Action: The goblin is blocking!")

            elif npc_action == '3':
                if enemy_heal_potion > 0:
                    if npc_hp < 50:
                        heal = min(10, 50 - npc_hp)
                        npc_hp += heal
                        enemy_heal_potion -= 1
                        print(f"Enemy Action: The goblin heals for {heal} HP! Goblin HP: {npc_hp}. Potions left: {enemy_heal_potion}")
                    else:
                        print("Enemy HP is already full!")
                else:
                    print("Enemy has no healing potions left!")

        if hp <= 0:
            print("\nDefeated! Game Over!")
            retry = input("Would you like to retry Level 1? (yes/no): ").strip().lower()
            if retry == "yes":
                hp = 50
                npc_hp = 50
                player_heal_potion = 3
                enemy_heal_potion = 3
                self.start()
            else:
                print("\nThanks for playing! See you next time.")
                exit()
        elif npc_hp <= 0:
            print("\nVictory! You defeated the goblin and shall now move on to next stage!")
            print("Congratulations on completing Level 1!")

class LevelTwo:
    def start(self, is_retry=False):
        global hp, npc_hp, player_heal_potion, enemy_heal_potion

        print(f"\nLevel 2: The Haunted Castle")
        print("You enter a haunted castle. A ghostly knight challenges you!")
        if not is_retry:
            print(f"You carry over {hp} HP from the previous level.")
            hp = min(hp + 10, 50)
            print(f"You feel refreshed and restore 10 HP! Your current HP: {hp}. Your potions are also refilled.")
        else:
            print(f"You retry the level with {hp} HP. Your potions are also refilled.")    
        print("Your current damage ranges from 5 to 15. The same goes with the knight.")
        print("Enemy's HP is now at 60.")

        npc_hp = 60
        player_heal_potion = 3
        enemy_heal_potion = 3

        while hp > 0 and npc_hp > 0:
            action = get_action()
            npc_action = choose_npc_action(2)

            # Process player action
            if action == '1':
                damage = random.randint(5, 15)
                if npc_action == '2':
                    reduced_damage = max(1, int(damage * 0.6))
                    print(f"Player Action: You attack the knight for {damage} damage!")
                    print(f"Enemy Action: The knight blocks (-40% DMG)! Knight HP: {npc_hp - reduced_damage}")
                    npc_hp -= reduced_damage
                else:
                    print(f"Player Action: You attack the knight for {damage} damage! Knight HP: {npc_hp - damage}")
                    npc_hp -= damage

            elif action == '2':
                if npc_action != '1':
                    print(f"Player Action: You are blocking!")

            elif action == '3':
                if player_heal_potion > 0:
                    if hp < 50:
                        heal = min(10, 50 - hp)
                        hp += heal
                        player_heal_potion -= 1
                        print(f"Player Action: You heal for {heal} HP! Your HP: {hp}. Potions left: {player_heal_potion}")
                    else:
                        print("Your HP is already full!")
                else:
                    print("No healing potions left!")

            # Process enemy action
            if npc_action == '1':
                damage = random.randint(5, 15)
                if action == '2':
                    reduced_damage = max(1, int(damage * 0.6))
                    print(f"Enemy Action: The knight attacks you for {damage} damage!")
                    print(f"Player Action: You block (-40% DMG)! Your HP: {hp - reduced_damage}")
                    hp -= reduced_damage
                else:
                    print(f"Enemy Action: The knight attacks you for {damage} damage! Your HP: {hp - damage}")
                    hp -= damage

            elif npc_action == '2':
                if action != '1':
                    print(f"Enemy Action: The knight is blocking!")

            elif npc_action == '3':
                if enemy_heal_potion > 0:
                    if npc_hp < 60:
                        heal = min(10, 60 - npc_hp)
                        npc_hp += heal
                        enemy_heal_potion -= 1
                        print(f"Enemy Action: The knight heals for {heal} HP! Knight HP: {npc_hp}. Potions left: {enemy_heal_potion}")
                    else:
                        print("Enemy HP is already full!")
                else:
                    print("Enemy has no healing potions left!")

        if hp <= 0:
            print("\nDefeated! Game Over!")
            retry = input("Would you like to retry Level 2? (yes/no): ").strip().lower()
            if retry == "yes":
                hp = 50
                npc_hp = 60
                player_heal_potion = 3
                enemy_heal_potion = 3
                self.start(is_retry=True)
            else:
                print("\nThanks for playing! See you next time.")
                exit()
        elif npc_hp <= 0:
            print("\nVictory! You defeated the ghostly knight!")
            print("Congratulations on completing Level 2! Moving on to the next stage...")

class LevelThree:
    def start(self, is_retry=False):
        global hp, npc_hp, player_heal_potion, enemy_heal_potion

        print(f"\nLevel 3: The Dragon's Lair")
        print("You enter the dragon's lair. A fierce dragon challenges you!")
        if not is_retry:
            print(f"You carry over {hp} HP from the previous level.")
            hp = min(hp + 10, 50)
            print(f"You feel refreshed and restore 10 HP! Your current HP: {hp}. Your potions are also refilled.")
        else:
            print(f"You retry the level with {hp} HP. Your potions are also refilled.")
        print("Your current damage ranges from 10 to 20. The dragon's damage is between 15 to 30.")
        print("Enemy's HP is now at 80.")

        npc_hp = 80
        player_heal_potion = 3
        enemy_heal_potion = 3

        while hp > 0 and npc_hp > 0:
            action = get_action()
            npc_action = choose_npc_action(3)

            # Process player action
            if action == '1':
                damage = random.randint(10, 20)
                if npc_action == '2':
                    reduced_damage = max(1, int(damage * 0.6))
                    print(f"Player Action: You attack the dragon for {damage} damage!")
                    print(f"Enemy Action: The dragon blocks (-40% DMG)! Dragon HP: {npc_hp - reduced_damage}")
                    npc_hp -= reduced_damage
                else:
                    print(f"Player Action: You attack the dragon for {damage} damage! Dragon HP: {npc_hp - damage}")
                    npc_hp -= damage

            elif action == '2':
                if npc_action != '1':
                    print(f"Player Action: You are blocking!")

            elif action == '3':
                if player_heal_potion > 0:
                    if hp < 50:
                        heal = min(10, 50 - hp)
                        hp += heal
                        player_heal_potion -= 1
                        print(f"Player Action: You heal for {heal} HP! Your HP: {hp}. Potions left: {player_heal_potion}")
                    else:
                        print("Your HP is already full!")
                else:
                    print("No healing potions left!")

            # Process enemy action
            if npc_action == '1':
                damage = random.randint(15, 30)
                if action == '2':
                    reduced_damage = max(1, int(damage * 0.6))
                    print(f"Enemy Action: The dragon attacks you for {damage} damage!")
                    print(f"Player Action: You block (-40% DMG)! Your HP: {hp - reduced_damage}")
                    hp -= reduced_damage
                else:
                    print(f"Enemy Action: The dragon attacks you for {damage} damage! Your HP: {hp - damage}")
                    hp -= damage

            elif npc_action == '2':
                if action != '1':
                    print(f"Enemy Action: The dragon is blocking!")

            elif npc_action == '3':
                if enemy_heal_potion > 0:
                    if npc_hp < 80:
                        heal = min(10, 80 - npc_hp)
                        npc_hp += heal
                        enemy_heal_potion -= 1
                        print(f"Enemy Action: The dragon heals for {heal} HP! Dragon HP: {npc_hp}. Potions left: {enemy_heal_potion}")
                    else:
                        print("Enemy HP is already full!")
                else:
                    print("Enemy has no healing potions left!")

        if hp <= 0:
            print("\nDefeated! Game Over!")
            retry = input("Would you like to retry Level 3? (yes/no): ").strip().lower()
            if retry == "yes":
                hp = 50
                npc_hp = 80
                player_heal_potion = 3
                enemy_heal_potion = 3
                self.start(is_retry=True)
            else:
                print("\nThanks for playing! See you next time.")
                exit()
        elif npc_hp <= 0:
            print("\nVictory! You defeated the fierce dragon and completed the game!")
            print("Congratulations! You've just earned the developer's respect!")

# Start the game
level1 = LevelOne()
level1.start()

if hp > 0:
    level2 = LevelTwo()
    level2.start()

if hp > 0:
    level3 = LevelThree()
    level3.start()