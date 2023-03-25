import tkinter
from tkinter import ttk


root = tkinter.Tk()

root.geometry("400x300")
root.title("Hour tracker")

frame = tkinter.Frame(root)
frame.pack()

time_in_frame = tkinter.LabelFrame(frame, text="Time in")
time_in_frame.grid(row=0, column=0, padx=20, pady=20)
hour_in_label = tkinter.Label(time_in_frame, text="Hour:")
hour_in_label.grid(row=0, column=0)
minute_in_label = tkinter.Label(time_in_frame, text="minute:")
minute_in_label.grid(row=0, column=1)
hour_in_entry = ttk.Combobox(time_in_frame, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])
minute_in_entry = ttk.Combobox(time_in_frame, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
hour_in_entry.grid(row=1, column=0)
minute_in_entry.grid(row=1, column=1)

total_time_frame = tkinter.LabelFrame(frame, text="Total time")
total_time_frame.grid(row=2, column=0, padx=20, pady=20)
total_hours_label = tkinter.Label(total_time_frame, text="Hours:")
total_hours_label.grid(row=2, column=0)
total_minutes_label = tkinter.Label(total_time_frame, text="minutes:")
total_minutes_label.grid(row=2, column=1)
total_hours_entry = ttk.Combobox(total_time_frame, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84])
total_minutes_entry = ttk.Combobox(total_time_frame, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59])
total_hours_entry.grid(row=3, column=0)
total_minutes_entry.grid(row=3, column=1)

time_remaining_frame = tkinter.LabelFrame(frame, text="Time remaining")
time_remaining_frame.grid(row=4, column=0, padx=10, pady=20)
time_remaining = tkinter.Label(time_remaining_frame, text="time remaining")
time_remaining.grid(row=5, column=0, padx=100, pady=20)

root.mainloop()
