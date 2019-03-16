import sys
import tkinter as tk
import time

class StopWatch(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self, master)
        self.master.title("Stop Watch")
        self.master.geometry('400x350')

        self.started = False
        self.first_start_time = 0
        self.start_time = 0
        self.stop_time = 0
        self.stoping_time = 0
        self.once_stoping_time = 0
        self.lap_time = 0
        self.lap_count = 0

        self.Label1 = tk.Label(self, text="00:00.00")
        self.Label1.pack()

        self.Button1 = tk.Button(self, text=u'Start', width=50, command=self.start)
        self.Button1.pack()
        self.Button2 = tk.Button(self, text=u'Stop', width=50, command=self.stop, state=tk.DISABLED)
        self.Button2.pack()
        self.Button3 = tk.Button(self, text=u'Lap', width=50, command=self.lap, state=tk.DISABLED)
        self.Button3.pack()
        self.Button4 = tk.Button(self, text=u'Reset', width=50, command=self.reset, state=tk.DISABLED)
        self.Button4.pack()

        self.ListFrame = tk.Frame(self)
        self.ListFrame.pack()
        self.scrollbar = tk.Scrollbar(self.ListFrame,orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.ListBox1 = tk.Listbox(self.ListFrame,width=55, height=14)
        self.ListBox1.pack(side=tk.LEFT, padx=(20, 0), pady=(10, 10))
        self.ListBox1["yscrollcommand"] = self.scrollbar.set

    def start(self):
        print("Start")
        self.start_time = time.time()
        self.started = True
        if self.first_start_time == 0:
            self.first_start_time = self.start_time
        if self.lap_time == 0:
            self.lap_time = self.first_start_time
        if self.stop_time > 0:
            self.stoping_time += self.start_time - self.stop_time
            self.once_stoping_time += self.start_time - self.stop_time
        self.Button1.configure(state=tk.DISABLED)
        self.Button2.configure(state=tk.NORMAL)
        self.Button3.configure(state=tk.NORMAL)
        self.Button4.configure(state=tk.NORMAL)
        self.after(0,self.update)

    def stop(self):
        print("Stop")
        self.stop_time = time.time()
        self.started = False
        self.Button1.configure(state=tk.NORMAL)
        self.Button2.configure(state=tk.DISABLED)
        self.Button3.configure(state=tk.DISABLED)

    def lap(self):
        print("Lap")
        now = time.time()
        t = now - self.lap_time -self.once_stoping_time
        self.lap_count += 1
        self.once_stoping_time = 0
        self.lap_time = now
        text = 'Lap%02d: %f' % (self.lap_count, t)
        self.ListBox1.insert(tk.END, text)

    def reset(self):
        print("Reset")
        self.ListBox1.delete(0,tk.END)
        self.started = False
        self.first_start_time = 0
        self.start_time = 0
        self.stop_time = 0
        self.stoping_time = 0
        self.once_stoping_time = 0
        self.lap_time = 0
        self.lap_count = 0
        self.Label1.configure(text="00:00.00")
        self.Button1.configure(state=tk.NORMAL)
        self.Button2.configure(state=tk.DISABLED)
        self.Button3.configure(state=tk.DISABLED)
        self.Button4.configure(state=tk.DISABLED)

    def update(self):
        if self.started==True:
            now = time.time()
            t = now - self.first_start_time - self.stoping_time
            sec = (t*100)%100
            s = '%02d:%02d.%02d' % (t/60,t%60,sec)
            self.Label1.configure(text=s)
            self.after(10,self.update)

if __name__=='__main__':
    w = StopWatch()
    w.pack()
    w.mainloop()
