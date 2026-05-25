from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_ftp_client_bounce_to import SnortInspFtpClientBounceTo


T = TypeVar("T", bound="SnortInspFtpClient")


@_attrs_define
class SnortInspFtpClient:
    """
    Attributes:
        bounce (bool | Unset): check for bounces; default false
        bounce_to (list[SnortInspFtpClientBounceTo] | Unset):
        ignore_telnet_erase_cmds (bool | Unset): ignore erase character and erase line commands when normalizing;
            default false
        max_resp_len (int | Unset): maximum FTP response accepted by client { 0:max32 }; default 4294967295
        telnet_cmds (bool | Unset): detect Telnet escape sequences on FTP control channel; default false
    """

    bounce: bool | Unset = UNSET
    bounce_to: list[SnortInspFtpClientBounceTo] | Unset = UNSET
    ignore_telnet_erase_cmds: bool | Unset = UNSET
    max_resp_len: int | Unset = UNSET
    telnet_cmds: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bounce = self.bounce

        bounce_to: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bounce_to, Unset):
            bounce_to = []
            for bounce_to_item_data in self.bounce_to:
                bounce_to_item = bounce_to_item_data.to_dict()
                bounce_to.append(bounce_to_item)

        ignore_telnet_erase_cmds = self.ignore_telnet_erase_cmds

        max_resp_len = self.max_resp_len

        telnet_cmds = self.telnet_cmds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bounce is not UNSET:
            field_dict["bounce"] = bounce
        if bounce_to is not UNSET:
            field_dict["bounce_to"] = bounce_to
        if ignore_telnet_erase_cmds is not UNSET:
            field_dict["ignore_telnet_erase_cmds"] = ignore_telnet_erase_cmds
        if max_resp_len is not UNSET:
            field_dict["max_resp_len"] = max_resp_len
        if telnet_cmds is not UNSET:
            field_dict["telnet_cmds"] = telnet_cmds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_ftp_client_bounce_to import SnortInspFtpClientBounceTo

        d = dict(src_dict)
        bounce = d.pop("bounce", UNSET)

        _bounce_to = d.pop("bounce_to", UNSET)
        bounce_to: list[SnortInspFtpClientBounceTo] | Unset = UNSET
        if _bounce_to is not UNSET:
            bounce_to = []
            for bounce_to_item_data in _bounce_to:
                bounce_to_item = SnortInspFtpClientBounceTo.from_dict(bounce_to_item_data)

                bounce_to.append(bounce_to_item)

        ignore_telnet_erase_cmds = d.pop("ignore_telnet_erase_cmds", UNSET)

        max_resp_len = d.pop("max_resp_len", UNSET)

        telnet_cmds = d.pop("telnet_cmds", UNSET)

        snort_insp_ftp_client = cls(
            bounce=bounce,
            bounce_to=bounce_to,
            ignore_telnet_erase_cmds=ignore_telnet_erase_cmds,
            max_resp_len=max_resp_len,
            telnet_cmds=telnet_cmds,
        )

        snort_insp_ftp_client.additional_properties = d
        return snort_insp_ftp_client

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
