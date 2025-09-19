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

    @mock.patch("ping3.ping", mock.Mock(side_effect=[1.234]))
    def test_ping(self):
        self.assertEqual(self.peer.ping(), 1.234)


if __name__ == "__main__":
    main()
