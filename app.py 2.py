# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 14:43:42 2026

@author: 22001691
"""

# English Vocabulary Helper – For reading, writing & learning complex words
# Run this file: python english_vocabulary_helper.py
# Works offline – no internet needed

import random
import time
import os

# Dictionary of complex / advanced English words
# Format: "word": {"meaning": "...", "pos": "...", "example": "...", "pron": "..."}
vocabulary = {
    "ubiquitous": {
        "meaning": "present or found everywhere",
        "pos": "adjective",
        "example": "Mobile phones are ubiquitous in modern life.",
        "pron": "yoo-BIK-wi-təs"
    },
    "ephemeral": {
        "meaning": "lasting for a very short time",
        "pos": "adjective",
        "example": "Social media trends are often ephemeral.",
        "pron": "ih-FEM-ə-rəl"
    },
    "ameliorate": {
        "meaning": "to make something better; improve",
        "pos": "verb",
        "example": "Education can ameliorate poverty over time.",
        "pron": "ə-MEEL-yə-rayt"
    },
    "capricious": {
        "meaning": "changing suddenly and unpredictably",
        "pos": "adjective",
        "example": "The weather in Limpopo can be capricious.",
        "pron": "kə-PRI-shəs"
    },
    "obfuscate": {
        "meaning": "to make something unclear or confusing on purpose",
        "pos": "verb",
        "example": "Some politicians obfuscate the truth.",
        "pron": "OB-fə-skayt"
    },
    "gregarious": {
        "meaning": "fond of company; very sociable",
        "pos": "adjective",
        "example": "She is gregarious and loves group activities.",
        "pron": "ɡri-GAIR-ee-əs"
    },
    "iconoclast": {
        "meaning": "a person who attacks traditional beliefs",
        "pos": "noun",
        "example": "The artist was seen as an iconoclast.",
        "pron": "eye-KON-ə-klast"
    },
    "juxtapose": {
        "meaning": "to place things side by side for contrast",
        "pos": "verb",
        "example": "The film juxtaposes wealth and poverty.",
        "pron": "JUK-stə-pohz"
    },
    "mellifluous": {
        "meaning": "sweet or musical; pleasant to hear",
        "pos": "adjective",
        "example": "Her mellifluous voice calmed everyone.",
        "pron": "me-LIF-loo-əs"
    },
    "nefarious": {
        "meaning": "extremely wicked or villainous",
        "pos": "adjective",
        "example": "The nefarious plan was discovered.",
        "pron": "nə-FAIR-ee-əs"
    },
    "pernicious": {
        "meaning": "having a harmful effect, especially gradually",
        "pos": "adjective",
        "example": "Fake news has a pernicious influence.",
        "pron": "pər-NISH-əs"
    },
    "recondite": {
        "meaning": "little known; very difficult to understand",
        "pos": "adjective",
        "example": "The lecture was full of recondite ideas.",
        "pron": "REK-ən-dite"
    },
    "sycophant": {
        "meaning": "a person who flatters important people for personal gain",
        "pos": "noun",
        "example": "He surrounded himself with sycophants.",
        "pron": "SIK-ə-fənt"
    },
    "verisimilitude": {
        "meaning": "the appearance of being true or real",
        "pos": "noun",
        "example": "The story has great verisimilitude.",
        "pron": "ver-ə-si-MIL-i-tood"
    },
    "abrogate": {
        "meaning": "to officially cancel or repeal",
        "pos": "verb",
        "example": "The law was abrogated last year.",
        "pron": "AB-rə-gayt"
    },
    "anachronism": {
        "meaning": "something out of place in time",
        "pos": "noun",
        "example": "A smartphone in a Shakespeare play is an anachronism.",
        "pron": "ə-NAK-rə-niz-əm"
    },
    "fastidious": {
        "meaning": "very attentive to detail; hard to please",
        "pos": "adjective",
        "example": "She is fastidious about her schoolwork.",
        "pron": "fas-TID-ee-əs"
    },
    "alacrity": {
        "meaning": "eager readiness or quickness",
        "pos": "noun",
        "example": "He accepted the task with alacrity.",
        "pron": "ə-LAK-ri-tee"
    },
    "cajole": {
        "meaning": "to persuade by flattery or gentle urging",
        "pos": "verb",
        "example": "She cajoled him into helping.",
        "pron": "kə-JOHL"
    },
    "pulchritude": {
        "meaning": "physical beauty",
        "pos": "noun",
        "example": "The painting celebrates human pulchritude.",
        "pron": "PUL-kri-tood"
    },
    # You can easily add 20–50 more words here in the same format
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_word(word):
    info = vocabulary[word]
    print(f"\n{'═' * 50}")
    print(f"WORD: {word.upper()}")
    print(f"Part of speech: {info['pos']}")
    print(f"Pronunciation:  {info['pron']}")
    print(f"Meaning:         {info['meaning']}")
    print(f"Example:         {info['example']}")
    print(f"{'═' * 50}\n")

def lookup_mode():
    while True:
        clear_screen()
        print("VOCABULARY LOOKUP MODE")
        print("Type a word (or 'back' to return)\n")
        query = input("> ").strip().lower()
        if query == 'back':
            return
        if query in vocabulary:
            show_word(query)
        else:
            print("Word not found. Try another!\n")
        input("\nPress Enter to continue...")

def quiz_mode():
    words = list(vocabulary.keys())
    score = 0
    total = 10  # You can change this number

    clear_screen()
    print(f"FLASHCARD QUIZ – {total} questions")
    print("For each meaning, type the word.\n")

    selected = random.sample(words, min(total, len(words)))

    for i, word in enumerate(selected, 1):
        info = vocabulary[word]
        print(f"\nQuestion {i}/{total}")
        print(f"Meaning: {info['meaning']}")
        print(f"Example: {info['example']}")
        answer = input("\nWhat is the word? → ").strip().lower()

        if answer == word:
            print("Correct! ✓")
            score += 1
        else:
            print(f"Wrong. The word is → {word}")
            print(f"Pron: {info['pron']}")

        input("Press Enter for next...")

    percent = (score / total) * 100
    clear_screen()
    print(f"QUIZ COMPLETE!")
    print(f"Score: {score}/{total}  ({percent:.1f}%)")
    if percent >= 80:
        print("Excellent! You're mastering advanced words!")
    elif percent >= 50:
        print("Good effort – keep practicing!")
    else:
        print("More practice will help – try again soon!")
    input("\nPress Enter to return...")

def spelling_mode():
    words = list(vocabulary.keys())
    total = 8

    clear_screen()
    print("SPELLING PRACTICE MODE")
    print("You will see a word for 4 seconds → then type it.\n")

    selected = random.sample(words, min(total, len(words)))

    score = 0
    for i, word in enumerate(selected, 1):
        clear_screen()
        print(f"Word {i}/{total}")
        print(f"\n{word.upper()}\n")
        time.sleep(4)
        clear_screen()
        print(f"Word {i}/{total} – now type it!")
        answer = input("> ").strip().lower()

        if answer == word:
            print("Correct spelling! ✓")
            score += 1
        else:
            print(f"Wrong. Correct spelling: {word}")

        input("Press Enter...")

    clear_screen()
    print(f"SPELLING PRACTICE DONE!")
    print(f"Correct: {score}/{total}")
    input("\nPress Enter to return...")

def main_menu():
    while True:
        clear_screen()
        print("═" * 50)
        print(" ENGLISH VOCABULARY HELPER ".center(50))
        print(" For reading, writing & mastering complex words ")
        print("═" * 50)
        print("1. Lookup a word (read meaning + example)")
        print("2. Flashcard Quiz (meaning → guess word)")
        print("3. Spelling Practice (see → type word)")
        print("4. Exit")
        print("═" * 50)

        choice = input("Enter 1–4: ").strip()

        if choice == '1':
            lookup_mode()
        elif choice == '2':
            quiz_mode()
        elif choice == '3':
            spelling_mode()
        elif choice == '4':
            clear_screen()
            print("Goodbye! Keep learning every day. 💪")
            time.sleep(1.5)
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(1.2)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nExited. See you next time!")