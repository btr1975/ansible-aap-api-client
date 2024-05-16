"""
A base connection class for the AAP API client.
"""
from typing import Optional
import requests


class _BaseConnection:

    def __init__(self, base_url: str, username: str, password: str, ssl_verify: Optional[bool] = True) -> None:
        self.base_url = base_url
        self.username = username
        self.password = password
        self.ssl_verify = ssl_verify
        self.api_version = "/api/v2"
        self.headers = {"Content-Type": "application/json"}

    def _post(self, uri: str, json_data: Optional[dict] = None) -> requests.Response:
        url = f"{self.base_url}{self.api_version}{uri}"
        response = requests.post(
            url=url, auth=(self.username, self.password), headers=self.headers, json=json_data, verify=self.ssl_verify
        )

        if response.ok:
            return response

        response.raise_for_status()

    def _get(self, uri: str) -> requests.Response:
        url = f"{self.base_url}{self.api_version}{uri}"
        response = requests.get(
            url=url, auth=(self.username, self.password), headers=self.headers, verify=self.ssl_verify
        )

        if response.ok:
            return response

        response.raise_for_status()
