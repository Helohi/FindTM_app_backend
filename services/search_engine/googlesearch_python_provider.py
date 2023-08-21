from services.search_engine.search_provider import SearchProvider
from googlesearch import search


class GoogleSearchPythonProvider(SearchProvider):
    error_of_search = [{'url': 'https://www.google.com/', 'title': "ERROR WITH API",
                        'description': "ERROR PLEASE COMMUNICATE WITH CREATOR"}]

    def checker(self):
        checking_query = 'Google'
        checking_number_of_results = 1
        try:
            for _ in search(checking_query, num_results=checking_number_of_results):
                pass
            return True
        except Exception as e:
            self.write_error_into_error_file(where_happened='checker', query=checking_query,
                                             number_of_results=checking_number_of_results, type_of_error=str(type(e)),
                                             error_massage=str(e))
            return False

    def search(self, query: str, number_of_results: int) -> list:
        responses = []
        try:
            for response in search(query, num_results=number_of_results, advanced=True, sleep_interval=2):
                responses.append({'url': response.url, 'title': response.title, 'description': response.description})
            return responses
        except Exception as e:
            self.write_error_into_error_file(where_happened='search', query=query, number_of_results=number_of_results,
                                             type_of_error=str(type(e)), error_massage=str(e))
            return self.error_of_search
