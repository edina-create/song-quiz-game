
import tkinter as tk
from tkinter import messagebox
import webbrowser

# Songs data: keys match exactly everywhere, no leading spaces
SONGS = {
    "Rain": {
        "link": "https://open.spotify.com/intl-de/track/6Jr2GutTFyfvAzGA36R2Uj?si=dc8502091dd5420d",
        "emoji": "🌧️"
    },
    "Like Crazy": {
        "link": "https://open.spotify.com/intl-de/track/3Ua0m0YmEjrMi9XErKcNiR?si=9490192e12604389",
        "emoji": "🌸"
    },
    "Stop": {
        "link": "https://open.spotify.com/intl-de/track/1XIIvx9S19CZVc7eow7EX7?si=ecbfe260696d41f3",
        "emoji": "🔥"
    },
    "Dont you say you love me": {
        "link": "https://open.spotify.com/intl-de/track/27xkOIER6uDLKALIelHylZ?si=d535063e951d4550",
        "emoji": "🛏️"
    },
    "Lost": {
        "link": "https://open.spotify.com/intl-de/track/02H58MSfVESkKyx4diDgu7?si=9bd07566ce784cf1",
        "emoji": "🏞️"
    },
    "Yes or no": {
        "link": "https://open.spotify.com/intl-de/track/2gkVEnpahpE3bQuvGuCpAV?si=052956e192114269",
        "emoji": "🎉"
    },
    "134340": {
        "link": "https://open.spotify.com/intl-de/track/1MX0g22bQkr9HDVe37fLnN?si=b5249602bf5540b4",
        "emoji": "✨"
    },
    "Slow dancing": {
        "link": "https://open.spotify.com/intl-de/track/5h1BN75CEh8wdSwE1xrbSe?si=2c14f5d0c2ed4a0e",
        "emoji": "💌"
    },
    "D-Day": {
        "link": "https://open.spotify.com/intl-de/track/22W6wI4hDTjMAYKKBQW9dU?si=63aac2b4b09e4fb7",
        "emoji": "🕊️"
    },
    "Love Maze": {
        "link": "https://open.spotify.com/intl-de/track/4ROdFnoZNn2RTmwct0cVpx?si=d834f47dbe3e4f7c",
        "emoji": "💖"
    },
    "Paradise": {
        "link": "https://open.spotify.com/intl-de/track/1YO4xJXhh9A1Feg9k8xuy2?si=9d051ccbc19848bd",
        "emoji": "🎭"
    },
    "Moving on": {
        "link": "https://open.spotify.com/intl-de/track/0jo4304s0u51JHHCv7it9K?si=5b8db0f4e4f54291",
        "emoji": "🌠"
    }
}

# Questions sample (7 questions) with answer options linked to song keys above
QUESTIONS = [
    {
        "question": "What mood do you prefer for your music?",
        "options": {
            "Calm and reflective": "Rain",
            "Energetic and upbeat": "Like Crazy",
            "Powerful and intense": "Stop",
            "Soft and emotional": "Dont you say you love me"
        }
    },
    {
        "question": "Pick a setting where you feel most inspired:",
        "options": {
            "A quiet rainy day": "Rain",
            "A lively party": "Yes or no",
            "A peaceful nature walk": "Lost",
            "A cozy night in": "Slow dancing"
        }
    },
    {
        "question": "Which emoji fits your personality?",
        "options": {
            "🌧️": "Rain",
            "🎉": "Yes or no",
            "✨": "134340",
            "🕊️": "D-Day"
        }
    },
    {
        "question": "Choose a theme you like in songs:",
        "options": {
            "Love and heartbreak": "Love Maze",
            "Dreams and hope": "Paradise",
            "Moving forward": "Moving on",
            "Inner conflict": "Lost"
        }
    },
    {
        "question": "What's your favorite pace in music?",
        "options": {
            "Slow and soft": "Slow dancing",
            "Mid-tempo": "Dont you say you love me",
            "Fast and driving": "Stop",
            "Mix of all": "Like Crazy"
        }
    },
    {
        "question": "Pick a color vibe you like:",
        "options": {
            "Light pink": "Yes or no",
            "Dark pink": "Moving on",
            "Blue": "134340",
            "Red": "Stop"
        }
    },
    {
        "question": "Which phrase speaks to you?",
        "options": {
            "Keep dreaming": "Paradise",
            "Never give up": "Moving on",
            "Cherish the moment": "Slow dancing",
            "Stay strong": "Stop"
        }
    }
]

class BTSQuiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Song Match Quiz 🎶")
        self.geometry("550x450")
        self.configure(bg="#FFC0CB")  # light pink default light mode bg

        # Score dictionary initialization
        self.score = {song: 0 for song in SONGS}

        self.current_question = 0
        self.selected_mode = "light"

        # UI Elements
        self.frame = tk.Frame(self, bg="#FFC0CB")
        self.frame.pack(pady=20)

        self.question_label = tk.Label(self.frame, text="", font=("Arial", 16, "bold"), bg="#FFC0CB")
        self.question_label.pack(pady=10)

        self.buttons = []
        for _ in range(4):
            btn = tk.Button(self.frame, text="", font=("Arial", 12), wraplength=400, command=lambda i=_: self.select_answer(i))
            btn.pack(fill="x", pady=5)
            self.buttons.append(btn)

        # Bottom frame for controls
        bottom_frame = tk.Frame(self, bg="#FFC0CB")
        bottom_frame.pack(pady=10)

        # Mode toggle button
        self.mode_button = tk.Button(bottom_frame, text="Switch to Dark Mode", command=self.toggle_mode)
        self.mode_button.pack(side="left", padx=10)

        # Retake quiz button
        self.retake_button = tk.Button(bottom_frame, text="Retake Quiz", command=self.retake_quiz)
        self.retake_button.pack(side="right", padx=10)

        self.show_question()

    def toggle_mode(self):
        if self.selected_mode == "light":
            self.selected_mode = "dark"
            bg_color = "#9B1B30"  # dark pink
            fg_color = "#FFC0CB"  # light pink text on dark bg
            self.mode_button.config(text="Switch to Light Mode")
        else:
            self.selected_mode = "light"
            bg_color = "#FFC0CB"  # light pink
            fg_color = "#9B1B30"  # dark pink text on light bg
            self.mode_button.config(text="Switch to Dark Mode")

        self.configure(bg=bg_color)
        self.frame.config(bg=bg_color)
        self.question_label.config(bg=bg_color, fg=fg_color)
        for btn in self.buttons:
            btn.config(bg=fg_color, fg=bg_color, activebackground=bg_color, activeforeground=fg_color)
        self.retake_button.config(bg=fg_color, fg=bg_color)
        self.mode_button.config(bg=fg_color, fg=bg_color)

    def show_question(self):
        q = QUESTIONS[self.current_question]
        self.question_label.config(text=q["question"])
        for i, (option_text, song_key) in enumerate(q["options"].items()):
            emoji = SONGS[song_key]["emoji"]
            self.buttons[i].config(text=f"{emoji}  {option_text}", command=lambda s=song_key: self.select_answer(s))
        # Hide unused buttons if fewer than 4 options
        for i in range(len(q["options"]), 4):
            self.buttons[i].pack_forget()

    def select_answer(self, selected_song):
        # Add to score
        if selected_song in self.score:
            self.score[selected_song] += 1
        else:
            messagebox.showerror("Error", f"Song '{selected_song}' not found in score dictionary!")
            return

        self.current_question += 1
        if self.current_question < len(QUESTIONS):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        # Find song with highest score
        max_score = max(self.score.values())
        winners = [song for song, score in self.score.items() if score == max_score]
        result_song = winners[0]  # if tie, pick first

        emoji = SONGS[result_song]["emoji"]
        link = SONGS[result_song]["link"]

        # Clear frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        result_text = f"Your song match is:\n\n{emoji} {result_song} {emoji}"
        self.result_label = tk.Label(self.frame, text=result_text, font=("Arial", 18, "bold"), bg=self.frame["bg"])
        self.result_label.pack(pady=20)

        # Spotify link button
        self.spotify_button = tk.Button(self.frame, text="Listen on Spotify", fg="blue", cursor="hand2", font=("Arial", 14, "underline"), bg=self.frame["bg"], bd=0,
                                        command=lambda: webbrowser.open(link))
        self.spotify_button.pack()

    def retake_quiz(self):
        # Reset
        self.score = {song: 0 for song in SONGS}
        self.current_question = 0

        # Clear result widgets
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Restore question widgets
        self.question_label = tk.Label(self.frame, text="", font=("Arial", 16, "bold"), bg=self.frame["bg"])
        self.question_label.pack(pady=10)

        self.buttons = []
        for _ in range(4):
            btn = tk.Button(self.frame, text="", font=("Arial", 12), wraplength=400, command=lambda i=_: self.select_answer(i))
            btn.pack(fill="x", pady=5)
            self.buttons.append(btn)

        self.show_question()


if __name__ == "__main__":
    app = BTSQuiz()
    app.mainloop()
