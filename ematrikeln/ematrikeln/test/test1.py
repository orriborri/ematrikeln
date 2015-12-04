import unittest
from django.test import Client

class randomTest(unittest.TestCase):
    def testRandomTest(self):
        self.assertTrue(True,'This should always be true')
class testView(unittest.TestCase):
    def test_get_root(self):
        c = Client()
        response = c.get("/")
        self.assertEqual(response.status_code, 200)
    def test404(self):
        c = Client()
        response = c.get("/random")
        self.assertEqual(response.status_code, 404)
    def test_newMember(self):
        c = Client()
        member = {
                "firstName":"name",
                "lastName":"lastname",
                "address":"street and number 1",
                "city": "city",
                "postcode": "00000",
                "phonenumber": "010123456",
                "gymnasium": "Lovisa Gymnasium",
                "hometown":"derp",
                "school": "herp",
                "study": "serp",
                "active": "true",
                "checkbox": "true",
                "graduerad": "true"
                }
        response = c.post("/new_member/",member)
        self.assertEqual(response.status_code, 200)
    def test_newMember(self):
        c = Client(enforce_csrf_checks=True)
        member = {
                "firstName":"name",
                "lastName":"lastname",
                "address":"street and number 1",
                "city": "city",
                "postcode": "00000",
                "phonenumber": "010123456",
                "gymnasium": "Lovisa Gymnasium",
                "hometown":"derp",
                "school": "herp",
                "study": "serp",
                "active": "true",
                "checkbox": "true",
                "graduerad": "true"
                }
        response =  c.post("/new_member/",member)
        self.assertEqual(response.status_code, 500)
    def test_newMember(self):
        c = Client()
        response = c.get("/new_member/")
        self.assertEqual(response.status_code,404)
if __name__ == '__main__':
    unittest.main()
