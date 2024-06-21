# visualize the information
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import curve

def compare4(orig, floor, max, med):
    fig, axs = plt.subplots(nrows=4, ncols=2)
    fig.set_size_inches(12,10)
    arr = [orig, floor, max, med]
    grades = [
        pd.DataFrame.from_dict(curve.grades(orig), orient='index'), 
        pd.DataFrame.from_dict(curve.grades(floor), orient='index'), 
        pd.DataFrame.from_dict(curve.grades(max), orient='index'), 
        pd.DataFrame.from_dict(curve.grades(med), orient='index')]
    bins=80
    names = ['raw scores', 'simple floor', 'scale to max', 'scale to median']
    for i in range(4):
        axs[i,0].hist(arr[i], bins, density=True, label='avg: ' + str(round(np.average(arr[i]))))
        axs[i,0].axvline(x=np.median(arr[i]), ymin=0, ymax=0.85, color='red', label='median: ' + str(round(np.median(arr[i]))))
        axs[i,0].set_xlim([min(arr[0]), 100])
        axs[i,0].set_ylabel(names[i])
        axs[i,0].yaxis.label.set_fontsize(14)
        axs[i,0].legend()
        grades[i] = grades[i][::-1]
        grades[i].plot(kind='bar', ax=axs[i,1])
        axs[i,1].legend(['min: ' + str(round(min(arr[i])))])
