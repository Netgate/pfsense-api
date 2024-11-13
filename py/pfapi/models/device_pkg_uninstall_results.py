from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_pkg_uninstall_results_devices import DevicePkgUninstallResultsDevices


T = TypeVar("T", bound="DevicePkgUninstallResults")


@_attrs_define
class DevicePkgUninstallResults:
    """
    Attributes:
        devices (Union[Unset, DevicePkgUninstallResultsDevices]):
    """

    devices: Union[Unset, "DevicePkgUninstallResultsDevices"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        devices: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.devices, Unset):
            devices = self.devices.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.device_pkg_uninstall_results_devices import DevicePkgUninstallResultsDevices

        d = src_dict.copy()
        _devices = d.pop("devices", UNSET)
        devices: Union[Unset, DevicePkgUninstallResultsDevices]
        if isinstance(_devices, Unset):
            devices = UNSET
        else:
            devices = DevicePkgUninstallResultsDevices.from_dict(_devices)

        device_pkg_uninstall_results = cls(
            devices=devices,
        )

        device_pkg_uninstall_results.additional_properties = d
        return device_pkg_uninstall_results

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
