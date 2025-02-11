from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VoucherRoll")


@_attrs_define
class VoucherRoll:
    """
    Attributes:
        zone (str):
        number (int):
        minutes (int):
        descr (str):
        count (str):
        used (str):
        active (bool):
        lastsync (int):
    """

    zone: str
    number: int
    minutes: int
    descr: str
    count: str
    used: str
    active: bool
    lastsync: int
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
        field_dict.update(
            {
                "zone": zone,
                "number": number,
                "minutes": minutes,
                "descr": descr,
                "count": count,
                "used": used,
                "active": active,
                "lastsync": lastsync,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        zone = d.pop("zone")

        number = d.pop("number")

        minutes = d.pop("minutes")

        descr = d.pop("descr")

        count = d.pop("count")

        used = d.pop("used")

        active = d.pop("active")

        lastsync = d.pop("lastsync")

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
