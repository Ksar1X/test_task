from tests.singleton import Singleton


class TestSingleton():

    def test_singleton(self):
        s1 = Singleton()
        s2 = Singleton()

        assert id(s1) == id(s2)