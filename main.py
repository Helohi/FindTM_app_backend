from services.search_engine.search_service import SearchService, SearchServiceFactory
from flask import Flask
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)
search_service = SearchService(factory=SearchServiceFactory.googlesearch_python)


class HandShake(Resource):
    @staticmethod
    def get():
        checkup = {
            'server_works': True,
            'google_search_works': search_service.checker(),
        }
        return json.dumps(checkup)


class GoogleSearch(Resource):
    @staticmethod
    def get(query, number_of_sites=10):
        results = search_service.search(query, number_of_sites)
        return json.dumps(results)


api.add_resource(HandShake, '/')
api.add_resource(GoogleSearch, '/google/<string:query>', '/google/<string:query>/<int:number_of_sites>')

if __name__ == '__main__':
    app.run(debug=True)