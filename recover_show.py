# Source Generated with Decompyle++
# File: show.cpython-312.pyc (Python 3.12)

import numpy as np
import pandas as pd
from matplotlib.pyplot import pyplot as plt
import curve

def simple(arr, grades):
    (fig, axs) = plt.subplots(nrows = 1, ncols = 2)
    fig.set_size_inches(6, 2.5)
    df = pd.DataFrame.from_dict(grades, orient = 'index')
    axs[0].hist(arr, 50, density = True, label = 'avg: ' + str(round(np.average(arr))))
    df.plot(kind = 'bar', ax = axs[1])
    axs[0].legend()
    axs[1].legend([
        'min: ' + str(round(min(arr)))])
    plt.show()


def compare(before, after):
    (fig, axs) = plt.subplots(nrows = 2, ncols = 2)
    fig.set_size_inches(8, 5)
    df_bef = pd.DataFrame.from_dict(curve.grades(before), orient = 'index')
    df_aft = pd.DataFrame.from_dict(curve.grades(after), orient = 'index')
    axs[(0, 0)].hist(before, 80, density = True, label = 'avg: ' + str(round(np.average(before))))
    axs[(1, 0)].hist(after, 80, density = True, label = 'avg: ' + str(round(np.average(after))))
    axs[(0, 0)].legend()
    axs[(1, 0)].legend()
    df_bef.plot(kind = 'bar', ax = axs[(0, 1)])
    df_aft.plot(kind = 'bar', ax = axs[(1, 1)])
    plt.setp(axs[(0, 0)], xlim = (min(before), 100))
    plt.setp(axs[(1, 0)], xlim = (min(before), 100))
    axs[(0, 1)].legend([
        'min: ' + str(round(min(before)))])
    axs[(1, 1)].legend([
        'min: ' + str(round(min(after)))])
    plt.show()


def compare3(arr1, arr2, arr3):
    (fig, axs) = plt.subplots(nrows = 3, ncols = 2)
    fig.set_size_inches(10, 8)
    df1 = pd.DataFrame.from_dict(curve.grades(arr1), orient = 'index')
    df1 = df1[::-1]
    df2 = pd.DataFrame.from_dict(curve.grades(arr2), orient = 'index')
    df2 = df2[::-1]
    df3 = pd.DataFrame.from_dict(curve.grades(arr3), orient = 'index')
    df3 = df3[::-1]
    arr = [
        arr1,
        arr2,
        arr3]
    bins = 25
    axs[(0, 0)].hist(arr1, bins, density = True, label = 'avg: ' + str(round(np.average(arr1))))
    axs[(1, 0)].hist(arr2, bins, density = True, label = 'avg: ' + str(round(np.average(arr2))))
    axs[(2, 0)].hist(arr3, bins, density = True, label = 'avg: ' + str(round(np.average(arr3))))
    df1.plot(kind = 'bar', ax = axs[(0, 1)])
    df2.plot(kind = 'bar', ax = axs[(1, 1)])
    df3.plot(kind = 'bar', ax = axs[(2, 1)])
# WARNING: Decompyle incomplete


def compare4(arr1, arr2, arr3, arr4):
    (fig, axs) = plt.subplots(nrows = 4, ncols = 2)
    fig.set_size_inches(12, 11)
    df1 = pd.DataFrame.from_dict(curve.grades(arr1), orient = 'index')
    df1 = df1[::-1]
    df2 = pd.DataFrame.from_dict(curve.grades(arr2), orient = 'index')
    df2 = df2[::-1]
    df3 = pd.DataFrame.from_dict(curve.grades(arr3), orient = 'index')
    df3 = df3[::-1]
    df4 = pd.DataFrame.from_dict(curve.grades(arr4), orient = 'index')
    df4 = df4[::-1]
    arr = [
        arr1,
        arr2,
        arr3,
        arr4]
    df = [
        df1,
        df2,
        df3,
        df4]
    ylabs = [
        'raw scores',
        'simple floor',
        'scale to max',
        'scale to median']
    bins = 75
# WARNING: Decompyle incomplete

