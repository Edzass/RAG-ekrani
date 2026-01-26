import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import os
import time
from time import sleep
import subprocess


STORY = {
    "start": {
        "image": "images/start.png",
        "text": "Tu uzmosties uz nezināmas planētas.  \n Tev pīkst skābeļa maska, kas liecina par skābekļa rezervju beigušanos.\n  (Atlikušas 30min)  \n Tava rīcība:",
        "choices": [
            ("1.Celties un meklēt jaunu masku.", "celties"),
            ("2.Ignorēt pīkstienu un turpināt gulēt.", "end"),
            
        ],
    },
    "celties": {
        "image": "images/forest.gif",
        "text": "Tu piecelies un dodies meklēt jaunu skābekļa masku. \n Tu redzi tālumā kosmosa kuģi, kas dūmo, iespējams, tur ir vēl kāds izdzīvojušais. \n Tava rīcība:",
        "choices": [
            ("1.Doties uz kosmosa kuģi (15min).", "kosmosa kuģis1"),
            ("2.Doties meklēt palīdzību uz pilsētu-vadoties pēc tālumā mirgojošām gaismiņām (25min).", "pilseta 1"),
        ],
    },
        "pilseta 1": {
        "image": "images/forest.gif",
        "text": "Tu uztruakumā skraidi pa pilsētu, vadoties pēc tālumā mirgojošām gaismiņām.\n Tev ir atlikušas 5 minūtes ar skābekļa rezervēm. \n Tu ieraugi veikalu ar skābeļa maskām, tomēr Tev nav resursu, lai to iegādātos. \n Tevi izmet no veikala. \n Tu ieraugi kādu vecu vīru, viņš saprot tavu situāciju. Tev tiek piedāvāta izvēle starp 2 skābekļa baloniņiem. \n Tava rīcība:",
        "choices": [
            ("1. Skābekļa baloņš, kas ir iepriekš izmantots un pārbaudīts. (+3h)", "parbaudīts baloniņs"),
            ("2. Nekad nedzirdēts, jauns skābekļa baloniņš. (+24h)", "neparbaudīts baloniņs"),
        ],
    },
    "kosmosa kuģis1": {
        "image": "images/forest.gif",
        "text": "Tu pavadi 10 minūtes izpētot kuģi, pēkšņi, tu ieraugi komandas biedru guļam tālāk meža virzienā. \n Tava rīcība:",
        "choices": [
            ("1.Pārbaudīt komandas biedra veselības stāvokli.", "komandas biedrs"),
            ("2. Pārbaudīt kosmosa kuģa kontrolpaneli ar pēdējiem video ierakstiem.", "kosmosa kuģis2"),
        ],
    },
    "komandas biedrs": {
        "image": "images/forest.gif",
        "text": "Tu secini, ka viņs ir miris.\n Tomēr uz viņa atrodas soma, iekšā ir skābeļa baloniņs un dažādi resursi turpmākai izdzīvošanai. \n Tu atjauno savas skābeļa rezerves. Tu esi uzvarējis!",
        "choices": [
            ("Doties uz sākumu", "start"),
            
        ],
    },
    "kosmosa kuģis2": {
        "image": "images/forest.gif",
        "text": "Pēc pāris sekundēm tev sāk pīkstēt maska. \n Tava rīcība:",
        "choices": [
            ("1. Skriet laukā no kosmosa kuģa", "skrien laukā"),
            ("2. Meklēt atbildes panelī", "kosmosa kuģis3"),
        ],
    },
    "kosmosa kuģis3": {
        "image": "images/forest.gif",
        "text": "Tev parādās laika atskaite ar gaisa rezervēm, atlikušas dažas sekundes. \n Tu atrodi video, kas izskaidro notikušo, tomēr tu nomirsti. \n Spēle beigusies!",
        "choices": [
            ("Doties uz sākumu", "start"),
            (),
        ],
    },
    "skrien laukā": {
        "image": "images/forest.gif",
        "text": "Tu ātri mēģini atrast jebkādu skābekļa baloniņu, tomēr tas neizdodas.\n Tu dzirdi, kā vadības panelis tālumā sāk pīkstēt, tā ir laika atskaite. \n Liels sprādziens!!! \n Spēle beigusies!",
        "choices": [
            ("Doties uz sākumu", "start"),
            (),
        ],
    },


    "end": {
        "image": "images/forest.gif",
        "text": "Pēc brīža tu sajūti, ka skābekļa rezerves ir beigušās un tu aizrijies. Spēle beigusies!",
        "choices": [
            ("Doties uz sākumu", "start"),
        ],
    },
}

def restart_computer():
    subprocess.call(["shutdown", "-r", "-t", "0"])
    

class AdventureApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Choose Your Own Adventure")
        self.root.configure(bg="#1a1a2e")

        # Create main frame that fills the window
        main_frame = tk.Frame(root, bg="#1a1a2e")
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)

        self.image_label = tk.Label(main_frame, bg="#1a1a2e")
        self.image_label.pack(padx=5, pady=10)

        # Text label with better styling
        self.text_label = tk.Label(
            main_frame,
            text="",
            wraplength=800,
            justify="center",
            font=("Arial", 14, "bold"),
            fg="#e0e0e0",
            bg="#0f0f1e",
            padx=15,
            pady=15
        )
        self.text_label.pack(padx=5, pady=10, fill="x", expand=False)

        # Buttons frame with background
        self.buttons_frame = tk.Frame(main_frame, bg="#1a1a2e")
        self.buttons_frame.pack(pady=10, fill="x")

        self._photo = None  # keep reference to avoid garbage collection
        self.frames = []
        self.frame_index = 0
        self.delay = 50
        self.animating = False
        self.pending_choices = None
        self._choice_after_id = None
        
        # Bind window resize event to update text wraplength
        self.root.bind("<Configure>", self.on_window_resize)
        
        self.show_scene("start")
    
    def on_window_resize(self, event):
        """Update text wraplength when window is resized."""
        new_width = self.root.winfo_width() - 40  # 40 for padding on both sides
        if new_width > 100:  # Only update if width is reasonable
            self.text_label.config(wraplength=new_width)
            # Update buttons wraplength so they reflow when window changes
            btn_wrap = max(150, new_width - 100)
            for child in self.buttons_frame.winfo_children():
                try:
                    child.config(wraplength=btn_wrap)
                except Exception:
                    pass

    def show_scene(self, scene_key: str):
        scene = STORY[scene_key]

        # Attēlo attēlu vai gifu
        img_path = scene["image"]
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"Missing image file: {img_path}")

        self.load_image(img_path)

        # Animate text display (typewriter effect)
        # Clear old buttons immediately so they aren't clickable during animation
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        # Store choices and start animation; buttons will be shown after animation
        self.pending_choices = scene["choices"]
        self.animate_text(scene["text"])

    def animate_text(self, full_text: str):
        """Animates text display character by character."""
        self.text_label.config(text="")
        char_delay = 50
        for i, char in enumerate(full_text):
            self.root.after(i * char_delay, lambda c=char, idx=i: self._update_text(c, idx, full_text))

        # Parāda izvēles iespējas pēc teksta animācijas pabeigšanas
        total_time = len(full_text) * char_delay + 50
        if self._choice_after_id:
            try:
                self.root.after_cancel(self._choice_after_id)
            except Exception:
                pass
        self._choice_after_id = self.root.after(total_time, self.show_choices)

    def _update_text(self, char: str, idx: int, full_text: str):
        """Helper to update text incrementally."""
        current_text = full_text[:idx + 1]
        self.text_label.config(text=current_text)

    def show_choices(self):
        """Create and display choice buttons after text animation finishes."""
        self._choice_after_id = None
        choices = self.pending_choices or []
        self.pending_choices = None

        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        btn_wrap = max(150, self.root.winfo_width() - 100)
        for (label, next_key) in choices:
            btn = tk.Button(
                self.buttons_frame,
                text=label,
                wraplength=btn_wrap,
                justify="center",
                padx=15,
                pady=8,
                font=("Arial", 11, "bold"),
                bg="#16213e",
                fg="#00d4ff",
                activebackground="#0f3460",
                activeforeground="#00d4ff",
                relief="raised",
                bd=2,
                cursor="hand2",
                command=lambda nk=next_key: self.show_scene(nk),
            )
            btn.pack(pady=6, padx=5)

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
    
    # Set window size to half width, 75% height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = screen_width // 2
    window_height = int(screen_height * 0.75)
    
    root.geometry(f"{window_width}x{window_height}+0+0")
    
    app = AdventureApp(root)
    root.mainloop()

    choice = "restart_game"  # This should be set based on user interaction
if choice == "restart_game":
    restart_computer()
else:
    # Normal game flow

