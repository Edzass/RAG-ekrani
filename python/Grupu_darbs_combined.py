import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import os
import random
import subprocess

# ================= STORY =================

STORY = {
    "start": {
        "image": "images/start.png",
        "script": [
            {"clear": True},
            "Tu uzmosties uz nezināmas planētas.\n",
            {"append": "Tev pīkst skābeļa maska, kas liecina par skābekļa rezervju beigušanos.\n"},
            {"append": "(Atlikušas 30min)\n"},
            {"append": "Tava rīcība:"},
        ],
        "choices": [
            ("1. Celties un meklēt jaunu masku.", "celties"),
            ("2. Ignorēt pīkstienu un turpināt gulēt.", "end"),
        ],
    },

    "celties": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu piecelies un dodies meklēt jaunu skābekļa masku.\n",
            {"append": "Tu redzi tālumā kosmosa kuģi, kas dūmo, iespējams, tur ir vēl kāds izdzīvojušais.\n"},
            {"append": "Tava rīcība:"},
        ],
        "choices": [
            ("1. Doties uz kosmosa kuģi (15min).", "kosmosa kuģis1"),
            ("2. Doties meklēt palīdzību uz pilsētu – vadoties pēc tālumā mirgojošām gaismiņām (25min).", "pilseta1"),
        ],
    },

    "pilseta1": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu uztraukumā skraidi pa pilsētu, vadoties pēc tālumā mirgojošām gaismiņām.\n",
            {"append": "Tev ir atlikušas 5 minūtes ar skābekļa rezervēm.\n"},
            {"append": "Tu ieraugi veikalu ar skābeļa maskām, tomēr Tev nav resursu, lai to iegādātos.\n"},
            {"append": "Tevi izmet no veikala.\n"},
            {"append": "Tu ieraugi kādu vecu vīru, viņš saprot tavu situāciju.\n"},
            {"append": "Tev tiek piedāvāta izvēle starp 2 skābekļa baloniņiem.\n"},
            {"append": "Tava rīcība:"},
        ],
        "choices": [
            ("1. Skābekļa baloniņš, kas ir iepriekš izmantots un pārbaudīts. (+3h)", "parbaudīts baloniņs"),
            ("2. Nekad nedzirdēts, jauns skābekļa baloniņš. (+24h)", "neparbaudīts baloniņs"),
        ],
    },
    "neparbaudīts baloniņs": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu tiec pie baloniņa, bet vīriņš kaut kur nozūd.\n",
            {"wait": 2000},
            {"clear": True},
            "Baloniņš bija pilns ar indi.\n",
            {"wait": 2000},
            {"end_game": True},
            
        ],
        "choices": [],
    },
    "parbaudīts baloniņs": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tavas skābekļa rezerves ir atjaunotas!\n",
            {"wait": 1000},
        ],
        "choices": [
            ("Pateikties par dāsno žestu un doties tālāk", "parbaudīts baloniņs1.1"),
            ("Uzdot jautājumu vīriņam?", "parbaudīts baloniņs2"),
        ],
    },

    "parbaudīts baloniņs2": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Kāds ir tavs jautājums?\n",
        ],
        "choices": [ 
            ("Kā es varu tikt mājāss?", "parbaudīts baloniņs3"),
            ("Ja tev ir trīs rokas - labā, kreisā..., kā sauc trešo?", "parbaudīts baloniņs2.1"),

        ],
    },

    "parbaudīts baloniņs2.1": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu uzzini atbildi.\n",
            {"wait": 1000},
            {"end_game": True},
        ],
        "choices": [
        ],
    },
        "parbaudīts baloniņs3": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Vīriņš paskaidro - augstākajā tornī ir teleportēšanās iekārta.\n",
            {"wait": 1000},
            {"clear": True},
            "Tava rīcība:",
            {"wait": 1000},
        ],
        "choices": [
            ("Uzdot otro jautājumu", "parbaudīts baloniņs3.1"),
            ("Nosist vīriņu un iegūt resursus.", "parbaudīts baloniņs3.2"),
        ],
    },
        "parbaudīts baloniņs3.1": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Kur ir resursu veikals?\n",
            {"wait": 2000},
            {"clear": True},
            "Ielas galā.",
            {"wait": 1000},
            "Piebilde no vīriņa - tev būs nepieciešama nauda.",
            {"wait": 1000},
            {"clear": True},
            "Vīriņam aizejot : tu dzirdi viņa kabatās skanam nauda monētas.",
            {"wait": 1000},
            
        ],
        "choices": [
            ("Nosist vīriņu un iegūt resursus.", "parbaudīts baloniņs3.2"),
        ],
    },
            "parbaudīts baloniņs3.2": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Bija liecinieks! Tiek izsaukta policija. \n",
            {"wait": 2000},
            {"random": True}
            
        ],
        "choices": [
            ("", "parbaudīts baloniņs4.1"),
            ("", "parbaudīts baloniņs4.2"),
        ],
    },
            "parbaudīts baloniņs4.1": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu izbēdz no policijas. \n",
            {"wait": 2000},
            {"clear": True},
            "Tu nokļīsti atpakaļ mājās.",
            {"wait": 2000},
            {"clear": True},
            "Apsveicu, tu uzvarēji!",
            {"end_game": True},

        ],
        "choices": [
           
        ],
    },
                "parbaudīts baloniņs4.2": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Policija tevi noķer. \n",
            {"wait": 1000},
            {"clear": True},
            "Tu nokļīsti cietumā- mūžīgā ieslodzījumā.",
            {"wait": 2000},
            {"end_game": True},

        ],
        "choices": [
           
        ],
    },
    "kosmosa kuģis1": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu pavadi 10 minūtes izpētot kuģi.\n",
            {"append": "Pēkšņi tu ieraugi komandas biedru guļam tālāk meža virzienā.\n"},
            {"append": "Tava rīcība:"},
        ],
        "choices": [
            ("1. Pārbaudīt komandas biedra veselības stāvokli.", "komandas biedrs"),
            ("2. Pārbaudīt kosmosa kuģa kontrolpaneli ar pēdējiem video ierakstiem.", "kosmosa kuģis2"),
        ],
    },

    "komandas biedrs": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu secini, ka viņš ir miris.\n",
            {"append": "Tomēr uz viņa atrodas soma – iekšā ir skābeļa baloniņš un dažādi resursi.\n"},
            {"append": "Tu atjauno savas skābeļa rezerves.\n"},
            {"append": "Tu dzirdi, kā kosmosa kuģa vadības panelis uzsprāgst.\n"},
            {"wait": 1500},
            {"clear": True},
            {"append": "Tava rīcība:"},
        ],
        "choices": [
            ("Pieņemt notikošo un doties tālāk", "komandas biedrs2"),
            ("Cieņpilni aprakt mirušo komanas biedru", "start"),
        ],
    },
        "komandas biedrs2": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu atceries, ka uz kuģa tev bija soma, kurā bija viss nepieciešamais, lai salabotu pilnīgi visu uz kosmusa kuģa, pat kontrolpaneli.\n",
            {"wait": 2000},
            {"clear": True},
            {"append": "Tu secini, ka somai ir jābūt tuvumā, tāpēc dodies dziļāk mežā, meklē somu.\n"},
            {"wait": 2000},
            {"clear": True},
            {"append": "Ir pagājusi pusstunda. \n"},
            {"random": True}
        ],
        "choices": [
            ("", "komandas biedrs2.1"),
            ("", "komandas biedrs3"),
        ],
    },
        "komandas biedrs2.1": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Meklējot somu, tu sadzirdi dīvainas skaņās no mugurpuses.\n",
            {"wait": 2000},
            {"clear": True},
            {"append": "Nezināms meža dzīvnieks tev uzbrūk un saplosa gabalos.\n"},
            {"clear": True},
            {"wait": 200},
            {"append": "Spēle beigusies!"},
            {"end_game": True},
        ],
        "choices": [
        ],
    },
        "komandas biedrs3": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu atrodi somu ar ekipejumu.\n",
            {"append": "Tu dodies uz kosmosa kuģi, lai salabotu kontrolpaneli.\n"},
            {"clear": True},
            {"wait": 2000},
            {"append": "Nonākot atpakaļ kuģa avārijas vietā, tu pārskati somu un ieraugi, ka tev ir pietiekami daudz gaisa baloniņi, lai spētu salabot kosmusa kuģi un ierocis, lai medītu meža dzīvniekus, no tiem pārtiktu."},
            {"append": "Tu pavadi nākamās 6-7 dienas labojot kosmusa kuģi, kontrolpaneli un pārtikot no meža dzīvniekiem.\n"},
            {"clear": True},
            {"wait": 2000},
            {"append": "Pēc 6 dienām kuģis ir pieņemamā stāvoklī, un panelis ir salabots.\n"},
            {"clear": True},
            {"wait": 1500},
            {"append": "Ielogojoties panelī tu atrodi informāciju par planētu, kur tu esi. Tu noskaidro, ka ir tornis, kur atrodas teleportēšanās iekārta, caur kuru tu vari tikt mājās.\n"},
            {"clear": True},
            {"wait": 1500},
            {"append": " Tava rīcība:\n"},

        ],
        "choices": [
            ("Intereses pēc tu noskaidro, kas nogāja greizi ar kuģi un atrodi atbildes uz saviem jautājumiem.", "komandas biedrs3.1"),
            ("Saprotot, ka tu vari tikt mājās, tu uzsāc lidojumu uz torni.", "komandas biedrs4"),
        ],
    },
        "komandas biedrs3.1": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu lido uz torni.\n",
            {"clear": True},
            {"wait": 2000},
            {"random": True}

        ],
        "choices": [
            ("", "komandas biedrs3.1.1"),
            ("", "komandas biedrs3.1.2"),
        ],
    },
            "komandas biedrs3.1.1": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Dzinējs uzrāda kļūdas paziņojumu.\n",
            {"clear": True},
            {"wait": 2000},
            "Pēc sekundes simtdaļas ir sprādziens un tu mirsti.\n",
            {"clear": True},
            {"wait": 2000},
            {"append": "Spēle beigusies!"},
            {"wait": 1000},
            {"end_game": True},

        ],
        "choices": [

        ],
    },
        "komandas biedrs4": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu atklāj, ka tavs dvīņu brālis sabotēja kuģi.\n",
            {"append": "Sadusmots un atriebības pilns tu izdomā lidot uz pilsētu un meklēt vainīgo\n"},
            {"clear": True},
            {"wait": 2000},
        ],
        "choices": [
            ("", "komandas biedrs4.1"),
            ("", "komandas biedrs4.2"),
        ],
    },
        "komandas biedrs4.1": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Ceļoties gaisā tu sāc dzirdēt dīvainas skaņas.\n",
            {"clear": True},
            {"wait": 2000},
            {"append": "Dzinējs eksplodē, kosmosa kuģis avarē.\n"},
            {"clear": True},
            {"wait": 1000},
            {"append": "Spēle beigusies!"},
            {"wait": 1000},
            {"end_game": True},
        ],
        "choices": [

        ],
    },
        "komandas biedrs4.2": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Sadusmots un atriebības pilns tu izdomā lidot uz pilsētu un meklēt vainīgo.\n",
            {"clear": True},
            {"wait": 2000},
            {"append": "Turpinājums sekos...\n"},
            {"wait": 1000},
            {"end_game": True},
        ],
        "choices": [

        ],
    },
            "komandas biedrs3.1.2": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu veiksmīgi nokļūsti tornī un teleportējies uz mājām.\n",
            {"clear": True},
            {"wait": 2000},
            {"append": "Apsveicu ar uzvaru!"},
        ],
        "choices": [
            ("Doties uz sākumu", "start"),
        ],
    },

    "kosmosa kuģis2": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Pēc pāris sekundēm tev sāk pīkstēt maska.\n",
            {"append": "Tava rīcība:"},
        ],
        "choices": [
            ("1. Skriet laukā no kosmosa kuģa.", "skrien laukā"),
            ("2. Meklēt atbildes panelī.", "kosmosa kuģis3"),
        ],
    },

    "kosmosa kuģis3": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tev parādās laika atskaite ar gaisa rezervēm – atlikušas dažas sekundes.\n",
            {"wait": 1500},
            {"clear": True},
            {"append": "Tu atrodi video, kas izskaidro notikušo, tomēr tu nomirsti.\n"},
            {"wait": 1000},
            {"clear": True},
            {"wait": 1500},
            {"append": "Spēle beigusies!"},
            {"end_game": True},
        ],
        "choices": [],
    },

    "skrien laukā": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Tu ātri mēģini atrast jebkādu skābekļa baloniņu, tomēr tas neizdodas.\n",
            {"wait": 1500},
            {"clear": True},
            {"append": "Tu dzirdi, kā vadības panelis tālumā sāk pīkstēt – tā ir laika atskaite.\n"},
            {"wait": 1500},
            {"clear": True},
            {"append": "Liels sprādziens!!!\n"},
            {"wait": 1000},
            {"clear": True},
            {"append": "Spēle beigusies!"},
            {"end_game": True},
        ],
        "choices": [],
    },

    "end": {
        "image": "images/forest.gif",
        "script": [
            {"clear": True},
            "Pēc brīža tu sajūti, ka skābekļa rezerves ir beigušās.\n",
            {"append": "Tu aizrijies.\n"},
            {"append": "Spēle beigusies!"},
            {"end_game": True},
        ],
        "choices": [],
    },
}

# ================= APP =================

class AdventureApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Adventure")
        self.root.configure(bg="#1a1a2e")
        
        # ===== GLOBĀLAIS TEKSTA PAZUŠANAS LAIKS =====
        self.char_delay = 50  # ms uz vienu burtu
        self.base_wait = 50   # papildu ms pēc teksta

        main = tk.Frame(root, bg="#1a1a2e")
        main.pack(fill="both", expand=True, padx=15, pady=15)

        self.image_label = tk.Label(main, bg="#1a1a2e")
        self.image_label.pack(pady=10)

        self.text_label = tk.Label(
            main,
            text="",
            wraplength=800,
            justify="center",
            font=("Arial", 14, "bold"),
            fg="#e0e0e0",
            bg="#0f0f1e",
            padx=15,
            pady=15
        )
        self.text_label.pack(fill="x")

        self.buttons = tk.Frame(main, bg="#1a1a2e")
        self.buttons.pack(pady=10)

        self.frames = []
        self.animating = False
        self.frame_index = 0
        self.delay = 200

        self.pending_choices = []
        self.show_scene("start")

    # ================= SCENE =================

    def show_scene(self, key):
        scene = STORY[key]

        self.clear_buttons()
        self.load_image(scene["image"])

        self.pending_choices = scene["choices"]
        self.run_script(scene["script"], 0)

    # ================= SCRIPT ENGINE =================

    def run_script(self, script, index):
        if index >= len(script):
            self.show_choices()
            return

        item = script[index]

        if isinstance(item, str):
            self.animate_text(
                item,
                lambda: self.run_script(script, index + 1),
                append=False
            )

        elif isinstance(item, dict):

            if "append" in item:
                self.animate_text(
                    item["append"],
                    lambda: self.run_script(script, index + 1),
                    append=True
                )

            elif "wait" in item:
                # Automātisks aprēķins: teksta garums × char_delay + base_wait
                # Ja wait ir skaitlis, izmanto to, ja nav - aprēķini
                wait_time = item["wait"]
                if isinstance(wait_time, str) and wait_time == "auto":
                    # Nākotnei, ja vajag auto aprēķinu
                    wait_time = len(self.text_label.cget("text")) * self.char_delay + self.base_wait
                self.root.after(
                    wait_time,
                    lambda: self.run_script(script, index + 1)
                )

            elif item.get("clear"):
                self.text_label.config(text="")
                self.run_script(script, index + 1)

            elif item.get("end_game"):
                self.pending_choices = [("Doties uz sākumu", "start")]
                self.show_choices()
            
            elif item.get("shutdown"):
                delay = item.get("shutdown", 5)
                subprocess.call(["shutdown", "-s", "-t", str(delay)])
                self.run_script(script, index + 1)
            
            elif item.get("random"):
                if self.pending_choices and len(self.pending_choices) >= 2:
                    choice = random.choice(self.pending_choices)
                    next_scene = choice[1]
                    self.show_scene(next_scene)
                else:
                    self.run_script(script, index + 1)

    # ================= TEXT =================

    def animate_text(self, text, callback, append=False):
        if not append:
            self.text_label.config(text="")

        base = self.text_label.cget("text")
        delay = self.char_delay  # Izmanto globālo iestatījumu

        for i in range(len(text)):
            self.root.after(
                i * delay,
                lambda i=i: self.text_label.config(
                    text=base + text[:i + 1]
                )
            )

        self.root.after(len(text) * delay + self.base_wait, callback)

    # ================= BUTTONS =================

    def show_choices(self):
        self.clear_buttons()
        for label, target in self.pending_choices:
            btn = tk.Button(
                self.buttons,
                text=label,
                font=("Arial", 11, "bold"),
                padx=15,
                pady=8,
                bg="#16213e",
                fg="#00d4ff",
                command=lambda t=target: self.show_scene(t)
            )
            btn.pack(pady=5)

    def clear_buttons(self):
        for w in self.buttons.winfo_children():
            w.destroy()

    # ================= IMAGE =================

    def load_image(self, path):
        self.animating = False
        self.frames.clear()

        if not os.path.exists(path):
            self.image_label.config(image="")
            return

        img = Image.open(path)
        img.thumbnail((900, 500))

        if path.lower().endswith(".gif") and img.is_animated:
            self.delay = img.info.get("duration", 100)
            for f in ImageSequence.Iterator(img):
                f = f.copy()
                f.thumbnail((900, 500))
                self.frames.append(ImageTk.PhotoImage(f))
            self.animating = True
            self.animate_gif()
        else:
            self.photo = ImageTk.PhotoImage(img)
            self.image_label.config(image=self.photo)

    def animate_gif(self):
        if self.animating and self.frames:
            self.image_label.config(image=self.frames[self.frame_index])
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.root.after(self.delay, self.animate_gif)

# ================= RUN =================

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x700")
    AdventureApp(root)
    root.mainloop()
