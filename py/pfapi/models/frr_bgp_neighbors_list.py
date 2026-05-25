from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_bgp_neighbor import FrrBgpNeighbor
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrBgpNeighborsList")


@_attrs_define
class FrrBgpNeighborsList:
    """
    Attributes:
        bgpneighbors (list[FrrBgpNeighbor] | Unset):
        peergroup_options (list[TextValue] | Unset):
        updatesource_options (list[TextValue] | Unset):
        defaultoriginateroutemap_options (list[TextValue] | Unset):
        distribute_in_options (list[TextValue] | Unset):
        distribute_out_options (list[TextValue] | Unset):
        prefixfilter_in_options (list[TextValue] | Unset):
        prefixfilter_out_options (list[TextValue] | Unset):
        aspathfilter_in_options (list[TextValue] | Unset):
        aspathfilter_out_options (list[TextValue] | Unset):
        routemap_in_options (list[TextValue] | Unset):
        routemap_out_options (list[TextValue] | Unset):
        unsuppressmap_options (list[TextValue] | Unset):
        bfd_peer_options (list[TextValue] | Unset):
    """

    bgpneighbors: list[FrrBgpNeighbor] | Unset = UNSET
    peergroup_options: list[TextValue] | Unset = UNSET
    updatesource_options: list[TextValue] | Unset = UNSET
    defaultoriginateroutemap_options: list[TextValue] | Unset = UNSET
    distribute_in_options: list[TextValue] | Unset = UNSET
    distribute_out_options: list[TextValue] | Unset = UNSET
    prefixfilter_in_options: list[TextValue] | Unset = UNSET
    prefixfilter_out_options: list[TextValue] | Unset = UNSET
    aspathfilter_in_options: list[TextValue] | Unset = UNSET
    aspathfilter_out_options: list[TextValue] | Unset = UNSET
    routemap_in_options: list[TextValue] | Unset = UNSET
    routemap_out_options: list[TextValue] | Unset = UNSET
    unsuppressmap_options: list[TextValue] | Unset = UNSET
    bfd_peer_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bgpneighbors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bgpneighbors, Unset):
            bgpneighbors = []
            for bgpneighbors_item_data in self.bgpneighbors:
                bgpneighbors_item = bgpneighbors_item_data.to_dict()
                bgpneighbors.append(bgpneighbors_item)

        peergroup_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.peergroup_options, Unset):
            peergroup_options = []
            for peergroup_options_item_data in self.peergroup_options:
                peergroup_options_item = peergroup_options_item_data.to_dict()
                peergroup_options.append(peergroup_options_item)

        updatesource_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.updatesource_options, Unset):
            updatesource_options = []
            for updatesource_options_item_data in self.updatesource_options:
                updatesource_options_item = updatesource_options_item_data.to_dict()
                updatesource_options.append(updatesource_options_item)

        defaultoriginateroutemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.defaultoriginateroutemap_options, Unset):
            defaultoriginateroutemap_options = []
            for defaultoriginateroutemap_options_item_data in self.defaultoriginateroutemap_options:
                defaultoriginateroutemap_options_item = defaultoriginateroutemap_options_item_data.to_dict()
                defaultoriginateroutemap_options.append(defaultoriginateroutemap_options_item)

        distribute_in_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.distribute_in_options, Unset):
            distribute_in_options = []
            for distribute_in_options_item_data in self.distribute_in_options:
                distribute_in_options_item = distribute_in_options_item_data.to_dict()
                distribute_in_options.append(distribute_in_options_item)

        distribute_out_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.distribute_out_options, Unset):
            distribute_out_options = []
            for distribute_out_options_item_data in self.distribute_out_options:
                distribute_out_options_item = distribute_out_options_item_data.to_dict()
                distribute_out_options.append(distribute_out_options_item)

        prefixfilter_in_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prefixfilter_in_options, Unset):
            prefixfilter_in_options = []
            for prefixfilter_in_options_item_data in self.prefixfilter_in_options:
                prefixfilter_in_options_item = prefixfilter_in_options_item_data.to_dict()
                prefixfilter_in_options.append(prefixfilter_in_options_item)

        prefixfilter_out_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.prefixfilter_out_options, Unset):
            prefixfilter_out_options = []
            for prefixfilter_out_options_item_data in self.prefixfilter_out_options:
                prefixfilter_out_options_item = prefixfilter_out_options_item_data.to_dict()
                prefixfilter_out_options.append(prefixfilter_out_options_item)

        aspathfilter_in_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aspathfilter_in_options, Unset):
            aspathfilter_in_options = []
            for aspathfilter_in_options_item_data in self.aspathfilter_in_options:
                aspathfilter_in_options_item = aspathfilter_in_options_item_data.to_dict()
                aspathfilter_in_options.append(aspathfilter_in_options_item)

        aspathfilter_out_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aspathfilter_out_options, Unset):
            aspathfilter_out_options = []
            for aspathfilter_out_options_item_data in self.aspathfilter_out_options:
                aspathfilter_out_options_item = aspathfilter_out_options_item_data.to_dict()
                aspathfilter_out_options.append(aspathfilter_out_options_item)

        routemap_in_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.routemap_in_options, Unset):
            routemap_in_options = []
            for routemap_in_options_item_data in self.routemap_in_options:
                routemap_in_options_item = routemap_in_options_item_data.to_dict()
                routemap_in_options.append(routemap_in_options_item)

        routemap_out_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.routemap_out_options, Unset):
            routemap_out_options = []
            for routemap_out_options_item_data in self.routemap_out_options:
                routemap_out_options_item = routemap_out_options_item_data.to_dict()
                routemap_out_options.append(routemap_out_options_item)

        unsuppressmap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unsuppressmap_options, Unset):
            unsuppressmap_options = []
            for unsuppressmap_options_item_data in self.unsuppressmap_options:
                unsuppressmap_options_item = unsuppressmap_options_item_data.to_dict()
                unsuppressmap_options.append(unsuppressmap_options_item)

        bfd_peer_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bfd_peer_options, Unset):
            bfd_peer_options = []
            for bfd_peer_options_item_data in self.bfd_peer_options:
                bfd_peer_options_item = bfd_peer_options_item_data.to_dict()
                bfd_peer_options.append(bfd_peer_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bgpneighbors is not UNSET:
            field_dict["bgpneighbors"] = bgpneighbors
        if peergroup_options is not UNSET:
            field_dict["peergroup_options"] = peergroup_options
        if updatesource_options is not UNSET:
            field_dict["updatesource_options"] = updatesource_options
        if defaultoriginateroutemap_options is not UNSET:
            field_dict["defaultoriginateroutemap_options"] = defaultoriginateroutemap_options
        if distribute_in_options is not UNSET:
            field_dict["distribute_in_options"] = distribute_in_options
        if distribute_out_options is not UNSET:
            field_dict["distribute_out_options"] = distribute_out_options
        if prefixfilter_in_options is not UNSET:
            field_dict["prefixfilter_in_options"] = prefixfilter_in_options
        if prefixfilter_out_options is not UNSET:
            field_dict["prefixfilter_out_options"] = prefixfilter_out_options
        if aspathfilter_in_options is not UNSET:
            field_dict["aspathfilter_in_options"] = aspathfilter_in_options
        if aspathfilter_out_options is not UNSET:
            field_dict["aspathfilter_out_options"] = aspathfilter_out_options
        if routemap_in_options is not UNSET:
            field_dict["routemap_in_options"] = routemap_in_options
        if routemap_out_options is not UNSET:
            field_dict["routemap_out_options"] = routemap_out_options
        if unsuppressmap_options is not UNSET:
            field_dict["unsuppressmap_options"] = unsuppressmap_options
        if bfd_peer_options is not UNSET:
            field_dict["bfd_peer_options"] = bfd_peer_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_bgp_neighbor import FrrBgpNeighbor
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _bgpneighbors = d.pop("bgpneighbors", UNSET)
        bgpneighbors: list[FrrBgpNeighbor] | Unset = UNSET
        if _bgpneighbors is not UNSET:
            bgpneighbors = []
            for bgpneighbors_item_data in _bgpneighbors:
                bgpneighbors_item = FrrBgpNeighbor.from_dict(bgpneighbors_item_data)

                bgpneighbors.append(bgpneighbors_item)

        _peergroup_options = d.pop("peergroup_options", UNSET)
        peergroup_options: list[TextValue] | Unset = UNSET
        if _peergroup_options is not UNSET:
            peergroup_options = []
            for peergroup_options_item_data in _peergroup_options:
                peergroup_options_item = TextValue.from_dict(peergroup_options_item_data)

                peergroup_options.append(peergroup_options_item)

        _updatesource_options = d.pop("updatesource_options", UNSET)
        updatesource_options: list[TextValue] | Unset = UNSET
        if _updatesource_options is not UNSET:
            updatesource_options = []
            for updatesource_options_item_data in _updatesource_options:
                updatesource_options_item = TextValue.from_dict(updatesource_options_item_data)

                updatesource_options.append(updatesource_options_item)

        _defaultoriginateroutemap_options = d.pop("defaultoriginateroutemap_options", UNSET)
        defaultoriginateroutemap_options: list[TextValue] | Unset = UNSET
        if _defaultoriginateroutemap_options is not UNSET:
            defaultoriginateroutemap_options = []
            for defaultoriginateroutemap_options_item_data in _defaultoriginateroutemap_options:
                defaultoriginateroutemap_options_item = TextValue.from_dict(defaultoriginateroutemap_options_item_data)

                defaultoriginateroutemap_options.append(defaultoriginateroutemap_options_item)

        _distribute_in_options = d.pop("distribute_in_options", UNSET)
        distribute_in_options: list[TextValue] | Unset = UNSET
        if _distribute_in_options is not UNSET:
            distribute_in_options = []
            for distribute_in_options_item_data in _distribute_in_options:
                distribute_in_options_item = TextValue.from_dict(distribute_in_options_item_data)

                distribute_in_options.append(distribute_in_options_item)

        _distribute_out_options = d.pop("distribute_out_options", UNSET)
        distribute_out_options: list[TextValue] | Unset = UNSET
        if _distribute_out_options is not UNSET:
            distribute_out_options = []
            for distribute_out_options_item_data in _distribute_out_options:
                distribute_out_options_item = TextValue.from_dict(distribute_out_options_item_data)

                distribute_out_options.append(distribute_out_options_item)

        _prefixfilter_in_options = d.pop("prefixfilter_in_options", UNSET)
        prefixfilter_in_options: list[TextValue] | Unset = UNSET
        if _prefixfilter_in_options is not UNSET:
            prefixfilter_in_options = []
            for prefixfilter_in_options_item_data in _prefixfilter_in_options:
                prefixfilter_in_options_item = TextValue.from_dict(prefixfilter_in_options_item_data)

                prefixfilter_in_options.append(prefixfilter_in_options_item)

        _prefixfilter_out_options = d.pop("prefixfilter_out_options", UNSET)
        prefixfilter_out_options: list[TextValue] | Unset = UNSET
        if _prefixfilter_out_options is not UNSET:
            prefixfilter_out_options = []
            for prefixfilter_out_options_item_data in _prefixfilter_out_options:
                prefixfilter_out_options_item = TextValue.from_dict(prefixfilter_out_options_item_data)

                prefixfilter_out_options.append(prefixfilter_out_options_item)

        _aspathfilter_in_options = d.pop("aspathfilter_in_options", UNSET)
        aspathfilter_in_options: list[TextValue] | Unset = UNSET
        if _aspathfilter_in_options is not UNSET:
            aspathfilter_in_options = []
            for aspathfilter_in_options_item_data in _aspathfilter_in_options:
                aspathfilter_in_options_item = TextValue.from_dict(aspathfilter_in_options_item_data)

                aspathfilter_in_options.append(aspathfilter_in_options_item)

        _aspathfilter_out_options = d.pop("aspathfilter_out_options", UNSET)
        aspathfilter_out_options: list[TextValue] | Unset = UNSET
        if _aspathfilter_out_options is not UNSET:
            aspathfilter_out_options = []
            for aspathfilter_out_options_item_data in _aspathfilter_out_options:
                aspathfilter_out_options_item = TextValue.from_dict(aspathfilter_out_options_item_data)

                aspathfilter_out_options.append(aspathfilter_out_options_item)

        _routemap_in_options = d.pop("routemap_in_options", UNSET)
        routemap_in_options: list[TextValue] | Unset = UNSET
        if _routemap_in_options is not UNSET:
            routemap_in_options = []
            for routemap_in_options_item_data in _routemap_in_options:
                routemap_in_options_item = TextValue.from_dict(routemap_in_options_item_data)

                routemap_in_options.append(routemap_in_options_item)

        _routemap_out_options = d.pop("routemap_out_options", UNSET)
        routemap_out_options: list[TextValue] | Unset = UNSET
        if _routemap_out_options is not UNSET:
            routemap_out_options = []
            for routemap_out_options_item_data in _routemap_out_options:
                routemap_out_options_item = TextValue.from_dict(routemap_out_options_item_data)

                routemap_out_options.append(routemap_out_options_item)

        _unsuppressmap_options = d.pop("unsuppressmap_options", UNSET)
        unsuppressmap_options: list[TextValue] | Unset = UNSET
        if _unsuppressmap_options is not UNSET:
            unsuppressmap_options = []
            for unsuppressmap_options_item_data in _unsuppressmap_options:
                unsuppressmap_options_item = TextValue.from_dict(unsuppressmap_options_item_data)

                unsuppressmap_options.append(unsuppressmap_options_item)

        _bfd_peer_options = d.pop("bfd_peer_options", UNSET)
        bfd_peer_options: list[TextValue] | Unset = UNSET
        if _bfd_peer_options is not UNSET:
            bfd_peer_options = []
            for bfd_peer_options_item_data in _bfd_peer_options:
                bfd_peer_options_item = TextValue.from_dict(bfd_peer_options_item_data)

                bfd_peer_options.append(bfd_peer_options_item)

        frr_bgp_neighbors_list = cls(
            bgpneighbors=bgpneighbors,
            peergroup_options=peergroup_options,
            updatesource_options=updatesource_options,
            defaultoriginateroutemap_options=defaultoriginateroutemap_options,
            distribute_in_options=distribute_in_options,
            distribute_out_options=distribute_out_options,
            prefixfilter_in_options=prefixfilter_in_options,
            prefixfilter_out_options=prefixfilter_out_options,
            aspathfilter_in_options=aspathfilter_in_options,
            aspathfilter_out_options=aspathfilter_out_options,
            routemap_in_options=routemap_in_options,
            routemap_out_options=routemap_out_options,
            unsuppressmap_options=unsuppressmap_options,
            bfd_peer_options=bfd_peer_options,
        )

        frr_bgp_neighbors_list.additional_properties = d
        return frr_bgp_neighbors_list

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
