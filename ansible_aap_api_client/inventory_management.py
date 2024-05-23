"""
AAP API client for inventory management
"""

from typing import List, Union
from ansible_aap_api_client.inventories import Inventory
from ansible_aap_api_client.schemas import (
    InventoryRequestSchema,
    InventoryGroupRequestSchema,
    InventoryHostRequestSchema,
)
from ansible_aap_api_client.hosts import Host
from ansible_aap_api_client.groups import Group


class InventoryManagement(Inventory, Group, Host):
    """Inventory management class

    :type base_url: str
    :param base_url: The base url to use
    :type username: str
    :param username: The username to use
    :type password: str
    :param password: The password to use
    :type ssl_verify: Optional[Union[bool, str]] = True
    :param ssl_verify: The SSL verification True or False or a path to a certificate
    """


class InventoryBuilder(InventoryManagement):
    """Inventory builder class

    :type base_url: str
    :param base_url: The base url to use
    :type username: str
    :param username: The username to use
    :type password: str
    :param password: The password to use
    :type ssl_verify: Optional[Union[bool, str]] = True
    :param ssl_verify: The SSL verification True or False or a path to a certificate
    """

    IOS_GROUP_VARS = {
        "ansible_connection": "ansible.netcommon.network_cli",
        "ansible_become": True,
        "ansibel_become_method": "enable",
        "ansible_network_os": "ios",
    }

    IOSXR_GROUP_VARS = {
        "ansible_connection": "ansible.netcommon.network_cli",
        "ansible_become": True,
        "ansibel_become_method": "enable",
        "ansible_network_os": "iosxr",
    }

    NXOS_GROUP_VARS = {
        "ansible_connection": "ansible.netcommon.network_cli",
        "ansible_become": True,
        "ansibel_become_method": "enable",
        "ansible_network_os": "nxos",
    }

    EOS_GROUP_VARS = {
        "ansible_connection": "ansible.netcommon.network_cli",
        "ansible_become": True,
        "ansibel_become_method": "enable",
        "ansible_network_os": "eos",
    }

    def __init__(  # pylint: disable=too-many-arguments
        self,
        base_url: str,
        username: str,
        password: str,
        ssl_verify: Union[bool, str],
        inventory: InventoryRequestSchema,
    ) -> None:
        super().__init__(base_url, username, password, ssl_verify)

        self.inventory_name = inventory.name
        self.inventory_id = self.create_inventory(inventory=inventory).get("id")
        self.ios_group_id = self.add_group_to_inventory(
            inventory_id=self.inventory_id,
            group=self._get_group_request_schema("ios"),
        ).get("id")
        self.iosxr_group_id = self.add_group_to_inventory(
            inventory_id=self.inventory_id,
            group=self._get_group_request_schema("iosxr"),
        ).get("id")
        self.nxos_group_id = self.add_group_to_inventory(
            inventory_id=self.inventory_id,
            group=self._get_group_request_schema("nxos"),
        ).get("id")
        self.eos_group_id = self.add_group_to_inventory(
            inventory_id=self.inventory_id,
            group=self._get_group_request_schema("eos"),
        ).get("id")

    def _get_group_request_schema(self, nos: str) -> InventoryGroupRequestSchema:
        """Protected method to get group request schema

        :type nos: str
        :param nos: The NOS to use

        :rtype: InventoryGroupRequestSchema
        :return: The group request schema

        :raises ValueError: If the NOS is not supported
        """
        if nos == "ios":
            group_vars = self.IOS_GROUP_VARS
        elif nos == "iosxr":
            group_vars = self.IOSXR_GROUP_VARS
        elif nos == "nxos":
            group_vars = self.NXOS_GROUP_VARS
        elif nos == "eos":
            group_vars = self.EOS_GROUP_VARS
        else:
            raise ValueError(f"Unsupported NOS: {nos}")

        return InventoryGroupRequestSchema(
            name=f"{self.inventory_name}-{nos}",
            description=f"Inventory {self.inventory_name} Group for {nos} devices",
            variables=group_vars,
        )

    def add_ios_host_to_inventory(self, host: InventoryHostRequestSchema) -> dict:
        """Add IOS host to inventory

        :type host: InventoryHostRequestSchema
        :param host: The host to add

        :rtype: dict
        :return: The response
        """
        return self.add_host_to_group(group_id=self.ios_group_id, host=host)

    def add_ios_hosts_to_inventory(self, hosts: List[InventoryHostRequestSchema]) -> List[dict]:
        """Add multiple IOS hosts to inventory

        :type hosts: List[InventoryHostRequestSchema]
        :param hosts: The hosts to add

        :rtype: List[dict]
        :return: The responses
        """
        responses = []
        for host in hosts:
            responses.append(self.add_ios_host_to_inventory(host=host))

        return responses

    def add_iosxr_host_to_inventory(self, host: InventoryHostRequestSchema) -> dict:
        """Add IOS-XR host to inventory

        :type host: InventoryHostRequestSchema
        :param host: The host to add

        :rtype: dict
        :return: The response
        """
        return self.add_host_to_group(group_id=self.iosxr_group_id, host=host)

    def add_iosxr_hosts_to_inventory(self, hosts: List[InventoryHostRequestSchema]) -> List[dict]:
        """Add multiple IOS-XR hosts to inventory

        :type hosts: List[InventoryHostRequestSchema]
        :param hosts: The hosts to add

        :rtype: List[dict]
        :return: The responses
        """
        responses = []
        for host in hosts:
            responses.append(self.add_iosxr_host_to_inventory(host=host))

        return responses

    def add_nxos_host_to_inventory(self, host: InventoryHostRequestSchema) -> dict:
        """Add NX-OS host to inventory

        :type host: InventoryHostRequestSchema
        :param host: The host to add

        :rtype: dict
        :return: The response
        """
        return self.add_host_to_group(group_id=self.nxos_group_id, host=host)

    def add_nxos_hosts_to_inventory(self, hosts: List[InventoryHostRequestSchema]) -> List[dict]:
        """Add multiple NX-OS hosts to inventory

        :type hosts: List[InventoryHostRequestSchema]
        :param hosts: The hosts to add

        :rtype: List[dict]
        :return: The responses
        """
        responses = []
        for host in hosts:
            responses.append(self.add_nxos_host_to_inventory(host=host))

        return responses

    def add_eos_host_to_inventory(self, host: InventoryHostRequestSchema) -> dict:
        """Add EOS host to inventory

        :type host: InventoryHostRequestSchema
        :param host: The host to add

        :rtype: dict
        :return: The response
        """
        return self.add_host_to_group(group_id=self.eos_group_id, host=host)

    def add_eos_hosts_to_inventory(self, hosts: List[InventoryHostRequestSchema]) -> List[dict]:
        """Add multiple EOS hosts to inventory

        :type hosts: List[InventoryHostRequestSchema]
        :param hosts: The hosts to add

        :rtype: List[dict]
        :return: The responses
        """
        responses = []
        for host in hosts:
            responses.append(self.add_eos_host_to_inventory(host=host))

        return responses
