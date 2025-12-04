from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pfsense_result import PfsenseResult


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """
    Attributes:
        errcode (int | Unset): Error code
        errlevel (str | Unset): Error level - debug, info, error (default)
        errmsg (str | Unset): Error message
        alerts (PfsenseResult | Unset):
    """

    errcode: int | Unset = UNSET
    errlevel: str | Unset = UNSET
    errmsg: str | Unset = UNSET
    alerts: PfsenseResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errcode = self.errcode

        errlevel = self.errlevel

        errmsg = self.errmsg

        alerts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = self.alerts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errcode is not UNSET:
            field_dict["errcode"] = errcode
        if errlevel is not UNSET:
            field_dict["errlevel"] = errlevel
        if errmsg is not UNSET:
            field_dict["errmsg"] = errmsg
        if alerts is not UNSET:
            field_dict["alerts"] = alerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pfsense_result import PfsenseResult

        d = dict(src_dict)
        errcode = d.pop("errcode", UNSET)

        errlevel = d.pop("errlevel", UNSET)

        errmsg = d.pop("errmsg", UNSET)

        _alerts = d.pop("alerts", UNSET)
        alerts: PfsenseResult | Unset
        if isinstance(_alerts, Unset):
            alerts = UNSET
        else:
            alerts = PfsenseResult.from_dict(_alerts)

        error = cls(
            errcode=errcode,
            errlevel=errlevel,
            errmsg=errmsg,
            alerts=alerts,
        )

        error.additional_properties = d
        return error

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
