"""
AAP Groups
"""

from ansible_aap_api_client.base_connection import _BaseConnection
from ansible_aap_api_client.schemas import InventoryHostRequestSchema


class Group(_BaseConnection):
    """Group class

    :type base_url: str
    :param base_url: The base url to use
    :type username: str
    :param username: The username to use
    :type password: str
    :param password: The password to use
    :type ssl_verify: Optional[bool] = True
    :param ssl_verify: The SSL verification flag
    """

    uri = "/groups/"

    def get_all_groups(self) -> dict:
        """Get all groups

        :rtype: Dict
        :returns: Response
        """
        return self._get(uri=self.uri).json()

    def get_group(self, name: str) -> dict:
        """Get all instances of a group by name

        :type name: str
        :param name: The name of the group

        :rtype: Dict
        :returns: Response
        """
        return self._get(uri=self.uri, params={"name": name}).json()

    def get_group_id(self, name: str) -> int:
        """Get the id of a group if one exists

        :type name: str
        :param name: The name of the group

        :rtype: int
        :returns: The id of the group

        :raises ValueError: If zero or more than one instance is found
        """
        response = self._get(uri=self.uri, params={"name": name}).json().get("results")

        if len(response) == 1:
            return response[0].get("id")

        raise ValueError(f"found {len(response)} groups with name {name}")

    def add_host(self, group_id: int, host: InventoryHostRequestSchema) -> dict:
        """Add host to group

        :type group_id: int
        :param group_id: The group id
        :type host: InventoryHostRequestSchema
        :param host: The host to add

        :rtype: Dict
        :returns: Response
        """
        uri = f"{self.uri}{group_id}/hosts/"

        if not isinstance(host, InventoryHostRequestSchema):
            raise TypeError(f"host must be of type InventoryHostRequestSchema, but received {type(host)}")

        return self._post(uri=uri, json_data=host.dict()).json()
