# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 11:44:37 2026

@author: 22001691
"""

# app.py
# Physical Sciences Helper – CAPS Grades 10–12
# Run locally:   streamlit run app.py
# Deploy:        Push to GitHub → connect at https://streamlit.io/cloud

import streamlit as st
import random

# ────────────────────────────────────────────────
# Topics data
# ────────────────────────────────────────────────

topics = {
    "Motion in One Dimension": {
        "grade": 10,
        "explanation": """Motion along a straight line.

Key quantities:
• Position, displacement (Δx – vector), distance (scalar)
• Velocity (vector), speed (scalar)
• Acceleration (vector)

Important equations:
v = u + at  
Δx = ut + ½at²  
v² = u² + 2aΔx  

Average velocity = Δx / Δt

Graphs:
• slope of position–time graph → velocity
• slope of velocity–time graph → acceleration
• area under velocity–time graph → displacement
""",
        "quiz": [
            {"q": "Displacement is a __________ quantity.", 
             "options": ["scalar", "vector", "both", "neither"], "ans": 1},
            {"q": "If an object moves 10 m east then 6 m west, displacement is:", 
             "options": ["16 m east", "4 m east", "4 m west", "16 m west"], "ans": 1},
            {"q": "The slope of a position-time graph gives:", 
             "options": ["acceleration", "velocity", "displacement", "time"], "ans": 1},
            {"q": "Constant negative acceleration means velocity is:", 
             "options": ["increasing", "decreasing", "constant", "zero"], "ans": 1}
        ]
    },

    "Waves and Pulses": {
        "grade": 10,
        "explanation": """Pulses and waves transfer energy without transferring matter.

• Pulse → single disturbance
• Transverse pulse → particles move perpendicular to direction of pulse
• Amplitude → maximum displacement from rest position
• Superposition → displacements add when waves/pulses meet
  - Constructive: larger amplitude
  - Destructive: smaller / zero amplitude
• Continuous transverse wave: crests, troughs, wavelength (λ), frequency (f), period (T = 1/f), speed v = fλ

Reflection:
• Fixed end → inverted
• Free end → not inverted
""",
        "quiz": [
            {"q": "A pulse is best described as:", 
             "options": ["continuous wave", "single disturbance", "electromagnetic only", "longitudinal wave"], "ans": 1},
            {"q": "In a transverse pulse on a string, particles move:", 
             "options": ["parallel to pulse", "perpendicular to pulse", "circular", "stationary"], "ans": 1},
            {"q": "Two identical pulses meeting head-on and overlapping perfectly show:", 
             "options": ["destructive interference", "constructive interference", "reflection", "refraction"], "ans": 1},
            {"q": "The principle allowing pulses to pass through each other unchanged is:", 
             "options": ["reflection", "superposition", "diffraction", "polarisation"], "ans": 1}
        ]
    },

    "Newton's Laws of Motion": {
        "grade": 11,
        "explanation": """Newton’s Three Laws:

1. Law of Inertia: An object remains at rest or in uniform motion unless acted on by a net external force.

2. F_net = m a  
   (resultant force causes acceleration proportional to mass)

3. Action–reaction: For every action there is an equal and opposite reaction (on different objects).

Key skills:
• Draw free-body diagrams
• Identify: weight (mg), normal force, friction, tension, applied force
""",
        "quiz": [
            {"q": "Newton’s First Law is also known as the law of", 
             "options": ["acceleration", "inertia", "action-reaction", "gravity"], "ans": 1},
            {"q": "If net force = 0, then acceleration is", 
             "options": ["increasing", "zero", "negative", "maximum"], "ans": 1},
            {"q": "The reaction force to the Earth pulling you down is:", 
             "options": ["your weight", "you pulling Earth up", "normal force", "friction"], "ans": 1}
        ]
    },

    "Faraday's Law": {
        "grade": 11,
        "explanation": """Electromagnetic induction:

Faraday’s Law:  
Induced emf (ε) = – (rate of change of magnetic flux)  
ε = – ΔΦ / Δt

Magnetic flux Φ = B ⋅ A ⋅ cosθ  
(B = magnetic field strength, A = area, θ = angle between B and normal to area)

Lenz’s Law: Induced current opposes the change that caused it.

Applications:  
• AC generators  
• Transformers  
• Induction hobs / metal detectors
""",
        "quiz": [
            {"q": "Faraday’s Law links induced emf to change in", 
             "options": ["current", "magnetic flux", "resistance", "voltage"], "ans": 1},
            {"q": "The negative sign in Faraday’s equation comes from", 
             "options": ["Ohm’s law", "Lenz’s law", "Newton’s law", "Coulomb’s law"], "ans": 1},
            {"q": "Pushing a magnet into a coil faster produces", 
             "options": ["smaller emf", "larger emf", "zero emf", "constant emf"], "ans": 1},
            {"q": "Maximum magnetic flux occurs when angle between B and area normal is", 
             "options": ["90°", "0°", "180°", "45°"], "ans": 1}
        ]
    },

    "Projectile Motion": {
        "grade": 12,
        "explanation": """Motion under gravity only (ignore air resistance).

Horizontal component: constant velocity  
vx = vi cos θ  
Range contribution: Δx = vx ⋅ t

Vertical component: constant acceleration g = 9.8 m/s² downward  
vy = vi sin θ – g t  
Δy = (vi sin θ) t – ½ g t²  
vy² = (vi sin θ)² – 2 g Δy

Key points:
• Time to max height = (vi sin θ) / g
• Total time of flight (level ground) = 2 (vi sin θ) / g
• Trajectory = parabola
""",
        "quiz": [
            {"q": "Horizontal acceleration in projectile motion is", 
             "options": ["9.8 m/s² down", "zero", "9.8 m/s² up", "depends on angle"], "ans": 1},
            {"q": "Time to reach maximum height is", 
             "options": ["(vi sin θ)/g", "(vi cos θ)/g", "2(vi sin θ)/g", "vi/g"], "ans": 0},
            {"q": "At maximum height, vertical component of velocity is", 
             "options": ["maximum", "zero", "negative", "vi sin θ"], "ans": 1},
            {"q": "The path followed by a projectile is", 
             "options": ["straight line", "parabola", "circle", "hyperbola"], "ans": 1}
        ]
    },

    "Doppler Effect": {
        "grade": 12,
        "explanation": """Change in observed frequency due to relative motion between source and observer.

Sound formula (general):  
f' = f  ×  (v ± vo) / (v ± vs)  
v = speed of sound (~340 m/s)  
+vo / –vs when approaching, –vo / +vs when receding

Effects:
• Source approaching listener → higher pitch
• Listener approaching source → higher pitch

Light:  
• Red shift → source moving away (galaxies → expanding universe)  
• Blue shift → source approaching
""",
        "quiz": [
            {"q": "When a sound source moves toward a stationary observer, observed frequency", 
             "options": ["decreases", "increases", "stays the same", "becomes zero"], "ans": 1},
            {"q": "The general Doppler formula for sound is", 
             "options": ["f' = f (v / vs)", "f' = f (v ± vo)/(v ± vs)", "f' = f v", "f' = f / v"], "ans": 1},
            {"q": "Red shift of light from distant galaxies indicates the universe is", 
             "options": ["contracting", "expanding", "stationary", "rotating"], "ans": 1},
            {"q": "If observer moves away from a stationary source, frequency", 
             "options": ["increases", "decreases", "doubles", "halves"], "ans": 1}
        ]
    },
}

# ────────────────────────────────────────────────
# Streamlit App
# ────────────────────────────────────────────────

st.title("Physical Sciences Helper – CAPS Grades 10–12")
st.markdown("Select a grade and topic to study or practise.")

grade_filter = st.selectbox("Grade", ["All", 10, 11, 12])

available = [
    name for name, data in topics.items()
    if grade_filter == "All" or data["grade"] == int(grade_filter)
]

if not available:
    st.warning("No topics available for the selected grade yet.")
else:
    topic = st.selectbox("Topic", available)

    if topic:
        data = topics[topic]

        tab_expl, tab_quiz = st.tabs(["📖 Explanation", "🧪 Quiz"])

        with tab_expl:
            st.markdown(data["explanation"])

        with tab_quiz:
            questions = data.get("quiz", [])
            if not questions:
                st.info("No quiz questions available for this topic yet.")
            else:
                random.shuffle(questions)
                score = 0
                total = len(questions)

                for i, q in enumerate(questions, 1):
                    st.subheader(f"Question {i} of {total}")
                    st.write(q["q"])

                    choice = st.radio(
                        "Choose one:",
                        q["options"],
                        index=None,
                        key=f"q_{topic}_{i}"
                    )

                    if choice is not None:
                        correct = q["options"][q["ans"]]
                        if choice == correct:
                            score += 1
                            st.success("Correct ✓")
                        else:
                            st.error(f"Wrong → correct answer: **{correct}**")

                if st.button("Finish Quiz – Show Score"):
                    percent = (score / total) * 100 if total > 0 else 0
                    st.markdown(f"**Score: {score} / {total}**  ({percent:.1f}%)")

                    if percent >= 80:
                        st.balloons()
                        st.success("Excellent! Well done 🔥")
                    elif percent >= 50:
                        st.info("Good effort – review and try again.")
                    else:
                        st.warning("Keep practising – you’ll get there!")

# Footer
st.markdown("---")
st.caption(
    "Built for CAPS Physical Sciences learners • "
    "Add more topics/questions in the code as needed • "
    "Questions shuffled each time for better practice"
)