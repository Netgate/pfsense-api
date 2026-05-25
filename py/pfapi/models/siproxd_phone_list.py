from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.siproxd_phone import SiproxdPhone


T = TypeVar("T", bound="SiproxdPhoneList")


@_attrs_define
class SiproxdPhoneList:
    """
    Attributes:
        phones (list[SiproxdPhone] | Unset):
    """

    phones: list[SiproxdPhone] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phones: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phones, Unset):
            phones = []
            for phones_item_data in self.phones:
                phones_item = phones_item_data.to_dict()
                phones.append(phones_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phones is not UNSET:
            field_dict["phones"] = phones

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.siproxd_phone import SiproxdPhone

        d = dict(src_dict)
        _phones = d.pop("phones", UNSET)
        phones: list[SiproxdPhone] | Unset = UNSET
        if _phones is not UNSET:
            phones = []
            for phones_item_data in _phones:
                phones_item = SiproxdPhone.from_dict(phones_item_data)

                phones.append(phones_item)

        siproxd_phone_list = cls(
            phones=phones,
        )

        siproxd_phone_list.additional_properties = d
        return siproxd_phone_list

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
