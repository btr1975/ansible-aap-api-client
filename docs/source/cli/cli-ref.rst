ansible-aap-api-client cli reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


ansible-aap-api-client cli top-level
``````````````````````````````````````

.. code-block:: bash

   usage: -c [-h] -b BASE_URL -u USERNAME -p PASSWORD {run-job-template} ...

   ansible-aap-api-client-cli

   options:
     -h, --help            show this help message and exit
     -b BASE_URL, --base-url BASE_URL
                           Base URL for the Tower/AAP
     -u USERNAME, --username USERNAME
                           The username
     -p PASSWORD, --password PASSWORD
                           The password

   commands:
     Valid commands: a single command is required

     {run-job-template}    CLI Help
       run-job-template    Run a job template in Tower/AAP


ansible-aap-api-client cli run-job-template
````````````````````````````````````````````

.. code-block:: bash

   usage: -c run-job-template [-h] -t TEMPLATE_NAME -i INVENTORY_NAME

   options:
     -h, --help            show this help message and exit
     -t TEMPLATE_NAME, --template-name TEMPLATE_NAME
                           The name of the Job Template
     -i INVENTORY_NAME, --inventory-name INVENTORY_NAME
                           The name of Inventory
