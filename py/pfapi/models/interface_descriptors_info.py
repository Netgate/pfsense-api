from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
        gre (Union[Unset, InterfaceDescriptorsInfoGre]):
        gif (Union[Unset, InterfaceDescriptorsInfoGif]):
        lagg (Union[Unset, InterfaceDescriptorsInfoLagg]):
        qinq (Union[Unset, InterfaceDescriptorsInfoQinq]):
        ppp (Union[Unset, InterfaceDescriptorsInfoPpp]):
        bridges (Union[Unset, InterfaceDescriptorsInfoBridges]):
        vlan (Union[Unset, InterfaceDescriptorsInfoVlan]):
        physical (Union[Unset, InterfaceDescriptorsInfoPhysical]):
    """

    gre: Union[Unset, "InterfaceDescriptorsInfoGre"] = UNSET
    gif: Union[Unset, "InterfaceDescriptorsInfoGif"] = UNSET
    lagg: Union[Unset, "InterfaceDescriptorsInfoLagg"] = UNSET
    qinq: Union[Unset, "InterfaceDescriptorsInfoQinq"] = UNSET
    ppp: Union[Unset, "InterfaceDescriptorsInfoPpp"] = UNSET
    bridges: Union[Unset, "InterfaceDescriptorsInfoBridges"] = UNSET
    vlan: Union[Unset, "InterfaceDescriptorsInfoVlan"] = UNSET
    physical: Union[Unset, "InterfaceDescriptorsInfoPhysical"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gre: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gre, Unset):
            gre = self.gre.to_dict()

        gif: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gif, Unset):
            gif = self.gif.to_dict()

        lagg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lagg, Unset):
            lagg = self.lagg.to_dict()

        qinq: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.qinq, Unset):
            qinq = self.qinq.to_dict()

        ppp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ppp, Unset):
            ppp = self.ppp.to_dict()

        bridges: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bridges, Unset):
            bridges = self.bridges.to_dict()

        vlan: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vlan, Unset):
            vlan = self.vlan.to_dict()

        physical: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.physical, Unset):
            physical = self.physical.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gre is not UNSET:
            field_dict["gre"] = gre
        if gif is not UNSET:
            field_dict["gif"] = gif
        if lagg is not UNSET:
            field_dict["lagg"] = lagg
        if qinq is not UNSET:
            field_dict["qinq"] = qinq
        if ppp is not UNSET:
            field_dict["ppp"] = ppp
        if bridges is not UNSET:
            field_dict["bridges"] = bridges
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if physical is not UNSET:
            field_dict["physical"] = physical

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
        _gre = d.pop("gre", UNSET)
        gre: Union[Unset, InterfaceDescriptorsInfoGre]
        if isinstance(_gre, Unset):
            gre = UNSET
        else:
            gre = InterfaceDescriptorsInfoGre.from_dict(_gre)

        _gif = d.pop("gif", UNSET)
        gif: Union[Unset, InterfaceDescriptorsInfoGif]
        if isinstance(_gif, Unset):
            gif = UNSET
        else:
            gif = InterfaceDescriptorsInfoGif.from_dict(_gif)

        _lagg = d.pop("lagg", UNSET)
        lagg: Union[Unset, InterfaceDescriptorsInfoLagg]
        if isinstance(_lagg, Unset):
            lagg = UNSET
        else:
            lagg = InterfaceDescriptorsInfoLagg.from_dict(_lagg)

        _qinq = d.pop("qinq", UNSET)
        qinq: Union[Unset, InterfaceDescriptorsInfoQinq]
        if isinstance(_qinq, Unset):
            qinq = UNSET
        else:
            qinq = InterfaceDescriptorsInfoQinq.from_dict(_qinq)

        _ppp = d.pop("ppp", UNSET)
        ppp: Union[Unset, InterfaceDescriptorsInfoPpp]
        if isinstance(_ppp, Unset):
            ppp = UNSET
        else:
            ppp = InterfaceDescriptorsInfoPpp.from_dict(_ppp)

        _bridges = d.pop("bridges", UNSET)
        bridges: Union[Unset, InterfaceDescriptorsInfoBridges]
        if isinstance(_bridges, Unset):
            bridges = UNSET
        else:
            bridges = InterfaceDescriptorsInfoBridges.from_dict(_bridges)

        _vlan = d.pop("vlan", UNSET)
        vlan: Union[Unset, InterfaceDescriptorsInfoVlan]
        if isinstance(_vlan, Unset):
            vlan = UNSET
        else:
            vlan = InterfaceDescriptorsInfoVlan.from_dict(_vlan)

        _physical = d.pop("physical", UNSET)
        physical: Union[Unset, InterfaceDescriptorsInfoPhysical]
        if isinstance(_physical, Unset):
            physical = UNSET
        else:
            physical = InterfaceDescriptorsInfoPhysical.from_dict(_physical)

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
