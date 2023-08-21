from abc import ABC, abstractmethod


class SearchProvider(ABC):
    @abstractmethod
    def checker(self) -> bool:
        """
        Function that return True if provider is working fine and False otherwise

        :return: is_provider_works
        :rtype: bool
        """

        pass

    @abstractmethod
    def search(self, query: str, number_of_results: int) -> list:
        """
        Must return a list of results in format of dict with given parameters:
        {'url': url, 'title': title, 'description': description}

        :param str query:
        :param int number_of_results:
        :return: results of search
        :rtype: list
        """

        pass

    @staticmethod
    def write_error_into_error_file(where_happened: str, query: str, number_of_results: int, type_of_error: str,
                                    error_massage: str):
        with open('ERROR_log.txt', 'a') as error_file:
            error_file.write(f'\nError thrown in {where_happened}:\nquery: {query}\n'
                             f'number_of_results: {number_of_results}\nType of error: {type_of_error}\n'
                             f'error_message: {error_massage}\n')
