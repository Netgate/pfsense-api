from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        radius (L2TPRadius):
        remoteip (str):
        localip (str):
        l2tp_subnet (str):
        interface (str):
        n_l2tp_units (str):
        secret (str):
        paporchap (str):
        dns1 (str):
        dns2 (str):
        user (Union[Unset, List['L2TPUser']]):
    """

    mode: str
    radius: "L2TPRadius"
    remoteip: str
    localip: str
    l2tp_subnet: str
    interface: str
    n_l2tp_units: str
    secret: str
    paporchap: str
    dns1: str
    dns2: str
    user: Union[Unset, List["L2TPUser"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mode = self.mode

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

        user: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user, Unset):
            user = []
            for user_item_data in self.user:
                user_item = user_item_data.to_dict()
                user.append(user_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "radius": radius,
                "remoteip": remoteip,
                "localip": localip,
                "l2tp_subnet": l2tp_subnet,
                "interface": interface,
                "n_l2tp_units": n_l2tp_units,
                "secret": secret,
                "paporchap": paporchap,
                "dns1": dns1,
                "dns2": dns2,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.l2tp_radius import L2TPRadius
        from ..models.l2tp_user import L2TPUser

        d = src_dict.copy()
        mode = d.pop("mode")

        radius = L2TPRadius.from_dict(d.pop("radius"))

        remoteip = d.pop("remoteip")

        localip = d.pop("localip")

        l2tp_subnet = d.pop("l2tp_subnet")

        interface = d.pop("interface")

        n_l2tp_units = d.pop("n_l2tp_units")

        secret = d.pop("secret")

        paporchap = d.pop("paporchap")

        dns1 = d.pop("dns1")

        dns2 = d.pop("dns2")

        user = []
        _user = d.pop("user", UNSET)
        for user_item_data in _user or []:
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
