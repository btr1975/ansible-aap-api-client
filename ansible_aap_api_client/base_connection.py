"""
A base connection class for the AAP API client.
"""

from typing import Optional, Union
import niquests as requests


class _BaseConnection:  # pylint: disable=too-few-public-methods
    """Base connection class

    :type base_url: str
    :param base_url: The base url to use
    :type username: str
    :param username: The username to use
    :type password: str
    :param password: The password to use
    :type ssl_verify: Optional[Union[bool, str]] = True
    :param ssl_verify: The SSL verification True or False or a path to a certificate

    :raises TypeError: If the base_url, username, password is not a string
    :raises TypeError: If ssl_verify is not a bool or str
    """

    def __init__(
        self, base_url: str, username: str, password: str, ssl_verify: Optional[Union[bool, str]] = True
    ) -> None:
        if not isinstance(base_url, str):
            raise TypeError(f"base_url must be of type str, but received {type(base_url)}")

        self._base_url = base_url

        if not isinstance(username, str):
            raise TypeError(f"username must be of type str, but received {type(username)}")

        self._username = username

        if not isinstance(password, str):
            raise TypeError(f"password must be of type str, but received {type(password)}")

        self._password = password

        if isinstance(ssl_verify, str):
            self._ssl_verify = ssl_verify

        elif isinstance(ssl_verify, bool):
            self._ssl_verify = ssl_verify

        else:
            raise TypeError(f"ssl_verify must be of type bool or str, but received {type(ssl_verify)}")

        self._api_version = "/api/v2"
        self._headers = {"Content-Type": "application/json"}

        self._session = requests.Session()
        self._session.auth = (self._username, self._password)
        self._session.headers = self._headers
        self._session.verify = self._ssl_verify

    def _post(self, uri: str, json_data: Optional[dict] = None) -> requests.Response:
        """Protected post method

        :type uri: str
        :param uri: The uri to post
        :type json_data: Optional[dict]
        :param json_data: The JSON data to post

        :rtype: requests.Response
        :return: A response object
        """
        url = f"{self._base_url}{self._api_version}{uri}"
        response = self._session.post(
            url=url,
            json=json_data,
            timeout=30,
        )

        if not response.ok:  # pragma: no cover
            response.raise_for_status()

        return response

    def _patch(self, uri: str, json_data: Optional[dict] = None) -> requests.Response:
        """Protected patch method

        :type uri: str
        :param uri: The uri to patch
        :type json_data: Optional[dict]
        :param json_data: The JSON data to patch

        :rtype: requests.Response
        :return: A response object
        """
        url = f"{self._base_url}{self._api_version}{uri}"
        response = self._session.patch(
            url=url,
            json=json_data,
            timeout=30,
        )

        if not response.ok:  # pragma: no cover
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
        url = f"{self._base_url}{self._api_version}{uri}"
        response = self._session.get(
            url=url,
            params=params,
            timeout=30,
        )

        if not response.ok:  # pragma: no cover
            response.raise_for_status()

        return response

    def _delete(self, uri: str, json_data: Optional[dict] = None) -> requests.Response:
        """Protected delete method

        :type uri: str
        :param uri: The uri to delete
        :type json_data: Optional[dict]
        :param json_data: The JSON data to delete

        :rtype: requests.Response
        :return: A response object
        """
        url = f"{self._base_url}{self._api_version}{uri}"
        response = self._session.delete(
            url=url,
            json=json_data,
            timeout=30,
        )

        if not response.ok:  # pragma: no cover
            response.raise_for_status()

        return response
