import pgzrun
import random

TITLE = "Quiz Master"
WIDTH = 900
HEIGHT = 650

# Layout
marquee_box = Rect((0, 0), (WIDTH, 60))
question_box = Rect((50, 80), (800, 120))
answer_boxes = [
    Rect((50, 220), (380, 100)),
    Rect((470, 220), (380, 100)),
    Rect((50, 340), (380, 100)),
    Rect((470, 340), (380, 100))
]
timer_box = Rect((720, 460), (150, 80))
skip_box = Rect((50, 460), (150, 80))

# Game variables
questions = []
current_question = []
question_index = 0
score = 0
time_left = 15
game_over_flag = False

# Marquee settings
marquee_text = "Welcome to Quiz Master!"
marquee_x = WIDTH

# Load questions from file
def load_questions(filename="Questions.txt"):
    global questions
    with open(filename, "r", encoding="latin1") as f:
        for line in f:
            parts = line.strip().split(",")
            print("Debug",parts)
            if len(parts) == 6:
                questions.append(parts)
    random.shuffle(questions)
    print("Total questions loaded:",len(questions))

# Get the next question
def next_question():
    global current_question, question_index, time_left, game_over_flag

    if question_index < len(questions):
        current_question = questions[question_index]
        question_index += 1
        time_left = 15
    else:
        game_over_flag = True

# Draw screen
def draw():
    screen.clear()
    screen.fill("black")

    # Marquee
    screen.draw.filled_rect(marquee_box, "darkblue")
    screen.draw.text(marquee_text, (marquee_x, 15), color="white", fontsize=30)

    if game_over_flag:
        msg = f"Game Over!\nYour Score: {score}/{len(questions)}"
        screen.draw.textbox(msg, Rect((150, 200), (600, 250)), color="white")
        return

    # Question box
    screen.draw.filled_rect(question_box, "navy")
    screen.draw.textbox(current_question[0], question_box, color="white")

    # Answer boxes
    for i, box in enumerate(answer_boxes):
        screen.draw.filled_rect(box, "darkorange")
        screen.draw.textbox(current_question[i + 1], box, color="black")

    # Timer
    screen.draw.filled_rect(timer_box, "purple")
    screen.draw.textbox(str(time_left), timer_box, color="white")

    # Skip button
    screen.draw.filled_rect(skip_box, "darkgreen")
    screen.draw.textbox("Skip", skip_box, color="white")

# Handle marquee movement
def update():
    global marquee_x
    marquee_x -= 2
    if marquee_x + 600 < 0:
        marquee_x = WIDTH
# Countdown timer
def update_timer():
    global time_left, game_over_flag
    if not game_over_flag:
        if time_left > 0:
            time_left -= 1
        else:
            next_question()

# Mouse click handler
def on_mouse_down(pos):
    global score
    if game_over_flag:
        return
    # Answer clicked?
    for i, box in enumerate(answer_boxes):
        if box.collidepoint(pos):
            if int(current_question[5]) == i + 1:
                score += 1
            next_question()
            return
    # Skip clicked?
    if skip_box.collidepoint(pos):
        next_question()

# Start game
load_questions()
next_question()
clock.schedule_interval(update_timer, 1)
pgzrun.go()
'''In order to run the code kindly use terminal and type the command pgzrun filename.py, make sure you are in the right directory.
Using run code button at top right of the VS code does not works as it is eligible to run only basic python script.
-> PygameZero (pgzrun) set up a special game loop(draw(), update(), events etc)
-> when we run the VS code "Run Code" button, Python tries to run the file as a normal script.
->pgzrun isn't starting the event loop propely, so things can break. In this case it was not calling the load_questions().
-> REason why "Run Code" fails to execute pgzrun files.
  pgzrun is not just a library- it is a runner that 
a) Initializes the Pygam Zero environment.
b) Wraps the game loop
c) Calls draw() and update() automatically.
  if we use python filename.py none of this happens and code breaks down.
However, to make the "Run Code" button work 
we can do this 
if __name__ = __main__:
  pgzrun.go()
  





'''

