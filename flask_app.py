from services.search_engine.search_service import SearchService, SearchServiceFactory
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HandShake(Resource):
    @staticmethod
    def get():
        checkup = {'server_works': True}
        for factory in SearchServiceFactory:
            checkup[factory.name] = SearchService(factory=factory).checker()
        return checkup


class GoogleSearch(Resource):
    @staticmethod
    def get(query, number_of_sites=10):
        results = SearchService(factory=SearchServiceFactory.googlesearch_python).search(query, number_of_sites)
        return results


class DuckDuckGoSearch(Resource):
    @staticmethod
    def get(query, number_of_sites=10):
        results = SearchService(factory=SearchServiceFactory.duckduckgo).search(query, number_of_sites)
        return results


api.add_resource(HandShake, '/')
api.add_resource(GoogleSearch, '/google/<string:query>', '/google/<string:query>/<int:number_of_sites>')
api.add_resource(DuckDuckGoSearch, '/ddg/<string:query>', '/ddg/<string:query>/<int:number_of_sites>')

if __name__ == '__main__':
    app.run(debug=False)
