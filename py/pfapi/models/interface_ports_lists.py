from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        gres (List['GREInterface']):
        gifs (List['GIFInterface']):
        bridges (List['BridgeInterface']):
        vlans (List['VLANInterface']):
        ppps (List['PPPInterface']):
        qinqs (List['QinQInterface']):
        laggs (List['LAGGInterface']):
        wan (Interface): Detailed interface information
        lan (Interface): Detailed interface information
        physical (List['PhysicalInterface']):
    """

    gres: List["GREInterface"]
    gifs: List["GIFInterface"]
    bridges: List["BridgeInterface"]
    vlans: List["VLANInterface"]
    ppps: List["PPPInterface"]
    qinqs: List["QinQInterface"]
    laggs: List["LAGGInterface"]
    wan: "Interface"
    lan: "Interface"
    physical: List["PhysicalInterface"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gres = []
        for gres_item_data in self.gres:
            gres_item = gres_item_data.to_dict()
            gres.append(gres_item)

        gifs = []
        for gifs_item_data in self.gifs:
            gifs_item = gifs_item_data.to_dict()
            gifs.append(gifs_item)

        bridges = []
        for bridges_item_data in self.bridges:
            bridges_item = bridges_item_data.to_dict()
            bridges.append(bridges_item)

        vlans = []
        for vlans_item_data in self.vlans:
            vlans_item = vlans_item_data.to_dict()
            vlans.append(vlans_item)

        ppps = []
        for ppps_item_data in self.ppps:
            ppps_item = ppps_item_data.to_dict()
            ppps.append(ppps_item)

        qinqs = []
        for qinqs_item_data in self.qinqs:
            qinqs_item = qinqs_item_data.to_dict()
            qinqs.append(qinqs_item)

        laggs = []
        for laggs_item_data in self.laggs:
            laggs_item = laggs_item_data.to_dict()
            laggs.append(laggs_item)

        wan = self.wan.to_dict()

        lan = self.lan.to_dict()

        physical = []
        for physical_item_data in self.physical:
            physical_item = physical_item_data.to_dict()
            physical.append(physical_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gres": gres,
                "gifs": gifs,
                "bridges": bridges,
                "vlans": vlans,
                "ppps": ppps,
                "qinqs": qinqs,
                "laggs": laggs,
                "wan": wan,
                "lan": lan,
                "physical": physical,
            }
        )

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
        _gres = d.pop("gres")
        for gres_item_data in _gres:
            gres_item = GREInterface.from_dict(gres_item_data)

            gres.append(gres_item)

        gifs = []
        _gifs = d.pop("gifs")
        for gifs_item_data in _gifs:
            gifs_item = GIFInterface.from_dict(gifs_item_data)

            gifs.append(gifs_item)

        bridges = []
        _bridges = d.pop("bridges")
        for bridges_item_data in _bridges:
            bridges_item = BridgeInterface.from_dict(bridges_item_data)

            bridges.append(bridges_item)

        vlans = []
        _vlans = d.pop("vlans")
        for vlans_item_data in _vlans:
            vlans_item = VLANInterface.from_dict(vlans_item_data)

            vlans.append(vlans_item)

        ppps = []
        _ppps = d.pop("ppps")
        for ppps_item_data in _ppps:
            ppps_item = PPPInterface.from_dict(ppps_item_data)

            ppps.append(ppps_item)

        qinqs = []
        _qinqs = d.pop("qinqs")
        for qinqs_item_data in _qinqs:
            qinqs_item = QinQInterface.from_dict(qinqs_item_data)

            qinqs.append(qinqs_item)

        laggs = []
        _laggs = d.pop("laggs")
        for laggs_item_data in _laggs:
            laggs_item = LAGGInterface.from_dict(laggs_item_data)

            laggs.append(laggs_item)

        wan = Interface.from_dict(d.pop("wan"))

        lan = Interface.from_dict(d.pop("lan"))

        physical = []
        _physical = d.pop("physical")
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
