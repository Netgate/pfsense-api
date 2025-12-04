from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rfc_item import RFCItem


T = TypeVar("T", bound="RFCItemList")


@_attrs_define
class RFCItemList:
    """
    Attributes:
        dnsupdate (list[RFCItem] | Unset):
    """

    dnsupdate: list[RFCItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dnsupdate: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dnsupdate, Unset):
            dnsupdate = []
            for dnsupdate_item_data in self.dnsupdate:
                dnsupdate_item = dnsupdate_item_data.to_dict()
                dnsupdate.append(dnsupdate_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dnsupdate is not UNSET:
            field_dict["dnsupdate"] = dnsupdate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rfc_item import RFCItem

        d = dict(src_dict)
        _dnsupdate = d.pop("dnsupdate", UNSET)
        dnsupdate: list[RFCItem] | Unset = UNSET
        if _dnsupdate is not UNSET:
            dnsupdate = []
            for dnsupdate_item_data in _dnsupdate:
                dnsupdate_item = RFCItem.from_dict(dnsupdate_item_data)

                dnsupdate.append(dnsupdate_item)

        rfc_item_list = cls(
            dnsupdate=dnsupdate,
        )

        rfc_item_list.additional_properties = d
        return rfc_item_list

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
