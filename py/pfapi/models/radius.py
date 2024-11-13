from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.radius_server import RadiusServer


T = TypeVar("T", bound="Radius")


@_attrs_define
class Radius:
    """
    Attributes:
        nasip (Union[Unset, str]):
        acct_update (Union[Unset, str]):
        server (Union[Unset, RadiusServer]):
        server2 (Union[Unset, RadiusServer]):
        accounting (Union[Unset, bool]):
        radiusissueips (Union[Unset, bool]):
    """

    nasip: Union[Unset, str] = UNSET
    acct_update: Union[Unset, str] = UNSET
    server: Union[Unset, "RadiusServer"] = UNSET
    server2: Union[Unset, "RadiusServer"] = UNSET
    accounting: Union[Unset, bool] = UNSET
    radiusissueips: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nasip = self.nasip

        acct_update = self.acct_update

        server: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        server2: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server2, Unset):
            server2 = self.server2.to_dict()

        accounting = self.accounting

        radiusissueips = self.radiusissueips

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nasip is not UNSET:
            field_dict["nasip"] = nasip
        if acct_update is not UNSET:
            field_dict["acct_update"] = acct_update
        if server is not UNSET:
            field_dict["server"] = server
        if server2 is not UNSET:
            field_dict["server2"] = server2
        if accounting is not UNSET:
            field_dict["accounting"] = accounting
        if radiusissueips is not UNSET:
            field_dict["radiusissueips"] = radiusissueips

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.radius_server import RadiusServer

        d = src_dict.copy()
        nasip = d.pop("nasip", UNSET)

        acct_update = d.pop("acct_update", UNSET)

        _server = d.pop("server", UNSET)
        server: Union[Unset, RadiusServer]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = RadiusServer.from_dict(_server)

        _server2 = d.pop("server2", UNSET)
        server2: Union[Unset, RadiusServer]
        if isinstance(_server2, Unset):
            server2 = UNSET
        else:
            server2 = RadiusServer.from_dict(_server2)

        accounting = d.pop("accounting", UNSET)

        radiusissueips = d.pop("radiusissueips", UNSET)

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
