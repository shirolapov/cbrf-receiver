import unittest
from datetime import datetime
from cbrf_receiver import get_value, get_values


class TestCBRFReceiverMethods(unittest.TestCase):
    def test_in_past_one_valute(self):
        date = datetime(year=2011, day=23, month=2)

        self.assertEqual(get_value("USD", date), 29.2859)
        self.assertEqual(get_value("EUR", date), 39.6795)
        self.assertEqual(get_value("NOK", date), 5.0995)
        self.assertEqual(get_value("PLN", date), 9.99928)

    def test_in_past_more_valute(self):
        date = datetime(year=2011, day=23, month=2)

        self.assertEqual(get_values(["USD", "EUR"], date),
                         [{'Value': 29.2859, 'CharCode': 'USD'}, {'Value': 39.6795, 'CharCode': 'EUR'}])
        self.assertEqual(get_values(["KZT", "LVL"], date),
                         [{'Value': 0.200321, 'CharCode': 'KZT'}, {'Value': 56.2866, 'CharCode': 'LVL'}])
        self.assertEqual(get_values(["MDL"], date),
                         [{'Value': 2.42785, 'CharCode': 'MDL'}])

    def test_all_courese_one_by_one(self):
        date = datetime(year=2014, day=15, month=7)

        self.assertEqual(get_value("AUD", date), 32.2444)  # 1 Австралийский доллар
        self.assertEqual(get_value("AZN", date), 43.8063)  # 2 Азербайджанский манат
        self.assertEqual(get_value("GBP", date), 58.7550)  # 3 Фунт стерлингов Соединенного королевства
        self.assertEqual(get_value("AMD", date), 0.0841017)  # 4 Армянских драмов
        self.assertEqual(get_value("BYR", date), 0.00335093)  # 5 Белорусских рублей
        self.assertEqual(get_value("BGN", date), 23.9035)  # 6 Болгарский лев
        self.assertEqual(get_value("BRL", date), 15.4503)  # 7 Бразильский реал
        self.assertEqual(get_value("HUF", date), 0.150961)  # 8 Венгерских форинтов
        self.assertEqual(get_value("DKK", date), 6.27028)  # 9 Датских крон
        self.assertEqual(get_value("USD", date), 34.3135)  # 10 Доллар США
        self.assertEqual(get_value("EUR", date), 46.6835)  # 11 Евро
        self.assertEqual(get_value("INR", date), 0.571796)  # 12 Индийских рупий
        self.assertEqual(get_value("KZT", date), 0.186984)  # 13 Казахстанских тенге
        self.assertEqual(get_value("CAD", date), 31.9403)  # 14 Канадский доллар
        self.assertEqual(get_value("KGS", date), 0.662743)  # 15 Киргизских сомов
        self.assertEqual(get_value("CNY", date), 5.52971)  # 16 Китайских юаней
        self.assertEqual(get_value("LTL", date), 13.5396)  # 17 Литовский лит
        self.assertEqual(get_value("MDL", date), 2.45009)  # 18 Молдавских леев
        self.assertEqual(get_value("NOK", date), 5.55855)  # 19 Норвежских крон
        self.assertEqual(get_value("PLN", date), 11.2951)  # 20 Польский злотый
        self.assertEqual(get_value("RON", date), 10.5801)  # 21 Румынский лей
        self.assertEqual(get_value("XDR", date), 53.0178)  # 22 СДР (специальные права заимствования)
        self.assertEqual(get_value("SGD", date), 27.6722)  # 23 Сингапурский доллар
        self.assertEqual(get_value("TJS", date), 6.83359)  # 24 Таджикских сомони
        self.assertEqual(get_value("TRY", date), 16.1894)  # 25 Турецкая лира
        self.assertEqual(get_value("TMT", date), 12.0386)  # 26 Новый туркменский манат
        self.assertEqual(get_value("UZS", date), 0.0149421)  # 27 Узбекских сумов
        self.assertEqual(get_value("UAH", date), 2.92154)  # 28 Украинских гривен
        self.assertEqual(get_value("CZK", date), 1.704)  # 29 Чешских крон
        self.assertEqual(get_value("SEK", date), 5.05554)  # 30 Шведских крон
        self.assertEqual(get_value("CHF", date), 38.4983)  # 31 Швейцарский франк
        self.assertEqual(get_value("ZAR", date), 3.1968)  # 32 Южноафриканских рэндов
        self.assertEqual(get_value("KRW", date), 0.033682)  # 33 Вон Республики Корея
        self.assertEqual(get_value("JPY", date), 0.338097)  # 34 Японских иен

    def test_all_course_in_one_request(self):
        date = datetime(year=2006, day=15, month=10)

        self.assertEqual(get_values(["AUD", "GBP", "BYR", "DKK", "USD",
                                     "EUR", "ISK", "KZT", "CAD", "CNY",
                                     "NOK", "XDR", "SGD", "TRY", "UAH",
                                     "SEK", "CHF", "JPY"
                                     ], date),
                         [
                             {'Value': 20.2282, 'CharCode': 'AUD'},
                             {'Value': 50.1193, 'CharCode': 'GBP'},
                             {'Value': 0.0125734, 'CharCode': 'BYR'},
                             {'Value': 4.53895, 'CharCode': 'DKK'},
                             {'Value': 26.9314, 'CharCode': 'USD'},

                             {'Value': 33.8393, 'CharCode': 'EUR'},
                             {'Value': 0.394368, 'CharCode': 'ISK'},
                             {'Value': 0.210855, 'CharCode': 'KZT'},
                             {'Value': 23.7616, 'CharCode': 'CAD'},
                             {'Value': 3.40731, 'CharCode': 'CNY'},

                             {'Value': 4.00813, 'CharCode': 'NOK'},
                             {'Value': 39.5213, 'CharCode': 'XDR'},
                             {'Value': 17.0064, 'CharCode': 'SGD'},
                             {'Value': 18.2834, 'CharCode': 'TRY'},
                             {'Value': 5.31936, 'CharCode': 'UAH'},

                             {'Value': 3.65172, 'CharCode': 'SEK'},
                             {'Value': 21.2409, 'CharCode': 'CHF'},
                             {'Value': 0.225613, 'CharCode': 'JPY'},
                         ])
