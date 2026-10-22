#question :list[type[str,list[str],str]]
from rich.console import Console
console = Console()

questions = [
    ("what's the best CMS?", ["A) Wordpress" , "B) Joomla" , "C) Drupal" , "D) Headless" ] , "A"),
    ("what's the best programming language?", ["A) Python" , "B) JavaScript" , "C)Java" , "D) c++"] , "A"),
    ("what's the best dataabase?", ["A) MySQL" , "B) PostgreSQL" , "C) MongoDB" , "D) SQLite" ] , "B")
]
#score=0
#BONUS=10
#PENALTY=3
#user_answer=0
#while True: # تغببر
def show_menu():
    user_imput: str = input ("do you want to start the quiz?(yes/no):").strip().lower()
    if user_imput=="yes":
        return True
    elif user_imput=="no":
        console.print("exiting the quiz . goodbye! " , style="Red on White")
        exit()
    else:
        console.print("invalid input . please enter 'yes' or 'no'." , style="Red on White")

def play_quiz():
    score=0
    #user_answer=0
    user_corrects=0
    BONUS=10
    PENALTY=3
    for question,options,correct_answer in questions :
        console.print(question ,style="Yellow on Black")
        for option in options:
            console.print(option , style="White on Black")
#تو  for باشه
    user_answer : str = input("Your choice:").strip().upper()
    if user_answer == correct_answer:
        console.print("Correct!" , style="Green on Black")
        score+=BONUS
        user_corrects+=1
    else:
        console.print("In correct!", style="Red on Blue")
        score-=PENALTY
    return score,user_answer 
def show_results(score , user_answer) :
    print(f"Your final score is :{score}")
    print(f"You answered {user_answer} questions correctly . ")
    print(f"Percentage : {user_answer / len(questions) * 100 }")
while True:
    if show_menu():
        break

score : int,user_answer: int=play_quiz()
show_results(score,user_answer)
