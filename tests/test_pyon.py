import unittest
import pyon

class TestPyon(unittest.TestCase):
    def test_decode_value(self):
        self.assertEqual(pyon.decode_value("true"), True)
        self.assertEqual(pyon.decode_value("false"), False)
        self.assertEqual(pyon.decode_value("null"), None)
        self.assertEqual(pyon.decode_value("42"), 42)
        self.assertEqual(pyon.decode_value("[1,2,3]"), [1, 2, 3])
        self.assertEqual(pyon.decode_value("{a:1,b:2}"), {"a": 1, "b": 2})

    def test_encode_value(self):
        self.assertEqual(pyon.encode_value(True), "true")
        self.assertEqual(pyon.encode_value(False), "false")
        self.assertEqual(pyon.encode_value(None), "null")
        self.assertEqual(pyon.encode_value(42), "42")
        self.assertEqual(pyon.encode_value([1, 2, 3]), "[1,2,3]")
        self.assertEqual(pyon.encode_value({"a": 1, "b": 2}), "{a:1,b:2}")

if __name__ == "__main__":
    unittest.main()