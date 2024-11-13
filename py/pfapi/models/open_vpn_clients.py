from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_client_config import OpenVPNClientConfig


T = TypeVar("T", bound="OpenVPNClients")


@_attrs_define
class OpenVPNClients:
    """
    Attributes:
        clients (Union[Unset, List['OpenVPNClientConfig']]):
    """

    clients: Union[Unset, List["OpenVPNClientConfig"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clients: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clients is not UNSET:
            field_dict["clients"] = clients

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_vpn_client_config import OpenVPNClientConfig

        d = src_dict.copy()
        clients = []
        _clients = d.pop("clients", UNSET)
        for clients_item_data in _clients or []:
            clients_item = OpenVPNClientConfig.from_dict(clients_item_data)

            clients.append(clients_item)

        open_vpn_clients = cls(
            clients=clients,
        )

        open_vpn_clients.additional_properties = d
        return open_vpn_clients

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
