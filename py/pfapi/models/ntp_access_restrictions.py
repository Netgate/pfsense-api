from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NtpAccessRestrictions")


@_attrs_define
class NtpAccessRestrictions:
    """
    Attributes:
        kod (bool):
        nomodify (bool):
        noquery (bool):
        noserve (bool):
        nopeer (bool):
        notrap (bool):
    """

    kod: bool
    nomodify: bool
    noquery: bool
    noserve: bool
    nopeer: bool
    notrap: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        kod = self.kod

        nomodify = self.nomodify

        noquery = self.noquery

        noserve = self.noserve

        nopeer = self.nopeer

        notrap = self.notrap

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kod": kod,
                "nomodify": nomodify,
                "noquery": noquery,
                "noserve": noserve,
                "nopeer": nopeer,
                "notrap": notrap,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kod = d.pop("kod")

        nomodify = d.pop("nomodify")

        noquery = d.pop("noquery")

        noserve = d.pop("noserve")

        nopeer = d.pop("nopeer")

        notrap = d.pop("notrap")

        ntp_access_restrictions = cls(
            kod=kod,
            nomodify=nomodify,
            noquery=noquery,
            noserve=noserve,
            nopeer=nopeer,
            notrap=notrap,
        )

        ntp_access_restrictions.additional_properties = d
        return ntp_access_restrictions

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
