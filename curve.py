# curve scores
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def floor(arr, fl):
    mask = (arr - fl) > 0
    return (arr - fl) * mask + fl

def scalemax(arr,fl):
    t_min = min(arr)
    if t_min > fl:
        print('no need to curve')
        return arr
    else:
        c_max = fl - t_min
        t_max = max(arr)
        t_avg = np.average(arr)
        n = len(arr)
        diff = t_max - arr
        t_avg_target = t_avg + c_max * np.sum(diff)/(n*(t_max - t_min))

        c = diff * n * (t_avg_target - t_avg) / np.sum(diff)
        return arr + c

def scalemed(arr, fl):
    if fl < min(arr):
        print('no need to curve')
        return arr
    else:
        median = np.median(arr)
        sorted = np.sort(arr)
        clipped = sorted[sorted < median]
        left = sorted[sorted >= median]
        curved = scalemax(clipped, fl)
        return np.append(left,curved)


    

def grades(arr):
    return {
        'A':round(100*np.count_nonzero(arr>=90)/len(arr)), 
        'B':round(100*np.count_nonzero((arr<90) & (arr>=80))/len(arr)), 
        'C': round(100*np.count_nonzero((arr < 80) & (arr>=70))/len(arr)),
        'D': round(100*np.count_nonzero((arr<70) & (arr>=60))/len(arr)), 
        'F': round(100*np.count_nonzero((arr<60))/len(arr)) }