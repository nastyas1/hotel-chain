from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('email', required=True)
parser.add_argument('about', required=True)
parser.add_argument('hotel_number_id', required=True)
