from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.altq_capable_interface import ALTQCapableInterface
    from ..models.altq_root_queue import ALTQRootQueue
    from ..models.limiter import Limiter


T = TypeVar("T", bound="TrafficShapers")


@_attrs_define
class TrafficShapers:
    """
    Attributes:
        altq (list[ALTQRootQueue] | Unset):
        altq_capable_ifs (list[ALTQCapableInterface] | Unset):
        limiter (list[Limiter] | Unset):
    """

    altq: list[ALTQRootQueue] | Unset = UNSET
    altq_capable_ifs: list[ALTQCapableInterface] | Unset = UNSET
    limiter: list[Limiter] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        altq: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.altq, Unset):
            altq = []
            for altq_item_data in self.altq:
                altq_item = altq_item_data.to_dict()
                altq.append(altq_item)

        altq_capable_ifs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.altq_capable_ifs, Unset):
            altq_capable_ifs = []
            for altq_capable_ifs_item_data in self.altq_capable_ifs:
                altq_capable_ifs_item = altq_capable_ifs_item_data.to_dict()
                altq_capable_ifs.append(altq_capable_ifs_item)

        limiter: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.limiter, Unset):
            limiter = []
            for limiter_item_data in self.limiter:
                limiter_item = limiter_item_data.to_dict()
                limiter.append(limiter_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if altq is not UNSET:
            field_dict["altq"] = altq
        if altq_capable_ifs is not UNSET:
            field_dict["altq_capable_ifs"] = altq_capable_ifs
        if limiter is not UNSET:
            field_dict["limiter"] = limiter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.altq_capable_interface import ALTQCapableInterface
        from ..models.altq_root_queue import ALTQRootQueue
        from ..models.limiter import Limiter

        d = dict(src_dict)
        _altq = d.pop("altq", UNSET)
        altq: list[ALTQRootQueue] | Unset = UNSET
        if _altq is not UNSET:
            altq = []
            for altq_item_data in _altq:
                altq_item = ALTQRootQueue.from_dict(altq_item_data)

                altq.append(altq_item)

        _altq_capable_ifs = d.pop("altq_capable_ifs", UNSET)
        altq_capable_ifs: list[ALTQCapableInterface] | Unset = UNSET
        if _altq_capable_ifs is not UNSET:
            altq_capable_ifs = []
            for altq_capable_ifs_item_data in _altq_capable_ifs:
                altq_capable_ifs_item = ALTQCapableInterface.from_dict(altq_capable_ifs_item_data)

                altq_capable_ifs.append(altq_capable_ifs_item)

        _limiter = d.pop("limiter", UNSET)
        limiter: list[Limiter] | Unset = UNSET
        if _limiter is not UNSET:
            limiter = []
            for limiter_item_data in _limiter:
                limiter_item = Limiter.from_dict(limiter_item_data)

                limiter.append(limiter_item)

        traffic_shapers = cls(
            altq=altq,
            altq_capable_ifs=altq_capable_ifs,
            limiter=limiter,
        )

        traffic_shapers.additional_properties = d
        return traffic_shapers

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
