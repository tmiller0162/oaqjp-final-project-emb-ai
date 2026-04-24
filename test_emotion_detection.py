import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion(self):
        test1_text = "I am glad this happened"
        test2_text = "I am really mad about this"
        test3_text = "I feel disgusted just hearing about this"
        test4_text = "I am so sad about this"
        test5_text = "I am really afraid that this will happen"

        test1 = emotion_detector(test1_text)["dominant_emotion"]
        test2 = emotion_detector(test2_text)["dominant_emotion"]
        test3 = emotion_detector(test3_text)["dominant_emotion"]
        test4 = emotion_detector(test4_text)["dominant_emotion"]
        test5 = emotion_detector(test5_text)["dominant_emotion"]

        self.assertEqual(test1, "joy")
        self.assertEqual(test2, "anger")
        self.assertEqual(test3, "disgust")
        self.assertEqual(test4, "sadness")
        self.assertEqual(test5, "fear")

unittest.main()
