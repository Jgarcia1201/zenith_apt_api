import unittest

from repository.complexRepo import score_complex, get_top_five

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

top_five_test_in = [
    {
        "score": 10
    },
    {
        "score": 15
    },
    {
        "score": 30
    },
    {
        "score": 5
    },
    {
        "score": 15
    },
    {
        "score": 0
    },
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

    def test_top_five(self):
        # Valid
        self.assertEqual(get_top_five(top_five_test_in), [{'score': 30}, {'score': 15}, {'score': 15}, {'score': 10},
                                                          {'score': 5}])
        # Empty Array
        self.assertEqual(get_top_five([]), [])
        # Array Shorter Than 5
        self.assertEqual(get_top_five(top_five_test_in[0:3]), [{'score': 30}, {'score': 15}, {'score': 10}])
        # Score Attribute Missing From A Dictionary
        self.assertEqual(get_top_five([{'score': 30}, {'score': 15}, {}]), [{'score': 30}, {'score': 15}])


