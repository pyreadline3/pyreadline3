
import unittest


class TestsMisc (unittest.TestCase):

    def test_doc_str(self):
        import readline

        assert "Widnows" in readline.__doc__
