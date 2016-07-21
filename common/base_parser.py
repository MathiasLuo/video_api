from flask_restful import reqparse

baseParser = reqparse.RequestParser()
baseParser.add_argument('url', type=str, required=True, help='this is the query url')

urlParse = baseParser.copy()
urlParse.add_argument('format', help='this is the video format')
urlParse.add_argument('time', type=bool, help='this arg is you want to return time arg')
