from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_basic_info import DeviceBasicInfo


T = TypeVar("T", bound="SoftwarePackage")


@_attrs_define
class SoftwarePackage:
    """
    Attributes:
        name (str | Unset): package name
        id (str | Unset): package identifier
        category (str | Unset): software category, e.g. security, netA
        description (str | Unset): description of software
        local_version (str | Unset): version cached in controller
        avail_version (str | Unset): version available in remote repo
        dependencies (list[str] | Unset):
        filename (str | Unset): archive name
        checksum (str | Unset): checksum of package
        os_type (str | Unset): correlates with device_type
        os_version (str | Unset):
        installed_on (list[DeviceBasicInfo] | Unset):
    """

    name: str | Unset = UNSET
    id: str | Unset = UNSET
    category: str | Unset = UNSET
    description: str | Unset = UNSET
    local_version: str | Unset = UNSET
    avail_version: str | Unset = UNSET
    dependencies: list[str] | Unset = UNSET
    filename: str | Unset = UNSET
    checksum: str | Unset = UNSET
    os_type: str | Unset = UNSET
    os_version: str | Unset = UNSET
    installed_on: list[DeviceBasicInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        category = self.category

        description = self.description

        local_version = self.local_version

        avail_version = self.avail_version

        dependencies: list[str] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        filename = self.filename

        checksum = self.checksum

        os_type = self.os_type

        os_version = self.os_version

        installed_on: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.installed_on, Unset):
            installed_on = []
            for installed_on_item_data in self.installed_on:
                installed_on_item = installed_on_item_data.to_dict()
                installed_on.append(installed_on_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if id is not UNSET:
            field_dict["id"] = id
        if category is not UNSET:
            field_dict["category"] = category
        if description is not UNSET:
            field_dict["description"] = description
        if local_version is not UNSET:
            field_dict["local_version"] = local_version
        if avail_version is not UNSET:
            field_dict["avail_version"] = avail_version
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if filename is not UNSET:
            field_dict["filename"] = filename
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if os_type is not UNSET:
            field_dict["os_type"] = os_type
        if os_version is not UNSET:
            field_dict["os_version"] = os_version
        if installed_on is not UNSET:
            field_dict["installed_on"] = installed_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_basic_info import DeviceBasicInfo

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        category = d.pop("category", UNSET)

        description = d.pop("description", UNSET)

        local_version = d.pop("local_version", UNSET)

        avail_version = d.pop("avail_version", UNSET)

        dependencies = cast(list[str], d.pop("dependencies", UNSET))

        filename = d.pop("filename", UNSET)

        checksum = d.pop("checksum", UNSET)

        os_type = d.pop("os_type", UNSET)

        os_version = d.pop("os_version", UNSET)

        _installed_on = d.pop("installed_on", UNSET)
        installed_on: list[DeviceBasicInfo] | Unset = UNSET
        if _installed_on is not UNSET:
            installed_on = []
            for installed_on_item_data in _installed_on:
                installed_on_item = DeviceBasicInfo.from_dict(installed_on_item_data)

                installed_on.append(installed_on_item)

        software_package = cls(
            name=name,
            id=id,
            category=category,
            description=description,
            local_version=local_version,
            avail_version=avail_version,
            dependencies=dependencies,
            filename=filename,
            checksum=checksum,
            os_type=os_type,
            os_version=os_version,
            installed_on=installed_on,
        )

        software_package.additional_properties = d
        return software_package

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
