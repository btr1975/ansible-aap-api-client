"""
Tests for AsyncJobManagement
"""

import pytest
from ansible_aap_api_client import AsyncJobManagement


def test_async_job_management_init_bad_job_template_name():
    with pytest.raises(TypeError):
        AsyncJobManagement(
            base_url="https://localhost:5000",
            username="test",
            password="test",
            ssl_verify=False,
            job_template_name=1,
            inventory_name="Demo Inventory",
        )


def test_async_job_management_init_bad_inventory_name():
    with pytest.raises(TypeError):
        AsyncJobManagement(
            base_url="https://localhost:5000",
            username="test",
            password="test",
            ssl_verify=False,
            job_template_name="Demo Job Template",
            inventory_name=1,
        )


async def test_async_job_management_run(
    requests_get_singe_job_template, requests_get_single_inventory, requests_job_template_job_launch
):
    job_management = AsyncJobManagement(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        job_template_name="Demo Job Template",
        inventory_name="Demo Inventory",
    )

    await job_management.run()

    assert job_management.job_template_id == 7
    assert job_management.job_id is not None
