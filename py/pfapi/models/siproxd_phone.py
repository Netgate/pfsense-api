from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.siproxd_phone_endpoint import SiproxdPhoneEndpoint


T = TypeVar("T", bound="SiproxdPhone")


@_attrs_define
class SiproxdPhone:
    """
    Attributes:
        expires (int | Unset): Unix timestamp when the registration expires
        real (SiproxdPhoneEndpoint | Unset):
        nat (SiproxdPhoneEndpoint | Unset):
        registered (SiproxdPhoneEndpoint | Unset):
    """

    expires: int | Unset = UNSET
    real: SiproxdPhoneEndpoint | Unset = UNSET
    nat: SiproxdPhoneEndpoint | Unset = UNSET
    registered: SiproxdPhoneEndpoint | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires = self.expires

        real: dict[str, Any] | Unset = UNSET
        if not isinstance(self.real, Unset):
            real = self.real.to_dict()

        nat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nat, Unset):
            nat = self.nat.to_dict()

        registered: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registered, Unset):
            registered = self.registered.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires is not UNSET:
            field_dict["expires"] = expires
        if real is not UNSET:
            field_dict["real"] = real
        if nat is not UNSET:
            field_dict["nat"] = nat
        if registered is not UNSET:
            field_dict["registered"] = registered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.siproxd_phone_endpoint import SiproxdPhoneEndpoint

        d = dict(src_dict)
        expires = d.pop("expires", UNSET)

        _real = d.pop("real", UNSET)
        real: SiproxdPhoneEndpoint | Unset
        if isinstance(_real, Unset):
            real = UNSET
        else:
            real = SiproxdPhoneEndpoint.from_dict(_real)

        _nat = d.pop("nat", UNSET)
        nat: SiproxdPhoneEndpoint | Unset
        if isinstance(_nat, Unset):
            nat = UNSET
        else:
            nat = SiproxdPhoneEndpoint.from_dict(_nat)

        _registered = d.pop("registered", UNSET)
        registered: SiproxdPhoneEndpoint | Unset
        if isinstance(_registered, Unset):
            registered = UNSET
        else:
            registered = SiproxdPhoneEndpoint.from_dict(_registered)

        siproxd_phone = cls(
            expires=expires,
            real=real,
            nat=nat,
            registered=registered,
        )

        siproxd_phone.additional_properties = d
        return siproxd_phone

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
