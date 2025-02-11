from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DhcpNetworkBooting")


@_attrs_define
class DhcpNetworkBooting:
    """
    Attributes:
        enable (bool):
        next_server (str):
        default_bios_name (str):
        uefi_32_filename (str):
        uefi_64_filename (str):
        arm_32_filename (str):
        arm_64_filename (str):
        uefi_http_boot_url (str):
        root_path (str):
        bootfile_url (str):
    """

    enable: bool
    next_server: str
    default_bios_name: str
    uefi_32_filename: str
    uefi_64_filename: str
    arm_32_filename: str
    arm_64_filename: str
    uefi_http_boot_url: str
    root_path: str
    bootfile_url: str
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
                "next_server": next_server,
                "default_bios_name": default_bios_name,
                "uefi_32_filename": uefi_32_filename,
                "uefi_64_filename": uefi_64_filename,
                "arm_32_filename": arm_32_filename,
                "arm_64_filename": arm_64_filename,
                "uefi_http_boot_url": uefi_http_boot_url,
                "root_path": root_path,
                "bootfile_url": bootfile_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enable = d.pop("enable")

        next_server = d.pop("next_server")

        default_bios_name = d.pop("default_bios_name")

        uefi_32_filename = d.pop("uefi_32_filename")

        uefi_64_filename = d.pop("uefi_64_filename")

        arm_32_filename = d.pop("arm_32_filename")

        arm_64_filename = d.pop("arm_64_filename")

        uefi_http_boot_url = d.pop("uefi_http_boot_url")

        root_path = d.pop("root_path")

        bootfile_url = d.pop("bootfile_url")

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
