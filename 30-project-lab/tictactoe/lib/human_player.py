from player import Player


class HumanPlayer(Player):
    """A Tic-Tac-Toe human player."""

    def __init__(self, name='Jon', shape='X'):
        super().__init__(shape)
        self.name = name

    def next_move(self):
        """Ask human player for its next move coordinates.

        :return: int, int representing 2D board coordinates.
        """
        next_move = input()
        x, y = next_move.split(',')
        return x, y
