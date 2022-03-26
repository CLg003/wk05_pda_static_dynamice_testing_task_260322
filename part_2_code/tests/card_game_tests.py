import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card("Hearts", 9)
        self.card_2 = Card("DIamonds", 10)
        self.card_3 = Card("Spades", 1)
        self.cards = [self.card_1, self.card_2, self.card_3]
        self.card_game = CardGame()

    def test_card_is_not_ace(self):
        result = self.card_game.check_for_ace(self.card_1)
        self.assertEqual(False, result)

    def test_card_is_ace(self):
        result = self.card_game.check_for_ace(self.card_3)
        self.assertEqual(True, result)

    def test_card_1_is_highest_card(self):
        result = self.card_game.highest_card(self.card_1, self.card_3)
        self.assertEqual(self.card_1, result)

    def test_card_2_is_highest_card(self):
        result = self.card_game.highest_card(self.card_1, self.card_2)
        self.assertEqual(self.card_2, result)

    def test_cards_total(self):
        result = self.card_game.cards_total(self.cards)
        self.assertEqual("You have a total of 20", result)


    

    @unittest.skip("delete this line to run the test")
    def test_card_has_suit(self):
        self.assertEqual("Hearts", self.card_1.suit)

    @unittest.skip("delete this line to run the test")
    def test_card_has_value(self):
        self.assertEqual(1, self.card_2.value)