from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

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
        name (str):
        id (str):
        category (str):
        description (str):
        local_version (str):
        avail_version (str):
        filename (str):
        checksum (str):
        os_type (str):
        os_version (str):
        dependencies (Union[Unset, List[str]]):
        installed_on (Union[Unset, List['DeviceBasicInfo']]):
    """

    name: str
    id: str
    category: str
    description: str
    local_version: str
    avail_version: str
    filename: str
    checksum: str
    os_type: str
    os_version: str
    dependencies: Union[Unset, List[str]] = UNSET
    installed_on: Union[Unset, List["DeviceBasicInfo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        id = self.id

        category = self.category

        description = self.description

        local_version = self.local_version

        avail_version = self.avail_version

        filename = self.filename

        checksum = self.checksum

        os_type = self.os_type

        os_version = self.os_version

        dependencies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        installed_on: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.installed_on, Unset):
            installed_on = []
            for installed_on_item_data in self.installed_on:
                installed_on_item = installed_on_item_data.to_dict()
                installed_on.append(installed_on_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "category": category,
                "description": description,
                "local_version": local_version,
                "avail_version": avail_version,
                "filename": filename,
                "checksum": checksum,
                "os_type": os_type,
                "os_version": os_version,
            }
        )
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if installed_on is not UNSET:
            field_dict["installed_on"] = installed_on

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_basic_info import DeviceBasicInfo

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id")

        category = d.pop("category")

        description = d.pop("description")

        local_version = d.pop("local_version")

        avail_version = d.pop("avail_version")

        filename = d.pop("filename")

        checksum = d.pop("checksum")

        os_type = d.pop("os_type")

        os_version = d.pop("os_version")

        dependencies = cast(List[str], d.pop("dependencies", UNSET))

        installed_on = []
        _installed_on = d.pop("installed_on", UNSET)
        for installed_on_item_data in _installed_on or []:
            installed_on_item = DeviceBasicInfo.from_dict(installed_on_item_data)

            installed_on.append(installed_on_item)

        software_package = cls(
            name=name,
            id=id,
            category=category,
            description=description,
            local_version=local_version,
            avail_version=avail_version,
            filename=filename,
            checksum=checksum,
            os_type=os_type,
            os_version=os_version,
            dependencies=dependencies,
            installed_on=installed_on,
        )

        software_package.additional_properties = d
        return software_package

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
