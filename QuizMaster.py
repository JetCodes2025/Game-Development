import pgzrun
import random 
TITLE = "Quiz Master"
WIDTH = 870
HEIGHT = 650

# Define rectangles for UI elements
marquee_box = Rect((0, 0), (880, 80))
question_box = Rect((20, 100), (650, 150))
timer_box = Rect((700, 100), (150, 150))
answer_boxes=[ Rect((50, 300), (300, 100)),
         Rect((520, 300), (300, 100)),
         Rect((50, 420), (300, 100)),
         Rect((520, 420), (300, 100)) ]
skip_box = Rect((700, 280), (150, 150))
# Game variables
questions=[]
current_question=[]
score = 0
time_left = 25
marquee_message = ""
is_game_over = False
question = []
questions = []
question_count = 0
question_index = 0
marquee_x=WIDTH
#loading the questions 
def load_questions(filename="Questions.txt"):
    global questions
    with open(filename,"r") as file:
        for line in file:
            parts=line.strip().split(",")
            if len(parts)==6:
                questions.append(parts)
    random.shuffle(questions)
#Get the next question
def next_question():
    global current_question, question_index,time_left,is_game_over
    if question_index<len(questions):
        current_question = questions[question_index]
        question_index += 1
        time_left = 15
    else:
        is_game_over = True

#Draw screen 
def draw():
    screen.clear()
    screen.fill("black")
    #Marquee Box
    screen.draw.filled_rect(marquee_box,"darkblue")
    screen.draw.text(marquee_message,(marquee_x,15),color="white",fontsize=30)
    #question Box 
    screen.draw.filled_rect(question_box,"navy")
    screen.draw.textbox(current_question[0],question_box,color="white",fontsize=30)
    #Answer Boxes 
    for i, box in enumerate(answer_boxes):
        screen.draw.filled_rect(box,"darkorange")
        screen.draw.textbox(current_question[i+1], box, color="black")
    #timer box 
    screen.draw.filled_rect(timer_box,"purple")
    screen.draw.textbox(str(time_left),timer_box, color="white")
    # skip button 
    screen.draw.filled_rect(skip_box,"darkgreen")
    screen.draw.textbox("Skip",skip_box, color="white")
#update 
def update():
    global marquee_x
    marquee_x -=2
    if marquee_x +600 <0:
        marquee_x = WIDTH
# Countdown timer 
def update_timer():
    global time_left, is_game_over
    if not is_game_over:
        if time_left > 0:
            time_left -=1
        else:
            next_question()
# mouse handler 
def on_mouse_down(pos):
    global score
    if is_game_over:
        return
    # 
    for i, box in enumerate(answer_boxes):
        if box.collidepoint(pos):
            if current_question[5] == i+1:
                score +=1
            next_question()
            return
    #skip clicked 
    if skip_box.collidepoint(pos):
        next_question()
#start the game 
load_questions()
next_question()
clock.schedule.interval(update_timer,1)
pgzrun.go()
