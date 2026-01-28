# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 15:04:09 2026

@author: 22001691
"""

# Newton's 2nd Law: F = m * a
import matplotlib.pyplot as plt
import numpy as np

m = 2  # mass (kg)
a_values = np.linspace(1, 10, 100)  # acceleration (m/s²)
F = m * a_values  # force (N)

plt.plot(a_values, F, label='F = m × a')
plt.xlabel('Acceleration (m/s²)')
plt.ylabel('Force (N)')
plt.title("Newton's 2nd Law Demo")
plt.grid(True)
plt.legend()
plt.show()

# Student task: Change mass and re-run
print("Try m=5 or m=10!")