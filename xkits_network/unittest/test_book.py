# coding:utf-8

from unittest import TestCase
from unittest import main  # noqa:H306

from xkits_network.book import IP64Book


class TestIP64Book(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.ip64: IP64Book[str] = IP64Book()
        self.ip64["127.0.0.1"] = "localhost"

    def tearDown(self):
        pass

    def test_get(self):
        self.assertRaises(KeyError, lambda: self.ip64["192.168.0.1"])
        self.assertEqual(self.ip64["127.0.0.1"], "localhost")
        self.ip64.update("127.0.0.1", "unittest")
        self.assertEqual(self.ip64["127.0.0.1"], "unittest")
        self.ip64.setdefault("127.0.0.1", "demo")
        self.assertEqual(self.ip64["127.0.0.1"], "unittest")
        self.assertEqual(len(self.ip64), 1)
        self.assertNotIn("192.168.0.1", self.ip64)
        self.assertIn("127.0.0.1", self.ip64)

    def test_iter(self):
        ip64: IP64Book[int] = IP64Book()
        ip64["192.168.0.1"] = 2
        ip64["192.168.1.1"] = 3
        ip64["127.0.0.1"] = 1
        ip64["0.0.0.0"] = 0

        for i, v in enumerate(ip64):
            self.assertEqual(i, v)


if __name__ == "__main__":
    main()
