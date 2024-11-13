from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_basic_info import DeviceBasicInfo
    from ..models.software_package import SoftwarePackage


T = TypeVar("T", bound="InstallSoftwarePackageInfo")


@_attrs_define
class InstallSoftwarePackageInfo:
    """
    Attributes:
        package (Union[Unset, SoftwarePackage]):
        installable (Union[Unset, List['DeviceBasicInfo']]):
    """

    package: Union[Unset, "SoftwarePackage"] = UNSET
    installable: Union[Unset, List["DeviceBasicInfo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        package: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.package, Unset):
            package = self.package.to_dict()

        installable: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.installable, Unset):
            installable = []
            for installable_item_data in self.installable:
                installable_item = installable_item_data.to_dict()
                installable.append(installable_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if package is not UNSET:
            field_dict["package"] = package
        if installable is not UNSET:
            field_dict["installable"] = installable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_basic_info import DeviceBasicInfo
        from ..models.software_package import SoftwarePackage

        d = src_dict.copy()
        _package = d.pop("package", UNSET)
        package: Union[Unset, SoftwarePackage]
        if isinstance(_package, Unset):
            package = UNSET
        else:
            package = SoftwarePackage.from_dict(_package)

        installable = []
        _installable = d.pop("installable", UNSET)
        for installable_item_data in _installable or []:
            installable_item = DeviceBasicInfo.from_dict(installable_item_data)

            installable.append(installable_item)

        install_software_package_info = cls(
            package=package,
            installable=installable,
        )

        install_software_package_info.additional_properties = d
        return install_software_package_info

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
