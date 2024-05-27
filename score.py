from pieces import Pieces
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Score:
    def __init__(self):
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.scoreboard = Pieces(0, 270, "classic", "white")
        self.scoreboard.part.hideturtle()
        self.scoreboard.set_pos()
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.scoreboard.part.clear()
        self.scoreboard.part.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.display_score()

    # def gameover(self):
    #     gameover_message = Pieces(0, 0, "classic", "white")
    #     gameover_message.set_pos()
    #     gameover_message.part.write("GAME OVER", align=ALIGNMENT, font=FONT)

