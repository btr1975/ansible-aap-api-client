"""
A base connection class for the AAP API client.
"""

from typing import Optional
import requests


class _BaseConnection:  # pylint: disable=too-few-public-methods
    """Base connection class

    :type base_url: str
    :param base_url: The base url to use
    :type username: str
    :param username: The username to use
    :type password: str
    :param password: The password to use
    :type ssl_verify: Optional[bool] = True
    :param ssl_verify: The SSL verification flag

    """

    def __init__(self, base_url: str, username: str, password: str, ssl_verify: Optional[bool] = True) -> None:
        self.base_url = base_url
        self.username = username
        self.password = password
        self.ssl_verify = ssl_verify
        self.api_version = "/api/v2"
        self.headers = {"Content-Type": "application/json"}

    def _post(self, uri: str, json_data: Optional[dict] = None) -> requests.Response:
        """Protected post method

        :type uri: str
        :param uri: The uri to post
        :type json_data: Optional[dict]
        :param json_data: The JSON data to post

        :rtype: requests.Response
        :return: A response object
        """
        url = f"{self.base_url}{self.api_version}{uri}"
        response = requests.post(
            url=url,
            auth=(self.username, self.password),
            headers=self.headers,
            json=json_data,
            verify=self.ssl_verify,
            timeout=30,
        )

        if not response.ok:
            response.raise_for_status()

        return response

    def _get(self, uri: str, params: Optional[dict] = None) -> requests.Response:
        """Protected GET method

        :type uri: str
        :param uri: The URI to use
        :type params: Optional[dict] = None
        :param params: The parameters to use

        :rtype: requests.Response
        :returns: A response object
        """
        url = f"{self.base_url}{self.api_version}{uri}"
        response = requests.get(
            url=url,
            auth=(self.username, self.password),
            params=params,
            headers=self.headers,
            verify=self.ssl_verify,
            timeout=30,
        )

        if not response.ok:
            response.raise_for_status()

        return response
