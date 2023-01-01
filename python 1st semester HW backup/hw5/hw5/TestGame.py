from unittest import TestCase
from Board import Board
from Hand import Hand
from MaxScorePlayer import MaxScorePlayer
from NaivePlayer import NaivePlayer
from Domino import Domino
from Team import Team
from Game import Game
from RandomPlayer import RandomPlayer


class TestGame(TestCase):
    def test_play(self):
        # game 1
        board1 = Board(28)
        domino1 = Domino(2, 5)
        domino2 = Domino(4, 2)
        domino3 = Domino(6, 6)
        domino4 = Domino(2, 5)
        domino5 = Domino(2, 2)
        domino6 = Domino(1, 5)
        hand1 = Hand([domino1, domino2, domino3])
        hand2 = Hand([domino4, domino5, domino6])
        maxplayer1 = NaivePlayer('susu', 88, hand1)
        maxplayer2 = MaxScorePlayer('ali', 102, hand2)
        team11 = Team('Beit avot beitjan', [maxplayer1])
        team22 = Team('Beit avot jenin', [maxplayer2])
        thegame = Game(board1, team11, team22)
        self.assertEqual(thegame.play(), "Team Beit avot jenin wins Team Beit avot beitjan")
        # game 2
        board1 = Board(28)
        domino1 = Domino(2, 5)
        domino2 = Domino(4, 2)
        domino3 = Domino(6, 6)
        domino4 = Domino(2, 6)
        domino5 = Domino(2, 2)
        domino6 = Domino(1, 5)
        hand1 = Hand([domino1, domino2, domino3])
        hand2 = Hand([domino4, domino5, domino6])
        maxplayer1 = NaivePlayer('susu', 88, hand1)
        maxplayer2 = MaxScorePlayer('ali', 102, hand2)
        team11 = Team('Beit avot beitjan', [maxplayer1])
        team22 = Team('Beit avot jenin', [maxplayer2])
        thegame = Game(board1, team11, team22)
        self.assertEqual(thegame.play(), "Draw!")
        # game 3
        board1 = Board(28)
        domino1 = Domino(2, 5)
        domino2 = Domino(4, 2)
        domino3 = Domino(2, 6)
        domino4 = Domino(2, 6)
        domino5 = Domino(2, 2)
        domino6 = Domino(1, 5)
        hand1 = Hand([domino1, domino2, domino3])
        hand2 = Hand([domino4, domino5, domino6])
        maxplayer1 = NaivePlayer('susu', 88, hand1)
        maxplayer2 = NaivePlayer('ali', 102, hand2)
        team11 = Team('Beit avot beitjan', [maxplayer1])
        team22 = Team('Beit avot jenin', [maxplayer2])
        thegame = Game(board1, team11, team22)
        self.assertEqual(thegame.play(), "Team Beit avot beitjan wins Team Beit avot jenin")
        # game 4
        board1 = Board(28)
        domino1 = Domino(1, 2)
        domino2 = Domino(1, 4)
        domino3 = Domino(6, 6)
        domino4 = Domino(2, 1)
        domino5 = Domino(4, 6)
        domino6 = Domino(5, 5)
        hand1 = Hand([domino1, domino2, domino3])
        hand2 = Hand([domino4, domino5, domino6])
        maxplayer1 = NaivePlayer('susu', 88, hand1)
        maxplayer2 = NaivePlayer('ali', 102, hand2)
        team11 = Team('Beit avot beitjan', [maxplayer1])
        team22 = Team('Beit avot jenin', [maxplayer2])
        thegame = Game(board1, team11, team22)
        self.assertEqual(thegame.play(), "Team Beit avot beitjan wins Team Beit avot jenin")
        # game 5
        board1 = Board(28)
        domino1 = Domino(1, 1)
        domino2 = Domino(2, 3)
        domino3 = Domino(4, 4)
        domino4 = Domino(1, 2)
        domino5 = Domino(3, 6)
        domino6 = Domino(4, 4)
        hand1 = Hand([domino1, domino2, domino3])
        hand2 = Hand([domino4, domino5, domino6])
        maxplayer1 = NaivePlayer('susu', 88, hand1)
        maxplayer2 = NaivePlayer('ali', 102, hand2)
        team11 = Team('Beit avot beitjan', [maxplayer1])
        team22 = Team('Beit avot jenin', [maxplayer2])
        thegame = Game(board1, team11, team22)
        self.assertEqual(thegame.play(), "Draw!")
        # game 6
        board1 = Board(28)
        domino1 = Domino(1, 1)
        domino2 = Domino(2, 3)
        domino3 = Domino(4, 4)
        domino4 = Domino(6, 6)
        domino5 = Domino(1, 2)
        domino6 = Domino(3, 6)
        domino7 = Domino(4, 4)
        domino8 = Domino(6, 3)
        hand1 = Hand([domino1, domino2])
        hand2 = Hand([domino3, domino4])
        hand3 = Hand([domino5, domino6])
        hand4 = Hand([domino7, domino8])
        maxplayer1 = NaivePlayer('susu', 88, hand1)
        maxplayer2 = NaivePlayer('ali', 102, hand2)
        maxplayer3 = NaivePlayer('baba', 102, hand3)
        maxplayer4 = NaivePlayer('gaga', 102, hand4)
        team11 = Team('Beit avot beitjan', [maxplayer1, maxplayer2])
        team22 = Team('Beit avot jenin', [maxplayer3, maxplayer4])
        thegame = Game(board1, team11, team22)
        self.assertEqual(thegame.play(), "Team Beit avot jenin wins Team Beit avot beitjan")

    def test_aa(self):
        try:
            from Team import Team
            from RandomPlayer import RandomPlayer
            from MaxScorePlayer import MaxScorePlayer
            from NaivePlayer import NaivePlayer
            list_hands = randomized_hands(7)
            p1 = MaxScorePlayer("Taylor Swift", 28, list_hands[0])
            p2 = RandomPlayer("Kanye West", 44, list_hands[1])
            p3 = NaivePlayer("Kim Kardashian", 41, list_hands[2])
            p4 = NaivePlayer("Beyonce", 40, list_hands[3])
            t1 = Team("Blue", [p1, p2, p3, p4])
            players = t1.get_team()
            players[0].name = "Error"
            self.assertNotEqual("Error", t1.get_team()[0].name)
        except:
            self.fail()
