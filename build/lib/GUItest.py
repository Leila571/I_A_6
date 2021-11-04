# Program to make a simple
# login screen
import tkinter as tk
from audioplayer import AudioPlayer
root = tk.Tk()

# setting the windows size
root.geometry("1000x41000")

# declaring string variable
# for storing name and password
input1_var = tk.StringVar()
input2_var = tk.StringVar()
input3_var = tk.StringVar()
input4_var = tk.StringVar()
input5_var = tk.StringVar()
input6_var = tk.StringVar()
input7_var = tk.StringVar()
input8_var = tk.StringVar()
input9_var = tk.StringVar()
input10_var = tk.StringVar()
input11_var = tk.StringVar()
input12_var = tk.StringVar()
input13_var = tk.StringVar()
input14_var = tk.StringVar()
input15_var = tk.StringVar()
input16_var = tk.StringVar()
input17_var = tk.StringVar()
input18_var = tk.StringVar()
input19_var = tk.StringVar()
input20_var = tk.StringVar()
input21_var = tk.StringVar()
input22_var = tk.StringVar()

# defining a function that will
# get the name and password and
# print them on the screen in pycharm
def submit():
    user_input_1 = input1_var.get()
    print("the first input is :" + user_input_1)
    input1_var.set("")
def time_sig_questions():
    time_sig_question_1 = input3_var.get()
    text1 = tk.Message(root, text="What is the most commmon time signature?" + time_sig_question_1)
    text1.grid(row=1, column=0)
    input3_var.set("")
    time_sig_question_2 = input4_var.get()
    text2 = tk.Message(root, text="What does the C represent?" + time_sig_question_2)
    text2.grid(row=2, column=0)
    input4_var.set("")
    time_sig_question_3 = input5_var.get()
    text3 = tk.Message(root, text="What does the C with a line through it represent?" + time_sig_question_3)
    text3.grid(row=3, column=0)
    input5_var.set("")
    time_sig_question_4 = input6_var.get()
    text4 = tk.Message(root, text="How many beats per measure does 7/8 time have?" + time_sig_question_4)
    text4.grid(row=4, column=0)
    input6_var.set("")
    time_sig_question_5 = input7_var.get()
    text5 = tk.Message(root, text="Is 2/2 a time signature?" + time_sig_question_5)
    text5.grid(row=5, column=0)
    input7_var.set("")
    box_2_label = tk.Label(root, text='Answer these time signature questions!', font=('calibre', 10, 'bold'))
    entry_box_2 = tk.Entry(root, textvariable=input3_var, font=('calibre', 10, 'normal'))
def key_sig_questions():
    key_sig_question_1 = input8_var.get()
    text6 = tk.Message(root, text="What is the order of sharps?" + key_sig_question_1)
    text6.grid(row=1, column=1)
    input8_var.set("")
    key_sig_question_2 = input9_var.get()
    text7 = tk.Message(root, text="What is the order of flats?" + key_sig_question_2)
    text7.grid(row=2, column=1)
    input9_var.set("")
    key_sig_question_3 = input10_var.get()
    text8 = tk.Message(root, text="What is the major scale with 3 sharps?" + key_sig_question_3)
    text8.grid(row=3, column=1)
    input10_var.set("")
    key_sig_question_4 = input11_var.get()
    text9 = tk.Message(root, text="Which way on the key signature line do you add flats?" + key_sig_question_4)
    text9.grid(row=4, column=1)
    input11_var.set("")
    key_sig_question_5 = input12_var.get()
    text10 = tk.Message(root, text="Are the minor keys above or below the line?" + key_sig_question_5)
    text10.grid(row=5, column=1)
    input12_var.set("")
    box_3_label = tk.Label(root, text='Answer these key signature questions!', font=('calibre', 10, 'bold'))
    entry_box_3 = tk.Entry(root, textvariable=input3_var, font=('calibre', 10, 'normal'))
def music_genre_questions():
    music_genre_question_1 = input8_var.get()
    text11 = tk.Message(root, text="What are the characteristics of blues?" + music_genre_question_1)
    text11.grid(row=1, column=2)
    input13_var.set("")
    music_genre_question_2 = input9_var.get()
    text12 = tk.Message(root, text="What are the characteristics of rock?" + music_genre_question_2)
    text12.grid(row=2, column=2)
    input14_var.set("")
    music_genre_question_3 = input10_var.get()
    text13 = tk.Message(root, text="What are the characteristics of classical?" + music_genre_question_3)
    text13.grid(row=3, column=2)
    input15_var.set("")
    music_genre_question_4 = input11_var.get()
    text14 = tk.Message(root, text="What are the characteristics of hip hop?" + music_genre_question_4)
    text14.grid(row=4, column=2)
    input16_var.set("")
    music_genre_question_5 = input12_var.get()
    text15 = tk.Message(root, text="What are the characteristics of reggae?" + music_genre_question_5)
    text15.grid(row=5, column=2)
    input17_var.set("")
    box_4_label = tk.Label(root, text='Answer these music genre questions!', font=('calibre', 10, 'bold'))
    entry_box_4 = tk.Entry(root, textvariable=input3_var, font=('calibre', 10, 'normal'))
def music_era_questions():
    music_era_question_1 = input18_var.get()
    text16 = tk.Message(root, text="When was the Baroque period?" + music_era_question_1)
    text16.grid(row=1, column=3)
    input18_var.set("")
    music_era_question_2 = input19_var.get()
    text17 = tk.Message(root, text="When was the start of jazz?" + music_era_question_2)
    text17.grid(row=2, column=3)
    input19_var.set("")
    music_era_question_3 = input20_var.get()
    text18 = tk.Message(root, text="When was the start of rock?" + music_era_question_3)
    text18.grid(row=3, column=3)
    input20_var.set("")
    music_era_question_4 = input21_var.get()
    text19 = tk.Message(root, text="When was the end of the Baroque period?" + music_era_question_4)
    text19.grid(row=4, column=3)
    input21_var.set("")
    music_era_question_5 = input22_var.get()
    text20 = tk.Message(root, text="Was alternative music started in the 90s?" + music_era_question_5)
    text20.grid(row=5, column=3)
    input22_var.set("")
    box_5_label = tk.Label(root, text='Answer these music era questions!', font=('calibre', 10, 'bold'))
    entry_box_5 = tk.Entry(root, textvariable=input3_var, font=('calibre', 10, 'normal'))
def set_text():
    user_input_1 = input1_var.get()
    user_input_2 = input2_var.get()
    entryText = tk.StringVar()
    entry = tk.Entry(root, textvariable=entryText)
    entry.grid(row=2, column=3)
    #entryText.set("Hello World")
    entryText.set(user_input_1)

# creating a label for
# name using widget Label
box_1_label = tk.Label(root, text='user-input-1', font=('calibre', 10, 'bold'))
# creating a entry for input
# name using widget Entry
entry_box_1 = tk.Entry(root, textvariable=input1_var, font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)
time_sig_btn = tk.Button(root, text='Time Signatures!', command=time_sig_questions)
key_sig_btn = tk.Button(root, text='Key Signatures!', command=key_sig_questions)
music_genre_btn = tk.Button(root, text='Music Genres!', command=music_genre_questions)
music_era_btn = tk.Button(root, text='Music Eras!', command=music_era_questions)
place_btn = tk.Button(root, text='Place', command=set_text)
text = tk.Message(root, text="gg")
# placing the label and entry in
# the required position using grid
# box_1_label.grid(row=0, column=0)
# entry_box_1.grid(row=0, column=1)
# sub_btn.grid(row=2, column=1)
# place_btn.grid(row=2, column=2)
time_sig_btn.grid(row=0, column=0)
key_sig_btn.grid(row=0, column=1)
music_genre_btn.grid(row=0, column=2)
music_era_btn.grid(row=0, column=3)
# performing an infinite loop
# for the window to display
time_sig_box_1 = tk.Entry(root)
time_sig_box_1.grid(row=6, column=0)
time_sig_submit_btn_1 = tk.Button(root, text='Submit', command=time_sig_questions)
time_sig_submit_btn_1.grid(row=7, column=0)
time_sig_box_2 = tk.Entry(root)
time_sig_box_2.grid(row=8, column=0)
time_sig_submit_btn_2 = tk.Button(root, text='Submit', command=time_sig_questions)
time_sig_submit_btn_2.grid(row=9, column=0)
time_sig_box_3 = tk.Entry(root)
time_sig_box_3.grid(row=10, column=0)
time_sig_submit_btn_3 = tk.Button(root, text='Submit', command=time_sig_questions)
time_sig_submit_btn_3.grid(row=11, column=0)
time_sig_box_4 = tk.Entry(root)
time_sig_box_4.grid(row=12, column=0)
time_sig_submit_btn_4 = tk.Button(root, text='Submit', command=time_sig_questions)
time_sig_submit_btn_4.grid(row=13, column=0)
time_sig_box_5 = tk.Entry(root)
time_sig_box_5.grid(row=14, column=0)
time_sig_submit_btn_5 = tk.Button(root, text='Submit', command=time_sig_questions)
time_sig_submit_btn_5.grid(row=15, column=0)
key_sig_box_1 = tk.Entry(root)
key_sig_box_1.grid(row=6, column=1)
key_sig_submit_btn_1 = tk.Button(root, text='Submit', command=key_sig_questions)
key_sig_submit_btn_1.grid(row=7, column=1)
key_sig_box_2 = tk.Entry(root)
key_sig_box_2.grid(row=8, column=1)
key_sig_submit_btn_2 = tk.Button(root, text='Submit', command=key_sig_questions)
key_sig_submit_btn_2.grid(row=9, column=1)
key_sig_box_3 = tk.Entry(root)
key_sig_box_3.grid(row=10, column=1)
key_sig_submit_btn_3 = tk.Button(root, text='Submit', command=key_sig_questions)
key_sig_submit_btn_3.grid(row=11, column=1)
key_sig_box_4 = tk.Entry(root)
key_sig_box_4.grid(row=12, column=1)
key_sig_submit_btn_4 = tk.Button(root, text='Submit', command=key_sig_questions)
key_sig_submit_btn_4.grid(row=13, column=1)
key_sig_box_5 = tk.Entry(root)
key_sig_box_5.grid(row=14, column=1)
key_sig_submit_btn_5 = tk.Button(root, text='Submit', command=key_sig_questions)
key_sig_submit_btn_5.grid(row=15, column=1)
music_genre_box_1 = tk.Entry(root)
music_genre_box_1.grid(row=6, column=2)
music_genre_submit_btn_1 = tk.Button(root, text='Submit', command=music_genre_questions)
music_genre_submit_btn_1.grid(row=7, column=2)
music_genre_box_2 = tk.Entry(root)
music_genre_box_2.grid(row=8, column=2)
music_genre_submit_btn_2 = tk.Button(root, text='Submit', command=music_genre_questions)
music_genre_submit_btn_2.grid(row=9, column=2)
music_genre_box_3 = tk.Entry(root)
music_genre_box_3.grid(row=10, column=2)
music_genre_submit_btn_3 = tk.Button(root, text='Submit', command=music_genre_questions)
music_genre_submit_btn_3.grid(row=11, column=2)
music_genre_box_4 = tk.Entry(root)
music_genre_box_4.grid(row=12, column=2)
music_genre_submit_btn_4 = tk.Button(root, text='Submit', command=music_genre_questions)
music_genre_submit_btn_4.grid(row=13, column=2)
music_genre_box_5 = tk.Entry(root)
music_genre_box_5.grid(row=14, column=2)
music_genre_submit_btn_5 = tk.Button(root, text='Submit', command=music_genre_questions)
music_genre_submit_btn_5.grid(row=15, column=2)
music_era_box_1 = tk.Entry(root)
music_era_box_1.grid(row=6, column=3)
music_era_submit_btn_1 = tk.Button(root, text='Submit', command=music_era_questions)
music_era_submit_btn_1.grid(row=7, column=3)
music_era_box_2 = tk.Entry(root)
music_era_box_2.grid(row=8, column=3)
music_era_submit_btn_2 = tk.Button(root, text='Submit', command=music_era_questions)
music_era_submit_btn_2.grid(row=9, column=3)
music_era_box_3 = tk.Entry(root)
music_era_box_3.grid(row=10, column=3)
music_era_submit_btn_3 = tk.Button(root, text='Submit', command=music_era_questions)
music_era_submit_btn_3.grid(row=11, column=3)
music_era_box_4 = tk.Entry(root)
music_era_box_4.grid(row=12, column=3)
music_era_submit_btn_4 = tk.Button(root, text='Submit', command=music_era_questions)
music_era_submit_btn_4.grid(row=13, column=3)
music_era_box_5 = tk.Entry(root)
music_era_box_5.grid(row=14, column=3)
music_era_submit_btn_5 = tk.Button(root, text='Submit', command=music_era_questions)
music_era_submit_btn_5.grid(row=15, column=3)
root.mainloop()

