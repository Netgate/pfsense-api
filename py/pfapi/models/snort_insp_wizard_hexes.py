from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_wizard_hexes_l_to_client import SnortInspWizardHexesLToClient
    from ..models.snort_insp_wizard_hexes_l_to_server import SnortInspWizardHexesLToServer


T = TypeVar("T", bound="SnortInspWizardHexes")


@_attrs_define
class SnortInspWizardHexes:
    """
    Attributes:
        service (str | Unset): name of service
        proto (str | Unset): protocol to scan { tcp | udp | any }; default any
        to_server (list[SnortInspWizardHexesLToServer] | Unset):
        to_client (list[SnortInspWizardHexesLToClient] | Unset):
    """

    service: str | Unset = UNSET
    proto: str | Unset = UNSET
    to_server: list[SnortInspWizardHexesLToServer] | Unset = UNSET
    to_client: list[SnortInspWizardHexesLToClient] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service = self.service

        proto = self.proto

        to_server: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.to_server, Unset):
            to_server = []
            for to_server_item_data in self.to_server:
                to_server_item = to_server_item_data.to_dict()
                to_server.append(to_server_item)

        to_client: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.to_client, Unset):
            to_client = []
            for to_client_item_data in self.to_client:
                to_client_item = to_client_item_data.to_dict()
                to_client.append(to_client_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service is not UNSET:
            field_dict["service"] = service
        if proto is not UNSET:
            field_dict["proto"] = proto
        if to_server is not UNSET:
            field_dict["to_server"] = to_server
        if to_client is not UNSET:
            field_dict["to_client"] = to_client

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_wizard_hexes_l_to_client import SnortInspWizardHexesLToClient
        from ..models.snort_insp_wizard_hexes_l_to_server import SnortInspWizardHexesLToServer

        d = dict(src_dict)
        service = d.pop("service", UNSET)

        proto = d.pop("proto", UNSET)

        _to_server = d.pop("to_server", UNSET)
        to_server: list[SnortInspWizardHexesLToServer] | Unset = UNSET
        if _to_server is not UNSET:
            to_server = []
            for to_server_item_data in _to_server:
                to_server_item = SnortInspWizardHexesLToServer.from_dict(to_server_item_data)

                to_server.append(to_server_item)

        _to_client = d.pop("to_client", UNSET)
        to_client: list[SnortInspWizardHexesLToClient] | Unset = UNSET
        if _to_client is not UNSET:
            to_client = []
            for to_client_item_data in _to_client:
                to_client_item = SnortInspWizardHexesLToClient.from_dict(to_client_item_data)

                to_client.append(to_client_item)

        snort_insp_wizard_hexes = cls(
            service=service,
            proto=proto,
            to_server=to_server,
            to_client=to_client,
        )

        snort_insp_wizard_hexes.additional_properties = d
        return snort_insp_wizard_hexes

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
