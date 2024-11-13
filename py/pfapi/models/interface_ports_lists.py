from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        gres (Union[Unset, List['GREInterface']]):
        gifs (Union[Unset, List['GIFInterface']]):
        bridges (Union[Unset, List['BridgeInterface']]):
        vlans (Union[Unset, List['VLANInterface']]):
        ppps (Union[Unset, List['PPPInterface']]):
        qinqs (Union[Unset, List['QinQInterface']]):
        laggs (Union[Unset, List['LAGGInterface']]):
        wan (Union[Unset, Interface]): Detailed interface information
        lan (Union[Unset, Interface]): Detailed interface information
        physical (Union[Unset, List['PhysicalInterface']]):
    """

    gres: Union[Unset, List["GREInterface"]] = UNSET
    gifs: Union[Unset, List["GIFInterface"]] = UNSET
    bridges: Union[Unset, List["BridgeInterface"]] = UNSET
    vlans: Union[Unset, List["VLANInterface"]] = UNSET
    ppps: Union[Unset, List["PPPInterface"]] = UNSET
    qinqs: Union[Unset, List["QinQInterface"]] = UNSET
    laggs: Union[Unset, List["LAGGInterface"]] = UNSET
    wan: Union[Unset, "Interface"] = UNSET
    lan: Union[Unset, "Interface"] = UNSET
    physical: Union[Unset, List["PhysicalInterface"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gres: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.gres, Unset):
            gres = []
            for gres_item_data in self.gres:
                gres_item = gres_item_data.to_dict()
                gres.append(gres_item)

        gifs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.gifs, Unset):
            gifs = []
            for gifs_item_data in self.gifs:
                gifs_item = gifs_item_data.to_dict()
                gifs.append(gifs_item)

        bridges: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bridges, Unset):
            bridges = []
            for bridges_item_data in self.bridges:
                bridges_item = bridges_item_data.to_dict()
                bridges.append(bridges_item)

        vlans: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vlans, Unset):
            vlans = []
            for vlans_item_data in self.vlans:
                vlans_item = vlans_item_data.to_dict()
                vlans.append(vlans_item)

        ppps: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ppps, Unset):
            ppps = []
            for ppps_item_data in self.ppps:
                ppps_item = ppps_item_data.to_dict()
                ppps.append(ppps_item)

        qinqs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.qinqs, Unset):
            qinqs = []
            for qinqs_item_data in self.qinqs:
                qinqs_item = qinqs_item_data.to_dict()
                qinqs.append(qinqs_item)

        laggs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.laggs, Unset):
            laggs = []
            for laggs_item_data in self.laggs:
                laggs_item = laggs_item_data.to_dict()
                laggs.append(laggs_item)

        wan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.wan, Unset):
            wan = self.wan.to_dict()

        lan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lan, Unset):
            lan = self.lan.to_dict()

        physical: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.physical, Unset):
            physical = []
            for physical_item_data in self.physical:
                physical_item = physical_item_data.to_dict()
                physical.append(physical_item)

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bridge_interface import BridgeInterface
        from ..models.gif_interface import GIFInterface
        from ..models.gre_interface import GREInterface
        from ..models.interface import Interface
        from ..models.lagg_interface import LAGGInterface
        from ..models.physical_interface import PhysicalInterface
        from ..models.ppp_interface import PPPInterface
        from ..models.qin_q_interface import QinQInterface
        from ..models.vlan_interface import VLANInterface

        d = src_dict.copy()
        gres = []
        _gres = d.pop("gres", UNSET)
        for gres_item_data in _gres or []:
            gres_item = GREInterface.from_dict(gres_item_data)

            gres.append(gres_item)

        gifs = []
        _gifs = d.pop("gifs", UNSET)
        for gifs_item_data in _gifs or []:
            gifs_item = GIFInterface.from_dict(gifs_item_data)

            gifs.append(gifs_item)

        bridges = []
        _bridges = d.pop("bridges", UNSET)
        for bridges_item_data in _bridges or []:
            bridges_item = BridgeInterface.from_dict(bridges_item_data)

            bridges.append(bridges_item)

        vlans = []
        _vlans = d.pop("vlans", UNSET)
        for vlans_item_data in _vlans or []:
            vlans_item = VLANInterface.from_dict(vlans_item_data)

            vlans.append(vlans_item)

        ppps = []
        _ppps = d.pop("ppps", UNSET)
        for ppps_item_data in _ppps or []:
            ppps_item = PPPInterface.from_dict(ppps_item_data)

            ppps.append(ppps_item)

        qinqs = []
        _qinqs = d.pop("qinqs", UNSET)
        for qinqs_item_data in _qinqs or []:
            qinqs_item = QinQInterface.from_dict(qinqs_item_data)

            qinqs.append(qinqs_item)

        laggs = []
        _laggs = d.pop("laggs", UNSET)
        for laggs_item_data in _laggs or []:
            laggs_item = LAGGInterface.from_dict(laggs_item_data)

            laggs.append(laggs_item)

        _wan = d.pop("wan", UNSET)
        wan: Union[Unset, Interface]
        if isinstance(_wan, Unset):
            wan = UNSET
        else:
            wan = Interface.from_dict(_wan)

        _lan = d.pop("lan", UNSET)
        lan: Union[Unset, Interface]
        if isinstance(_lan, Unset):
            lan = UNSET
        else:
            lan = Interface.from_dict(_lan)

        physical = []
        _physical = d.pop("physical", UNSET)
        for physical_item_data in _physical or []:
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
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
