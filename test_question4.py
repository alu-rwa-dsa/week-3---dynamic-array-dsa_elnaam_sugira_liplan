import unittest
from question4 import asso_list


class TestQuestion4(unittest.TestCase):
    def test_first(self):
        p = asso_list()
        self.assertEqual(p.add("liplan", 19, "CSS", "UTf"), {'name': 'liplan', 'age': 20, 'major': 'CSS', 'country': 'KE'})

    def test_second(self):
        p = asso_list()
        p.add("liplan", 19, "CSS", "KE")
        self.assertEqual(p.a_remove("age"), {'name': 'liplan', 'major': 'CSS', 'country': 'KE'})

    def test_third(self):
        p = asso_list()
        p.add("liplan", 19, "CSS", "KE")
        self.assertEqual(p.a_modify("liplan", "CSS", "KE"), {'name': 'liplan', 'age' : 19, 'major': 'CSS', 'country': 'KE'})

    def test_fourth(self):
        p = asso_list()
        p.add("liplan", 89, "19", "KE")
        self.assertEqual(p.a_lookup("age"), "not found")


    if __name__ == "__main__":
        unittest.main()
