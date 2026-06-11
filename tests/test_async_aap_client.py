"""
Tests for AsyncAAPClient
"""

import pytest
from ansible_aap_api_client import AsyncAAPClient


# ── Groups ──────────────────────────────────────────────────────────────────


async def test_async_get_all_groups(requests_get_two_group):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test", ssl_verify=False)
    response = await obj.get_all_groups()


async def test_async_get_group(requests_get_two_group):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_group(name="test_group")


async def test_async_get_group_bad(requests_get_two_group):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.get_group(name=1)


async def test_async_get_group_id(requests_get_single_group):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    response = await obj.get_group_id(name="test_group")
    assert response == 2


async def test_async_get_group_id_bad(requests_get_two_group):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(ValueError):
        await obj.get_group_id(name="test_group")

    with pytest.raises(TypeError):
        await obj.get_group_id(name=1)


async def test_async_delete_group(requests_delete_group):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    response = await obj.delete_group(group_id=2)


async def test_async_delete_group_bad(requests_delete_group):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.delete_group(group_id="bad")


async def test_async_update_group_bad(requests_delete_group, inventory_group_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.update_group(group_id="bad", group=inventory_group_request_schema)

    with pytest.raises(TypeError):
        await obj.update_group(group_id=2, group="bad")


async def test_async_add_host_to_group(requests_add_host_group, inventory_host_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    response = await obj.add_host_to_group(group_id=2, host=inventory_host_request_schema)


async def test_async_add_host_to_group_bad(requests_add_host_group, inventory_host_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.add_host_to_group(group_id=2, host="bad")

    with pytest.raises(TypeError):
        await obj.add_host_to_group(group_id="bad", host=inventory_host_request_schema)


# ── Hosts ────────────────────────────────────────────────────────────────────


async def test_async_get_all_hosts(requests_get_two_host):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    response = await obj.get_all_hosts()


async def test_async_get_host(requests_get_two_host):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_host(name="test_host")


async def test_async_get_host_bad(requests_get_two_host):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.get_host(name=1)


async def test_async_get_host_id(requests_get_single_host):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    response = await obj.get_host_id(name="test_host")
    assert response == 1


async def test_async_get_host_id_bad(requests_get_two_host):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(ValueError):
        await obj.get_host_id(name="test_host")

    with pytest.raises(TypeError):
        await obj.get_host_id(name=1)


async def test_async_delete_host(requests_delete_host):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    response = await obj.delete_host(host_id=2)


async def test_async_delete_host_bad(requests_delete_host):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.delete_host(host_id="bad")


async def test_async_update_host_bad(requests_delete_host, inventory_host_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.update_host(host_id="bad", host=inventory_host_request_schema)

    with pytest.raises(TypeError):
        await obj.update_host(host_id=2, host="bad")


# ── Inventories ──────────────────────────────────────────────────────────────


async def test_async_get_all_inventories(requests_get_two_inventory):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    response = await obj.get_all_inventories()


async def test_async_get_inventory(requests_get_single_inventory):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_inventory(name="Demo Inventory")


async def test_async_get_inventory_bad(requests_get_single_inventory):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.get_inventory(name=1)


async def test_async_get_inventory_id_bad(requests_get_two_inventory):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(ValueError):
        await obj.get_inventory_id(name="Demo Inventory")

    with pytest.raises(TypeError):
        await obj.get_inventory_id(name=1)


async def test_async_create_inventory(requests_create_inventory, inventory_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    response = await obj.create_inventory(inventory=inventory_request_schema)


async def test_async_create_inventory_bad(requests_create_inventory):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.create_inventory(inventory="bad")


async def test_async_delete_inventory(requests_delete_inventory):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    response = await obj.delete_inventory(inventory_id=2)


async def test_async_delete_inventory_bad(requests_delete_inventory):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.delete_inventory(inventory_id="bad")


async def test_async_update_inventory_bad(requests_delete_inventory, inventory_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.update_inventory(inventory_id="bad", inventory=inventory_request_schema)

    with pytest.raises(TypeError):
        await obj.update_inventory(inventory_id=2, inventory="bad")


async def test_async_add_host_to_inventory(requests_add_host_inventory, inventory_host_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    response = await obj.add_host_to_inventory(inventory_id=38, host=inventory_host_request_schema)


async def test_async_add_host_to_inventory_bad(requests_add_host_inventory, inventory_host_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.add_host_to_inventory(inventory_id=38, host="bad")

    with pytest.raises(TypeError):
        await obj.add_host_to_inventory(inventory_id="bad", host=inventory_host_request_schema)


async def test_async_add_group_to_inventory(requests_add_group_inventory, inventory_group_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    response = await obj.add_group_to_inventory(inventory_id=38, group=inventory_group_request_schema)


async def test_async_add_group_to_inventory_bad(requests_add_group_inventory, inventory_group_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.add_group_to_inventory(inventory_id=38, group="bad")

    with pytest.raises(TypeError):
        await obj.add_group_to_inventory(inventory_id="bad", group=inventory_group_request_schema)


# ── Job Templates ─────────────────────────────────────────────────────────────


async def test_async_get_all_job_templates(requests_get_two_job_template):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_all_job_templates()


async def test_async_get_job_template(requests_get_singe_job_template):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_job_template(name="Demo Job Template")


async def test_async_get_job_template_bad(requests_get_singe_job_template):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.get_job_template(name=1)


async def test_async_get_job_template_id(requests_get_singe_job_template):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    result = await obj.get_job_template_id(name="Demo Job Template")
    assert result == 7


async def test_async_get_job_template_id_bad(requests_get_two_job_template):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(ValueError):
        await obj.get_job_template_id(name="Demo Job Template")

    with pytest.raises(TypeError):
        await obj.get_job_template_id(name=1)


async def test_async_launch_job_template(requests_job_template_job_launch):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.launch_job_template(job_template_id=7)


async def test_async_launch_job_template_bad(requests_job_template_job_launch):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.launch_job_template(job_template_id="bad")


# ── Jobs ──────────────────────────────────────────────────────────────────────


async def test_async_get_all_jobs(requests_all_jobs):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_all_jobs()


async def test_async_get_job(requests_single_job):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_job(job_id=35)


async def test_async_get_job_bad(requests_single_job):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.get_job(job_id="bad")


async def test_async_get_job_stdout(requests_job_stdout):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_job_stdout(job_id=35, output_format="txt")


async def test_async_get_job_stdout_bad(requests_job_stdout):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.get_job_stdout(job_id="bad", output_format="txt")


async def test_async_get_job_status(requests_single_job):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_job_status(job_id=35)


async def test_async_get_job_status_bad(requests_single_job):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.get_job_status(job_id="bad")


# ── Organizations ─────────────────────────────────────────────────────────────


async def test_async_get_all_organizations(requests_get_two_organization):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_all_organizations()


async def test_async_get_organization(requests_get_two_organization):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_organization(name="Default")


async def test_async_get_organization_bad(requests_get_two_organization):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.get_organization(name=1)


async def test_async_get_organization_id(requests_get_single_organization):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.get_organization_id(name="Default")


async def test_async_get_organization_id_bad(requests_get_two_organization):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(ValueError):
        await obj.get_organization_id(name="Default")

    with pytest.raises(TypeError):
        await obj.get_organization_id(name=1)


async def test_async_delete_organization(requests_delete_organization):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.delete_organization(organization_id=1)


async def test_async_delete_organization_bad(requests_delete_organization):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.delete_organization(organization_id="bad")


async def test_async_create_organization(requests_create_organization, organization_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    await obj.create_organization(organization=organization_request_schema)


async def test_async_create_organization_bad(requests_create_organization):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.create_organization(organization="bad")


async def test_async_update_organization_bad(requests_delete_organization, organization_request_schema):
    obj = AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test")
    with pytest.raises(TypeError):
        await obj.update_organization(organization_id="bad", organization=organization_request_schema)

    with pytest.raises(TypeError):
        await obj.update_organization(organization_id=1, organization="bad")


# ── Constructor validation ────────────────────────────────────────────────────


def test_async_aap_client_invalid_url_scheme():
    with pytest.raises(ValueError):
        AsyncAAPClient(base_url="ftp://localhost:5000", username="test", password="test")


def test_async_aap_client_invalid_ssl_verify():
    with pytest.raises(TypeError):
        AsyncAAPClient(base_url="https://localhost:5000", username="test", password="test", ssl_verify=123)


def test_async_aap_client_invalid_username():
    with pytest.raises(TypeError):
        AsyncAAPClient(base_url="https://localhost:5000", username=123, password="test")


def test_async_aap_client_invalid_password():
    with pytest.raises(TypeError):
        AsyncAAPClient(base_url="https://localhost:5000", username="test", password=123)
