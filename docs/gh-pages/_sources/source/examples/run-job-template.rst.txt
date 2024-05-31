ansible-aap-api-client run job template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import json
   import os
   from ansible_aap_api_client import (
       JobManagement,
   )
   from dotenv import load_dotenv

   load_dotenv()

   BASE_URL = os.getenv("BASE_URL")
   USER_NAME = os.getenv("USER_NAME")
   PASSWORD = os.getenv("PASSWORD")
   HOME_INVENTORY_NAME = "some-inventory"
   HOME_ORGANIZATION_NAME = "Default"
   JOB_TEMPLATE_NAME = "some-job-template-name"


   def to_json(data: dict) -> None:
       print(json.dumps(data, indent=4))


   job_mgmnt_obj = JobManagement(
       base_url=BASE_URL,
       username=USER_NAME,
       password=PASSWORD,
       ssl_verify=False,
       job_template_name=JOB_TEMPLATE_NAME,
       inventory_name=HOME_INVENTORY_NAME,
   )

   job_mgmnt_obj.run()


ansible-aap-api-client run job template poll and get output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import json
   import os
   from ansible_aap_api_client import (
       JobManagement,
   )
   from dotenv import load_dotenv

   load_dotenv()

   BASE_URL = os.getenv("BASE_URL")
   USER_NAME = os.getenv("USER_NAME")
   PASSWORD = os.getenv("PASSWORD")
   HOME_INVENTORY_NAME = "some-inventory"
   HOME_ORGANIZATION_NAME = "Default"
   JOB_TEMPLATE_NAME = "some-job-template-name"


   def to_json(data: dict) -> None:
       print(json.dumps(data, indent=4))


   job_mgmnt_obj = JobManagement(
       base_url=BASE_URL,
       username=USER_NAME,
       password=PASSWORD,
       ssl_verify=False,
       job_template_name=JOB_TEMPLATE_NAME,
       inventory_name=HOME_INVENTORY_NAME,
   )

   job_mgmnt_obj.poll_completion(print_status=True)

   print(job_mgmnt_obj.get_job_stdout(job_mgmnt_obj.job_id, "txt"))
