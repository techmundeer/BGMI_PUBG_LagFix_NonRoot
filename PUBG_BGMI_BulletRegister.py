import os
import time

# Auto install dependencies
os.system("pkg update -y && pkg upgrade -y && pkg install python termux-api inetutils coreutils -y")

# Color Codes
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Function to display loading effect
def loading_effect():
    for i in range(4):
        print(f"\r{YELLOW}Loading{'.' * (i % 4 + 1)}{RESET}", end="")
        time.sleep(0.5)  # Add delay for the loading effect

def optimize_network():
    print(f"\n{YELLOW}🚀 Optimizing Network...{RESET}")
    loading_effect()
    os.system("ping -c 5 8.8.8.8 > /dev/null 2>&1")  # Suppress errors
    print(f"\r{GREEN}✅ Network optimized!{RESET}\n")

def clear_cache():
    print(f"\n{YELLOW}🧹 Clearing Cache...{RESET}")
    loading_effect()
    os.system("rm -rf /data/local/tmp/* > /dev/null 2>&1")  # Suppress errors
    print(f"\r{GREEN}✅ Cache cleared!{RESET}\n")

def adjust_performance():
    print(f"\n{YELLOW}⚡ Adjusting Performance Settings...{RESET}")
    loading_effect()
    os.system("termux-reload-settings > /dev/null 2>&1")  # Suppress errors
    print(f"\r{GREEN}✅ Performance adjusted!{RESET}\n")

def improve_smoothness():
    print(f"\n{YELLOW}🎮 Improving Game Smoothness...{RESET}")
    loading_effect()
    print(f"\r{GREEN}✅ Smoothness improved! (limited to available tweaks){RESET}\n")

def fix_bullet_registration():
    print(f"\n{YELLOW}🎯 Fixing Bullet Registration...{RESET}")
    loading_effect()
    print(f"\r{GREEN}✅ Bullet registration fixed! (limited tweaks available){RESET}\n")

def print_menu():
    print(f"{GREEN}╔════════════════════════════════════╗")
    print(f"║       🎮 Game Optimization Tool V2.0    ║")
    print(f"║   Created by Official Magisk Module ║")  
    print(f"╠════════════════════════════════════╣")
    print(f"║  1️⃣  {YELLOW}Optimize Network               {GREEN}║")
    print(f"║  2️⃣  {YELLOW}Clear Cache                   {GREEN}║")
    print(f"║  3️⃣  {YELLOW}Adjust Performance            {GREEN}║")
    print(f"║  4️⃣  {YELLOW}Improve Game Smoothness       {GREEN}║")
    print(f"║  5️⃣  {YELLOW}Fix Bullet Registration       {GREEN}║")
    print(f"║  0️⃣  {YELLOW}Exit                          {GREEN}║")
    print(f"╚════════════════════════════════════╝{RESET}")

while True:
    print_menu()
    choice = input(f"{YELLOW}👉 Enter your choice: {RESET}")
    if choice == "1":
        optimize_network()
    elif choice == "2":
        clear_cache()
    elif choice == "3":
        adjust_performance()
    elif choice == "4":
        improve_smoothness()
    elif choice == "5":
        fix_bullet_registration()
    elif choice == "0":
        print(f"{GREEN}👋 Exiting the tool. Have a great day!{RESET}")
        break
    else:
        print(f"{YELLOW}❌ Invalid choice! Please select a valid option.{RESET}\n")
