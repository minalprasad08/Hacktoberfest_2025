# positive_vibes_generator.py
# Hacktoberfest 2025 – Beginner-friendly project 

import random
import datetime

def get_greeting():
    now = datetime.datetime.now().hour
    if now < 12:
        return "Good morning"
    elif now < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def main():
    user = input("Enter your name: ").strip() or "Friend"
    greeting = get_greeting()
    quotes = {
        "motivation": [
            "You are doing great! Keep going 💪",
            "Believe in yourself — you are stronger than you think 🌟"
        ],
        "gratitude": [
            "Take a moment to appreciate how far you’ve come 🌈",
            "Small steps every day lead to big changes ✨"
        ],
        "fun": [
            "Smile! Your brain loves happy what you’re doing 😊",
            "Life’s short — make laughing your daily habit 😄"
        ]
    }

    print("\n---------------------------------------------")
    print(f"{greeting}, {user}! 🌸")
    print("🌼 Welcome to the Positive Vibes Generator 🌼")
    category = random.choice(list(quotes.keys()))
    print(f"Category: {category.capitalize()}")
    print(f"✨ {random.choice(quotes[category])} ✨")
    now_str = datetime.datetime.now().strftime("%A, %d %B %Y %H:%M:%S")
    print(f"\nGenerated on: {now_str}")
    print("---------------------------------------------\n")

if __name__ == "__main__":
    main()
