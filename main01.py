#question :list[type[str,list[str],str]]
questions = [
    ("what's the best CMS?", ["A) Wordpress" , "B) Joomla" , "C) Drupal" , "D) Headless" ] , "A"),
    ("what's the best programming language?", ["A) Python" , "B) JavaScript" , "C)Java" , "D) c++"] , "A"),
    ("what's the best dataabase?", ["A) MySQL" , "B) PostgreSQL" , "C) MongoDB" , "D) SQLite" ] , "B")
]
score=0
BONUS=10
PENALTY=3
user_answer=0
for question,options,correct_answer in questions :
    print(question)
    for option in options:
        print(option)
#تو  for باشه
    user_answer : str = input("Your choice:").strip().upper()
    if user_answer == correct_answer:
        print("Correct!")
        score+=BONUS
        user_answer+=1
    else:
        print("In correct!")
        score-=PENALTY
print(f"Your final score is :{score}")
print(f"You answered {user_answer} questions correctly . ")
print(f"Percentage : {user_answer / len(questions) * 100 }")