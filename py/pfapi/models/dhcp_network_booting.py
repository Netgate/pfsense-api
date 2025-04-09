from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpNetworkBooting")


@_attrs_define
class DhcpNetworkBooting:
    """
    Attributes:
        enable (bool):
        next_server (Union[Unset, str]):
        default_bios_name (Union[Unset, str]):
        uefi_32_filename (Union[Unset, str]):
        uefi_64_filename (Union[Unset, str]):
        arm_32_filename (Union[Unset, str]):
        arm_64_filename (Union[Unset, str]):
        uefi_http_boot_url (Union[Unset, str]):
        root_path (Union[Unset, str]):
        bootfile_url (Union[Unset, str]):
    """

    enable: bool
    next_server: Union[Unset, str] = UNSET
    default_bios_name: Union[Unset, str] = UNSET
    uefi_32_filename: Union[Unset, str] = UNSET
    uefi_64_filename: Union[Unset, str] = UNSET
    arm_32_filename: Union[Unset, str] = UNSET
    arm_64_filename: Union[Unset, str] = UNSET
    uefi_http_boot_url: Union[Unset, str] = UNSET
    root_path: Union[Unset, str] = UNSET
    bootfile_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        next_server = self.next_server

        default_bios_name = self.default_bios_name

        uefi_32_filename = self.uefi_32_filename

        uefi_64_filename = self.uefi_64_filename

        arm_32_filename = self.arm_32_filename

        arm_64_filename = self.arm_64_filename

        uefi_http_boot_url = self.uefi_http_boot_url

        root_path = self.root_path

        bootfile_url = self.bootfile_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if next_server is not UNSET:
            field_dict["next_server"] = next_server
        if default_bios_name is not UNSET:
            field_dict["default_bios_name"] = default_bios_name
        if uefi_32_filename is not UNSET:
            field_dict["uefi_32_filename"] = uefi_32_filename
        if uefi_64_filename is not UNSET:
            field_dict["uefi_64_filename"] = uefi_64_filename
        if arm_32_filename is not UNSET:
            field_dict["arm_32_filename"] = arm_32_filename
        if arm_64_filename is not UNSET:
            field_dict["arm_64_filename"] = arm_64_filename
        if uefi_http_boot_url is not UNSET:
            field_dict["uefi_http_boot_url"] = uefi_http_boot_url
        if root_path is not UNSET:
            field_dict["root_path"] = root_path
        if bootfile_url is not UNSET:
            field_dict["bootfile_url"] = bootfile_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable")

        next_server = d.pop("next_server", UNSET)

        default_bios_name = d.pop("default_bios_name", UNSET)

        uefi_32_filename = d.pop("uefi_32_filename", UNSET)

        uefi_64_filename = d.pop("uefi_64_filename", UNSET)

        arm_32_filename = d.pop("arm_32_filename", UNSET)

        arm_64_filename = d.pop("arm_64_filename", UNSET)

        uefi_http_boot_url = d.pop("uefi_http_boot_url", UNSET)

        root_path = d.pop("root_path", UNSET)

        bootfile_url = d.pop("bootfile_url", UNSET)

        dhcp_network_booting = cls(
            enable=enable,
            next_server=next_server,
            default_bios_name=default_bios_name,
            uefi_32_filename=uefi_32_filename,
            uefi_64_filename=uefi_64_filename,
            arm_32_filename=arm_32_filename,
            arm_64_filename=arm_64_filename,
            uefi_http_boot_url=uefi_http_boot_url,
            root_path=root_path,
            bootfile_url=bootfile_url,
        )

        dhcp_network_booting.additional_properties = d
        return dhcp_network_booting

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
