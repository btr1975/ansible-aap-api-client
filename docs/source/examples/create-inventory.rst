ansible-aap-api-client create basic inventory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import json
   import os
   from ansible_aap_api_client import (
       InventoryBuilder,
       InventoryRequestSchema,
       InventoryHostRequestSchema,
       Organization,
   )
   from dotenv import load_dotenv

   load_dotenv()

   BASE_URL = os.getenv("BASE_URL")
   USER_NAME = os.getenv("USER_NAME")
   PASSWORD = os.getenv("PASSWORD")
   HOME_INVENTORY_NAME = "some-inventory"
   HOME_ORGANIZATION_NAME = "Default"


   inventory_host_request_schema = InventoryHostRequestSchema(
       name="3560G",
       description="This is a test host",
   )

   ios_hosts = [
       inventory_host_request_schema,
   ]

   obj_organization = Organization(base_url=BASE_URL, username=USER_NAME, password=PASSWORD, ssl_verify=False)

   inventory_request_schema = InventoryRequestSchema(
       name=HOME_INVENTORY_NAME,
       description="This is some inventory home",
       organization=obj_organization.get_organization_id(HOME_ORGANIZATION_NAME),
   )

   obj_inventory = InventoryBuilder(
       base_url=BASE_URL, username=USER_NAME, password=PASSWORD, ssl_verify=False, inventory=inventory_request_schema
   )

   obj_inventory.add_ios_hosts_to_inventory(hosts=ios_hosts)

   obj_inventory.run()


ansible-aap-api-client create a more complex inventory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import json
   import os
   from ansible_aap_api_client import (
       InventoryBuilder,
       InventoryRequestSchema,
       InventoryHostRequestSchema,
       InventoryGroupRequestSchema,
       Organization,
   )
   from dotenv import load_dotenv

   load_dotenv()

   BASE_URL = os.getenv("BASE_URL")
   USER_NAME = os.getenv("USER_NAME")
   PASSWORD = os.getenv("PASSWORD")
   HOME_INVENTORY_NAME = "my-inventory-with-custom-groups-and-hosts"
   HOME_ORGANIZATION_NAME = "Default"


   def to_json(data: dict) -> None:
       print(json.dumps(data, indent=4))


   inventory_host_request_schema = InventoryHostRequestSchema(
       name="FAKE-DEVICE",
       description="This is a test host",
   )

   custom_group_vars = {
       "ansible_ssh_host": "something",
       "ansible_ssh_user": "admin",
       "ansible_ssh_pass": "admin",
       "ansible_network_os": "moo",
   }

   custom_group = InventoryGroupRequestSchema(
       name="CUSTOM-GROUP",
       description="This is a test group",
       variables=custom_group_vars,
   )

   custom_hosts = [
       inventory_host_request_schema,
   ]

   custom_groups = [
       custom_group,
   ]

   obj_organization = Organization(base_url=BASE_URL, username=USER_NAME, password=PASSWORD, ssl_verify=False)

   inventory_request_schema = InventoryRequestSchema(
       name=HOME_INVENTORY_NAME,
       description="This is a test inventory",
       organization=obj_organization.get_organization_id(HOME_ORGANIZATION_NAME),
   )

   obj_inventory = InventoryBuilder(
       base_url=BASE_URL, username=USER_NAME, password=PASSWORD, ssl_verify=False, inventory=inventory_request_schema
   )

   obj_inventory.add_custom_groups_to_inventory(groups=custom_groups)

   print(obj_inventory.custom_groups)
   print(obj_inventory.custom_groups_data)

   obj_inventory.add_hosts_to_custom_group_to_inventory(group_name="CUSTOM-GROUP", hosts=custom_hosts)

   print(obj_inventory.custom_hosts)

   obj_inventory.run()

   print(obj_inventory.custom_groups_data)
