from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.radius_server import RadiusServer


T = TypeVar("T", bound="Radius")


@_attrs_define
class Radius:
    """
    Attributes:
        nasip (str):
        acct_update (str):
        server (RadiusServer):
        server2 (RadiusServer):
        accounting (bool):
        radiusissueips (bool):
    """

    nasip: str
    acct_update: str
    server: "RadiusServer"
    server2: "RadiusServer"
    accounting: bool
    radiusissueips: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nasip = self.nasip

        acct_update = self.acct_update

        server = self.server.to_dict()

        server2 = self.server2.to_dict()

        accounting = self.accounting

        radiusissueips = self.radiusissueips

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nasip": nasip,
                "acct_update": acct_update,
                "server": server,
                "server2": server2,
                "accounting": accounting,
                "radiusissueips": radiusissueips,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.radius_server import RadiusServer

        d = src_dict.copy()
        nasip = d.pop("nasip")

        acct_update = d.pop("acct_update")

        server = RadiusServer.from_dict(d.pop("server"))

        server2 = RadiusServer.from_dict(d.pop("server2"))

        accounting = d.pop("accounting")

        radiusissueips = d.pop("radiusissueips")

        radius = cls(
            nasip=nasip,
            acct_update=acct_update,
            server=server,
            server2=server2,
            accounting=accounting,
            radiusissueips=radiusissueips,
        )

        radius.additional_properties = d
        return radius

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
