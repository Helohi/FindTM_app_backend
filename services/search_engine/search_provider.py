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

    @abstractmethod
    def write_error_into_error_file(self, where_happened: str, query: str, number_of_results: int, type_of_error: str,
                                    error_massage: str):
        """
        Must ->ADD<- error in ERROR_log.txt in a given way:\n
        Error thrown in {where_happened}:
            query: {query}\n
            number_of_results: {number_of_results}\n
            Type of error: {type_of_error}\n
            error_message: {error_massage}\n

        :param str where_happened: where error occur
        :param str query: what search was made
        :param int number_of_results: how many results was needed
        :param str type_of_error: type of error that occurred
        :param str error_massage: message of an error
        :return: None
        """
        pass
