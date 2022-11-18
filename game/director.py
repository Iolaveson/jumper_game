from game.terminal_service import TerminalService
from game.person import Jumper
from game.word import Word

class Director:

    def __init__(self):
        
        self._jumper = Jumper()
        self._word = Word()
        self._is_playing = True
        self._terminal_service = TerminalService()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._update()
            self._results()


    def _get_inputs(self):

        guess = self._terminal_service.read_text('Guess a letter: ')
        self._word._check_guess(guess)

    def _update(self):

        if self._word._check_guess is False:
            self._jumper.set_parachute()
        
        
        

    def _results(self):

        if self._word is True:
            self._terminal_service.write_text('That letter is correct')
        else:
            self._terminal_service.write_text('Sorry that letter is not part of this word.')
        
        self._terminal_service.write_text(self._jumper.get_parachute())


        if self._word._completed_word():
            self._terminal_service.write_text('You got it!')
            self._terminal_service.write_text(self._word._completed_word())
            self._is_playing = False
