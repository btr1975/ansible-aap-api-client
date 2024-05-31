ansible-aap-api-client delete inventory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import os
   from ansible_aap_api_client import (
       InventoryManagement,
   )
   from dotenv import load_dotenv

   load_dotenv()

   BASE_URL = os.getenv("BASE_URL")
   USER_NAME = os.getenv("USER_NAME")
   PASSWORD = os.getenv("PASSWORD")
   HOME_INVENTORY_NAME = "some-inventory"


   inventory_obj = InventoryManagement(base_url=BASE_URL, username=USER_NAME, password=PASSWORD, ssl_verify=False)

   print(inventory_obj.delete_inventory(inventory_obj.get_inventory_id(HOME_INVENTORY_NAME)))
