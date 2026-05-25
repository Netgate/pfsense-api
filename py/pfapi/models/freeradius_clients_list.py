from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freeradiusclient import Freeradiusclient


T = TypeVar("T", bound="FreeradiusClientsList")


@_attrs_define
class FreeradiusClientsList:
    """
    Attributes:
        clients (list[Freeradiusclient] | Unset):
    """

    clients: list[Freeradiusclient] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clients is not UNSET:
            field_dict["clients"] = clients

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.freeradiusclient import Freeradiusclient

        d = dict(src_dict)
        _clients = d.pop("clients", UNSET)
        clients: list[Freeradiusclient] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = Freeradiusclient.from_dict(clients_item_data)

                clients.append(clients_item)

        freeradius_clients_list = cls(
            clients=clients,
        )

        freeradius_clients_list.additional_properties = d
        return freeradius_clients_list

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
