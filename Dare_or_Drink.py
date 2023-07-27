import tkinter as tk
from PIL import Image, ImageTk
import random

class TruthOrDareGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dare or Drink")
        self.geometry("1280x900")
        self.players = []
        self.current_player_index = 0
        self.truths = []
        self.dares = []
        self.choice = None
        self.backdoor = False
        self.totalshots = 0
        self.random_index = 0
        self.random_player = None
        self.random_2 = None
        self.index_2 = 0
        self.scare = False
        self.phase2 = False
        self.load_truths_and_dares()
        self.create_title_screen()

    def load_truths_and_dares(self):
        with open("dares.txt", "r", encoding="utf-8") as dare_file:
            self.dares = dare_file.readlines()

    def load_phase2(self):
        with open("hard.txt", "r", encoding="utf-8") as phase2_file:
            self.dares = phase2_file.readlines()

    def jumpscare(self):
        self.clear_screen()
        self.scare = True

        self.jump_scare = tk.Label(
                self,
                text="JUMPSCARE!!! EVERY PLAYER MUST TAKE A 5 HOUR ENERGY",
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
        self.jump_scare.pack()
        self.continue_button = tk.Button(
            self,
            text="CONTINUE",
            command=self.continue_game,
            font=("Comic Sans MS", 24),
            fg="green",
            bg="black",
        )
        self.continue_button.pack()
        image = Image.open("food.gif")
        frames = []

        # Extract individual frames from the animated GIF
        try:
            while True:
                frames.append(ImageTk.PhotoImage(image))
                image.seek(len(frames))  # Move to the next frame
        except EOFError:
            pass

        # Create a Canvas widget to display the animated GIF
        canvas = tk.Canvas(self, width=image.width, height=image.height, highlightthickness=0)
        canvas.pack()

        # Display the frames in a loop to simulate animation
        delay = image.info.get('duration', 100)  # Get the frame delay (in milliseconds)
        frame_count = len(frames)

        def animate_frame(index):
            canvas.create_image(0, 0, anchor='nw', image=frames[index])

            # Move to the next frame
            self.after(delay, animate_frame, (index + 1) % frame_count)

        # Start the animation
        animate_frame(0)

    def player_roll(self):
        self.random_index = random.randint(0, len(self.players) - 1)
        self.random_player = self.players[self.random_index]
        while self.random_player == self.current_player:
            self.random_index = random.randint(0, len(self.players) - 1)
            self.random_player = self.players[self.random_index]
        self.random_name = tk.Label(
                self,
                text=str(self.random_player["name"]) + "has been chosen randomly",
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
        self.random_name.pack()
        self.random_roll.config(state=tk.DISABLED)
    def player_roll_pass(self):
        self.index_2 = random.randint(0, len(self.players) - 1)
        self.random_2 = self.players[self.index_2]
        while self.random_2 == self.random_player:
            self.index_2 = random.randint(0, len(self.players) - 1)
            self.random_2 = self.players[self.index_2]
        self.random_name_2 = tk.Label(
            self,
            text=str(self.random_2["name"]) + "has been chosen randomly",
            font=("Comic Sans MS", 24),
            fg="white",
            bg="black",
            )
        self.random_name_2.pack()
        self.random_roll_2.config(state=tk.DISABLED)
        
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
        image = Image.open("sponge.gif")
        frames = []

        # Extract individual frames from the animated GIF
        try:
            while True:
                frames.append(ImageTk.PhotoImage(image))
                image.seek(len(frames))  # Move to the next frame
        except EOFError:
            pass

        # Create a Canvas widget to display the animated GIF
        canvas = tk.Canvas(self, width=image.width, height=image.height, highlightthickness=0)
        canvas.pack()

        # Display the frames in a loop to simulate animation
        delay = image.info.get('duration', 100)  # Get the frame delay (in milliseconds)
        frame_count = len(frames)

        def animate_frame(index):
            canvas.create_image(0, 0, anchor='nw', image=frames[index])

            # Move to the next frame
            self.after(delay, animate_frame, (index + 1) % frame_count)

        # Start the animation
        animate_frame(0)

    def group_skip(self):
        self.clear_screen()
        self.current_player["shot_count"] -= 2
        self.players[self.random_index]["Dares_completed"] -= 1
        self.totalshots -= 2
        for player in self.players:
            player["shot_count"] += 1
            self.totalshots += 1 
        self.roll_label = tk.Label(
            self, text="The group has skipped, everyone take a shot.", font=("Comic Sans MS", 24), fg="red", bg="black"
        )
        self.roll_label.pack()
        self.continue_button = tk.Button(
            self,
            text="CONTINUE",
            command=self.continue_game,
            font=("Comic Sans MS", 24),
            fg="green",
            bg="black",
        )
        self.continue_button.pack()
        image = Image.open("image.gif")
        frames = []

        # Extract individual frames from the animated GIF
        try:
            while True:
                frames.append(ImageTk.PhotoImage(image))
                image.seek(len(frames))  # Move to the next frame
        except EOFError:
            pass

        # Create a Canvas widget to display the animated GIF
        canvas = tk.Canvas(self, width=image.width, height=image.height, highlightthickness=0)
        canvas.pack()

        # Display the frames in a loop to simulate animation
        delay = image.info.get('duration', 100)  # Get the frame delay (in milliseconds)
        frame_count = len(frames)

        def animate_frame(index):
            canvas.create_image(0, 0, anchor='nw', image=frames[index])

            # Move to the next frame
            self.after(delay, animate_frame, (index + 1) % frame_count)

        # Start the animation
        animate_frame(0)


    def add_player(self):
        name = self.name_entry.get()
        if name:
            self.players.append({"name": name, "shot_count": 0, "Dares_completed":0})
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
        print(self.totalshots)
        if self.totalshots >= 12 and self.phase2 == False:
            self.load_phase2()
            self.phase2 = True
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
                text=str(player["name"]) + ", Shot Count: " + str(player["shot_count"]) + ', Dares Completed: ' + str(player["Dares_completed"]),
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
            text=str(self.current_player["name"]) + ", your dare is:",
            font=("Comic Sans MS", 24),
            fg="white",
            bg="black",
            wraplength=400
        )
        self.dare_label.pack()

        self.current_dare = "Take off your shirt until the end of the game."

        self.dare_text = tk.Label(
                self, text=self.current_dare, font=("Comic Sans MS", 24), fg="red", bg="black", wraplength=700

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
    
        
        for player in self.players:
            self.list_players = tk.Label(
                self,
                text=str(player["name"]) + ", Shot Count: " + str(player["shot_count"]) + ', Dares Completed: ' + str(player["Dares_completed"]),
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
            )
            self.list_players.pack()
        self.random_roll = tk.Button(
            self,
            text="Choose Random Player",
            command=self.player_roll,
            font=("Comic Sans MS", 24),
            fg="blue",
            bg="black",
        )
        self.random_roll.pack() 

        self.add_shot = tk.Button(
            self,
            text="Take a shot.",
            command=self.add,
            font=("Comic Sans MS", 24),
            fg="blue",
            bg="black",
        )
        self.add_shot.pack() 
    def roll(self):
        if self.backdoor == False and random.randint(0, 25) == 2 and self.totalshots >= 10:
            self.clear_screen()

            self.current_player = self.players[0]
            self.player_label = tk.Label(
                self,
                text=str(self.current_player["name"]) + ", It is your turn!",
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
                text="Click for your Dare:",
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
            self.dare_button.pack()
            
        
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
                text="Click for your Dare:",
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
            self.dare_button.pack() 

    def select_dare(self):
        self.clear_screen()
        self.choice = "Dare"
        self.create_dare_screen()                              

    def create_dare_screen(self):
        if self.scare == False and self.totalshots  >= 15:
            self.jumpscare()
        else: 
            self.dare_label = tk.Label(
                self,
                text=str(self.current_player["name"]) + ", your dare is:",
                font=("Comic Sans MS", 24),
                fg="white",
                bg="black",
                wraplength=700
            )
            self.dare_label.pack()

            self.current_dare = random.choice(self.dares)
            self.dares.remove(self.current_dare)

            self.dare_text = tk.Label(
                self, text=self.current_dare, font=("Comic Sans MS", 24), fg="red", bg="black", wraplength=700

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
        
            
            for player in self.players:
                self.list_players = tk.Label(
                    self,
                    text=str(player["name"]) + ", Shot Count: " + str(player["shot_count"]) + ', Dares Completed: ' + str(player["Dares_completed"]),
                    font=("Comic Sans MS", 24),
                    fg="white",
                    bg="black",
                )
                self.list_players.pack()
            self.random_roll = tk.Button(
                self,
                text="Choose Random Player",
                command=self.player_roll,
                font=("Comic Sans MS", 24),
                fg="blue",
                bg="black",
            )
            self.random_roll.pack() 

            self.add_shot = tk.Button(
                self,
                text="Take a shot.",
                command=self.add,
                font=("Comic Sans MS", 24),
                fg="blue",
                bg="black",
            )
            self.add_shot.pack() 

    def add(self):
        self.current_player["shot_count"] += 1
        self.totalshots += 1
        self.shot_message = tk.Label(
            self,
            text=self.current_player["name"] + ", has taken a shot",
            font=("Comic Sans MS", 24),
            fg="orange",
            bg="black",
        )
        self.shot_message.pack()
        self.add_shot.config(state=tk.DISABLED)

    def addrandom(self):
        self.random_player["shot_count"] += 1
        self.totalshots += 1
        self.shot_message = tk.Label(
            self,
            text=self.random_player["name"] + ", has taken a shot",
            font=("Comic Sans MS", 24),
            fg="orange",
            bg="black",
        )
        self.shot_message.pack()
        self.add_shot_random.config(state=tk.DISABLED)

    def skip(self):
        self.current_player["shot_count"] += 1
        self.totalshots += 1
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
        image = Image.open("boom.gif")
        frames = []

        # Extract individual frames from the animated GIF
        try:
            while True:
                frames.append(ImageTk.PhotoImage(image))
                image.seek(len(frames))  # Move to the next frame
        except EOFError:
            pass

        # Create a Canvas widget to display the animated GIF
        canvas = tk.Canvas(self, width=image.width, height=image.height, highlightthickness=0)
        canvas.pack()

        # Display the frames in a loop to simulate animation
        delay = image.info.get('duration', 100)  # Get the frame delay (in milliseconds)
        frame_count = len(frames)

        def animate_frame(index):
            canvas.create_image(0, 0, anchor='nw', image=frames[index])

            # Move to the next frame
            self.after(delay, animate_frame, (index + 1) % frame_count)

        # Start the animation
        animate_frame(0)


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
        self.totalshots += 2
        self.random_index = random.randint(0, len(self.players) - 1)
        self.random_player = self.players[self.random_index]
        while self.random_player == self.current_player:
            self.random_index = random.randint(0, len(self.players) - 1)
            self.random_player = self.players[self.random_index]
        self.new_person = tk.Label(
            self,
            text=self.random_player["name"] + " must complete the task",
            font=("Comic Sans MS", 24),
            fg="white",
            bg="black",
        )
        self.new_person.pack()
        self.players[self.random_index]["Dares_completed"] += 1
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
                                 
        self.continue_button = tk.Button(
            self,
            text="CONTINUE",
            command=self.continue_game,
            font=("Comic Sans MS", 24),
            fg="green",
            bg="black",
        )
        self.continue_button.pack()
        self.groupskip = tk.Button(
            self,
            text="GROUP SKIP",
            command=self.group_skip,
            font=("Comic Sans MS", 24),
            fg="purple",
            bg="black",
        )
        self.groupskip.pack()

        self.add_shot_random = tk.Button(
            self,
            text="Take a shot.",
            command=self.addrandom,
            font=("Comic Sans MS", 24),
            fg="blue",
            bg="black",
        )
        self.add_shot_random.pack() 

        self.random_roll_2 = tk.Button(
            self,
            text="Choose Random Player",
            command=self.player_roll_pass,
            font=("Comic Sans MS", 24),
            fg="blue",
            bg="black",
        )
        self.random_roll_2.pack()    

    def done(self):
        self.clear_screen()
        self.current_player["Dares_completed"] += 1
        self.create_game_screen()

    def continue_game(self):
        self.clear_screen()
        self.choice = None
        self.create_game_screen()
    

if __name__ == "__main__":
    game = TruthOrDareGame()
    game.configure(bg="black")
    game.mainloop()