from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freeradiusauthorizedmac import Freeradiusauthorizedmac


T = TypeVar("T", bound="FreeradiusAuthorizedmacsList")


@_attrs_define
class FreeradiusAuthorizedmacsList:
    """
    Attributes:
        macs (list[Freeradiusauthorizedmac] | Unset):
    """

    macs: list[Freeradiusauthorizedmac] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        macs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.macs, Unset):
            macs = []
            for macs_item_data in self.macs:
                macs_item = macs_item_data.to_dict()
                macs.append(macs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if macs is not UNSET:
            field_dict["macs"] = macs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.freeradiusauthorizedmac import Freeradiusauthorizedmac

        d = dict(src_dict)
        _macs = d.pop("macs", UNSET)
        macs: list[Freeradiusauthorizedmac] | Unset = UNSET
        if _macs is not UNSET:
            macs = []
            for macs_item_data in _macs:
                macs_item = Freeradiusauthorizedmac.from_dict(macs_item_data)

                macs.append(macs_item)

        freeradius_authorizedmacs_list = cls(
            macs=macs,
        )

        freeradius_authorizedmacs_list.additional_properties = d
        return freeradius_authorizedmacs_list

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
