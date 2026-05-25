from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_client_export_config import OpenVPNClientExportConfig


T = TypeVar("T", bound="ExportOpenVPNClientReq")


@_attrs_define
class ExportOpenVPNClientReq:
    """
    Attributes:
        config (OpenVPNClientExportConfig | Unset):
        type_ (str | Unset):
        userid (str | Unset):
        certid (str | Unset):
    """

    config: OpenVPNClientExportConfig | Unset = UNSET
    type_: str | Unset = UNSET
    userid: str | Unset = UNSET
    certid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        type_ = self.type_

        userid = self.userid

        certid = self.certid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if type_ is not UNSET:
            field_dict["type"] = type_
        if userid is not UNSET:
            field_dict["userid"] = userid
        if certid is not UNSET:
            field_dict["certid"] = certid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_vpn_client_export_config import OpenVPNClientExportConfig

        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: OpenVPNClientExportConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = OpenVPNClientExportConfig.from_dict(_config)

        type_ = d.pop("type", UNSET)

        userid = d.pop("userid", UNSET)

        certid = d.pop("certid", UNSET)

        export_open_vpn_client_req = cls(
            config=config,
            type_=type_,
            userid=userid,
            certid=certid,
        )

        export_open_vpn_client_req.additional_properties = d
        return export_open_vpn_client_req

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
