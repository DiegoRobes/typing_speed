from tkinter import *
import random

# ------LISTS OF WORDS--------
words = "start side know mother took so open far list would always want at and about while family man try over mean " \
        "live show school must earth made song between later your name two try I get any after much saw look get them "\
        "all his home put might too city home any start can we his white every should learn does between big great " \
        "oil another enough feet idea example always those might oil go fire way got state no show your fire oil all " \
        "back saw below four cut one war any begin black talk fire world go little some her sea without home its " \
        "world hand move came got much put three as mile around word set word part need here look which once carry" \
        "must well two group state grow letter face could hard too I list her call book do may always number " \
        "were next us upon an by may after car feet men say little next her really both well there air show high " \
        "land come old then read then write work took without open a our under open often girl never water with most" \
        "sound spell sometimes write more about see this she into thing every carry until best above girl again head " \
        "story face mean every country can set eye him mother find for did such study work boy later your say there" \
        "thing another them food change different start under go are grow life change answer under two kind your for " \
        "only thing through mean know before eat found come being another car said school at have way family hear" \
        "here later them set children took near any were near use light if read below never help list idea she " \
        "home them family long learn said school air car until change away do live begin head high into on mile " \
        "again go live one all open have house side red high something what us set carry from who along will any " \
        "they had made those then did day more plant only just another people she above time had point not write one" \
        "spell away most mean down always sea below this"

og_list = list(words.split(" "))
working_list = list(words.split(" "))
random.shuffle(working_list)
typed_words = []


# ------new word funct------
def pop_word(event):
    new_word = working_list.pop()
    typed_words.append(typing.get().strip(" "))
    typing.delete(0, "end")
    word.config(text=new_word)


# ------clock------
def start_clock():
    countdown(60)


def countdown(secs):
    seconds = secs % 60
    if seconds < 10:
        seconds = "0" + str(seconds)
    if secs > -1:
        clock.config(text=f"{seconds}")
        window.after(1000, countdown, secs - 1)
    else:
        results()


# ------results--------
def results():
    clock.destroy()
    typing.destroy()
    start.destroy()
    word.destroy()
    correct_words = 0
    for i in typed_words:
        if i in og_list:
            correct_words += 1
    answer = Label(text=f"Your typing speed is {correct_words} WPM", font=("Arial", 10, "bold"))
    answer.pack(pady=(75, 25))


# ------GUI--------
window = Tk()
window.title("Typing Speed")
window.minsize(width=420, height=200)
window.config(padx=10, pady=5)

# title--------
title = Label(text="Speed Test", font=("Arial", 10, "bold"))
title.pack()

# word--------
font_2 = ("Arial", 60, "bold")
word = Label(text="!", font=font_2)
word.pack(pady=(0, 15))

# clock--------
clock = Label(text="", font=("Arial", 10, "bold"))
clock.pack(pady=(0, 25))

# entry--------
typing = Entry(width=30)
typing.pack(pady=(0, 10))

# button--------
start = Button(text="Start", command=start_clock)
start.pack(pady=(0, 10))

# run--------
typing.bind("<space>", pop_word)
window.mainloop()
