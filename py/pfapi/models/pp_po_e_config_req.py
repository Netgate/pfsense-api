from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pp_po_e_server import PPPoEServer


T = TypeVar("T", bound="PPPoEConfigReq")


@_attrs_define
class PPPoEConfigReq:
    """
    Attributes:
        pppoe (list[PPPoEServer] | Unset):
    """

    pppoe: list[PPPoEServer] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pppoe: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pppoe, Unset):
            pppoe = []
            for pppoe_item_data in self.pppoe:
                pppoe_item = pppoe_item_data.to_dict()
                pppoe.append(pppoe_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pppoe is not UNSET:
            field_dict["pppoe"] = pppoe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pp_po_e_server import PPPoEServer

        d = dict(src_dict)
        _pppoe = d.pop("pppoe", UNSET)
        pppoe: list[PPPoEServer] | Unset = UNSET
        if _pppoe is not UNSET:
            pppoe = []
            for pppoe_item_data in _pppoe:
                pppoe_item = PPPoEServer.from_dict(pppoe_item_data)

                pppoe.append(pppoe_item)

        pp_po_e_config_req = cls(
            pppoe=pppoe,
        )

        pp_po_e_config_req.additional_properties = d
        return pp_po_e_config_req

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
