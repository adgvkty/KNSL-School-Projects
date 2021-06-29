from pygame import *
from random import *
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy

sizeMin = ''
sizeMax = ''
arr_size = 0
array = []
el = 0
sMax = 0
sMin = 0
fentry = ''
export = ''


def gen_mas():

    global el
    global array
    global sMax
    global sMin

    try:
        arr_size = size_array.get()
        arr_size = int(arr_size)
        sMax = sizeMax_entry.get()
        sMin = sizeMin_entry.get()

        array = []

        if sMax == '' or sMin == '':
            error('Entry is empty')
        else:
            sMin = int(sMin)
            sMax = int(sMax)
            if sMin > sMax:
                error('Wrong Array Size')
            if arr_size == '':
                if sMin != abs(sMin):
                    arr_size = abs(sMin) + sMax
                else:
                    arr_size = sMax - sMin
                    print(arr_size)
            for el in range(arr_size):
                array.append(randint(sMin, sMax))
            print(array)
            message('Array has been generated')
    except Exception as e:
        error(e)


def export_mas():

    global sMin
    global sMax
    global array
    global export

    try:
        export = export_entry.get()
        if not array:
            error('Array is not generated')
        elif export == '':
            error('File name is empty')
        else:

            f = open(f'{export}.txt', 'w')
            f.write(str(array))
            f.close()
            numpy.save(f'{export}', array)
            message('Exported Successfully')
    except Exception as e:
        error(e)


def import_mas():

    global array
    fentry = fname_entry.get()

    try:
        f = open(f'{fentry}', 'rt')
        temp = f.read()
        print(temp)
        message('Imported Successfully')
    except Exception as e:
        error(e)


def sort_create():

    global array
    global text

    sMax = sizeMax_entry.get()
    sMax = int(sMax)
    arr_size = size_array.get()
    arr_size = int(arr_size)

    try:
        sort = sort_alg.get()
        if sort == "Bubble Sort":
            title = "Bubble Sort"
            algo = sort_buble(array)
        elif sort == "Insertion Sort":
            title = "Insertion Sort"
            algo = insertion_sort(array)
        elif sort == "Quick Sort":
            title = "Quick Sort"
            algo = quick_Sort(array, 0, arr_size - 1)
        elif sort == "Selection Sort":
            title = "Selection Sort"
            algo = selection_sort(array)
        elif sort == "Merge Sort":
            title = "Merge Sort"
            algo = merge_sort(array, 0, arr_size - 1)
        elif sort == "Heap Sort":
            title = "Heap Sort"
            algo = heap_sort(array)
        elif sort == "Shell Sort":
            title = "Shell Sort"
            algo = shell_sort(array)
        else:
            title = "Count Sort"
            algo = count_sort(array)

        fig, ax = plt.subplots()
        ax.set_title(title)

        bar_rec = ax.bar(range(len(array)), array, align='edge')

        ax.set_xlim(0, arr_size)
        ax.set_ylim(0, int(sMax * 1.1))

        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

        epochs = [0]

        anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=1,
                                   repeat=False)
        plt.show()
    except Exception as e:
        error(e)


def error(e):
    messagebox.showerror(title='Error', message=e)


def message(m):
    messagebox.showinfo(title='Info', message=m)


def swap(A, i, j):
    a = A[j]
    A[j] = A[i]
    A[i] = a


def sort_buble(arr):
    if len(arr) == 1:
        return
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
            yield arr


def insertion_sort(arr):
    if len(arr) == 1:
        return
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            swap(arr, j, j - 1)
            j -= 1
            yield arr


def quick_Sort(arr, p, q):
    if p >= q:
        return
    piv = arr[q]
    pivindx = p
    for i in range(p, q):
        if arr[i] < piv:
            swap(arr, i, pivindx)
            pivindx += 1
        yield arr
    swap(arr, q, pivindx)
    yield arr

    yield from quick_Sort(arr, p, pivindx - 1)
    yield from quick_Sort(arr, pivindx + 1, q)


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
            yield arr
        if min != i:
            swap(arr, i, min)
            yield arr


def merge_sort(arr, lb, ub):
    if ub <= lb:
        return
    elif lb < ub:
        mid = (lb + ub) // 2
        yield from merge_sort(arr, lb, mid)
        yield from merge_sort(arr, mid + 1, ub)
        yield from merge(arr, lb, mid, ub)
        yield arr


def merge(arr, lb, mid, ub):
    new = []
    i = lb
    j = mid + 1
    while i <= mid and j <= ub:
        if arr[i] < arr[j]:
            new.append(arr[i])
            i += 1
        else:
            new.append(arr[j])
            j += 1
    if i > mid:
        while j <= ub:
            new.append(arr[j])
            j += 1
    else:
        while i <= mid:
            new.append(arr[i])
            i += 1
    for i, val in enumerate(new):
        arr[lb + i] = val
        yield arr


def heapify(arr, n, i):
    largest = i
    l = i * 2 + 1
    r = i * 2 + 2
    while l < n and arr[l] > arr[largest]:
        largest = l
    while r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        swap(arr, i, largest)
        yield arr
        yield from heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        yield from heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        yield arr
        yield from heapify(arr, i, 0)


def shell_sort(arr):
    sublistcount = len(arr) // 2
    while sublistcount > 0:
        for start_position in range(sublistcount):
            yield from gap_InsertionSort(arr, start_position, sublistcount)
        sublistcount = sublistcount // 2


def gap_InsertionSort(nlist, start, gap):
    for i in range(start + gap, len(nlist), gap):

        current_value = nlist[i]
        position = i

        while position >= gap and nlist[position - gap] > current_value:
            nlist[position] = nlist[position - gap]
            position = position - gap
            yield nlist

        nlist[position] = current_value
        yield nlist


def count_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1
        yield arr
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
            yield arr
        yield arr


def update_plot(array, rec, epochs):

    global text

    for rec, val in zip(rec, array):
        rec.set_height(val)
    epochs[0] += 1
    text.set_text("No.of operations :{}".format(epochs[0]))


root = Tk()
root.title('Visualisation settings')
root.resizable(False, False)

OptionList = ["Bubble Sort",
              "Insertion Sort",
              "Quick Sort",
              "Selection Sort",
              "Merge Sort",
              "Shell Sort",
              "Heap Sort",
              "Count Sort"]

sort_alg = StringVar(root)
sort_alg.set(OptionList[0])

sizeLabel = Label(root, width=20, height=1, text='Elements range:', font=('Times New Roman', 15, "bold"))
sizeLabel.grid(row=1, column=0, sticky='nsew')

array_size = Label(root, width=6, height=1, font=("Times New Roman", 15, "bold"), text='Array elements:')
array_size.grid(row=0, columnspan=2, sticky="nsew")

sizeMin_entry = Entry(textvariable=sizeMin)
sizeMin_entry.grid(column=2, row=1, sticky='nsew')

sizeMax_entry = Entry(textvariable=sizeMax)
sizeMax_entry.grid(column=3, row=1, sticky='nsew')

fname_entry = Entry(textvariable=fentry)
fname_entry.grid(column=2, row=4, columnspan=2, sticky='nsew')

export_entry = Entry(textvariable=export)
export_entry.grid(column=2, row=3, columnspan=2, sticky='nsew')

size_array = Entry(textvariable=arr_size)
size_array.grid(column=2, row=0, columnspan=2, sticky='nsew')

sort_algs = OptionMenu(root, sort_alg, *OptionList)
sort_algs.config(font=("Times New Roman", 15, "bold"), borderwidth=0)
sort_algs.grid(row=5, columnspan=4, sticky="nsew")

gen_masButton = Button(root, width=6, height=1, font=("Times New Roman", 15, "bold"), text='Generate Array',
                       borderwidth=0, command=lambda: gen_mas())
gen_masButton.grid(row=2, columnspan=4, sticky="nsew")

export_masButton = Button(root, width=6, height=1, font=("Times New Roman", 15, "bold"), text='Export FileName:',
                          borderwidth=0, command=lambda: export_mas())
export_masButton.grid(row=3, columnspan=2, sticky="nsew")

import_masButton = Button(root, width=6, height=1, font=("Times New Roman", 15, "bold"),
                          text='Import FileName:', borderwidth=0, command=lambda: import_mas())
import_masButton.grid(row=4, columnspan=2, sticky="nsew")

sort_masButton = Button(root, width=6, height=1, font=("Times New Roman", 15, "bold"), text='Sort Array',
                        borderwidth=0, command=lambda: sort_create())
sort_masButton.grid(row=6, columnspan=4, sticky="nsew")

root.mainloop()
