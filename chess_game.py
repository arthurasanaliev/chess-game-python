class ChessGame:
    def __init__(self):
        self.board = Board()
        self.player1 = Player('Artur', 'White')
        self.player2 = Player('Aidar', 'Black')
        self.current_player = self.player1
        
    def play(self):
        pass
    
    def is_game_over(self):
        pass
    
    def switch_players(self):
        pass
    
    def print_board(self):
        pass
    
    def make_move(self, move):
        pass
    
    def is_valid_move(self, move):
        pass
    
    def is_check(self, player):
        pass
    
    def is_checkmate(self, player):
        pass
    
    def is_stalemate(self, player):
        pass