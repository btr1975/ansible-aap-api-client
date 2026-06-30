"""
Enumerations
"""

from enum import Enum


class OrganizationDataEnum(str, Enum):
    """Enumeration for Organization Data"""

    PROJECTS = "projects"
    INVENTORIES = "inventories"
    JOB_TEMPLATES = "job_templates"
