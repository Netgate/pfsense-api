from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoucherRoll")


@_attrs_define
class VoucherRoll:
    """
    Attributes:
        zone (Union[Unset, str]):
        number (Union[Unset, int]):
        minutes (Union[Unset, int]):
        descr (Union[Unset, str]):
        count (Union[Unset, str]):
        used (Union[Unset, str]):
        active (Union[Unset, bool]):
        lastsync (Union[Unset, int]):
    """

    zone: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    minutes: Union[Unset, int] = UNSET
    descr: Union[Unset, str] = UNSET
    count: Union[Unset, str] = UNSET
    used: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    lastsync: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        zone = self.zone

        number = self.number

        minutes = self.minutes

        descr = self.descr

        count = self.count

        used = self.used

        active = self.active

        lastsync = self.lastsync

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if zone is not UNSET:
            field_dict["zone"] = zone
        if number is not UNSET:
            field_dict["number"] = number
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if descr is not UNSET:
            field_dict["descr"] = descr
        if count is not UNSET:
            field_dict["count"] = count
        if used is not UNSET:
            field_dict["used"] = used
        if active is not UNSET:
            field_dict["active"] = active
        if lastsync is not UNSET:
            field_dict["lastsync"] = lastsync

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        zone = d.pop("zone", UNSET)

        number = d.pop("number", UNSET)

        minutes = d.pop("minutes", UNSET)

        descr = d.pop("descr", UNSET)

        count = d.pop("count", UNSET)

        used = d.pop("used", UNSET)

        active = d.pop("active", UNSET)

        lastsync = d.pop("lastsync", UNSET)

        voucher_roll = cls(
            zone=zone,
            number=number,
            minutes=minutes,
            descr=descr,
            count=count,
            used=used,
            active=active,
            lastsync=lastsync,
        )

        voucher_roll.additional_properties = d
        return voucher_roll

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
