import lab05 as lab05
import unittest
from unittest.mock import patch
from io import StringIO


class TestLabFunctions(unittest.TestCase):

    def test_play_again_returns_True(self):

        user_input = ["YeS"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.play_again()
                self.assertTrue(
                    results, "When input is yes the function should return True")

    def test_play_again_returns_False_with_N_or_NO(self):

        user_input = ["nO"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.play_again()
                self.assertFalse(
                    results, "When input is No play_again should return False")

    def test_play_again_warns_user_with_bad_input(self):

        user_input = ["incorrect", "nO"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.play_again()
                self.assertFalse(
                    results, "When input is no the play_again should return False")
                l = es
        self.assertIn("try again", l.getvalue().lower(
        ), "Bad input should be followed with an error with at least Please Try again in it.")

    def test_play_again_works_with_multiple_bad_inputs(self):

        user_input = ["chiefs", "incorrect", "nO"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.play_again()
                self.assertFalse(
                    results, "play_again should return False when given 2 incorrect inputs and then no")

    def test_get_wager_returns_wager_amount(self):

        user_input = ["30"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.get_wager(200)
                self.assertEqual(
                    30, results, "getWager should return 30 when the user enters 30")

    def test_get_wager_returns_wager_amount_after_negative(self):

        user_input = ["-5", "45"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.get_wager(200)
                self.assertEqual(
                    45, results, "getWager should return 45 when the user enters -5, 30")

    def test_get_wager_returns_wager_amount_after_negative(self):

        user_input = ["-5", "45"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.get_wager(200)
                self.assertEqual(
                    45, results, "getWager should return 45 when the user enters -5, 30")
                l = es

    def test_get_wager_returns_wager_amount_after_too_high_value(self):

        user_input = ["105", "22"]
        with patch('sys.stdout', new_callable=StringIO) as es:
            with patch('builtins.input', side_effect=user_input):
                results = lab05.get_wager(30)
                self.assertEqual(
                    22, results, "getWager should return 22 when the user enters 105, 22, and the bank is less than 105")
                l = es

    def test_get_slot_results_returns_a_tuple_of_integers(self):

        results = lab05.get_slot_results()
        self.assertIsInstance(
            results, tuple, "get_slot_results should return a tuple")
        self.assertEqual(
            3, len(results), "get_slot_results shoudl return 3 items")
        self.assertIsInstance(
            results[0], int, "Item at index 0 was not an integer")
        self.assertIsInstance(
            results[1], int, "Item at index 1 was not an integer")
        self.assertIsInstance(
            results[2], int, "Item at index 2 was not an integer")

    def test_get_matches_returns_correct_number_of_matches(self):

        results = lab05.get_matches(3, 3, 3)
        self.assertEqual(
            3, results, "get_matches returns 3 when given 3 matching values")
        results = lab05.get_matches(4, 4, 4)
        self.assertEqual(
            3, results, "get_matches returns 3 when given 3 matching values")
        results = lab05.get_matches(4, 4, 5)
        self.assertEqual(
            2, results, "get_matches returns 2 when given 2 matching values")
        results = lab05.get_matches(8, 4, 4)
        self.assertEqual(
            2, results, "get_matches returns 2 when given 2 matching values")
        results = lab05.get_matches(8, 4, 8)
        self.assertEqual(
            2, results, "get_matches returns 2 when given 2 matching values")
        results = lab05.get_matches(8, 4, 3)
        self.assertEqual(
            0, results, "get_matches returns 0 when given 0 matching values")

    def test_get_payout_returns_correct_results(self):

        results = lab05.get_payout(3, 0)
        self.assertEqual(-3, results,
                         "get_payout returns -3 when given 3 and no matches.")
        results = lab05.get_payout(2, 3)
        self.assertEqual(
            20, results, "get_payout returns 20 when given 2 and 3 matches.")
        results = lab05.get_payout(5, 2)
        self.assertEqual(
            15, results, "get_payout returns 15 when given 5 and 2 matches.")


if __name__ == "__main__":
    __unittest = True
    unittest.main()
