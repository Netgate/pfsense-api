from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adv_network_setting import AdvNetworkSetting


T = TypeVar("T", bound="AdvNetworking")


@_attrs_define
class AdvNetworking:
    """
    Attributes:
        networking (Union[Unset, AdvNetworkSetting]):
    """

    networking: Union[Unset, "AdvNetworkSetting"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        networking: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.networking, Unset):
            networking = self.networking.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if networking is not UNSET:
            field_dict["networking"] = networking

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adv_network_setting import AdvNetworkSetting

        d = src_dict.copy()
        _networking = d.pop("networking", UNSET)
        networking: Union[Unset, AdvNetworkSetting]
        if isinstance(_networking, Unset):
            networking = UNSET
        else:
            networking = AdvNetworkSetting.from_dict(_networking)

        adv_networking = cls(
            networking=networking,
        )

        adv_networking.additional_properties = d
        return adv_networking

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
