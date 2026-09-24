import random
import time

def print_slow(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_game():
    print_slow("=" * 50)
    print_slow("         WELCOME TO BUNKER 'SHELTER-101'        ")
    print_slow("=" * 50)
    print_slow("The world outside is destroyed. Your goal is to survive 20 days.")
    print_slow("Manage your resources, make tough choices, and scavenge the surface.\n")

    day = 1
    health = 100
    food = 5
    water = 5
    scrap = 0  
    has_weapon = False
    filter_status = 100 

    while day <= 20 and health > 0:
        print("\n" + "-"*40)
        print(f" DAY: {day}/20 | Health: {health}% | Air Filter: {filter_status}%")
        print(f" Resources — Food: {food} | Water: {water} | Scrap: {scrap}")
        print(f" Weapon: {'Yes (Shotgun)' if has_weapon else 'No'}")
        print("-"*40)

        if filter_status <= 0:
            print_slow("❌ The air filter completely clogged with toxic dust! You suffocated.")
            health = 0
            break

        print("What will you do today?")
        print("1. Eat and drink (-1 Food, -1 Water, +20 Health)")
        print("2. Scavenge the surface for supplies (Dangerous!)")
        print("3. Repair the air filter (-3 Scrap, +40% Filter)")
        print("4. Craft a shotgun (-5 Scrap)")
        print("5. Conserve energy (Do nothing, -10 Health from hunger)")
        
        choice = input("Your choice (1-5): ").strip()

        if choice == "1":
            if food > 0 and water > 0:
                food -= 1
                water -= 1
                health = min(100, health + 20)
                print_slow("🥗 You had a decent meal and quenched your thirst. Health recovered.")
            else:
                print_slow("⚠️ Not enough food or water! You went to bed starving.")
                health -= 15
        
        elif choice == "2":
            print_slow("🦺 You put on your hazmat suit and open the blast doors...")
            time.sleep(1)
            
            event = random.choice(["loot", "danger", "empty", "trader"])
            
            if event == "loot":
                found_food = random.randint(1, 3)
                found_water = random.randint(1, 3)
                found_scrap = random.randint(2, 5)
                food += found_food
                water += found_water
                scrap += found_scrap
                print_slow(f"🎉 Success! You found an abandoned grocery shop. Received: Food +{found_food}, Water +{found_water}, Scrap +{found_scrap}")
            
            elif event == "danger":
                print_slow("☣️ You got ambushed by mutant scavengers!")
                if has_weapon:
                    print_slow("🔫 You blasted them away with your shotgun! They fled, but you took minor damage.")
                    health -= 15
                    scrap += random.randint(1, 3)
                else:
                    print_slow("🩸 Defenseless, you had to run away and drop some gear. You were severely injured.")
                    health -= 40
                    food = max(0, food - 1)
            
            elif event == "trader":
                print_slow("🤝 You met a wandering trader.")
                if scrap >= 3:
                    trade = input("He offers 2 Food and 2 Water for 3 Scrap. Accept? (yes/no): ").lower().strip()
                    if trade in ["yes", "y"]:
                        scrap -= 3
                        food += 2
                        water += 2
                        print_slow("✅ The deal is done!")
                    else:
                        print_slow("You parted ways peacefully.")
                else:
                    print_slow("You have nothing valuable to trade. The merchant left.")
            
            else:
                print_slow("💨 Empty. You searched for hours but found nothing but radioactive ash.")
                health -= 5

        elif choice == "3":
            if scrap >= 3:
                scrap -= 3
                filter_status = min(100, filter_status + 40)
                print_slow("🔧 You successfully replaced the charcoal plates in the filter.")
            else:
                print_slow("⚠️ Not enough scrap! You need at least 3 units.")
                continue 

        elif choice == "4":
            if has_weapon:
                print_slow("You already have a weapon!")
                continue
            if scrap >= 5:
                scrap -= 5
                has_weapon = True
                print_slow("🛠️ Using pipes and scrap metal, you crafted a homemade shotgun!")
            else:
                print_slow("⚠️ Not enough scrap to craft a weapon (5 units required).")
                continue

        elif choice == "5":
            print_slow("💤 You spent the whole day resting on your bunk. Your stomach grumbles.")
            health -= 10

        else:
            print_slow("🤔 You hesitated and ended up wasting the entire day.")
            health -= 5

        filter_status -= random.randint(8, 15)
        day += 1
        time.sleep(0.5)

    print("\n" + "="*50)
    if health > 0:
        print_slow("🎉 CONGRATULATIONS! You survived all 20 days! 🎉")
        print_slow("A government rescue squad arrived at your coordinates. You are saved!")
    else:
        print_slow("💀 GAME OVER. You perished inside the depths of the bunker...")
    print("="*50)

if __name__ == "__main__":
    start_game()
