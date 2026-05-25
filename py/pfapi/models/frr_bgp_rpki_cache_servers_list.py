from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_bgp_rpki_cache_server import FrrBgpRpkiCacheServer


T = TypeVar("T", bound="FrrBgpRpkiCacheServersList")


@_attrs_define
class FrrBgpRpkiCacheServersList:
    """
    Attributes:
        bgprpkicacheservers (list[FrrBgpRpkiCacheServer] | Unset):
    """

    bgprpkicacheservers: list[FrrBgpRpkiCacheServer] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgprpkicacheservers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bgprpkicacheservers, Unset):
            bgprpkicacheservers = []
            for bgprpkicacheservers_item_data in self.bgprpkicacheservers:
                bgprpkicacheservers_item = bgprpkicacheservers_item_data.to_dict()
                bgprpkicacheservers.append(bgprpkicacheservers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgprpkicacheservers is not UNSET:
            field_dict["bgprpkicacheservers"] = bgprpkicacheservers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_bgp_rpki_cache_server import FrrBgpRpkiCacheServer

        d = dict(src_dict)
        _bgprpkicacheservers = d.pop("bgprpkicacheservers", UNSET)
        bgprpkicacheservers: list[FrrBgpRpkiCacheServer] | Unset = UNSET
        if _bgprpkicacheservers is not UNSET:
            bgprpkicacheservers = []
            for bgprpkicacheservers_item_data in _bgprpkicacheservers:
                bgprpkicacheservers_item = FrrBgpRpkiCacheServer.from_dict(bgprpkicacheservers_item_data)

                bgprpkicacheservers.append(bgprpkicacheservers_item)

        frr_bgp_rpki_cache_servers_list = cls(
            bgprpkicacheservers=bgprpkicacheservers,
        )

        frr_bgp_rpki_cache_servers_list.additional_properties = d
        return frr_bgp_rpki_cache_servers_list

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
