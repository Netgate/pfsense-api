from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bridge_interface import BridgeInterface
    from ..models.gif_interface import GIFInterface
    from ..models.gre_interface import GREInterface
    from ..models.interface import Interface
    from ..models.lagg_interface import LAGGInterface
    from ..models.physical_interface import PhysicalInterface
    from ..models.ppp_interface import PPPInterface
    from ..models.qin_q_interface import QinQInterface
    from ..models.vlan_interface import VLANInterface


T = TypeVar("T", bound="InterfacePortsLists")


@_attrs_define
class InterfacePortsLists:
    """
    Attributes:
        gres (list[GREInterface] | Unset):
        gifs (list[GIFInterface] | Unset):
        bridges (list[BridgeInterface] | Unset):
        vlans (list[VLANInterface] | Unset):
        ppps (list[PPPInterface] | Unset):
        qinqs (list[QinQInterface] | Unset):
        laggs (list[LAGGInterface] | Unset):
        wan (Interface | Unset): Detailed interface information
        lan (Interface | Unset): Detailed interface information
        physical (list[PhysicalInterface] | Unset):
    """

    gres: list[GREInterface] | Unset = UNSET
    gifs: list[GIFInterface] | Unset = UNSET
    bridges: list[BridgeInterface] | Unset = UNSET
    vlans: list[VLANInterface] | Unset = UNSET
    ppps: list[PPPInterface] | Unset = UNSET
    qinqs: list[QinQInterface] | Unset = UNSET
    laggs: list[LAGGInterface] | Unset = UNSET
    wan: Interface | Unset = UNSET
    lan: Interface | Unset = UNSET
    physical: list[PhysicalInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gres: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gres, Unset):
            gres = []
            for gres_item_data in self.gres:
                gres_item = gres_item_data.to_dict()
                gres.append(gres_item)

        gifs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gifs, Unset):
            gifs = []
            for gifs_item_data in self.gifs:
                gifs_item = gifs_item_data.to_dict()
                gifs.append(gifs_item)

        bridges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bridges, Unset):
            bridges = []
            for bridges_item_data in self.bridges:
                bridges_item = bridges_item_data.to_dict()
                bridges.append(bridges_item)

        vlans: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vlans, Unset):
            vlans = []
            for vlans_item_data in self.vlans:
                vlans_item = vlans_item_data.to_dict()
                vlans.append(vlans_item)

        ppps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ppps, Unset):
            ppps = []
            for ppps_item_data in self.ppps:
                ppps_item = ppps_item_data.to_dict()
                ppps.append(ppps_item)

        qinqs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.qinqs, Unset):
            qinqs = []
            for qinqs_item_data in self.qinqs:
                qinqs_item = qinqs_item_data.to_dict()
                qinqs.append(qinqs_item)

        laggs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.laggs, Unset):
            laggs = []
            for laggs_item_data in self.laggs:
                laggs_item = laggs_item_data.to_dict()
                laggs.append(laggs_item)

        wan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan, Unset):
            wan = self.wan.to_dict()

        lan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lan, Unset):
            lan = self.lan.to_dict()

        physical: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.physical, Unset):
            physical = []
            for physical_item_data in self.physical:
                physical_item = physical_item_data.to_dict()
                physical.append(physical_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gres is not UNSET:
            field_dict["gres"] = gres
        if gifs is not UNSET:
            field_dict["gifs"] = gifs
        if bridges is not UNSET:
            field_dict["bridges"] = bridges
        if vlans is not UNSET:
            field_dict["vlans"] = vlans
        if ppps is not UNSET:
            field_dict["ppps"] = ppps
        if qinqs is not UNSET:
            field_dict["qinqs"] = qinqs
        if laggs is not UNSET:
            field_dict["laggs"] = laggs
        if wan is not UNSET:
            field_dict["wan"] = wan
        if lan is not UNSET:
            field_dict["lan"] = lan
        if physical is not UNSET:
            field_dict["physical"] = physical

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bridge_interface import BridgeInterface
        from ..models.gif_interface import GIFInterface
        from ..models.gre_interface import GREInterface
        from ..models.interface import Interface
        from ..models.lagg_interface import LAGGInterface
        from ..models.physical_interface import PhysicalInterface
        from ..models.ppp_interface import PPPInterface
        from ..models.qin_q_interface import QinQInterface
        from ..models.vlan_interface import VLANInterface

        d = dict(src_dict)
        _gres = d.pop("gres", UNSET)
        gres: list[GREInterface] | Unset = UNSET
        if _gres is not UNSET:
            gres = []
            for gres_item_data in _gres:
                gres_item = GREInterface.from_dict(gres_item_data)

                gres.append(gres_item)

        _gifs = d.pop("gifs", UNSET)
        gifs: list[GIFInterface] | Unset = UNSET
        if _gifs is not UNSET:
            gifs = []
            for gifs_item_data in _gifs:
                gifs_item = GIFInterface.from_dict(gifs_item_data)

                gifs.append(gifs_item)

        _bridges = d.pop("bridges", UNSET)
        bridges: list[BridgeInterface] | Unset = UNSET
        if _bridges is not UNSET:
            bridges = []
            for bridges_item_data in _bridges:
                bridges_item = BridgeInterface.from_dict(bridges_item_data)

                bridges.append(bridges_item)

        _vlans = d.pop("vlans", UNSET)
        vlans: list[VLANInterface] | Unset = UNSET
        if _vlans is not UNSET:
            vlans = []
            for vlans_item_data in _vlans:
                vlans_item = VLANInterface.from_dict(vlans_item_data)

                vlans.append(vlans_item)

        _ppps = d.pop("ppps", UNSET)
        ppps: list[PPPInterface] | Unset = UNSET
        if _ppps is not UNSET:
            ppps = []
            for ppps_item_data in _ppps:
                ppps_item = PPPInterface.from_dict(ppps_item_data)

                ppps.append(ppps_item)

        _qinqs = d.pop("qinqs", UNSET)
        qinqs: list[QinQInterface] | Unset = UNSET
        if _qinqs is not UNSET:
            qinqs = []
            for qinqs_item_data in _qinqs:
                qinqs_item = QinQInterface.from_dict(qinqs_item_data)

                qinqs.append(qinqs_item)

        _laggs = d.pop("laggs", UNSET)
        laggs: list[LAGGInterface] | Unset = UNSET
        if _laggs is not UNSET:
            laggs = []
            for laggs_item_data in _laggs:
                laggs_item = LAGGInterface.from_dict(laggs_item_data)

                laggs.append(laggs_item)

        _wan = d.pop("wan", UNSET)
        wan: Interface | Unset
        if isinstance(_wan, Unset):
            wan = UNSET
        else:
            wan = Interface.from_dict(_wan)

        _lan = d.pop("lan", UNSET)
        lan: Interface | Unset
        if isinstance(_lan, Unset):
            lan = UNSET
        else:
            lan = Interface.from_dict(_lan)

        _physical = d.pop("physical", UNSET)
        physical: list[PhysicalInterface] | Unset = UNSET
        if _physical is not UNSET:
            physical = []
            for physical_item_data in _physical:
                physical_item = PhysicalInterface.from_dict(physical_item_data)

                physical.append(physical_item)

        interface_ports_lists = cls(
            gres=gres,
            gifs=gifs,
            bridges=bridges,
            vlans=vlans,
            ppps=ppps,
            qinqs=qinqs,
            laggs=laggs,
            wan=wan,
            lan=lan,
            physical=physical,
        )

        interface_ports_lists.additional_properties = d
        return interface_ports_lists

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
