import unittest
from main import Main

class TestTatooine(unittest.TestCase):

    def test_one(self):
        autonomy = 6
        departure = "Dagobah"
        arrival = "Endor"
        countdown = 9
        bounty_hunters = [
        {"planet": "Hoth", "day": 6 }, 
        {"planet": "Hoth", "day": 7 },
        {"planet": "Hoth", "day": 8 }
        ]

        result = Main(departure, arrival, autonomy, bounty_hunters, countdown)

        self.assertEqual(result.run_method(), 0)


    def test_two(self):
        autonomy = 6
        departure = "Dagobah"
        arrival = "Endor"
        countdown = 6
        bounty_hunters = [
        {"planet": "Hoth", "day": 6 }, 
        {"planet": "Hoth", "day": 7 },
        {"planet": "Hoth", "day": 8 }
        ]

        result = Main(departure, arrival, autonomy, bounty_hunters, countdown)

        self.assertEqual(result.run_method(), 0)

    def test_three(self):

        autonomy = 6
        departure = "Dagobah"
        arrival = "Endor"
        countdown = 10
        bounty_hunters = [
        {"planet": "Hoth", "day": 6 }, 
        {"planet": "Hoth", "day": 7 },
        {"planet": "Hoth", "day": 8 }
        ]
        result = Main(departure, arrival, autonomy, bounty_hunters, countdown)

        self.assertEqual(result.run_method(), 73)

    def test_three(self):

        autonomy = 6
        departure = "Dagobah"
        arrival = "Endor"
        countdown = 10
        bounty_hunters = [
        {"planet": "Hoth", "day": 6 }
        ]
        result = Main(departure, arrival, autonomy, bounty_hunters, countdown)

        self.assertEqual(result.run_method(), 90)

# class Dagobah(unittest.TestCase):

# class Endor(unittest.TestCase):

# class Hoth(unittest.TestCase):


if __name__ == "__main__":
    unittest.main()