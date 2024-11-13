from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_server_config import OpenVPNServerConfig


T = TypeVar("T", bound="OpenVPNServer")


@_attrs_define
class OpenVPNServer:
    """
    Attributes:
        authservers (Union[Unset, List[str]]):
        server (Union[Unset, OpenVPNServerConfig]):
    """

    authservers: Union[Unset, List[str]] = UNSET
    server: Union[Unset, "OpenVPNServerConfig"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authservers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.authservers, Unset):
            authservers = self.authservers

        server: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authservers is not UNSET:
            field_dict["authservers"] = authservers
        if server is not UNSET:
            field_dict["server"] = server

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_vpn_server_config import OpenVPNServerConfig

        d = src_dict.copy()
        authservers = cast(List[str], d.pop("authservers", UNSET))

        _server = d.pop("server", UNSET)
        server: Union[Unset, OpenVPNServerConfig]
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = OpenVPNServerConfig.from_dict(_server)

        open_vpn_server = cls(
            authservers=authservers,
            server=server,
        )

        open_vpn_server.additional_properties = d
        return open_vpn_server

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
