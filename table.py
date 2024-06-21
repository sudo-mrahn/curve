#!/usr/bin/env python3
from nicegui import events, ui
import matplotlib.pyplot as plt
import curve
import pandas as pd
import numpy as np
import show

columns = [
    {'name': 'name', 'label': 'Name', 'field': 'name', 'align': 'left'},
    {'name': 'score', 'label': 'Score', 'field': 'score'},
]
rows = [
    {'id': 0, 'name': 'Alice', 'score': 78},
    {'id': 1, 'name': 'Bob', 'score': 91},
    {'id': 2, 'name': 'Carol', 'score': 20},
]

def add_row() -> None:
    new_id = max((dx['id'] for dx in rows), default=-1) + 1
    rows.append({'id': new_id, 'name': 'Student', 'score': 100})
    # ui.notify(f'Added new row with ID {new_id}')
    table.update()

def get_data() -> None:
    data = np.empty(len(rows))
    for i in range(len(rows)):
        data[i] = table.rows[i]['score']
    ui.notify('average: ' + str(round(np.average(data))))
    return data

def compute() -> None:
    fl = 50
    orig = get_data()
    floor = curve.floor(orig, fl)
    max = curve.scalemax(orig, fl)
    med = curve.scalemed(orig, fl)
    arr = [orig, floor, max, med]
    return arr



def rename(e: events.GenericEventArguments) -> None:
    for row in rows:
        if row['id'] == e.args['id']:
            row.update(e.args)
    ui.notify(f'Updated rows to: {table.rows}')
    table.update()


def delete(e: events.GenericEventArguments) -> None:
    rows[:] = [row for row in rows if row['id'] != e.args['id']]
    ui.notify(f'Deleted row with ID {e.args["id"]}')
    table.update()


table = ui.table(columns=columns, rows=rows, row_key='name').classes('w-2/3')
table.add_slot('header', r'''
    <q-tr :props="props">
        <q-th auto-width />
        <q-th v-for="col in props.cols" :key="col.name" :props="props">
            {{ col.label }}
        </q-th>
    </q-tr>
''')
table.add_slot('body', r'''
    <q-tr :props="props">
        <q-td auto-width >
            <q-btn size="sm" color="warning" round dense icon="delete"
                @click="() => $parent.$emit('delete', props.row)"
            />
        </q-td>
        <q-td key="name" :props="props">
            {{ props.row.name }}
            <q-popup-edit v-model="props.row.name" v-slot="scope"
                @update:model-value="() => $parent.$emit('rename', props.row)"
            >
                <q-input v-model="scope.value" dense autofocus counter @keyup.enter="scope.set" />
            </q-popup-edit>
        </q-td>
        <q-td key="score" :props="props">
            {{ props.row.score }}
            <q-popup-edit v-model="props.row.score" v-slot="scope"
                @update:model-value="() => $parent.$emit('rename', props.row)"
            >
                <q-input v-model.number="scope.value" type="number" dense autofocus counter @keyup.enter="scope.set" />
            </q-popup-edit>
        </q-td>
    </q-tr>
''')
with table.add_slot('bottom-row'):
    with table.cell().props('colspan=3'):
        ui.button('Add row', icon='add', color='accent', on_click=add_row).classes('w-full')
table.on('rename', rename)
table.on('delete', delete)

def visualize():
    with ui.pyplot() as plot:
        fig, axs = plt.subplots(nrows=4, ncols=2)
        fig.set_size_inches(10,8)
        arr = compute()
        grades = []
        for i in range(len(arr)):
            grades.append(
                pd.DataFrame.from_dict(curve.grades(arr[i]), 
                                    orient='index'))
        bins=80
        names = ['raw scores', 'simple floor', 'scale to max', 'scale to median']
        for i in range(4):
            axs[i,0].hist(arr[i], bins, density=True, label='avg: ' + str(round(np.average(arr[i]))))
            axs[i,0].axvline(x=np.median(arr[i]), ymin=0, ymax=0.85, color='red', label='median: ' + str(round(np.median(arr[i]))))
            axs[i,0].set_xlim([min(arr[0]), 100])
            axs[i,0].set_ylabel(names[i])
            axs[i,0].yaxis.label.set_fontsize(10)
            axs[i,0].legend()
            grades[i] = grades[i][::-1]
            grades[i].plot(kind='bar', ax=axs[i,1])
            axs[i,1].legend(['min: ' + str(round(min(arr[i])))])
        plot.fig = fig
        ui.button('clear figure', on_click=lambda: fig.clf())


ui.button('compute curve', on_click=lambda: (
    ui.notify('computing curve...'),
    visualize(),
))

ui.run()








