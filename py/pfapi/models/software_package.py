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
        name (Union[Unset, str]):
        id (Union[Unset, str]):
        category (Union[Unset, str]):
        description (Union[Unset, str]):
        local_version (Union[Unset, str]):
        avail_version (Union[Unset, str]):
        dependencies (Union[Unset, List[str]]):
        filename (Union[Unset, str]):
        checksum (Union[Unset, str]):
        os_type (Union[Unset, str]):
        os_version (Union[Unset, str]):
        installed_on (Union[Unset, List['DeviceBasicInfo']]):
    """

    name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    local_version: Union[Unset, str] = UNSET
    avail_version: Union[Unset, str] = UNSET
    dependencies: Union[Unset, List[str]] = UNSET
    filename: Union[Unset, str] = UNSET
    checksum: Union[Unset, str] = UNSET
    os_type: Union[Unset, str] = UNSET
    os_version: Union[Unset, str] = UNSET
    installed_on: Union[Unset, List["DeviceBasicInfo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        id = self.id

        category = self.category

        description = self.description

        local_version = self.local_version

        avail_version = self.avail_version

        dependencies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = self.dependencies

        filename = self.filename

        checksum = self.checksum

        os_type = self.os_type

        os_version = self.os_version

        installed_on: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.installed_on, Unset):
            installed_on = []
            for installed_on_item_data in self.installed_on:
                installed_on_item = installed_on_item_data.to_dict()
                installed_on.append(installed_on_item)

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_basic_info import DeviceBasicInfo

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        id = d.pop("id", UNSET)

        category = d.pop("category", UNSET)

        description = d.pop("description", UNSET)

        local_version = d.pop("local_version", UNSET)

        avail_version = d.pop("avail_version", UNSET)

        dependencies = cast(List[str], d.pop("dependencies", UNSET))

        filename = d.pop("filename", UNSET)

        checksum = d.pop("checksum", UNSET)

        os_type = d.pop("os_type", UNSET)

        os_version = d.pop("os_version", UNSET)

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
