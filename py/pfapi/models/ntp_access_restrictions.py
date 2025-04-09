from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NtpAccessRestrictions")


@_attrs_define
class NtpAccessRestrictions:
    """
    Attributes:
        kod (Union[Unset, bool]):
        nomodify (Union[Unset, bool]):
        noquery (Union[Unset, bool]):
        noserve (Union[Unset, bool]):
        nopeer (Union[Unset, bool]):
        notrap (Union[Unset, bool]):
    """

    kod: Union[Unset, bool] = UNSET
    nomodify: Union[Unset, bool] = UNSET
    noquery: Union[Unset, bool] = UNSET
    noserve: Union[Unset, bool] = UNSET
    nopeer: Union[Unset, bool] = UNSET
    notrap: Union[Unset, bool] = UNSET
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
        field_dict.update({})
        if kod is not UNSET:
            field_dict["kod"] = kod
        if nomodify is not UNSET:
            field_dict["nomodify"] = nomodify
        if noquery is not UNSET:
            field_dict["noquery"] = noquery
        if noserve is not UNSET:
            field_dict["noserve"] = noserve
        if nopeer is not UNSET:
            field_dict["nopeer"] = nopeer
        if notrap is not UNSET:
            field_dict["notrap"] = notrap

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        kod = d.pop("kod", UNSET)

        nomodify = d.pop("nomodify", UNSET)

        noquery = d.pop("noquery", UNSET)

        noserve = d.pop("noserve", UNSET)

        nopeer = d.pop("nopeer", UNSET)

        notrap = d.pop("notrap", UNSET)

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
