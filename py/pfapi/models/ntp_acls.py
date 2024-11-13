from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ntp_access_restrictions import NtpAccessRestrictions
    from ..models.ntp_network_access_restriction import NtpNetworkAccessRestriction


T = TypeVar("T", bound="NtpAcls")


@_attrs_define
class NtpAcls:
    """
    Attributes:
        default_restrictions (Union[Unset, NtpAccessRestrictions]):
        custom_restrictions (Union[Unset, List['NtpNetworkAccessRestriction']]):
    """

    default_restrictions: Union[Unset, "NtpAccessRestrictions"] = UNSET
    custom_restrictions: Union[Unset, List["NtpNetworkAccessRestriction"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_restrictions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.default_restrictions, Unset):
            default_restrictions = self.default_restrictions.to_dict()

        custom_restrictions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.custom_restrictions, Unset):
            custom_restrictions = []
            for custom_restrictions_item_data in self.custom_restrictions:
                custom_restrictions_item = custom_restrictions_item_data.to_dict()
                custom_restrictions.append(custom_restrictions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_restrictions is not UNSET:
            field_dict["default_restrictions"] = default_restrictions
        if custom_restrictions is not UNSET:
            field_dict["custom_restrictions"] = custom_restrictions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ntp_access_restrictions import NtpAccessRestrictions
        from ..models.ntp_network_access_restriction import NtpNetworkAccessRestriction

        d = src_dict.copy()
        _default_restrictions = d.pop("default_restrictions", UNSET)
        default_restrictions: Union[Unset, NtpAccessRestrictions]
        if isinstance(_default_restrictions, Unset):
            default_restrictions = UNSET
        else:
            default_restrictions = NtpAccessRestrictions.from_dict(_default_restrictions)

        custom_restrictions = []
        _custom_restrictions = d.pop("custom_restrictions", UNSET)
        for custom_restrictions_item_data in _custom_restrictions or []:
            custom_restrictions_item = NtpNetworkAccessRestriction.from_dict(custom_restrictions_item_data)

            custom_restrictions.append(custom_restrictions_item)

        ntp_acls = cls(
            default_restrictions=default_restrictions,
            custom_restrictions=custom_restrictions,
        )

        ntp_acls.additional_properties = d
        return ntp_acls

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
