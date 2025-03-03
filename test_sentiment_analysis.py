from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        test1 = sentiment_analyzer('I love this course')
        self.assertEqual(test1['label'], 'SENT_POSITIVE')

        test2 = sentiment_analyzer('I hate working with Coursera')
        self.assertEqual(test2['label'], 'SENT_NEGATIVE')

        test3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(test3['label'], 'SENT_NEUTRAL')

unittest.main()