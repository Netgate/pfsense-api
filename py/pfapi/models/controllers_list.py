from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controller_info import ControllerInfo


T = TypeVar("T", bound="ControllersList")


@_attrs_define
class ControllersList:
    """
    Attributes:
        device_pubkey (str | Unset):
        controllers (list[ControllerInfo] | Unset):
    """

    device_pubkey: str | Unset = UNSET
    controllers: list[ControllerInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_pubkey = self.device_pubkey

        controllers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.controllers, Unset):
            controllers = []
            for controllers_item_data in self.controllers:
                controllers_item = controllers_item_data.to_dict()
                controllers.append(controllers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_pubkey is not UNSET:
            field_dict["device_pubkey"] = device_pubkey
        if controllers is not UNSET:
            field_dict["controllers"] = controllers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.controller_info import ControllerInfo

        d = dict(src_dict)
        device_pubkey = d.pop("device_pubkey", UNSET)

        _controllers = d.pop("controllers", UNSET)
        controllers: list[ControllerInfo] | Unset = UNSET
        if _controllers is not UNSET:
            controllers = []
            for controllers_item_data in _controllers:
                controllers_item = ControllerInfo.from_dict(controllers_item_data)

                controllers.append(controllers_item)

        controllers_list = cls(
            device_pubkey=device_pubkey,
            controllers=controllers,
        )

        controllers_list.additional_properties = d
        return controllers_list

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
