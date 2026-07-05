
import tkinter as tk
class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.passage = "The quick brown fox jumps over the lazy dog. Pack my box with five dozen liquor jugs. How valiantly did Bez Madhav Bhatt jump the Swift ox. The five boxing wizards jump quickly. Sphinx of black quartz judge my vow."
        self.timer_id = None
        self.time_left = 60
        self.test_running = False
        self.correct_keystrokes = 0
        self.total_keystrokes = 0
        self.passage_label = tk.Label(self.root, text=self.passage,wraplength=600)
        self.passage_label.pack()
        self.timer_label = tk.Label(self.root, text=self.time_left)
        self.timer_label.pack()
        self.text_widget = tk.Text(self.root,height=5,width=60,state=tk.DISABLED)
        self.text_widget.pack()
        self.result_label = tk.Label(self.root, text='')
        self.result_label.pack()
        self.start_button = tk.Button(self.root,text='Start Test',command=self.start_test)
        self.start_button.pack()
        self.reset_button = tk.Button(self.root,text='Reset Test',command=self.reset_test)
        self.reset_button.pack()

    def start_test(self):
        if self.test_running:
            return

        self.time_left = 60
        self.correct_keystrokes = 0
        self.total_keystrokes = 0
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete('1.0',tk.END)
        self.result_label.config(text='')
        self.test_running = True
        self.text_widget.bind('<Key>',self.on_keypress)
        self.countdown()

    def countdown(self):
        if self.time_left > 0:
            self.timer_label.config(text=self.time_left)
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.countdown)

        else:
            self.end_test()
    def on_keypress(self, event):
        if not self.test_running:
            return
        self.total_keystrokes += 1
        typed = self.text_widget.get("1.0", tk.END).strip()
        index = len(typed) - 1
        if index >= 0 and index < len(self.passage):
            if typed[index] == self.passage[index]:
                self.correct_keystrokes += 1

    def end_test(self):
        self.test_running = False
        self.text_widget.config(state=tk.DISABLED)
        wpm = int(self.correct_keystrokes / 5)
        accuracy = (self.correct_keystrokes / self.total_keystrokes) * 100 if self.total_keystrokes > 0 else 0
        self.result_label.config(text=f'{wpm} WPM | {accuracy:.1f}% Accuracy')

    def reset_test(self):
        if self.timer_id is not None:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        self.time_left = 60
        self.correct_keystrokes = 0
        self.total_keystrokes = 0
        self.test_running = False
        self.timer_label.config(text=60)
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.config(state=tk.DISABLED)
        self.result_label.config(text="")








root = tk.Tk()
app = TypingTestApp(root)
root.mainloop()