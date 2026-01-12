import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

class GifPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GIF Choice Player")

        self.label = tk.Label(root)
        self.label.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.buttons = []
        for i in range(3):
            btn = tk.Button(
                self.button_frame,
                text=f"Choice {i+1}",
                width=15,
                command=lambda i=i: self.make_choice(i)
            )
            btn.grid(row=0, column=i, padx=5)
            self.buttons.append(btn)

        # Define branching logic
        self.story = {
            "start": {
                "gif": "gifs/start.gif",
                "choices": ["choice1", "choice2", "choice3"]
            },
            "choice1": {
                "gif": "gifs/choice1.gif",
                "choices": ["start", "choice2", "choice3"]
            },
            "choice2": {
                "gif": "gifs/choice2.gif",
                "choices": ["start", "choice1", "choice3"]
            },
            "choice3": {
                "gif": "gifs/choice3.gif",
                "choices": ["start", "choice1", "choice2"]
            }
        }

        self.current_node = "start"
        self.frames = []
        self.frame_index = 0
        self.delay = 100

        self.load_gif(self.story[self.current_node]["gif"])
        self.animate()

    def load_gif(self, path):
        self.frames.clear()
        self.frame_index = 0

        img = Image.open(path)
        self.delay = img.info.get("duration", 100)

        for frame in ImageSequence.Iterator(img):
            frame = frame.resize((400, 300))
            self.frames.append(ImageTk.PhotoImage(frame))

    def animate(self):
        if self.frames:
            self.label.config(image=self.frames[self.frame_index])
            self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.root.after(self.delay, self.animate)

    def make_choice(self, index):
        next_node = self.story[self.current_node]["choices"][index]
        self.current_node = next_node
        self.load_gif(self.story[self.current_node]["gif"])


if __name__ == "__main__":
    root = tk.Tk()
    app = GifPlayerApp(root)
    root.mainloop()