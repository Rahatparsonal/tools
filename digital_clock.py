import tkinter as tk
from datetime import datetime
import pytz

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.timezones = ['UTC', 'US/Eastern', 'US/Central', 'US/Mountain', 'US/Pacific', 'Europe/London', 'Europe/Berlin', 'Asia/Tokyo', 'Australia/Sydney']
        self.labels = {}
        self.create_widgets()
        self.update_time()

    def create_widgets(self):
        for tz in self.timezones:
            label = tk.Label(self.root, font=('calibri', 40), bg='black', fg='white', width=15)
            label.pack(padx=20, pady=20)
            self.labels[tz] = label

    def update_time(self):
        for tz in self.timezones:
            current_time = datetime.now(pytz.timezone(tz)).strftime('%Y-%m-%d %H:%M:%S')
            self.labels[tz]['text'] = f'{tz}:\n{current_time}'
        self.root.after(1000, self.update_time)

if __name__ == '__main__':
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()