"""
init for ansible_aap_api_client
"""

from ansible_aap_api_client.ansible_aap_api_client_cli import cli
from ansible_aap_api_client.inventories import Inventory
from ansible_aap_api_client.groups import Group
from ansible_aap_api_client.schemas import (
    InventoryRequestSchema,
    InventoryHostRequestSchema,
    InventoryGroupRequestSchema,
)
