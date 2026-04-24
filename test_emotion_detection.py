import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion(self):
        test1 = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(test1, "joy")

unittest.main()
