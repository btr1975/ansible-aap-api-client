"""
Tests for AsyncInventoryBuilder
"""

import pytest
from ansible_aap_api_client import AsyncInventoryBuilder
from ansible_aap_api_client import (
    InventoryRequestSchema,
    InventoryGroupRequestSchema,
    InventoryHostRequestSchema,
)


# ── Constructor ───────────────────────────────────────────────────────────────


def test_async_inventory_builder_init(inventory_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    assert obj.inventory_name == "test_inventory"
    assert obj.inventory_id is None


def test_async_inventory_builder_init_bad_inventory():
    with pytest.raises(TypeError):
        AsyncInventoryBuilder(
            base_url="https://localhost:5000",
            username="test",
            password="test",
            ssl_verify=False,
            inventory="bad",
        )


# ── add_ios_host_to_inventory ─────────────────────────────────────────────────


def test_add_ios_host_to_inventory(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_ios_host_to_inventory(host=inventory_host_request_schema)
    assert len(obj.ios_hosts) == 1


def test_add_ios_host_to_inventory_bad(inventory_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_ios_host_to_inventory(host="bad")


def test_add_ios_hosts_to_inventory(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_ios_hosts_to_inventory(hosts=[inventory_host_request_schema])
    assert len(obj.ios_hosts) == 1


def test_add_ios_hosts_to_inventory_bad(inventory_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_ios_hosts_to_inventory(hosts=["bad"])


# ── add_iosxr_host_to_inventory ───────────────────────────────────────────────


def test_add_iosxr_host_to_inventory(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_iosxr_host_to_inventory(host=inventory_host_request_schema)
    assert len(obj.iosxr_hosts) == 1


def test_add_iosxr_host_to_inventory_bad(inventory_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_iosxr_host_to_inventory(host="bad")


def test_add_iosxr_hosts_to_inventory(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_iosxr_hosts_to_inventory(hosts=[inventory_host_request_schema])
    assert len(obj.iosxr_hosts) == 1


def test_add_iosxr_hosts_to_inventory_bad(inventory_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_iosxr_hosts_to_inventory(hosts=["bad"])


# ── add_nxos_host_to_inventory ────────────────────────────────────────────────


def test_add_nxos_host_to_inventory(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_nxos_host_to_inventory(host=inventory_host_request_schema)
    assert len(obj.nxos_hosts) == 1


def test_add_nxos_host_to_inventory_bad(inventory_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_nxos_host_to_inventory(host="bad")


def test_add_nxos_hosts_to_inventory(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_nxos_hosts_to_inventory(hosts=[inventory_host_request_schema])
    assert len(obj.nxos_hosts) == 1


def test_add_nxos_hosts_to_inventory_bad(inventory_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_nxos_hosts_to_inventory(hosts=["bad"])


# ── add_eos_host_to_inventory ─────────────────────────────────────────────────


def test_add_eos_host_to_inventory(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_eos_host_to_inventory(host=inventory_host_request_schema)
    assert len(obj.eos_hosts) == 1


def test_add_eos_host_to_inventory_bad(inventory_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_eos_host_to_inventory(host="bad")


def test_add_eos_hosts_to_inventory(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_eos_hosts_to_inventory(hosts=[inventory_host_request_schema])
    assert len(obj.eos_hosts) == 1


def test_add_eos_hosts_to_inventory_bad(inventory_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_eos_hosts_to_inventory(hosts=["bad"])


# ── add_custom_group / host ───────────────────────────────────────────────────


def test_add_custom_group_to_inventory(inventory_request_schema, inventory_group_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_custom_group_to_inventory(group=inventory_group_request_schema)
    assert len(obj.custom_groups) == 1


def test_add_custom_group_to_inventory_bad(inventory_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_custom_group_to_inventory(group="bad")


def test_add_custom_groups_to_inventory(inventory_request_schema, inventory_group_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_custom_groups_to_inventory(groups=[inventory_group_request_schema])
    assert len(obj.custom_groups) == 1


def test_add_custom_groups_to_inventory_bad(inventory_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_custom_groups_to_inventory(groups=["bad"])


def test_add_host_to_custom_group_to_inventory(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_host_to_custom_group_to_inventory(group_name="my_group", host=inventory_host_request_schema)
    assert len(obj.custom_hosts) == 1


def test_add_host_to_custom_group_to_inventory_bad(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_host_to_custom_group_to_inventory(group_name=123, host=inventory_host_request_schema)

    with pytest.raises(TypeError):
        obj.add_host_to_custom_group_to_inventory(group_name="my_group", host="bad")


def test_add_hosts_to_custom_group_to_inventory(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    obj.add_hosts_to_custom_group_to_inventory(group_name="my_group", hosts=[inventory_host_request_schema])
    assert len(obj.custom_hosts) == 1


def test_add_hosts_to_custom_group_to_inventory_bad(inventory_request_schema, inventory_host_request_schema):
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )
    with pytest.raises(TypeError):
        obj.add_hosts_to_custom_group_to_inventory(group_name=123, hosts=[inventory_host_request_schema])

    with pytest.raises(TypeError):
        obj.add_hosts_to_custom_group_to_inventory(group_name="my_group", hosts=["bad"])


# ── run ───────────────────────────────────────────────────────────────────────


async def test_async_inventory_builder_run(
    requests_create_inventory, requests_add_group_inventory, inventory_request_schema
):
    """Test the full run cycle - creates inventory then adds the 4 default NOS groups."""
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )

    await obj.run()

    assert obj.inventory_id == 38
    assert obj.ios_group_id == 2
    assert obj.iosxr_group_id == 2
    assert obj.nxos_group_id == 2
    assert obj.eos_group_id == 2


async def test_async_inventory_builder_run_with_hosts(
    requests_create_inventory,
    requests_add_group_inventory,
    requests_add_host_group,
    inventory_request_schema,
    inventory_host_request_schema,
):
    """Test the run cycle with hosts added to each NOS group."""
    obj = AsyncInventoryBuilder(
        base_url="https://localhost:5000",
        username="test",
        password="test",
        ssl_verify=False,
        inventory=inventory_request_schema,
    )

    obj.add_ios_host_to_inventory(host=inventory_host_request_schema)
    obj.add_iosxr_host_to_inventory(host=inventory_host_request_schema)
    obj.add_nxos_host_to_inventory(host=inventory_host_request_schema)
    obj.add_eos_host_to_inventory(host=inventory_host_request_schema)

    await obj.run()

    assert obj.inventory_id == 38
