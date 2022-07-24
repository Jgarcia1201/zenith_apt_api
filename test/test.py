import unittest

from repository.complexController import score_complex

test_client = {
        'name': 'James',
        'email': 'james@james.com',
        'lux_score': 7,
        'liv_score': 5,
        'rent_min': 1200,
        'rent_max': 1700,
        "pets": True,
        "desiredBr": 1
    }

test_complexes = [
    {
        'name': "Luxury Condos",
        'address': "1212 Kanah ln",
        'lux_score': 8,
        'liv_score': 4
    },
    {
        'name': "Luxury Condos",
        'address': "1212 Kanah ln",
        'lux_score': 7,
        'liv_score': 5
    },
    {
        'name': "Luxury Condos",
        'address': "1212 Kanah ln",
        'lux_score': 5,
        'liv_score': 7,
    },
    {
        'name': "Luxury Condos",
        'address': "1212 Kanah ln",
        'lux_score': 4,
        'liv_score': 8,
    }
]


class TestApi(unittest.TestCase):

    def test_scoring(self):
        # Valid One Off
        self.assertEqual(score_complex(test_complexes[0], test_client), 20)
        # Null
        self.assertEqual(score_complex({}, {}), 0)
        # Valid Spot On
        self.assertEqual(score_complex(test_complexes[1], test_client), 30)
        # Valid Two Off
        self.assertEqual(score_complex(test_complexes[2], test_client), 10)
        # Valid Three Off
        self.assertEqual(score_complex(test_complexes[3], test_client), 0)
