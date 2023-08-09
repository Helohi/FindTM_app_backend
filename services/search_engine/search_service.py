from services.search_engine.search_provider import SearchProvider
from services.search_engine.googlesearch_python_provider import GoogleSearchPythonProvider
from enum import Enum


class SearchServiceProviderNotProvidedException(Exception):
    pass


class SearchServiceFactory(Enum):
    googlesearch_python = 1


class SearchService(SearchProvider):
    def __init__(self, provider: SearchProvider = None, factory: SearchServiceFactory = None):
        if provider is None:
            if factory == SearchServiceFactory.googlesearch_python:
                provider = GoogleSearchPythonProvider()
            else:
                raise SearchServiceProviderNotProvidedException('You must provide either provider or factory')

        self.provider = provider

    def checker(self) -> bool:
        return self.provider.checker()

    def search(self, query: str, number_of_results: int) -> list:
        return self.provider.search(query, number_of_results)

    def write_error_into_error_file(self, where_happened: str, query: str, number_of_results: int, type_of_error: str,
                                    error_massage: str):
        return self.provider.write_error_into_error_file(where_happened, query, number_of_results, type_of_error,
                                                         error_massage)
