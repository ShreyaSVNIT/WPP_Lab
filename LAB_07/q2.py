import random

class RockPaperScissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.curr_round = 0
        self.player_wins = 0
        self.comp_wins = 0
        self.choices = ["rock", "paper", "scissors"]

    def comp_choice(self):
        return random.choice(self.choices)

    def winner(self, player, comp):
        if player == comp:
            print(f"Round {self.curr_round}: It's a tie!")
        elif (player == "rock" and comp == "scissors") or \
             (player == "scissors" and comp == "paper") or \
             (player == "paper" and comp == "rock"):
            print(f"Round {self.curr_round}: You win! {player} beats {comp}.")
            self.player_wins += 1
        else:
            print(f"Round {self.curr_round}: You lose! {comp} beats {player}.")
            self.comp_wins += 1

    def check_winner(self):
        if self.player_wins > self.rounds // 2:
            print("\nCongratulations! You won the game! ")
            return True
        elif self.comp_wins > self.rounds // 2:
            print("\nOh no! The computer won the game.")
            return True
        return False

    def play(self):
        print(f"Welcome to Rock, Paper, Scissors! Best of {self.rounds} rounds.\n")
        while self.curr_round < self.rounds:
            self.curr_round += 1
            player_choice = input("Enter rock, paper, or scissors: ").lower()
            
            if player_choice not in self.choices:
                print("Invalid choice. Please try again.")
                self.curr_round -= 1  
                continue

            comp_choice = self.comp_choice()
            self.winner(player_choice, comp_choice)

            if self.check_winner():
                break

        print(f"\nFinal Score - You: {self.player_wins}, Computer: {self.comp_wins}")

if __name__ == "__main__":
    rounds = int(input("Enter the number of rounds: "))
    game = RockPaperScissors(rounds)
    game.play()


