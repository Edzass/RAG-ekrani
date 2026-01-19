import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import os
import time
from time import sleep

# --- Your story graph: each scene has an image, text, and choices ---
# choices: list of (button_text, next_scene_key)
STORY = {
    "start": {
        "image": "images/start.png",
        "text": "Tu uzmosties uz nezināmas planētas.  \n Tev pīkstst skābeļa maska, kas liecina par skābekļa rezervju beigušanos. \n Tava rīcība:",
        "choices": [
            ("1.Celties un meklēt jaunu masku.", "1"),
            ("2.Ignorēt pīkstienu un turpināt gulēt.", "end"),
            
        ],
    },
    "1": {
        "image": "images/forest.gif",
        "text": "Tu piecelies un dodies ties meklēt jaunu skābekļa masku. \n Tu redzi tālumā kosmosa kuģi, kas dūmo, iespējams, tur ir vēl kāds izdzīvojušais. \n Tava rīcība:",
        "choices": [
            ("1.Doties uz kosmosa kuģi (10min).", "2"),
            ("2.Doties meklēt palīdzību uz pilsētu-vadoties pēc tālumā mirgojošām gaismiņām (25min).", "pilseta"),
        ],
    },
        "pilseta": {
        "image": "images/forest.gif",
        "text": "Tu uztruakumā skraidi pa pilsētu, vadoties pēc tālumā mirgojošām gaismiņām. \n Tava rīcība:",
        "choices": [
            ("1..", "2"),
            ("2..", "pilseta"),
        ],
    },
    "2": {
        "image": "images/forest.gif",
        "text": "Tu redzi, ka kuģis ir pilnībā iznīcināts, un tu nevari atrast nevienu izdzīvojušo. \n TOMĒR \n Tu ieraugi interesantu somu. \n Tava rīcība:",
        "choices": [
            ("1.Ieskatīties somā.", "3"),
            ("2.Meklēt pēc negadījuma videoklipa- kuģa melnajā kastē.", "start"),
        ],
    },
    "3": {
        "image": "images/forest.gif",
        "text": "Tur atrodas jauns skābekļa baloniņš un pārtikas krājumi. \n Ko tu dari tālāk?",
        "choices": [
            ("Take the treasure (win)", "end"),
            ("Leave it and return", "start"),
        ],
    },
    "end": {
        "image": "images/forest.gif",
        "text": "Pēc brīža tu sajūti, ka skābekļa rezerves ir beigušās un tu aizrijies. Spēle beigusies!",
        "choices": [
            ("Restart", "start"),
        ],
    },
}


class AdventureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Choose Your Own Adventure")

        self.image_label = tk.Label(root)
        self.image_label.pack(padx=10, pady=10)

        self.text_label = tk.Label(root, text="", wraplength=600, justify="center", font=("Arial", 14))
        self.text_label.pack(padx=10, pady=(0, 10))

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=10)

        self._photo = None  # keep reference to avoid garbage collection
        self.frames = []
        self.frame_index = 0
        self.delay = 50
        self.animating = False
        self.show_scene("start")

    def show_scene(self, scene_key: str):
        scene = STORY[scene_key]

        # Load and display image
        img_path = scene["image"]
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"Missing image file: {img_path}")

        self.load_image(img_path)

        # Animate text display (typewriter effect)
        self.animate_text(scene["text"])

        # Clear old buttons
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        # Create choice buttons
        for (label, next_key) in scene["choices"]:
            btn = tk.Button(
                self.buttons_frame,
                text=label,
                width=30,
                command=lambda nk=next_key: self.show_scene(nk),
            )
            btn.pack(pady=5)

    def animate_text(self, full_text: str):
        """Animates text display character by character."""
        self.text_label.config(text="")
        for i, char in enumerate(full_text):
            self.root.after(i * 50, lambda c=char, idx=i: self._update_text(c, idx, full_text))

    def _update_text(self, char: str, idx: int, full_text: str):
        """Helper to update text incrementally."""
        current_text = full_text[:idx + 1]
        self.text_label.config(text=current_text)

    def load_image(self, path):
        # Stop any ongoing animation
        self.animating = False
        self.frames.clear()
        self.frame_index = 0

        img = Image.open(path)

        # Optional: scale down large images to fit nicely (keeps aspect ratio)
        max_w, max_h = 900, 500
        img.thumbnail((max_w, max_h))

        if path.lower().endswith('.gif') and img.is_animated:
            # Load all frames for animation
            self.delay = img.info.get("duration", 100)
            for frame in ImageSequence.Iterator(img):
                frame = frame.copy()  # thumbnail already applied to img, but need to resize each frame?
                # Actually, since thumbnail modifies img in place, but for frames, better to resize each
                frame.thumbnail((max_w, max_h))
                self.frames.append(ImageTk.PhotoImage(frame))
            self.animating = True
            self.animate()
        else:
            self._photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self._photo)

    def animate(self):
        if self.animating and self.frames:
            self.image_label.config(image=self.frames[self.frame_index])
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.root.after(self.delay, self.animate)
            
if __name__ == "__main__":
    root = tk.Tk()
    app = AdventureApp(root)
    root.mainloop()

