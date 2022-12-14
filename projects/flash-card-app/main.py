from    tkinter  import  *
from    tkinter  import  messagebox
from    random   import  choice
import  pandas

BACKGROUND_COLOR = "#B1DDC6"
FLIP_TIME = 5000

current_card = {}
to_learn = {}

# ---------------------------- FLASH CARD SETUP ------------------------------- #
try:
    data = pandas.read_csv("projects/flash-card-app/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("projects/flash-card-app/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    current_card = choice(to_learn)
    
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    
    flip_timer = window.after(FLIP_TIME, func=flip_card)
    

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    
      
def is_know():
    to_learn.remove(current_card)
    
    data = pandas.DataFrame(to_learn)
    data.to_csv("projects/flash-card-app/data/words_to_learn.csv", index=False)
    
    next_card()
    
    
# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Flash-Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(FLIP_TIME, func=flip_card)

# Card Setup
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="projects/flash-card-app/images/card_front.png")
card_back_img = PhotoImage(file="projects/flash-card-app/images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)

# Canvas Text
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="projects/flash-card-app/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_know)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="projects/flash-card-app/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)


next_card()

window.mainloop( )
