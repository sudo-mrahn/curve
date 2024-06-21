import numpy as np
import matplotlib.pyplot as plt
from nicegui import ui

with ui.pyplot(figsize=(3,2)):
    x = np.linspace(0, 5)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    plt.plot(x,y,'-')

ui.run()