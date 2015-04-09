from tile import *
from stack import *
from constants import *
import pygame

def run(self, screen, is_player_white, cpu_level, fen_string):
	# Move piece animations
	self.animate = True

	# Avatars and names
	self.image_file_user = "res/avatars/dragonite_sample.png"
	self.image_file_opp = "res/avatars/stockfish_sample.png"
	self.name_opp = "Stockfish"
	self.name_user = "Player"

	# Captured pieces
	self.user_captured = Stack()
	self.opponent_captured = Stack()

	# Player color specifics
	self.is_player_white = is_player_white
	self.goal_rank = 7 if self.is_player_white else 0

	# Initialize the board and the stack
	self.board = [[Tile() for i in range(8)] for i in range(8)]
	self.stack = Stack()

	# HP bars
	self.user_hp_max = 40
	self.user_hp_current = 40
	self.user_hp_current_before = 40
	self.opponent_hp_max = 40
	self.opponent_hp_current = 40
	self.opponent_hp_current_before = 40

	# Important attributes for the FEN notation
	self.active_turn = 'w'
	self.kingside_white = 'K'
	self.kingside_black = 'k'
	self.queenside_white = 'Q'
	self.queenside_black = 'q'
	self.en_passant = '-'
	self.is_undergoing_promotion = False
	self.halfmove_clock = 0
	self.fullmove_clock = 1

	# Set up the board given the fen_string
	self.convert_fen_to_board(fen_string, True)

	# Game Window information
	self.clock = pygame.time.Clock()

	# Source move
	self.source_x = 0
	self.source_y = 0

	# Stockfish
	self.cpu_level = cpu_level

	# Board stuff
	self.is_board_clickable = True
	self.temp_board = [[Tile() for i in range(8)] for i in range(8)]
	self.currmove_source_x = 0
	self.currmove_source_y = 0
	self.currmove_destination_x = 0
	self.currmove_destination_y = 0
	self.last_source_x = 0
	self.last_source_y = 0
	self.last_destination_x = 0
	self.last_destination_y = 0

	# Right panel buttons
	self.promotions = {}

	# Debug mode: Disables opponent's moves
	self.debug_mode = False

	# Sidebar buttons
	self.sidebar_buttons = []
	self.aftergame_options = []
	self.populate_sidebar()

	# Checks and checkmate
	self.is_stalemate = False
	self.is_user_check = False
	self.is_50_move_rule = False
	self.is_user_checkmate = False
	self.is_opponent_check = False
	self.is_opponent_checkmate = False
	self.is_game_over = False

	self.screen = screen
	pygame.display.flip()