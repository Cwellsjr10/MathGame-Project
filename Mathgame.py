# Math Game - A simple game to practice math skills
# By: Cedric Wells Jr.
# Date: 10/15/2023
# Description: This is a simple math game that allows the user to practice their math skills.
# Usage: Run the game and follow the instructions to practice your math skills.



class Question:
    def __init__(self, question: str, answer: int):
        self.question = question
        self.answer = answer

    def ask(self) -> str:
        return self.question

    def check_answer(self, answer: int) -> bool:
        return self.answer == answer


class Round:
    def __init__(self, name: str, questions: list):
        self.name = name
        self.questions = questions
        self.round_score = 0

    def play(self, game: "MathGame") -> None:
        for question in self.questions:

            while True:
                print(question.ask())
                answer = input("Enter your answer: ")

                if answer.isdigit():
                    answer = int(answer)
                    break
                else:
                    print("Invalid input. Please enter a number.")

            if question.check_answer(answer):
                game.add_points(100)
                self.round_score += 100
            else:
                game.add_points(-50)
                self.round_score -= 50

            print(f"Round {self.name} score: {self.round_score}")

            if game.points >= game.target_points:
                print("Target reached! You have reached the target points. Congratulations!")
                break

    def summary(self) -> None:
        print(f"Round {self.name} summary: {self.round_score} points")
       
class AdditionRound(Round):
    def __init__(self):
        questions = [
            Question("If you add 5 and 3, what is the result?", 8),
            Question("If you add 10 and 7, what is the result?", 17),
            Question("If you add 15 and 5, what is the result?", 20),
            Question("If you add 20 and 10, what is the result?", 30),
        ]
        super().__init__("Addition Round", questions)


class MultiplicationRound(Round):
    def __init__(self):
        questions = [
            Question("If you multiply 5 by 3, what is the result?", 15),
            Question("If you multiply 6 by 7, what is the result?", 42),
            Question("If you multiply 8 by 6, what is the result?", 48),
            Question("If you multiply 10 by 5, what is the result?", 50),
        ]
        super().__init__("Multiplication Round", questions)


class DivisionRound(Round):
    def __init__(self):
        questions = [
            Question("If you divide 20 by 5, what is the result?", 4),
            Question("If you divide 12 by 3, what is the result?", 4),
            Question("If you divide 15 by 3, what is the result?", 5),
            Question("If you divide 10 by 2, what is the result?", 5),
        ]
        super().__init__("Division Round", questions)


class MathGame:
    def __init__(self, target_points: int = 1000):
        self.target_points = target_points
        self._points = 0
        self.rounds = [
            AdditionRound(),
            MultiplicationRound(),
            DivisionRound(),
        ]

    @property
    def points(self) -> int:
        return self._points

    def add_points(self, points: int) -> None:
        self._points += points

    def play(self) -> None:
        print(
            f"Welcome to the Math Game!\n"
            f"Reach {self.target_points} points to win.\n"
            f"Every correct answer gives you 100 points.\n"
            f"Every incorrect answer subtracts 50 points.\n"
            f"Good luck!"
        )

        for r in self.rounds:
            r.play(self)

            if self.points >= self.target_points:
                print("Target reached! You have reached the target points. Congratulations!")
                break

            r.summary()

        self.final_score()

    def final_score(self) -> None:
        print(f"Final score: {self.points} points")

        if self.points >= self.target_points:
            print("Congratulations! You have reached the target points.")
        else:
            print("Better luck next time!")


if __name__ == "__main__":
    game = MathGame()
    game.play()
