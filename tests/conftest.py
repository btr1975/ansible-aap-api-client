import os, sys, json, re
import pytest
from niquests_mock import MockRouter


base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))

from ansible_aap_api_client import (
    InventoryRequestSchema,
    InventoryGroupRequestSchema,
    InventoryHostRequestSchema,
    OrganizationRequestSchema,
)


@pytest.fixture
def requests_mock_fixture():
    with MockRouter() as m:
        yield m


def get_fixture_data(file_name: str) -> str:
    """Get fixture data from a file

    :type file_name: str
    :param file_name: The name of the file to read

    :rtype: str
    :return: The data from the file
    """
    with open(os.path.join(base_path, "tests", "data", file_name), "r") as f:
        data = f.read()

    return data


@pytest.fixture
def inventory_request_schema() -> InventoryRequestSchema:
    return InventoryRequestSchema(
        name="test_inventory",
        description="This is a test inventory",
        organization=1,
        variables={"test_var": "test_value"},
    )


@pytest.fixture
def inventory_group_request_schema() -> InventoryGroupRequestSchema:
    return InventoryGroupRequestSchema(
        name="test_group",
        description="This is a test group",
        variables={"test_group_var": "test_group_value"},
    )


@pytest.fixture
def organization_request_schema() -> OrganizationRequestSchema:
    return OrganizationRequestSchema(
        name="test_inventory",
        description="This is a test inventory",
        max_hosts=50,
    )


@pytest.fixture
def inventory_host_request_schema() -> InventoryHostRequestSchema:
    return InventoryHostRequestSchema(
        name="test_host", description="This is a test host", variables={"test_host_var": "test_host_value"}
    )


@pytest.fixture
def requests_get_single_inventory(requests_mock_fixture):
    route = requests_mock_fixture.get(re.compile(r"https://localhost:5000/api/v2/inventories/"))
    route.respond(json=json.loads(get_fixture_data("single-inventory-response.json")))
    return route


@pytest.fixture
def requests_get_two_inventory(requests_mock_fixture):
    route = requests_mock_fixture.get(re.compile(r"https://localhost:5000/api/v2/inventories/"))
    route.respond(json=json.loads(get_fixture_data("two-inventory-response.json")))
    return route


@pytest.fixture
def requests_create_inventory(requests_mock_fixture):
    route = requests_mock_fixture.post("https://localhost:5000/api/v2/inventories/")
    route.respond(json=json.loads(get_fixture_data("created-inventory-response.json")))
    return route


@pytest.fixture
def requests_add_host_inventory(requests_mock_fixture):
    route = requests_mock_fixture.post("https://localhost:5000/api/v2/inventories/38/hosts/")
    route.respond(json=json.loads(get_fixture_data("added-host-to-inventory-response.json")))
    return route


@pytest.fixture
def requests_add_group_inventory(requests_mock_fixture):
    route = requests_mock_fixture.post("https://localhost:5000/api/v2/inventories/38/groups/")
    route.respond(json=json.loads(get_fixture_data("added-group-to-inventory-response.json")))
    return route


@pytest.fixture
def requests_delete_inventory(requests_mock_fixture):
    route = requests_mock_fixture.delete("https://localhost:5000/api/v2/inventories/2/")
    route.respond(status_code=202)
    return route


@pytest.fixture
def requests_get_single_group(niquests_mock):
    route = niquests_mock.get(re.compile(r"https://localhost:5000/api/v2/groups/"))
    route.respond(status_code=200, json=json.loads(get_fixture_data("single-group-response.json")))
    return route


@pytest.fixture
def requests_delete_group(niquests_mock):
    route = niquests_mock.delete("https://localhost:5000/api/v2/groups/2/")
    route.respond(status_code=202)
    return route


@pytest.fixture
def requests_get_two_group(niquests_mock):
    route = niquests_mock.get(re.compile(r"https://localhost:5000/api/v2/groups/"))
    route.respond(status_code=200, json=json.loads(get_fixture_data("two-group-response.json")))
    return route


@pytest.fixture
def requests_add_host_group(requests_mock_fixture):
    route = requests_mock_fixture.post("https://localhost:5000/api/v2/groups/2/hosts/")
    route.respond(json=json.loads(get_fixture_data("added-host-to-group-response.json")))
    return route


@pytest.fixture
def requests_get_single_host(requests_mock_fixture):
    route = requests_mock_fixture.get(re.compile(r"https://localhost:5000/api/v2/hosts/"))
    route.respond(json=json.loads(get_fixture_data("single-host-response.json")))
    return route


@pytest.fixture
def requests_get_two_host(requests_mock_fixture):
    route = requests_mock_fixture.get(re.compile(r"https://localhost:5000/api/v2/hosts/"))
    route.respond(json=json.loads(get_fixture_data("two-host-response.json")))
    return route


@pytest.fixture
def requests_delete_host(requests_mock_fixture):
    route = requests_mock_fixture.delete("https://localhost:5000/api/v2/hosts/2/")
    route.respond(status_code=202)
    return route


@pytest.fixture
def requests_single_job(requests_mock_fixture):
    route = requests_mock_fixture.get(re.compile(r"https://localhost:5000/api/v2/jobs/35/"))
    route.respond(json=json.loads(get_fixture_data("single-job-response.json")))
    return route


@pytest.fixture
def requests_job_stdout(requests_mock_fixture):
    route = requests_mock_fixture.get(re.compile(r"https://localhost:5000/api/v2/jobs/35/stdout/"))
    route.respond(text=get_fixture_data("job-stdout.txt"))
    return route


@pytest.fixture
def requests_get_single_organization(requests_mock_fixture):
    route = requests_mock_fixture.get(re.compile(r"https://localhost:5000/api/v2/organizations/"))
    route.respond(json=json.loads(get_fixture_data("single-host-response.json")))
    return route


@pytest.fixture
def requests_get_two_organization(requests_mock_fixture):
    route = requests_mock_fixture.get(re.compile(r"https://localhost:5000/api/v2/organizations/"))
    route.respond(json=json.loads(get_fixture_data("two-host-response.json")))
    return route


@pytest.fixture
def requests_delete_organization(requests_mock_fixture):
    route = requests_mock_fixture.delete("https://localhost:5000/api/v2/organizations/1/")
    route.respond(status_code=202)
    return route


@pytest.fixture
def requests_create_organization(requests_mock_fixture):
    route = requests_mock_fixture.post("https://localhost:5000/api/v2/organizations/")
    route.respond(json=json.loads(get_fixture_data("created-organization-response.json")))
    return route


@pytest.fixture
def requests_get_singe_job_template(requests_mock_fixture):
    route = requests_mock_fixture.get(re.compile(r"https://localhost:5000/api/v2/job_templates/"))
    route.respond(json=json.loads(get_fixture_data("single-job-template-response.json")))
    return route


@pytest.fixture
def requests_get_two_job_template(requests_mock_fixture):
    route = requests_mock_fixture.get(re.compile(r"https://localhost:5000/api/v2/job_templates/"))
    route.respond(json=json.loads(get_fixture_data("two-job-template-response.json")))
    return route


@pytest.fixture
def requests_job_template_job_launch(requests_mock_fixture):
    route = requests_mock_fixture.post("https://localhost:5000/api/v2/job_templates/7/launch/")
    route.respond(json=json.loads(get_fixture_data("job-launch-response.json")))
    return route
