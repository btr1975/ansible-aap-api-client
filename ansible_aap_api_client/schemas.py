"""
Data schemas
"""

from typing import Union, Optional
import json
from dataclasses import dataclass


@dataclass
class _BaseSchema:
    """Base Dataclass Schema"""

    def dict(self) -> dict:
        """Get a dict representation of the Dataclass

        :rtype: dict
        :returns: A dict representation of the Dataclass
        """
        return self.__dict__

    def json(self, pretty=False) -> str:
        """Get a JSON representation of the Dataclass

        :type pretty: bool
        :param pretty: Get pretty JSON

        :rtype: str
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

        :type value: str
        :param value: Value to validate
        :type name: str
        :param name: Name of the value
        """
        if not isinstance(value, str):
            raise TypeError(f"{name} must be a string, but received {type(value)}")

    @staticmethod
    def validate_boolean(name: str, value: bool) -> None:
        """Validate a boolean

        :type value: bool
        :param value: Value to validate
        :type name: str
        :param name: Name of the value
        """
        if not isinstance(value, bool):
            raise TypeError(f"{name} must be a boolean, but received {type(value)}")

    @staticmethod
    def validate_integer(name: str, value: int) -> None:
        """Validate an integer

        :type value: int
        :param value: Value to validate
        :type name: str
        :param name: Name of the value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer, but received {type(value)}")


@dataclass
class InventoryRequestSchema(_BaseSchema):
    """Inventory Request Schema

    :type name: str
    :cvar name: Name of the Inventory
    :type description: str
    :cvar description: Description of the Inventory
    :type organization: str
    :cvar organization: Organization the Inventory belongs to
    :type kind: Optional[str] = ""
    :cvar kind: Kind of the Inventory
    :type host_filter: Optional[str] = ""
    :cvar host_filter: Host filter of the Inventory
    :type variables: Optional[Union[str, dict]] = "---"
    :cvar variables: Variables of the all group of the Inventory in JSON or YAML format
    :type prevent_instance_group_fallback: Optional[bool] = False
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

    :type name: str
    :cvar name: Name of the Host
    :type description: str
    :cvar description: Description of the Host
    :type enabled: Optional[bool] = True
    :cvar enabled: Whether to enable the Host
    :type instance_id: Optional[str] = ""
    :cvar instance_id: Instance ID of the Host
    :type variables: Optional[Union[str, dict]] = "---"
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

    :type name: str
    :cvar name: Name of the Group
    :type description: str
    :cvar description: Description of the Group
    :type variables: Optional[Union[str, dict]] = "---"
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
