"""
AAP Inventories
"""

from ansible_aap_api_client.base_connection import _BaseConnection
from ansible_aap_api_client.schemas import (
    InventoryRequestSchema,
    InventoryHostRequestSchema,
    InventoryGroupRequestSchema,
)


class Inventory(_BaseConnection):
    """Inventory class

    :type base_url: str
    :param base_url: The base url to use
    :type username: str
    :param username: The username to use
    :type password: str
    :param password: The password to use
    :type ssl_verify: Optional[Union[bool, str]] = True
    :param ssl_verify: The SSL verification True or False or a path to a certificate
    """

    uri = "/inventories/"

    def get_all_inventories(self) -> dict:
        """Get all inventories

        :rtype: Dict
        :returns: Response
        """
        return self._get(uri=self.uri).json()

    def get_inventory(self, name: str) -> dict:
        """Get all instances of an inventory by name

        :type name: str
        :param name: The inventory name

        :rtype: Dict
        :returns: Response

        :raises TypeError: If name is not of type str
        """
        if not isinstance(name, str):
            raise TypeError(f"name must be of type str, but received {type(name)}")

        return self._get(uri=self.uri, params={"name": name}).json()

    def get_inventory_id(self, name: str) -> int:
        """Get the id of an inventory if one exists

        :type name: str
        :param name: The name of the inventory

        :rtype: int
        :returns: The id of the inventory

        :raises ValueError: If zero or more than one instance is found
        :raises TypeError: If name is not of type str
        """
        if not isinstance(name, str):
            raise TypeError(f"name must be of type str, but received {type(name)}")

        response = self._get(uri=self.uri, params={"name": name}).json().get("results")

        if len(response) == 1:
            return response[0].get("id")

        raise ValueError(f"found {len(response)} inventories with name {name}")

    def create_inventory(self, inventory: InventoryRequestSchema) -> dict:
        """Create inventory

        :type inventory: InventoryRequestSchema
        :param inventory: The inventory to create

        :rtype: Dict
        :returns: Response

        :raises TypeError: If inventory is not a InventoryRequestSchema
        """
        if not isinstance(inventory, InventoryRequestSchema):
            raise TypeError(f"inventory must be of type InventoryRequestSchema, but received {type(inventory)}")

        return self._post(uri=self.uri, json_data=inventory.dict()).json()

    def add_host(self, inventory_id: int, host: InventoryHostRequestSchema) -> dict:
        """Add host to inventory

        :type inventory_id: int
        :param inventory_id: The inventory id
        :type host: InventoryHostRequestSchema
        :param host: The host to add

        :rtype: Dict
        :returns: Response

        :raises TypeError: If host is not an InventoryHostRequestSchema
        """
        uri = f"{self.uri}{inventory_id}/hosts/"

        if not isinstance(inventory_id, int):
            raise TypeError(f"inventory_id must be of type int, but received {type(inventory_id)}")

        if not isinstance(host, InventoryHostRequestSchema):
            raise TypeError(f"host must be of type InventoryHostRequestSchema, but received {type(host)}")

        return self._post(uri=uri, json_data=host.dict()).json()

    def add_group(self, inventory_id: int, group: InventoryGroupRequestSchema) -> dict:
        """Add group to inventory

        :type inventory_id: int
        :param inventory_id: The inventory id
        :type group: InventoryGroupRequestSchema
        :param group: The group to add

        :rtype: Dict
        :returns: Response

        :raises TypeError: If group is not an InventoryGroupRequestSchema
        """
        uri = f"{self.uri}{inventory_id}/groups/"

        if not isinstance(inventory_id, int):
            raise TypeError(f"inventory_id must be of type int, but received {type(inventory_id)}")

        if not isinstance(group, InventoryGroupRequestSchema):
            raise TypeError(f"group must be of type InventoryGroupRequestSchema, but received {type(group)}")

        return self._post(uri=uri, json_data=group.dict()).json()
