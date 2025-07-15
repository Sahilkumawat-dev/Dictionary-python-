from tkinter import *
from tkinter import messagebox
from nltk.corpus import wordnet
from googletrans import Translator
import asyncio

#tkinter
root = Tk()
root.title("Dictionary")
root.geometry("1000x400")

#translator
translator = Translator()

import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')


async def translate_text(text, src_language='en', dest_language='hi'):
    try:
        #translation result
        translation = await asyncio.to_thread(translator.translate, text, src=src_language, dest=dest_language)
        return translation.text
    except Exception as e:
        return f"Translation error: {e}"


def getMeaning():
    word_input = word.get()
    meaning = None

    synsets = wordnet.synsets(word_input)
    if synsets:
        meaning = synsets[0].definition()

    if meaning:
        #translate meaning to Hindi
        meaning_hindi = asyncio.run(translate_text(meaning))  #translation
        meaning_label.config(text=f"Meaning (English): {meaning}\nMeaning (Hindi): {meaning_hindi}")
    else:
        messagebox.showinfo("Error", "Word not found or invalid. Please try a different word.")


heading_label = Label(root, text="DICTIONARY", font=("Helvetica 35 bold"), foreground='Blue')
heading_label.config(anchor=CENTER)
heading_label.pack(pady=10)

#frame search box search button
frame = Frame(root)
Label(frame, text="Enter Word", font=("Helvetica 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Helvetica 15 bold"))
word.pack(padx=10)
frame.pack()

#search button for fetching meaning
search_button = Button(root, text="Search Word", font=("Helvetica 15 bold"), relief=RIDGE, borderwidth=3,
                       cursor="hand2", foreground='Green', command=getMeaning)
search_button.config(anchor=CENTER)
search_button.pack(pady=10)

frame1 = Frame(root)
Label(frame1, text="Meaning : ", font=("Helvetica 15 bold")).pack(side=LEFT)
meaning_label = Label(frame1, text="", font=("Helvetica 12"), wraplength=900)
meaning_label.pack(pady=5)
frame1.pack(pady=10) 

root.mainloop()
