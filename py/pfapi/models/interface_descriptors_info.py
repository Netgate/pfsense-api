from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.interface_descriptors_info_bridges import InterfaceDescriptorsInfoBridges
    from ..models.interface_descriptors_info_gif import InterfaceDescriptorsInfoGif
    from ..models.interface_descriptors_info_gre import InterfaceDescriptorsInfoGre
    from ..models.interface_descriptors_info_lagg import InterfaceDescriptorsInfoLagg
    from ..models.interface_descriptors_info_physical import InterfaceDescriptorsInfoPhysical
    from ..models.interface_descriptors_info_ppp import InterfaceDescriptorsInfoPpp
    from ..models.interface_descriptors_info_qinq import InterfaceDescriptorsInfoQinq
    from ..models.interface_descriptors_info_vlan import InterfaceDescriptorsInfoVlan


T = TypeVar("T", bound="InterfaceDescriptorsInfo")


@_attrs_define
class InterfaceDescriptorsInfo:
    """Mapping of interface names to their descriptions.

    Attributes:
        gre (InterfaceDescriptorsInfoGre):
        gif (InterfaceDescriptorsInfoGif):
        lagg (InterfaceDescriptorsInfoLagg):
        qinq (InterfaceDescriptorsInfoQinq):
        ppp (InterfaceDescriptorsInfoPpp):
        bridges (InterfaceDescriptorsInfoBridges):
        vlan (InterfaceDescriptorsInfoVlan):
        physical (InterfaceDescriptorsInfoPhysical):
    """

    gre: "InterfaceDescriptorsInfoGre"
    gif: "InterfaceDescriptorsInfoGif"
    lagg: "InterfaceDescriptorsInfoLagg"
    qinq: "InterfaceDescriptorsInfoQinq"
    ppp: "InterfaceDescriptorsInfoPpp"
    bridges: "InterfaceDescriptorsInfoBridges"
    vlan: "InterfaceDescriptorsInfoVlan"
    physical: "InterfaceDescriptorsInfoPhysical"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gre = self.gre.to_dict()

        gif = self.gif.to_dict()

        lagg = self.lagg.to_dict()

        qinq = self.qinq.to_dict()

        ppp = self.ppp.to_dict()

        bridges = self.bridges.to_dict()

        vlan = self.vlan.to_dict()

        physical = self.physical.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gre": gre,
                "gif": gif,
                "lagg": lagg,
                "qinq": qinq,
                "ppp": ppp,
                "bridges": bridges,
                "vlan": vlan,
                "physical": physical,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interface_descriptors_info_bridges import InterfaceDescriptorsInfoBridges
        from ..models.interface_descriptors_info_gif import InterfaceDescriptorsInfoGif
        from ..models.interface_descriptors_info_gre import InterfaceDescriptorsInfoGre
        from ..models.interface_descriptors_info_lagg import InterfaceDescriptorsInfoLagg
        from ..models.interface_descriptors_info_physical import InterfaceDescriptorsInfoPhysical
        from ..models.interface_descriptors_info_ppp import InterfaceDescriptorsInfoPpp
        from ..models.interface_descriptors_info_qinq import InterfaceDescriptorsInfoQinq
        from ..models.interface_descriptors_info_vlan import InterfaceDescriptorsInfoVlan

        d = src_dict.copy()
        gre = InterfaceDescriptorsInfoGre.from_dict(d.pop("gre"))

        gif = InterfaceDescriptorsInfoGif.from_dict(d.pop("gif"))

        lagg = InterfaceDescriptorsInfoLagg.from_dict(d.pop("lagg"))

        qinq = InterfaceDescriptorsInfoQinq.from_dict(d.pop("qinq"))

        ppp = InterfaceDescriptorsInfoPpp.from_dict(d.pop("ppp"))

        bridges = InterfaceDescriptorsInfoBridges.from_dict(d.pop("bridges"))

        vlan = InterfaceDescriptorsInfoVlan.from_dict(d.pop("vlan"))

        physical = InterfaceDescriptorsInfoPhysical.from_dict(d.pop("physical"))

        interface_descriptors_info = cls(
            gre=gre,
            gif=gif,
            lagg=lagg,
            qinq=qinq,
            ppp=ppp,
            bridges=bridges,
            vlan=vlan,
            physical=physical,
        )

        interface_descriptors_info.additional_properties = d
        return interface_descriptors_info

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
