"""
AAP API client for inventory management
"""

from ansible_aap_api_client.inventories import Inventory
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
