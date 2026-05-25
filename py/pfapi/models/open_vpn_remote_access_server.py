from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_client_export_user_info import OpenVPNClientExportUserInfo


T = TypeVar("T", bound="OpenVPNRemoteAccessServer")


@_attrs_define
class OpenVPNRemoteAccessServer:
    """
    Attributes:
        vpnid (str | Unset):
        desc (str | Unset):
        mode (str | Unset):
        user_list (list[OpenVPNClientExportUserInfo] | Unset):
        cert_list (list[OpenVPNClientExportUserInfo] | Unset):
    """

    vpnid: str | Unset = UNSET
    desc: str | Unset = UNSET
    mode: str | Unset = UNSET
    user_list: list[OpenVPNClientExportUserInfo] | Unset = UNSET
    cert_list: list[OpenVPNClientExportUserInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpnid = self.vpnid

        desc = self.desc

        mode = self.mode

        user_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_list, Unset):
            user_list = []
            for user_list_item_data in self.user_list:
                user_list_item = user_list_item_data.to_dict()
                user_list.append(user_list_item)

        cert_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cert_list, Unset):
            cert_list = []
            for cert_list_item_data in self.cert_list:
                cert_list_item = cert_list_item_data.to_dict()
                cert_list.append(cert_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpnid is not UNSET:
            field_dict["vpnid"] = vpnid
        if desc is not UNSET:
            field_dict["desc"] = desc
        if mode is not UNSET:
            field_dict["mode"] = mode
        if user_list is not UNSET:
            field_dict["user_list"] = user_list
        if cert_list is not UNSET:
            field_dict["cert_list"] = cert_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_vpn_client_export_user_info import OpenVPNClientExportUserInfo

        d = dict(src_dict)
        vpnid = d.pop("vpnid", UNSET)

        desc = d.pop("desc", UNSET)

        mode = d.pop("mode", UNSET)

        _user_list = d.pop("user_list", UNSET)
        user_list: list[OpenVPNClientExportUserInfo] | Unset = UNSET
        if _user_list is not UNSET:
            user_list = []
            for user_list_item_data in _user_list:
                user_list_item = OpenVPNClientExportUserInfo.from_dict(user_list_item_data)

                user_list.append(user_list_item)

        _cert_list = d.pop("cert_list", UNSET)
        cert_list: list[OpenVPNClientExportUserInfo] | Unset = UNSET
        if _cert_list is not UNSET:
            cert_list = []
            for cert_list_item_data in _cert_list:
                cert_list_item = OpenVPNClientExportUserInfo.from_dict(cert_list_item_data)

                cert_list.append(cert_list_item)

        open_vpn_remote_access_server = cls(
            vpnid=vpnid,
            desc=desc,
            mode=mode,
            user_list=user_list,
            cert_list=cert_list,
        )

        open_vpn_remote_access_server.additional_properties = d
        return open_vpn_remote_access_server

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
