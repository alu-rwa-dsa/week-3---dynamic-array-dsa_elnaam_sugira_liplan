import unittest
from question4 import asso_list


class TestQuestion4(unittest.TestCase):
    def test_first(self):
        p = asso_list()
        self.assertEqual(p.add("meonly", 19, "CSS", "UTK"), {'name': 'meonly', 'age': 19, 'major': 'CSS', 'country': 'UTK'})

    def test_second(self):
        p = asso_list()
        p.add("meonly", 19, "CSS", "UTK")
        self.assertEqual(p.a_remove("age"), {'name': 'meonly', 'major': 'CSS', 'country': 'UTK'})

    def test_third(self):
        p = asso_list()
        p.add("meonly", 19, "CSS", "UTK")
        self.assertEqual(p.a_modify("meonly2", "CSS", "UTK"), {'name': 'meonly2', 'age' : 19, 'major': 'CSS', 'country': 'UTK'})

    def test_fourth(self):
        p = asso_list()
        p.add("meonly", 89, "19", "UTK")
        self.assertEqual(p.a_lookup("age"), "not found")


    if __name__ == "__main__":
        unittest.main()
