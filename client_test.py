import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    # Testing getDataPoint method
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            expected = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                        (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
            actual = getDataPoint(quote)
            self.assertEqual(expected, actual)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            expected = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                        (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
            actual = getDataPoint(quote)
            self.assertEqual(expected, actual)

    def test_getDataPoint_calculatePriceBidIsNegative(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': -120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': -117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            expected = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                        (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
            actual = getDataPoint(quote)
            self.assertEqual(expected, actual)

    def test_getDataPoint_calculatePriceBidIsMillions(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 2000700, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 10009000, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            expected = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                        (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
            actual = getDataPoint(quote)
            self.assertEqual(expected, actual)

    def test_getDataPoint_calculatePriceBidEqualAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 119.2, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 121.68, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            expected = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                        (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
            actual = getDataPoint(quote)
            self.assertEqual(expected, actual)

    # Testing getRatio method
    def test_getRatio_calculateBothPrice_aAndPrice_bAreGreaterThanZero(self):
        price_a = 543.20
        price_b = 632.90

        self.assertEqual(getRatio(price_a, price_b), price_a / price_b)

    def test_getRatio_calculatePrice_bIsZero(self):
        price_a = 543.20
        price_b = 0.00

        self.assertEqual(getRatio(price_a, price_b), None)

    def test_getRatio_calculateEitherPrice_aOrPrice_bIsNegative(self):
        price_a = 543.20
        price_b = -632.90

        self.assertEqual(getRatio(price_a, price_b), price_a / price_b)


if __name__ == '__main__':
    unittest.main()
