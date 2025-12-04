from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.altq_root_queue import ALTQRootQueue


T = TypeVar("T", bound="ALTQRootQueues")


@_attrs_define
class ALTQRootQueues:
    """
    Attributes:
        altq (list[ALTQRootQueue] | Unset):
    """

    altq: list[ALTQRootQueue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        altq: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.altq, Unset):
            altq = []
            for altq_item_data in self.altq:
                altq_item = altq_item_data.to_dict()
                altq.append(altq_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if altq is not UNSET:
            field_dict["altq"] = altq

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.altq_root_queue import ALTQRootQueue

        d = dict(src_dict)
        _altq = d.pop("altq", UNSET)
        altq: list[ALTQRootQueue] | Unset = UNSET
        if _altq is not UNSET:
            altq = []
            for altq_item_data in _altq:
                altq_item = ALTQRootQueue.from_dict(altq_item_data)

                altq.append(altq_item)

        altq_root_queues = cls(
            altq=altq,
        )

        altq_root_queues.additional_properties = d
        return altq_root_queues

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
