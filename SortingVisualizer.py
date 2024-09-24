import tkinter as tk
import random
import time

# Create the main window
window = tk.Tk()
window.title("Sorting Algorithm Visualizer")
window.geometry("900x600")
window.config(bg="#282c34")

# Global variables
array = []
delay = 0.05


# Function to generate an array of random numbers
def generate_array():
    global array
    array = [random.randint(10, 100) for _ in range(50)]
    draw_array(array, ["#61dafb" for _ in range(len(array))])


# Function to draw the array on the canvas
def draw_array(array, colorArray):
    canvas.delete("all")
    canvas_height = 400
    canvas_width = 800
    bar_width = canvas_width / len(array)

    for i, val in enumerate(array):
        x0 = i * bar_width
        y0 = canvas_height - val * 3
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        # Gradient from blue to green
        bar_color = colorArray[
            i] if colorArray else f'#{int(255 * (i / len(array))):02x}{int(255 * (1 - i / len(array))):02x}ff'
        canvas.create_rectangle(x0, y0, x1, y1, fill=bar_color, outline="")
    window.update()


# Bubble Sort algorithm with visualization
def bubble_sort():
    global array
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            draw_array(array, ["green" if x == j or x == j + 1 else "blue" for x in range(len(array))])
            time.sleep(delay)
    draw_array(array, ["green" for _ in range(len(array))])

# Merge Sort algorithm with visualization
def merge_sort(array, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(array, l, m)
        merge_sort(array, m + 1, r)
        merge(array, l, m, r)

def merge(array, l, m, r):
    left = array[l:m + 1]
    right = array[m + 1:r + 1]
    i = j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
        draw_array(array, ["green" if x >= l and x <= r else "blue" for x in range(len(array))])
        time.sleep(delay)

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


def selection_sort():
    # Traverse through all array elements
    for i in range(len(array)):
        # Find the minimum element in the remaining unsorted part of the array
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        array[i], array[min_index] = array[min_index], array[i]

        # Visualize the swap by coloring the current sorted portion green and ongoing comparisons blue
        draw_array(array, ["green" if x <= i else "blue" for x in range(len(array))])
        time.sleep(delay)

    # Visualize the final sorted array as green
    draw_array(array, ["green" for _ in range(len(array))])
# Quick Sort algorithm with visualization
def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
        draw_array(array, ["green" if x == i or x == j else "blue" for x in range(len(array))])
        time.sleep(delay)

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# Function to select and start the chosen sorting algorithm
def start_sorting():
    global array
    algorithm = algorithm_var.get()
    if algorithm == "Bubble Sort":
        bubble_sort()
    elif algorithm == "Merge Sort":
        merge_sort(array, 0, len(array) - 1)
        draw_array(array, ["green" for _ in range(len(array))])
    elif algorithm == "Quick Sort":
        quick_sort(array, 0, len(array) - 1)
        draw_array(array, ["green" for _ in range(len(array))])
    elif algorithm == "Selection Sort":
        selection_sort()
        draw_array(array, ["green" for _ in range(len(array))])

# GUI Elements
control_frame = tk.Frame(window, bg="#282c34", padx=10, pady=10)
control_frame.pack(side=tk.TOP)

canvas = tk.Canvas(window, width=800, height=400, bg="#282c34", highlightthickness=0)
canvas.pack(side=tk.BOTTOM)

start_button = tk.Button(control_frame, text="Start Sorting", bg="#61dafb", fg="#282c34", relief="raised",
                         font=("Arial", 14), command=start_sorting)
start_button.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(control_frame, text="Generate Array", bg="#61dafb", fg="#282c34", relief="raised",
                            font=("Arial", 14), command=generate_array)
generate_button.pack(side=tk.LEFT, padx=5)

speed_label = tk.Label(control_frame, text="Speed [s]", fg="white", bg="#282c34", font=("Arial", 12))
speed_label.pack(side=tk.LEFT, padx=10)

speed_scale = tk.Scale(control_frame, from_=0.01, to=1.0, length=200, digits=2, resolution=0.01, orient=tk.HORIZONTAL,
                       bg="#61dafb", troughcolor="#98c379", command=lambda x: adjust_speed(x))
speed_scale.pack(side=tk.LEFT, padx=5)


algorithm_var = tk.StringVar()
algorithm_menu = tk.OptionMenu(window, algorithm_var, "Bubble Sort", "Merge Sort", "Quick Sort","Selection Sort")
algorithm_menu.pack()

def adjust_speed(value):
    global delay
    delay = float(value)


# Initialize with a random array
generate_array()

window.mainloop()
