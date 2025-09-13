import pgzrun
import random 

#game settings 
WIDTH=950
HEIGHT=600
CENTRE_X=WIDTH/2
CENTER_Y = HEIGHT/2
CENTER=(CENTRE_X, CENTER_Y)
FINAL_LEVEL=6
ITEMS=['bag','bottle','battery','chips']

#game state 
game_over = False
game_complete=False
current_level=1
items=[]
animations=[]
#draw function 
def draw():
    global items, current_level,game_over,game_complete
    screen.clear()
    screen.blit("background",(0,0))
    #check for game over 
    if game_over:
        display_message("Game Over, Try Again")
    elif game_complete:
        display_message("You Won!!Well Done")
def update():
    global items
    if len(items) ==0:
        items = make_items(current_level)
def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(new_items)
    layout_items(new_items)
    animate_items(new_items)
    return new_items
def create_items(items_to_create):
    new_items =[]
    for option in items_to_create:
        item=Actor(option)
        new_items.append(item)
    return new_items
def layout_items(items_to_layout):
    number_of_gaps=len(items_to_layout) +1
    gap_size= WIDTH / number_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        item.x=(index+1) * gap_size
        item.y=0
def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        animation=animate(item,duration=4,on_finished = handle_game_over, y= HEIGHT)
        animations.append(animation)
def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete()
            else:
                handle_game_over()
def handle_game_complete():
    global current_level, items, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level +=1
        items=[]
        animations =[]
def handle_game_over():
    global game_over, items, animations
    stop_animations(animations)
    game_over = True

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()











