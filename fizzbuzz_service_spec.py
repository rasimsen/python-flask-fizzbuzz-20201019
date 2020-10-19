import unittest

from fizzbuzz_service import FizzBuzzService


class FizzBuzzServiceTest(unittest.TestCase):
    # def test_firsttest(self):
    #     self.assertEqual("fail", FizzBuzzService.validate(3))

    def test_fizz(self):
        self.assertEqual("Fizz", FizzBuzzService.validate(3))
        self.assertEqual("Fizz", FizzBuzzService.validate(9999))
        self.assertEqual("Fizz", FizzBuzzService.validate(33))

    def test_buzz(self):
        self.assertEqual("Buzz", FizzBuzzService.validate(5))
        self.assertEqual("Buzz", FizzBuzzService.validate(55))
        self.assertEqual("Buzz", FizzBuzzService.validate(5555))

    def test_fizzbuzz(self):
        self.assertEqual(13, FizzBuzzService.validate(13))
        self.assertEqual(11, FizzBuzzService.validate(11))

# TDD
## RED-GREEN-BLUE
