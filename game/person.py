


class Jumper:
    '''Creates and returns the main character
    '''
    def __init__(self):
        self.parachute = ['''
                         __
                        |  |
                        \  /
                        \ /
                         O
                        /|\|
                        / \|
                        ''', 
                        '''
                        |  |
                        \  /
                        \ /
                         O
                        /|\|
                        / \|
                        ''', 
                        '''
                        \  /
                        \ /
                         O
                        /|\|
                        / \|
                        ''',
                        '''
                        \ /
                         O
                        /|\|
                        / \|
                        ''',
                        '''
                         X
                        /|\|
                        / \|
                        '''
        ]

    def set_parachute(self):
        self.parachute.pop(0)
        
    def get_parachute(self):
        return self.parachute[0]