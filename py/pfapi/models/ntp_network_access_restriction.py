from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ntp_access_restrictions import NtpAccessRestrictions


T = TypeVar("T", bound="NtpNetworkAccessRestriction")


@_attrs_define
class NtpNetworkAccessRestriction:
    """
    Attributes:
        network (str):
        mask (Union[Unset, int]):
        restrictions (Union[Unset, NtpAccessRestrictions]):
    """

    network: str
    mask: Union[Unset, int] = UNSET
    restrictions: Union[Unset, "NtpAccessRestrictions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        network = self.network

        mask = self.mask

        restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.restrictions, Unset):
            restrictions = self.restrictions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "network": network,
            }
        )
        if mask is not UNSET:
            field_dict["mask"] = mask
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ntp_access_restrictions import NtpAccessRestrictions

        d = src_dict.copy()
        network = d.pop("network")

        mask = d.pop("mask", UNSET)

        _restrictions = d.pop("restrictions", UNSET)
        restrictions: Union[Unset, NtpAccessRestrictions]
        if isinstance(_restrictions, Unset):
            restrictions = UNSET
        else:
            restrictions = NtpAccessRestrictions.from_dict(_restrictions)

        ntp_network_access_restriction = cls(
            network=network,
            mask=mask,
            restrictions=restrictions,
        )

        ntp_network_access_restriction.additional_properties = d
        return ntp_network_access_restriction

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
