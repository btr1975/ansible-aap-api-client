"""
Common needs for integrations
"""

import urllib.parse


class _CommonClientNeeds:
    """Common needs for APIs"""

    GROUPS_URI = "groups"
    HOSTS_URI = "hosts"
    INVENTORIES_URI = "inventories"
    JOB_TEMPLATES_URI = "job_templates"
    JOBS_URI = "jobs"
    ORGANIZATIONS_URI = "organizations"

    @staticmethod
    def url_join(base_url: str, *args) -> str:
        """Helper to join a URL in a clean format

        :param base_url: The base URL
        :param args: The portions of the URL to join

        :return: The joined URL
        """
        args_strings = list(map(str, args))

        joined_parts = "/".join(args_strings)

        return urllib.parse.urljoin(f"{base_url}", f"{joined_parts}/")

    @staticmethod
    def get_url_scheme(url: str) -> str:
        """Helper to get a URL scheme

        :param url: The URL

        :return: The URL scheme
        """
        split_url = urllib.parse.urlsplit(url)

        return split_url.scheme

    @staticmethod
    def is_port_valid(port: int) -> None:
        """Helper to check if a port is valid

        :param port: The port to check

        :return: Nothing

        :raises ValueError: If the port is invalid
        """
        if int(port) not in range(1, 65536):
            raise ValueError(f"port must be in the range of 1 to 65535, but received port '{port}'")

    @staticmethod
    def is_string(value: str) -> None:
        """Check for a valid string

        :param value: The value to check

        :return: Nothing

        :raises ValueError: If the value is not a string
        """
        if not isinstance(value, str):
            raise TypeError(f"{value} must be a string")

    @staticmethod
    def is_boolean(value: bool) -> None:
        """Check for a valid boolean

        :param value: The value to check

        :return: Nothing

        :raises ValueError: If the value is not a boolean
        """
        if not isinstance(value, bool):
            raise TypeError(f"{value} must be a boolean")

    @staticmethod
    def is_integer(value: int) -> None:
        """Check for a valid integer

        :param value: The value to check

        :return: Nothing

        :raises ValueError: If the value is not a integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{value} must be a integer")
