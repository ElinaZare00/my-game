# بازی آزمون چهارگزینه‌ای
# منو: شروع بازی یا خروج
# با انتخاب «شروع دوباره»، بازی و امتیازها از ابتدا شروع می‌شوند.

BONUS = 10
PENALTY = 3

questions = [
    (
        "What's the best CMS?",
        ["A: WordPress", "B: Joomla", "C: Drupal", "D: Headless"],
        "A",
    ),
    (
        "What's the best programming language?",
        ["A: Python", "B: JavaScript", "C: Java", "D: C++"],
        "A",
    ),
    (
        "What's the best database?",
        ["A: MySQL", "B: PostgreSQL", "C: MongoDB", "D: SQLite"],
        "B",
    ),
]


def play_game():
    # هر بار اجرای تابع، امتیازها از صفر شروع می‌شوند.
    score = 0
    user_corrects = 0

    print("\n--- Game started ---")

    for question, options, correct_answer in questions:
        print(f"\n{question}")
        for option in options:
            print(option)

        user_answer = input("Your choice (A/B/C/D): ").strip().upper()

        if user_answer == correct_answer:
            print("Correct!")
            score += BONUS
            user_corrects += 1
        else:
            print(f"Incorrect! The correct answer is {correct_answer}.")
            score -= PENALTY

    percentage = user_corrects / len(questions) * 100
    print("\n--- Game results ---")
    print(f"Your final score is: {score}")
    print(f"You answered {user_corrects} questions correctly.")
    print(f"Percentage: {percentage:.1f}%")


def main():
    while True:
        print("\n====== MAIN MENU ======")
        print("1. Start / Restart game")
        print("2. Exit")

        choice = input("Choose an option (1/2): ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
