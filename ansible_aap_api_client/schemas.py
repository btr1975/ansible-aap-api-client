"""
Data schemas
"""

from typing import Union, Optional, Literal
import json
from dataclasses import dataclass


@dataclass
class _BaseSchema:
    """Base Dataclass Schema"""

    def dict(self) -> dict:
        """Get a dict representation of the Dataclass

        :returns: A dict representation of the Dataclass
        """
        return self.__dict__

    def json(self, pretty=False) -> str:
        """Get a JSON representation of the Dataclass

        :param pretty: Get pretty JSON

        :returns: A JSON representation of the Dataclass
        """
        if pretty:
            indent = 4

        else:
            indent = None

        return json.dumps(self.dict(), indent=indent)

    @staticmethod
    def validate_string(name: str, value: str) -> None:
        """Validate a string

        :param value: Value to validate
        :param name: Name of the value
        """
        if not isinstance(value, str):
            raise TypeError(f"{name} must be a string, but received {type(value)}")

    @staticmethod
    def validate_boolean(name: str, value: bool) -> None:
        """Validate a boolean

        :param value: Value to validate
        :param name: Name of the value
        """
        if not isinstance(value, bool):
            raise TypeError(f"{name} must be a boolean, but received {type(value)}")

    @staticmethod
    def validate_integer(name: str, value: int) -> None:
        """Validate an integer

        :param value: Value to validate
        :param name: Name of the value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer, but received {type(value)}")


@dataclass
class InventoryRequestSchema(_BaseSchema):
    """Inventory Request Schema

    :cvar name: Name of the Inventory
    :cvar description: Description of the Inventory
    :cvar organization: Organization the Inventory belongs to
    :cvar kind: Kind of the Inventory
    :cvar host_filter: Host filter of the Inventory
    :cvar variables: Variables of the all group of the Inventory in JSON or YAML format
    :cvar prevent_instance_group_fallback: Whether to prevent fallback
    """

    name: str
    description: str
    organization: int
    kind: Optional[str] = ""
    host_filter: Optional[str] = None
    variables: Optional[Union[str, dict]] = "---"
    prevent_instance_group_fallback: Optional[bool] = False

    def __post_init__(self):
        if isinstance(self.variables, dict):
            self.variables = json.dumps(self.variables)

        self.validate_string("name", self.name)
        self.validate_string("description", self.description)
        self.validate_integer("organization", self.organization)
        self.validate_string("kind", self.kind)

        if self.host_filter:
            self.validate_string("host_filter", self.host_filter)

        self.validate_boolean("prevent_instance_group_fallback", self.prevent_instance_group_fallback)


@dataclass
class InventoryHostRequestSchema(_BaseSchema):
    """Inventory Host Request Schema

    :cvar name: Name of the Host
    :cvar description: Description of the Host
    :cvar enabled: Whether to enable the Host
    :cvar instance_id: Instance ID of the Host
    :cvar variables: Variables of the host in JSON or YAML format
    """

    name: str
    description: str
    enabled: Optional[bool] = True
    instance_id: Optional[str] = ""
    variables: Optional[Union[str, dict]] = "---"

    def __post_init__(self):
        if isinstance(self.variables, dict):
            self.variables = json.dumps(self.variables)

        self.validate_string("name", self.name)
        self.validate_string("description", self.description)
        self.validate_boolean("enabled", self.enabled)
        self.validate_string("instance_id", self.instance_id)


@dataclass
class InventoryGroupRequestSchema(_BaseSchema):
    """Inventory Group Request Schema

    :cvar name: Name of the Group
    :cvar description: Description of the Group
    :cvar variables: Variables of the group in JSON or YAML format
    """

    name: str
    description: str
    variables: Optional[Union[str, dict]] = "---"

    def __post_init__(self):
        if isinstance(self.variables, dict):
            self.variables = json.dumps(self.variables)

        self.validate_string("name", self.name)
        self.validate_string("description", self.description)


@dataclass
class OrganizationRequestSchema(_BaseSchema):
    """Organization Request Schema

    :cvar name: Name of the Group
    :cvar description: Description of the Group
    :cvar max_hosts: The maximum hosts 0 means unlimited
    :cvar default_environment: The id of the execution environment
    """

    name: str
    description: str
    max_hosts: Optional[int] = 0
    default_environment: Optional[int] = None

    def __post_init__(self):
        self.validate_string("name", self.name)
        self.validate_string("description", self.description)
        self.validate_integer("max_hosts", self.max_hosts)

        if self.default_environment:
            self.validate_integer("default_environment", self.default_environment)


@dataclass
class JobTemplateRequestSchema(_BaseSchema):  # pylint: disable=too-many-instance-attributes
    """Job Template Request Schema"""

    name: Optional[str] = ""
    description: Optional[str] = ""
    job_type: Optional[Literal["run", "check"]] = "run"
    inventory: Optional[int] = None
    project: Optional[int] = None
    playbook: Optional[str] = ""
    scm_branch: Optional[str] = ""
    forks: Optional[int] = 0
    limit: Optional[str] = ""
    verbosity: Optional[Literal[0, 1, 2, 3, 4, 5]] = 0
    extra_vars: Optional[str] = ""
    job_tags: Optional[str] = ""
    force_handlers: Optional[bool] = False
    skip_tags: Optional[str] = ""
    start_at_task: Optional[str] = ""
    timeout: Optional[int] = 0
    use_fact_cache: Optional[bool] = False
    execution_environment: Optional[int] = None
    host_config_key: Optional[str] = ""
    ask_scm_branch_on_launch: Optional[bool] = False
    ask_diff_mode_on_launch: Optional[bool] = False
    ask_variables_on_launch: Optional[bool] = False
    ask_limit_on_launch: Optional[bool] = False
    ask_tags_on_launch: Optional[bool] = False
    ask_skip_tags_on_launch: Optional[bool] = False
    ask_job_type_on_launch: Optional[bool] = False
    ask_verbosity_on_launch: Optional[bool] = False
    ask_inventory_on_launch: Optional[bool] = False
    ask_credential_on_launch: Optional[bool] = False
    ask_execution_environment_on_launch: Optional[bool] = False
    ask_labels_on_launch: Optional[bool] = False
    ask_forks_on_launch: Optional[bool] = False
    ask_job_slice_count_on_launch: Optional[bool] = False
    ask_timeout_on_launch: Optional[bool] = False
    ask_instance_groups_on_launch: Optional[bool] = False
    survey_enabled: Optional[bool] = False
    become_enabled: Optional[bool] = False
    diff_mode: Optional[bool] = False
    allow_simultaneous: Optional[bool] = False
    job_slice_count: Optional[int] = 1
    webhook_service: Optional[Literal["", "github", "gitlab", "bitbucket_dc"]] = None
    webhook_credential: Optional[int] = None
    prevent_instance_group_fallback: Optional[bool] = False


@dataclass
class JobManagementRunStatus(_BaseSchema):
    """Job run status schema

    :cvar status: The job status
    :cvar job_id: The Job ID
    """

    status: str
    job_id: int

    def __post_init__(self):
        self.validate_string("status", self.status)
        self.validate_integer("job_id", self.job_id)
