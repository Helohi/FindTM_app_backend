from services.search_engine.search_provider import SearchProvider
from duckduckgo_search import DDGS


class DuckDuckGoSearchProvider(SearchProvider):
    error_of_search = [{'url': 'https://www.duckduckgo.com/', 'title': "ERROR WITH API",
                        'description': "ERROR PLEASE COMMUNICATE WITH CREATOR"}]

    def checker(self) -> bool:
        checking_query = "DuckDuckGo"
        checking_number_of_results = 1
        try:
            with DDGS() as ddgs:
                for num, _ in enumerate(ddgs.text(checking_query)):
                    if num >= checking_number_of_results:
                        break
                    pass
            return True
        except Exception as e:
            self.write_error_into_error_file(where_happened='DuckDuckGoSearchProvider checker', query=checking_query,
                                             number_of_results=checking_number_of_results, type_of_error=str(type(e)),
                                             error_massage=str(e))
            return False

    def search(self, query: str, number_of_results: int = 20) -> list:
        # TODO: max of number_of_results is 41, increase it to infinity
        results = []
        try:
            with DDGS() as ddgs:
                for result in ddgs.text(query):
                    if len(results) >= number_of_results:
                        break
                    results.append({'url': result['href'], 'title': result['title'], 'description': result['body']})

            return results
        except Exception as e:
            self.write_error_into_error_file(where_happened='DuckDuckGoSearchProvider checker', query=query,
                                             number_of_results=number_of_results, type_of_error=str(type(e)),
                                             error_massage=str(e))
            return self.error_of_search
