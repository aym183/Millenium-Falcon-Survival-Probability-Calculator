import unittest
from main import Main

# Classes containing unit tests that validates the entire program

# Tests for origin with Dagobah
class Dagobah(unittest.TestCase):

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

    def test_four(self):

        autonomy = 6
        departure = "Dagobah"
        arrival = "Endor"
        countdown = 10
        bounty_hunters = [
        {"planet": "Hoth", "day": 6 }
        ]
        result = Main(departure, arrival, autonomy, bounty_hunters, countdown)
        self.assertEqual(result.run_method(), 90)

# Tests for origin with Tatooine
class TestTatooine(unittest.TestCase):

    def test_one(self):
        autonomy = 6
        departure = "Tatooine"
        arrival = "Endor"
        countdown = 7
        bounty_hunters = [
        {"planet": "Hoth", "day": 6 }, 
        {"planet": "Hoth", "day": 7 },
        {"planet": "Hoth", "day": 8 }
        ]

        result = Main(departure, arrival, autonomy, bounty_hunters, countdown)
        self.assertEqual(result.run_method(), 81)


    def test_two(self):
        autonomy = 6
        departure = "Tatooine"
        arrival = "Endor"
        countdown = 8
        bounty_hunters = [
        {"planet": "Hoth", "day": 6 }, 
        {"planet": "Hoth", "day": 7 },
        {"planet": "Hoth", "day": 8 }
        ]

        result = Main(departure, arrival, autonomy, bounty_hunters, countdown)
        self.assertEqual(result.run_method(), 73)

    def test_three(self):

        autonomy = 6
        departure = "Tatooine"
        arrival = "Endor"
        countdown = 10
        bounty_hunters = [
        {"planet": "Hoth", "day": 6 }
        ]
        
        result = Main(departure, arrival, autonomy, bounty_hunters, countdown)
        self.assertEqual(result.run_method(), 90)

# Tests for origin with Hoth
class Hoth(unittest.TestCase):

    def test_one(self):
        autonomy = 6
        departure = "Hoth"
        arrival = "Endor"
        countdown = 8
        bounty_hunters = [
        {"planet": "Hoth", "day": 6 }, 
        {"planet": "Hoth", "day": 7 },
        {"planet": "Hoth", "day": 8 }
        ]

        result = Main(departure, arrival, autonomy, bounty_hunters, countdown)
        self.assertEqual(result.run_method(), 81)


    def test_two(self):
        autonomy = 7
        departure = "Hoth"
        arrival = "Endor"
        countdown = 9
        bounty_hunters = [
        {"planet": "Hoth", "day": 6 }
        ]

        result = Main(departure, arrival, autonomy, bounty_hunters, countdown)
        self.assertEqual(result.run_method(), 90)

if __name__ == "__main__":
    unittest.main()