import os


class Tictactoe:
    def __init__(self):
        self.field = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def __str__(self):
        return f"{self.field}"

    def is_full(self):
        for i, j in enumerate(self.field):
            if all(x == "x" for x in j):
                return True
            elif all(x == "o" for x in j):
                return False

            if all(j[i] == "x" for j in self.field):
                return True
            elif all(j[i] == "o" for j in self.field):
                return False

        if all(j[i] == "x" for i, j in enumerate(self.field)) \
                or all(j[i] == "x" for i, j in enumerate(self.field[::-1])):
            return True
        elif all(j[i] == "o" for i, j in enumerate(self.field)) \
                or all(j[i] == "o" for i, j in enumerate(self.field[::-1])):
            return False

    def show_field(self):
        os.system('cls')
        print(" ", *[i for i, j in enumerate(self.field)])
        for i, j in enumerate(self.field):
            print(i, *j)

    def input_x(self, i, j):
        if 0 <= i < len(self.field) and 0 <= j < len(self.field[0]) and not self.field[i][j] in ["o", "x"]:
            self.field[i][j] = "x"
            self.show_field()
            return True
        return False

    def input_o(self, i, j):
        if 0 <= i < len(self.field) and 0 <= j < len(self.field[0]) and not self.field[i][j] in ["o", "x"]:
            self.field[i][j] = "o"
            self.show_field()
            return True
        return False

    def start_game(self):
        self.show_field()
        count = 0
        while True:
            pos_x, pos_y = map(int, input("Enter the position: ").split())
            if count % 2 == 0 and self.input_x(pos_x, pos_y):
                count += 1
            elif count % 2 != 0 and self.input_o(pos_x, pos_y):
                count += 1
            else:
                print("The field is occupied or an incorrect position!")

            is_full = self.is_full()

            if is_full and is_full is not None:
                self.show_field()
                print("\nX won!")
                break
            elif not is_full and is_full is not None:
                self.show_field()
                print("\nO won!")
                break

            if count == len(self.field) * len(self.field[0]):
                self.show_field()
                print("\nDraw!")
                break


def main():
    if input("Start game? y / n: ") == "y":
        test = Tictactoe()
        test.start_game()


main()
