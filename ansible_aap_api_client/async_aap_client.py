"""
Async APP Client
"""

from niquests import AsyncSession
from ansible_aap_api_client.common_client_needs import _CommonClientNeeds
from ansible_aap_api_client.schemas import InventoryGroupRequestSchema, InventoryHostRequestSchema


class AsyncAAPClient(_CommonClientNeeds):
    """Asynchronous APP Client

    :param str base_url: Base URL for APP Client example: https://example.com
    :param str username: APP Username
    :param str password: APP Password
    :param ssl_verify: Verify SSL certificates True, False or pass the path to the certificate file
    """

    def __init__(self, base_url: str, username: str, password: str, ssl_verify: bool | str = True) -> None:
        self.is_string(value=base_url)
        self.is_string(value=username)
        self.is_string(value=password)

        if isinstance(ssl_verify, bool):
            self._ssl_verify = ssl_verify

        elif isinstance(ssl_verify, str):
            self._ssl_verify = ssl_verify

        else:
            raise TypeError(f"ssl_verify '{ssl_verify}' must be a string or boolean")

        if self.get_url_scheme(url=base_url) not in ("http", "https"):
            raise ValueError(f"invalid URL scheme: {base_url}")

        self._base_url = base_url
        self._api_version = "/api/v2"
        self._headers = {"Content-Type": "application/json"}
        self._session = AsyncSession()
        self._session.auth = (username, password)
        self._session.headers = self._headers
        self._session.verify = ssl_verify

    async def get_all_groups(self) -> dict:
        """Get all groups

        :returns: Response
        """
        url = self.url_join(self._base_url, self.GROUPS_URI)

        response = await self._session.get(url=url)

        return response.json()

    async def get_group(self, name: str) -> dict:
        """Get all instances of a group by name

        :param name: The name of the group

        :returns: Response

        :raises TypeError: If name is not of type str
        """
        self.is_string(value=name)

        url = self.url_join(self._base_url, self.GROUPS_URI)

        response = await self._session.get(url=url, params={"name": name})

        return response.json()

    async def get_group_id(self, name: str) -> int:
        """Get the id of a group if one exists

        :param name: The name of the group

        :returns: The id of the group

        :raises ValueError: If zero or more than one instance is found
        :raises TypeError: If name is not of type str
        """
        self.is_string(value=name)

        response = await self.get_group(name=name)

        results = response["results"]

        if len(results) != 1:
            raise ValueError(f"found {len(results)} groups with name {name}")

        return response[0]["id"]

    async def delete_group(self, group_id: int) -> int | None:
        """Delete group

        :param group_id: The group id

        :returns: Response Status Code

        :raises TypeError: If inventory_id is not of type int
        """
        self.is_integer(value=group_id)

        url = self.url_join(self._base_url, self.GROUPS_URI, group_id)

        response = await self._session.delete(url=url)

        return response.status_code

    async def update_group(self, group_id: int, group: InventoryGroupRequestSchema) -> dict:
        """Update group

        :param group_id: The group id
        :param group: The group data

        :returns: Response

        :raises TypeError: If group is not a InventoryGroupRequestSchema
        :raises TypeError: If group_id is not of type int
        """
        self.is_integer(value=group_id)

        if not isinstance(group, InventoryGroupRequestSchema):
            raise TypeError(f"group must be of type InventoryGroupRequestSchema, but received {type(group)}")

        url = self.url_join(self._base_url, self.GROUPS_URI, group_id)

        response = await self._session.patch(url=url, json=group.dict())

        return response.json()

    async def add_host_to_group(self, group_id: int, host: InventoryHostRequestSchema) -> dict:
        """Add host to group

        :param group_id: The group id
        :param host: The host to add

        :returns: Response

        :raises TypeError: If host is not of type InventoryHostRequestSchema
        :raises TypeError: If group_id is not of type int
        """
        self.is_integer(value=group_id)

        if not isinstance(host, InventoryHostRequestSchema):
            raise TypeError(f"host must be of type InventoryHostRequestSchema, but received {type(host)}")

        url = self.url_join(self._base_url, self.GROUPS_URI, group_id, "hosts")

        response = await self._session.post(url=url, json=host.dict())

        return response.json()
