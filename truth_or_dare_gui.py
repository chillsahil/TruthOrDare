import tkinter as tk
from PIL import Image, ImageTk
import random

class TruthOrDareGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Truth or Dare Game")
        self.geometry("1280x720")
        self.players = []
        self.current_player_index = 0
        self.truths = []
        self.dares = []
        self.choice = None
        self.backdoor = False
        self.load_truths_and_dares()
        self.create_title_screen()

    def load_truths_and_dares(self):
        with open("truths.txt", "r", encoding="utf-8") as truth_file:
            self.truths = truth_file.readlines()
        with open("dares.txt", "r", encoding="utf-8") as dare_file:
            self.dares = dare_file.readlines()

    def create_title_screen(self):
        self.title_label = tk.Label(
            self, text="Enter player names:", font=("Comic Sans MS", 24), fg="white", bg="black"
        )
        self.title_label.pack()

        self.name_entry = tk.Entry(self, font=("Comic Sans MS", 24))
        self.name_entry.pack()

        self.add_player_button = tk.Button(
            self,
            text="Add Player",
            command=self.add_player,
            font=("Comic Sans MS", 24),
            fg="white",
            bg="black",
        )
        self.add_player_button.pack()

        self.players_label = tk.Label(
            self, text="Players:", font=("Comic Sans MS", 24), fg="white", bg="black"
        )
        self.players_label.pack()

        self.players_frame = tk.Frame(self)
        self.players_frame.pack()

        self.start_game_button = tk.Button(
            self,
            text="Start Game",
            command=self.start_game,
            state=tk.DISABLED,
            font=("Comic Sans MS", 24),
            fg="white",
            bg="black",
        )
        self.start_game_button.pack()

    def add_player(self):
        name = self.name_entry.get()
        if name:
            self.players.append({"name": name, "shot_count": 0})
            player_label = tk.Label(
                self.players_frame,
                text=name,
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            player_label.pack()
            self.name_entry.delete(0, tk.END)
            self.start_game_button.configure(state=tk.NORMAL)

    def start_game(self):
        self.clear_screen()
        self.create_game_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_game_screen(self):
        self.roll_label = tk.Label(
            self, text="ROLL TIME!", font=("Comic Sans MS", 24), fg="white", bg="black"
        )
        self.roll_label.pack()
        self.roll_button = tk.Button(
            self,
            text="ROLL",
            command=self.roll,
            font=("Comic Sans MS", 24),
            fg="white",
            bg="black",
        )
        self.roll_button.pack()
        for player in self.players:
            self.list_players = tk.Label(
                self,
                text=str(player["name"]) + ", Shot Count: " + str(player["shot_count"]),
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.list_players.pack()
        self.current_player_index = random.randint(0, len(self.players) - 1)
        self.current_player = self.players[self.current_player_index]
    def backdoor_dare(self):
        self.clear_screen()
        self.choice = "Dare"
        self.dare_label = tk.Label(
            self,
            text=str(self.current_player["name"]) + " Your dare is:",
            font=("Comic Sans MS", 24),
            fg="white",
            bg="black",
            wraplength=400
        )
        self.dare_label.pack()

        self.current_dare = "Flash everyone"

        self.dare_text = tk.Label(
            self, text=self.current_dare, font=("Comic Sans MS", 24), fg="red", bg="black", wraplength=400

        )
        self.dare_text.pack()
        self.backdoor = True
        self.skip_button = tk.Button(
            self,
            text="SKIP",
            command=self.skip,
            font=("Comic Sans MS", 24),
            fg="yellow",
            bg="black",
        )
        self.skip_button.pack(side=tk.LEFT)
        self.pass_button = tk.Button(
            self,
            text="PASS",
            command=self.pass_turn,
            font=("Comic Sans MS", 24),
            fg="red",
            bg="black",
        )
        self.pass_button.pack(side=tk.LEFT)
        self.done_button = tk.Button(
            self,
            text="DONE",
            command=self.done,
            font=("Comic Sans MS", 24),
            fg="green",
            bg="black",
        )
        self.done_button.pack(side=tk.LEFT)

    def roll(self):
        if self.backdoor == False and random.randint(0, 25) == 2:
            self.clear_screen()

            self.current_player = self.players[0]
            self.player_label = tk.Label(
                self,
                text=str(self.current_player["name"]) + ", It is your turn",
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.player_label.pack()
            self.shot_count_label = tk.Label(
                self,
                text="Shot Count: " + str(self.current_player["shot_count"]),
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.shot_count_label.pack()
            self.dare_or_truth_label = tk.Label(
                self,
                text="Select Dare or Truth:",
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.dare_or_truth_label.pack()

            self.dare_button = tk.Button(
                self,
                text="DARE",
                command=self.backdoor_dare,
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.dare_button.pack(side=tk.LEFT)
            self.truth_button = tk.Button(
                self,
                text="TRUTH",
                command=self.select_truth,
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.truth_button.pack(side=tk.RIGHT)
        
        else:
            self.clear_screen()
            self.current_player = self.players[self.current_player_index]
            self.player_label = tk.Label(
                self,
                text=str(self.current_player["name"]) + ", It is your turn.",
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.player_label.pack()
            self.shot_count_label = tk.Label(
                self,
                text="Shot Count: " + str(self.current_player["shot_count"]),
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.shot_count_label.pack()
            self.dare_or_truth_label = tk.Label(
                self,
                text="Select Dare or Truth:",
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.dare_or_truth_label.pack()

            self.dare_button = tk.Button(
                self,
                text="DARE",
                command=self.select_dare,
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.dare_button.pack(side=tk.LEFT)
            self.truth_button = tk.Button(
                self,
                text="TRUTH",
                command=self.select_truth,
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.truth_button.pack(side=tk.RIGHT)

    def select_dare(self):
        self.clear_screen()
        self.choice = "Dare"
        self.create_dare_screen()

    def select_truth(self):
        self.clear_screen()
        self.choice = "Truth"
        self.create_truth_screen()

    def create_dare_screen(self):
        self.dare_label = tk.Label(
            self,
            text=str(self.current_player["name"]) + " Your dare is:",
            font=("Comic Sans MS", 24),
            fg="white",
            bg="black",
            wraplength=400
        )
        self.dare_label.pack()

        self.current_dare = random.choice(self.dares)
        self.dares.remove(self.current_dare)

        self.dare_text = tk.Label(
            self, text=self.current_dare, font=("Comic Sans MS", 24), fg="red", bg="black", wraplength=400

        )
        self.dare_text.pack()

        self.skip_button = tk.Button(
            self,
            text="SKIP",
            command=self.skip,
            font=("Comic Sans MS", 24),
            fg="yellow",
            bg="black",
        )
        self.skip_button.pack(side=tk.LEFT)
        self.pass_button = tk.Button(
            self,
            text="PASS",
            command=self.pass_turn,
            font=("Comic Sans MS", 24),
            fg="red",
            bg="black",
        )
        self.pass_button.pack(side=tk.RIGHT)
        self.done_button = tk.Button(
            self,
            text="DONE",
            command=self.done,
            font=("Comic Sans MS", 24),
            fg="green",
            bg="black",
        )
        self.done_button.pack()

    def create_truth_screen(self):
        self.truth_label = tk.Label(
            self,
            text=str(self.current_player["name"]) + " Your truth is:",
            font=("Comic Sans MS", 24),
            fg="white",
            bg="black",
            wraplength=500
        )
        self.truth_label.pack()

        self.current_truth = random.choice(self.truths)
        self.truths.remove(self.current_truth)

        self.truth_text = tk.Label(
            self, text=self.current_truth, font=("Comic Sans MS", 24), fg="red", bg="black"
        )
        self.truth_text.pack()

        self.skip_button = tk.Button(
            self,
            text="SKIP",
            command=self.skip,
            font=("Comic Sans MS", 24),
            fg="yellow",
            bg="black",
        )
        self.skip_button.pack(side=tk.LEFT)
        self.pass_button = tk.Button(
            self,
            text="PASS",
            command=self.pass_turn,
            font=("Comic Sans MS", 24),
            fg="red",
            bg="black",
        )
        self.pass_button.pack(side=tk.RIGHT)
        self.done_button = tk.Button(
            self,
            text="DONE",
            command=self.done,
            font=("Comic Sans MS", 24),
            fg="green",
            bg="black",
        )
        self.done_button.pack()

    def skip(self):
        self.current_player["shot_count"] += 1
        self.clear_screen()
        self.create_skip_screen()

    def create_skip_screen(self):
        self.skip_label = tk.Label(
            self,
            text=self.current_player["name"] + ", please take a shot",
            font=("Comic Sans MS", 24),
            fg="orange",
            bg="black",
        )
        self.skip_label.pack()

        self.continue_button = tk.Button(
            self,
            text="CONTINUE",
            command=self.continue_game,
            font=("Comic Sans MS", 24),
            fg="green",
            bg="black",
        )
        self.continue_button.pack()

    def pass_turn(self):
        self.clear_screen()
        self.create_pass_screen()

    def create_pass_screen(self):
        self.skip_label = tk.Label(
            self,
            text=self.current_player["name"] + " had passed and must take two shots!",
            font=("Comic Sans MS", 24),
            fg="yellow",
            bg="black",
        )
        self.skip_label.pack()
        self.current_player["shot_count"] += 2

        random_index = random.randint(0, len(self.players) - 1)
        random_player = self.players[random_index]
        while random_player == self.current_player:
            random_index = random.randint(0, len(self.players) - 1)
            random_player = self.players[random_index]
        self.new_person = tk.Label(
            self,
            text=random_player["name"] + " must complete the task",
            font=("Comic Sans MS", 24),
            fg="white",
            bg="black",
        )
        self.new_person.pack()
        if self.choice == "Dare":
            self.print_choice = tk.Label(
                self,
                text="Your dare is: " + str(self.current_dare),
                font=("Comic Sans MS", 24),
                fg="red",
                bg="black",
                wraplength=500
            )
            self.print_choice.pack()
        elif self.choice == "Truth":
            self.print_choice = tk.Label(
                self,
                text="Your truth is: " + str(self.current_truth),
                font=("Comic Sans MS", 24),
                fg="red",
                bg="black",
                wraplength=500
            )
            self.print_choice.pack()

        self.continue_button = tk.Button(
            self,
            text="CONTINUE",
            command=self.continue_game,
            font=("Comic Sans MS", 24),
            fg="green",
            bg="black",
        )
        self.continue_button.pack()

    def done(self):
        self.clear_screen()
        self.create_game_screen()

    def continue_game(self):
        self.clear_screen()
        self.choice = None
        self.create_game_screen()


if __name__ == "__main__":
    game = TruthOrDareGame()
    game.configure(bg="black")
    game.mainloop()
