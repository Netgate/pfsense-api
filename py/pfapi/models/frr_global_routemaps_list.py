from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_global_routemap import FrrGlobalRoutemap
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrGlobalRoutemapsList")


@_attrs_define
class FrrGlobalRoutemapsList:
    """
    Attributes:
        globalroutemaps (list[FrrGlobalRoutemap] | Unset):
        call_options (list[TextValue] | Unset):
        exitaction_options (list[TextValue] | Unset):
        acl_match_options (list[TextValue] | Unset):
        prefix_match_options (list[TextValue] | Unset):
        nexthop_peer_options (list[TextValue] | Unset):
        nexthop_acl_options (list[TextValue] | Unset):
        nexthop_pl_options (list[TextValue] | Unset):
        aspath_match_options (list[TextValue] | Unset):
        community_match_options (list[TextValue] | Unset):
    """

    globalroutemaps: list[FrrGlobalRoutemap] | Unset = UNSET
    call_options: list[TextValue] | Unset = UNSET
    exitaction_options: list[TextValue] | Unset = UNSET
    acl_match_options: list[TextValue] | Unset = UNSET
    prefix_match_options: list[TextValue] | Unset = UNSET
    nexthop_peer_options: list[TextValue] | Unset = UNSET
    nexthop_acl_options: list[TextValue] | Unset = UNSET
    nexthop_pl_options: list[TextValue] | Unset = UNSET
    aspath_match_options: list[TextValue] | Unset = UNSET
    community_match_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        globalroutemaps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.globalroutemaps, Unset):
            globalroutemaps = []
            for globalroutemaps_item_data in self.globalroutemaps:
                globalroutemaps_item = globalroutemaps_item_data.to_dict()
                globalroutemaps.append(globalroutemaps_item)

        call_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.call_options, Unset):
            call_options = []
            for call_options_item_data in self.call_options:
                call_options_item = call_options_item_data.to_dict()
                call_options.append(call_options_item)

        exitaction_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exitaction_options, Unset):
            exitaction_options = []
            for exitaction_options_item_data in self.exitaction_options:
                exitaction_options_item = exitaction_options_item_data.to_dict()
                exitaction_options.append(exitaction_options_item)

        acl_match_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.acl_match_options, Unset):
            acl_match_options = []
            for acl_match_options_item_data in self.acl_match_options:
                acl_match_options_item = acl_match_options_item_data.to_dict()
                acl_match_options.append(acl_match_options_item)

        prefix_match_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prefix_match_options, Unset):
            prefix_match_options = []
            for prefix_match_options_item_data in self.prefix_match_options:
                prefix_match_options_item = prefix_match_options_item_data.to_dict()
                prefix_match_options.append(prefix_match_options_item)

        nexthop_peer_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nexthop_peer_options, Unset):
            nexthop_peer_options = []
            for nexthop_peer_options_item_data in self.nexthop_peer_options:
                nexthop_peer_options_item = nexthop_peer_options_item_data.to_dict()
                nexthop_peer_options.append(nexthop_peer_options_item)

        nexthop_acl_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nexthop_acl_options, Unset):
            nexthop_acl_options = []
            for nexthop_acl_options_item_data in self.nexthop_acl_options:
                nexthop_acl_options_item = nexthop_acl_options_item_data.to_dict()
                nexthop_acl_options.append(nexthop_acl_options_item)

        nexthop_pl_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nexthop_pl_options, Unset):
            nexthop_pl_options = []
            for nexthop_pl_options_item_data in self.nexthop_pl_options:
                nexthop_pl_options_item = nexthop_pl_options_item_data.to_dict()
                nexthop_pl_options.append(nexthop_pl_options_item)

        aspath_match_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aspath_match_options, Unset):
            aspath_match_options = []
            for aspath_match_options_item_data in self.aspath_match_options:
                aspath_match_options_item = aspath_match_options_item_data.to_dict()
                aspath_match_options.append(aspath_match_options_item)

        community_match_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.community_match_options, Unset):
            community_match_options = []
            for community_match_options_item_data in self.community_match_options:
                community_match_options_item = community_match_options_item_data.to_dict()
                community_match_options.append(community_match_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if globalroutemaps is not UNSET:
            field_dict["globalroutemaps"] = globalroutemaps
        if call_options is not UNSET:
            field_dict["call_options"] = call_options
        if exitaction_options is not UNSET:
            field_dict["exitaction_options"] = exitaction_options
        if acl_match_options is not UNSET:
            field_dict["acl_match_options"] = acl_match_options
        if prefix_match_options is not UNSET:
            field_dict["prefix_match_options"] = prefix_match_options
        if nexthop_peer_options is not UNSET:
            field_dict["nexthop_peer_options"] = nexthop_peer_options
        if nexthop_acl_options is not UNSET:
            field_dict["nexthop_acl_options"] = nexthop_acl_options
        if nexthop_pl_options is not UNSET:
            field_dict["nexthop_pl_options"] = nexthop_pl_options
        if aspath_match_options is not UNSET:
            field_dict["aspath_match_options"] = aspath_match_options
        if community_match_options is not UNSET:
            field_dict["community_match_options"] = community_match_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_global_routemap import FrrGlobalRoutemap
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _globalroutemaps = d.pop("globalroutemaps", UNSET)
        globalroutemaps: list[FrrGlobalRoutemap] | Unset = UNSET
        if _globalroutemaps is not UNSET:
            globalroutemaps = []
            for globalroutemaps_item_data in _globalroutemaps:
                globalroutemaps_item = FrrGlobalRoutemap.from_dict(globalroutemaps_item_data)

                globalroutemaps.append(globalroutemaps_item)

        _call_options = d.pop("call_options", UNSET)
        call_options: list[TextValue] | Unset = UNSET
        if _call_options is not UNSET:
            call_options = []
            for call_options_item_data in _call_options:
                call_options_item = TextValue.from_dict(call_options_item_data)

                call_options.append(call_options_item)

        _exitaction_options = d.pop("exitaction_options", UNSET)
        exitaction_options: list[TextValue] | Unset = UNSET
        if _exitaction_options is not UNSET:
            exitaction_options = []
            for exitaction_options_item_data in _exitaction_options:
                exitaction_options_item = TextValue.from_dict(exitaction_options_item_data)

                exitaction_options.append(exitaction_options_item)

        _acl_match_options = d.pop("acl_match_options", UNSET)
        acl_match_options: list[TextValue] | Unset = UNSET
        if _acl_match_options is not UNSET:
            acl_match_options = []
            for acl_match_options_item_data in _acl_match_options:
                acl_match_options_item = TextValue.from_dict(acl_match_options_item_data)

                acl_match_options.append(acl_match_options_item)

        _prefix_match_options = d.pop("prefix_match_options", UNSET)
        prefix_match_options: list[TextValue] | Unset = UNSET
        if _prefix_match_options is not UNSET:
            prefix_match_options = []
            for prefix_match_options_item_data in _prefix_match_options:
                prefix_match_options_item = TextValue.from_dict(prefix_match_options_item_data)

                prefix_match_options.append(prefix_match_options_item)

        _nexthop_peer_options = d.pop("nexthop_peer_options", UNSET)
        nexthop_peer_options: list[TextValue] | Unset = UNSET
        if _nexthop_peer_options is not UNSET:
            nexthop_peer_options = []
            for nexthop_peer_options_item_data in _nexthop_peer_options:
                nexthop_peer_options_item = TextValue.from_dict(nexthop_peer_options_item_data)

                nexthop_peer_options.append(nexthop_peer_options_item)

        _nexthop_acl_options = d.pop("nexthop_acl_options", UNSET)
        nexthop_acl_options: list[TextValue] | Unset = UNSET
        if _nexthop_acl_options is not UNSET:
            nexthop_acl_options = []
            for nexthop_acl_options_item_data in _nexthop_acl_options:
                nexthop_acl_options_item = TextValue.from_dict(nexthop_acl_options_item_data)

                nexthop_acl_options.append(nexthop_acl_options_item)

        _nexthop_pl_options = d.pop("nexthop_pl_options", UNSET)
        nexthop_pl_options: list[TextValue] | Unset = UNSET
        if _nexthop_pl_options is not UNSET:
            nexthop_pl_options = []
            for nexthop_pl_options_item_data in _nexthop_pl_options:
                nexthop_pl_options_item = TextValue.from_dict(nexthop_pl_options_item_data)

                nexthop_pl_options.append(nexthop_pl_options_item)

        _aspath_match_options = d.pop("aspath_match_options", UNSET)
        aspath_match_options: list[TextValue] | Unset = UNSET
        if _aspath_match_options is not UNSET:
            aspath_match_options = []
            for aspath_match_options_item_data in _aspath_match_options:
                aspath_match_options_item = TextValue.from_dict(aspath_match_options_item_data)

                aspath_match_options.append(aspath_match_options_item)

        _community_match_options = d.pop("community_match_options", UNSET)
        community_match_options: list[TextValue] | Unset = UNSET
        if _community_match_options is not UNSET:
            community_match_options = []
            for community_match_options_item_data in _community_match_options:
                community_match_options_item = TextValue.from_dict(community_match_options_item_data)

                community_match_options.append(community_match_options_item)

        frr_global_routemaps_list = cls(
            globalroutemaps=globalroutemaps,
            call_options=call_options,
            exitaction_options=exitaction_options,
            acl_match_options=acl_match_options,
            prefix_match_options=prefix_match_options,
            nexthop_peer_options=nexthop_peer_options,
            nexthop_acl_options=nexthop_acl_options,
            nexthop_pl_options=nexthop_pl_options,
            aspath_match_options=aspath_match_options,
            community_match_options=community_match_options,
        )

        frr_global_routemaps_list.additional_properties = d
        return frr_global_routemaps_list

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
