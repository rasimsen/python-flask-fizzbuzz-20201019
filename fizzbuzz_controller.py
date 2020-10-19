from flask_restful import Resource

from fizzbuzz_service import FizzBuzzService


class FizzBuzzController(Resource):
    def get(self, input_variable):
        return FizzBuzzService.validate(input_variable)
