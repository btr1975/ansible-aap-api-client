"""
Async AAP Job Management
"""

from typing import Optional, Union
import time
from ansible_aap_api_client.async_aap_client import AsyncAAPClient
from ansible_aap_api_client.interfaces.runable import AsyncRunable


class AsyncJobManagement(AsyncRunable, AsyncAAPClient):  # pylint: disable=too-many-ancestors
    """Job management class, to run a job template against an inventory

    :param base_url: The base url to use
    :param username: The username to use
    :param password: The password to use
    :param ssl_verify: The SSL verification True or False or a path to a certificate
    :param job_template_name: The name of the job template
    :param inventory_name: The name of the inventory

    :raises TypeError: If job_template_name is not of type str
    :raises TypeError: If inventory_name is not of type str
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        base_url: str,
        username: str,
        password: str,
        ssl_verify: Union[bool, str],
        job_template_name: str,
        inventory_name: str,
    ) -> None:
        super().__init__(base_url=base_url, username=username, password=password, ssl_verify=ssl_verify)

        if not isinstance(job_template_name, str):
            raise TypeError(f"job_template_name must be of type str, but received {type(job_template_name)}")

        if not isinstance(inventory_name, str):
            raise TypeError(f"inventory_name must be of type str, but received {type(inventory_name)}")

        self.job_template_name = job_template_name
        self.job_template_id = None
        self.inventory_name = inventory_name
        self.inventory_id = None
        self.job_id = None

    async def run(self, **kwargs) -> None:
        """Run the job management

        :param kwargs: The keyword arguments to pass to the launch_job_template method

        :return: Runs the inventory builder
        """
        self.job_template_id = await self.get_job_template_id(name=self.job_template_name)
        self.inventory_id = await self.get_inventory_id(name=self.inventory_name)
        response = await self.launch_job_template(
            job_template_id=self.job_template_id, inventory=self.inventory_id, **kwargs
        )

        self.job_id = response.get("id")

    async def poll_completion(self, print_status: Optional[bool] = False, **kwargs) -> str:  # pragma: no cover
        """Run the job and poll the completion of a job

        :param print_status: Print the status of the job
        :param kwargs: The keyword arguments to pass to the launch_job_template method

        :returns: The completed status of the job

        :raises TypeError: If print_status is not of type bool
        """
        if not isinstance(print_status, bool):
            raise TypeError(f"print_status must be of type bool, but received {type(print_status)}")

        if not self.job_id:
            await self.run(**kwargs)

        ok_statuses = ["successful", "failed", "error", "cancelled"]

        job_status = "new"

        if print_status:
            print(f"Polling job_id {self.job_id} current status {job_status}")

        while job_status not in ok_statuses:
            time.sleep(5)
            job_status = await self.get_job_status(job_id=self.job_id)

            if print_status:
                print(f"Polling job_id {self.job_id} current status {job_status}")

            if job_status in ok_statuses:
                break

        if print_status:
            print(f"Polling job_id {self.job_id} completed status {job_status}")

        return job_status
