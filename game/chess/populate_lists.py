# populate_lists
def run(self):
	# Single player menu
	if not self.is_two_player:
		# Sidebar buttons
		self.sidebar_buttons.append(["sidebar_undo.png", "Undo Move", "sidebar_undo"])
		# self.sidebar_buttons.append(["sidebar_default.png", "Help", "help"])
		# self.sidebar_buttons.append(["sidebar_default.png", "Quick Help", "quick_help"])

		# After game options
		self.aftergame_options.append(["Undo Last Move", "endgame_undo"])
		self.aftergame_options.append(["Play Again", "endgame_play_again"])

	# Sidebar buttons
	self.sidebar_buttons.append(["sidebar_forfeit.png", "Forfeit", "sidebar_forfeit"])
	
	# After game options
	self.aftergame_options.append(["Review Game", "endgame_undo"])
	self.aftergame_options.append(["Main Menu", "endgame_main_menu"])

	# Game over
	self.is_game_over = {
		'in_game': False,
		'promoting': False,
		'user_check': False,
		'opponent_check': False,
		'is_forfeitting': False,
		'forfeit': True,
		'stalemate': True,
		'50_move_rule': True,
		'user_checkmate': True,
		'opponent_checkmate': True,
		'opponent_forfeited': True
	}