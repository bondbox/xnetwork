# coding:utf-8

from unittest import TestCase
from unittest import main  # noqa:H306
from unittest import mock

from xkits_network.inet import Peer


class TestPeer(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.peer = Peer.from_string("127.0.0.1")

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @mock.patch("ping3.ping", mock.Mock(side_effect=[0.0, 1.234, -1.0]))
    def test_ping(self):
        generator = self.peer.ping(count=3)
        self.assertEqual(next(generator), 1.234)
        self.assertRaises(StopIteration, next, generator)

    def test_ping_once(self):
        with mock.patch("ping3.ping", mock.Mock(side_effect=[0.0, -1.0, 1.234])):  # noqa:E501
            self.assertEqual(self.peer.ping_once(), 1.234)

        with mock.patch("ping3.ping", mock.Mock(side_effect=[-1.0, 0.0, -2.0])):  # noqa:E501
            self.assertEqual(self.peer.ping_once(retries=3), -self.peer.timeout)  # noqa:E501


if __name__ == "__main__":
    main()
