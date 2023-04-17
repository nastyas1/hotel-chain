from flask_restful import reqparse


parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('number', required=True)
parser.add_argument('free_time', required=True)
