
class EmptyBoardException(Exception):
    pass


class FullBoardException(Exception):
    pass


class NoSuchDominoException(Exception):
    pass


class InvalidNumberException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return 'ERROR' + ' ' + self.msg

