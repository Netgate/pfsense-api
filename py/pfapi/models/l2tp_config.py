from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.l2tp_radius import L2TPRadius
    from ..models.l2tp_user import L2TPUser


T = TypeVar("T", bound="L2TPConfig")


@_attrs_define
class L2TPConfig:
    """
    Attributes:
        mode (str):
        radius (L2TPRadius | Unset):
        remoteip (str | Unset):
        localip (str | Unset):
        l2tp_subnet (str | Unset):
        interface (str | Unset):
        n_l2tp_units (str | Unset):
        secret (str | Unset):
        paporchap (str | Unset):
        dns1 (str | Unset):
        dns2 (str | Unset):
        user (list[L2TPUser] | Unset):
    """

    mode: str
    radius: L2TPRadius | Unset = UNSET
    remoteip: str | Unset = UNSET
    localip: str | Unset = UNSET
    l2tp_subnet: str | Unset = UNSET
    interface: str | Unset = UNSET
    n_l2tp_units: str | Unset = UNSET
    secret: str | Unset = UNSET
    paporchap: str | Unset = UNSET
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    user: list[L2TPUser] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        radius: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radius, Unset):
            radius = self.radius.to_dict()

        remoteip = self.remoteip

        localip = self.localip

        l2tp_subnet = self.l2tp_subnet

        interface = self.interface

        n_l2tp_units = self.n_l2tp_units

        secret = self.secret

        paporchap = self.paporchap

        dns1 = self.dns1

        dns2 = self.dns2

        user: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = []
            for user_item_data in self.user:
                user_item = user_item_data.to_dict()
                user.append(user_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if radius is not UNSET:
            field_dict["radius"] = radius
        if remoteip is not UNSET:
            field_dict["remoteip"] = remoteip
        if localip is not UNSET:
            field_dict["localip"] = localip
        if l2tp_subnet is not UNSET:
            field_dict["l2tp_subnet"] = l2tp_subnet
        if interface is not UNSET:
            field_dict["interface"] = interface
        if n_l2tp_units is not UNSET:
            field_dict["n_l2tp_units"] = n_l2tp_units
        if secret is not UNSET:
            field_dict["secret"] = secret
        if paporchap is not UNSET:
            field_dict["paporchap"] = paporchap
        if dns1 is not UNSET:
            field_dict["dns1"] = dns1
        if dns2 is not UNSET:
            field_dict["dns2"] = dns2
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.l2tp_radius import L2TPRadius
        from ..models.l2tp_user import L2TPUser

        d = dict(src_dict)
        mode = d.pop("mode")

        _radius = d.pop("radius", UNSET)
        radius: L2TPRadius | Unset
        if isinstance(_radius, Unset):
            radius = UNSET
        else:
            radius = L2TPRadius.from_dict(_radius)

        remoteip = d.pop("remoteip", UNSET)

        localip = d.pop("localip", UNSET)

        l2tp_subnet = d.pop("l2tp_subnet", UNSET)

        interface = d.pop("interface", UNSET)

        n_l2tp_units = d.pop("n_l2tp_units", UNSET)

        secret = d.pop("secret", UNSET)

        paporchap = d.pop("paporchap", UNSET)

        dns1 = d.pop("dns1", UNSET)

        dns2 = d.pop("dns2", UNSET)

        _user = d.pop("user", UNSET)
        user: list[L2TPUser] | Unset = UNSET
        if _user is not UNSET:
            user = []
            for user_item_data in _user:
                user_item = L2TPUser.from_dict(user_item_data)

                user.append(user_item)

        l2tp_config = cls(
            mode=mode,
            radius=radius,
            remoteip=remoteip,
            localip=localip,
            l2tp_subnet=l2tp_subnet,
            interface=interface,
            n_l2tp_units=n_l2tp_units,
            secret=secret,
            paporchap=paporchap,
            dns1=dns1,
            dns2=dns2,
            user=user,
        )

        l2tp_config.additional_properties = d
        return l2tp_config

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
