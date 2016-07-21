from flask_restful import reqparse

baseParser = reqparse.RequestParser()
baseParser.add_argument('url', type=str, required=True)

urlParse = baseParser.copy()
urlParse.add_argument('format')
urlParse.add_argument('time', type=bool)
