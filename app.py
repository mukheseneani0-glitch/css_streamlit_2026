# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 10:25:54 2026

@author: 22001691
"""

# Physical Sciences CAPS Study App (Grades 10-12) - Python Console Version
# For high school learners in South Africa

def clear_screen():
    print("\n" * 50)  # Simple way to "clear" console

def print_header(title):
    print("=" * 60)
    print(f" {title.upper()} ".center(60, "="))
    print("=" * 60)
    print()

def main_menu():
    while True:
        clear_screen()
        print_header("PHYSICAL SCIENCES STUDY APP - CAPS GRADES 10-12")
        print("Choose your grade:")
        print("1. Grade 10")
        print("2. Grade 11")
        print("3. Grade 12")
        print("0. Exit")
        choice = input("\nEnter number: ").strip()
        
        if choice == "1":
            grade_10_menu()
        elif choice == "2":
            grade_11_menu()
        elif choice == "3":
            grade_12_menu()
        elif choice == "0":
            print("\nThank you for studying! Keep working hard! 🚀")
            break
        else:
            print("Invalid choice. Try again.")

# ───────────────────────────────────────────────
# GRADE 10 MENU & TOPICS
# ───────────────────────────────────────────────

def grade_10_menu():
    while True:
        clear_screen()
        print_header("GRADE 10 TOPICS")
        print("1. Mechanics")
        print("2. Waves, Sound & Light")
        print("3. Electricity & Magnetism")
        print("4. Matter & Materials")
        print("5. Chemical Systems (Hydrosphere)")
        print("6. Chemical Change")
        print("0. Back to main menu")
        choice = input("\nEnter number: ").strip()
        
        if choice == "1": mechanics_g10()
        elif choice == "2": waves_sound_light_g10()
        elif choice == "3": electricity_magnetism_g10()
        elif choice == "4": matter_materials_g10()
        elif choice == "5": chemical_systems_g10()
        elif choice == "6": chemical_change_g10()
        elif choice == "0": break
        else: print("Invalid choice.")

def mechanics_g10():
    while True:
        clear_screen()
        print_header("GRADE 10 - MECHANICS")
        print("1. Vectors & Scalars + Motion in 1D")
        print("2. Energy & Conservation")
        print("0. Back")
        sub = input("\nChoose: ")
        if sub == "1":
            show_content("Vectors & Scalars + Motion",
                         "Key Highlight: Scalars have magnitude only (e.g. mass, speed). Vectors have magnitude AND direction (e.g. velocity, force). Use kinematic equations: v = u + at, s = ut + ½at², v² = u² + 2as",
                         "Notes: Position, displacement, distance, average/instantaneous speed & velocity, acceleration. Graphs: s-t, v-t.",
                         ["Quiz: Which is a vector? A) Speed B) Distance C) Velocity", "C"],
                         ["Homework: Plot position-time graph for object moving at constant velocity.",
                          "Classwork: Solve 5 problems using kinematic equations."])
        elif sub == "2":
            show_content("Energy",
                         "Key Highlight: Mechanical energy (KE + PE) is conserved when no non-conservative forces act. KE = ½mv², PE = mgh.",
                         "Notes: Work-energy theorem, power = work/time.",
                         ["Quiz: Formula for kinetic energy? A) mgh B) ½mv² C) Fd", "B"],
                         ["Homework: Calculate KE & PE for a 2 kg ball dropped from 10 m.",
                          "Classwork: Show conservation of energy in free fall."])
        elif sub == "0": break

def waves_sound_light_g10():
    show_content("Waves, Sound & Light (Grade 10)",
                 "Key Highlight: v = fλ (wave speed = frequency × wavelength). Sound is longitudinal; light is electromagnetic.",
                 "Notes: Transverse vs longitudinal waves, superposition, pitch (frequency), loudness (amplitude), EM spectrum, photon energy E = hf.",
                 ["Quiz: Unit of frequency? A) m/s B) Hz C) m", "B"],
                 ["Homework: Calculate wavelength if f=50 Hz and v=340 m/s.",
                  "Classwork: Draw EM spectrum and label uses."])

def electricity_magnetism_g10():
    show_content("Electricity & Magnetism (Grade 10)",
                 "Key Highlight: Ohm's Law: V = IR. Like charges repel, unlike attract.",
                 "Notes: Magnetic field lines (N to S), series/parallel resistors, emf vs pd.",
                 ["Quiz: Ohm's Law formula? A) V=IR B) P=VI C) E=mc²", "A"],
                 ["Homework: Calculate current in 12 V circuit with 4 Ω resistor.",
                  "Classwork: Draw circuit with 2 resistors in parallel."])

def matter_materials_g10():
    show_content("Matter & Materials (Grade 10)",
                 "Key Highlight: Kinetic Molecular Theory explains states of matter. Atoms have protons, neutrons, electrons.",
                 "Notes: Periodic table trends, covalent/ionic/metallic bonding, isotopes.",
                 ["Quiz: Ionic bonding involves? A) Sharing electrons B) Transfer of electrons C) Delocalised electrons", "B"],
                 ["Homework: Draw electron configuration for Na and Cl.",
                  "Classwork: Classify 10 substances as metal/non-metal/compound."])

def chemical_systems_g10():
    show_content("Chemical Systems - Hydrosphere",
                 "Key Highlight: Water is polar → unique properties (high boiling point, solvent).",
                 "Notes: Water cycle, desalination, pollution effects.",
                 ["Quiz: Water is a good solvent because? A) Non-polar B) Polar C) Gas", "B"],
                 ["Homework: Draw labelled water cycle diagram.",
                  "Classwork: Discuss advantages/disadvantages of desalination."])

def chemical_change_g10():
    show_content("Chemical Change (Grade 10)",
                 "Key Highlight: Chemical change forms new substances (e.g. rusting, burning). Physical change does not.",
                 "Notes: Conservation of mass, balanced equations, separation techniques.",
                 ["Quiz: Burning paper is? A) Physical B) Chemical C) Neither", "B"],
                 ["Homework: Balance 5 simple equations (e.g. Mg + O₂ → MgO).",
                  "Classwork: List 5 examples each of physical & chemical changes."])

# ───────────────────────────────────────────────
# GRADE 11 & 12 (similar pattern - abbreviated for brevity)
# ───────────────────────────────────────────────

def grade_11_menu():
    print_header("GRADE 11 TOPICS (select to view)")
    print("Main areas: Vectors in 2D, Newton's Laws, Geometrical Optics, Electrostatics, Electromagnetism, Molecular Structure, Ideal Gases, Lithosphere")
    input("\nPress Enter to return...")
    # You can add full functions like above for each topic

def grade_12_menu():
    print_header("GRADE 12 TOPICS (select to view)")
    print("Main areas: Momentum & Impulse, Vertical Projectiles, Work-Energy-Power, Doppler Effect, Electric Circuits (advanced), Photoelectric Effect, Organic Chemistry, Chemical Industry")
    input("\nPress Enter to return...")
    # Expand similarly

# ───────────────────────────────────────────────
# HELPER FUNCTION TO DISPLAY CONTENT
# ───────────────────────────────────────────────

def show_content(title, highlight, notes, quiz, tasks):
    clear_screen()
    print_header(title)
    print("★★★ KEY HIGHLIGHT ★★★")
    print(highlight)
    print("\nNOTES SUMMARY:")
    print(notes)
    print("\nQUIZ:")
    for q in quiz[:-1]:
        print(q)
    answer = input("\nYour answer (A/B/C): ").strip().upper()
    correct = quiz[-1]
    if answer == correct:
        print("\nCorrect! Well done! 🎉")
    else:
        print(f"\nSorry, the correct answer is {correct}.")
    print("\nHOMEWORK / CLASSWORK IDEAS:")
    for t in tasks:
        print(f"- {t}")
    input("\nPress Enter to continue...")

# Start the app
if __name__ == "__main__":
    main_menu()