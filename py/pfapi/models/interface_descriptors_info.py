from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
    from ..models.interface_descriptors_info_vxlan import InterfaceDescriptorsInfoVxlan


T = TypeVar("T", bound="InterfaceDescriptorsInfo")


@_attrs_define
class InterfaceDescriptorsInfo:
    """Mapping of interface names to their descriptions.

    Attributes:
        gre (InterfaceDescriptorsInfoGre | Unset):
        gif (InterfaceDescriptorsInfoGif | Unset):
        lagg (InterfaceDescriptorsInfoLagg | Unset):
        qinq (InterfaceDescriptorsInfoQinq | Unset):
        ppp (InterfaceDescriptorsInfoPpp | Unset):
        bridges (InterfaceDescriptorsInfoBridges | Unset):
        vlan (InterfaceDescriptorsInfoVlan | Unset):
        vxlan (InterfaceDescriptorsInfoVxlan | Unset):
        physical (InterfaceDescriptorsInfoPhysical | Unset):
    """

    gre: InterfaceDescriptorsInfoGre | Unset = UNSET
    gif: InterfaceDescriptorsInfoGif | Unset = UNSET
    lagg: InterfaceDescriptorsInfoLagg | Unset = UNSET
    qinq: InterfaceDescriptorsInfoQinq | Unset = UNSET
    ppp: InterfaceDescriptorsInfoPpp | Unset = UNSET
    bridges: InterfaceDescriptorsInfoBridges | Unset = UNSET
    vlan: InterfaceDescriptorsInfoVlan | Unset = UNSET
    vxlan: InterfaceDescriptorsInfoVxlan | Unset = UNSET
    physical: InterfaceDescriptorsInfoPhysical | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gre: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gre, Unset):
            gre = self.gre.to_dict()

        gif: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gif, Unset):
            gif = self.gif.to_dict()

        lagg: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lagg, Unset):
            lagg = self.lagg.to_dict()

        qinq: dict[str, Any] | Unset = UNSET
        if not isinstance(self.qinq, Unset):
            qinq = self.qinq.to_dict()

        ppp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ppp, Unset):
            ppp = self.ppp.to_dict()

        bridges: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bridges, Unset):
            bridges = self.bridges.to_dict()

        vlan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vlan, Unset):
            vlan = self.vlan.to_dict()

        vxlan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vxlan, Unset):
            vxlan = self.vxlan.to_dict()

        physical: dict[str, Any] | Unset = UNSET
        if not isinstance(self.physical, Unset):
            physical = self.physical.to_dict()

        field_dict: dict[str, Any] = {}
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
        if vxlan is not UNSET:
            field_dict["vxlan"] = vxlan
        if physical is not UNSET:
            field_dict["physical"] = physical

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interface_descriptors_info_bridges import InterfaceDescriptorsInfoBridges
        from ..models.interface_descriptors_info_gif import InterfaceDescriptorsInfoGif
        from ..models.interface_descriptors_info_gre import InterfaceDescriptorsInfoGre
        from ..models.interface_descriptors_info_lagg import InterfaceDescriptorsInfoLagg
        from ..models.interface_descriptors_info_physical import InterfaceDescriptorsInfoPhysical
        from ..models.interface_descriptors_info_ppp import InterfaceDescriptorsInfoPpp
        from ..models.interface_descriptors_info_qinq import InterfaceDescriptorsInfoQinq
        from ..models.interface_descriptors_info_vlan import InterfaceDescriptorsInfoVlan
        from ..models.interface_descriptors_info_vxlan import InterfaceDescriptorsInfoVxlan

        d = dict(src_dict)
        _gre = d.pop("gre", UNSET)
        gre: InterfaceDescriptorsInfoGre | Unset
        if isinstance(_gre, Unset):
            gre = UNSET
        else:
            gre = InterfaceDescriptorsInfoGre.from_dict(_gre)

        _gif = d.pop("gif", UNSET)
        gif: InterfaceDescriptorsInfoGif | Unset
        if isinstance(_gif, Unset):
            gif = UNSET
        else:
            gif = InterfaceDescriptorsInfoGif.from_dict(_gif)

        _lagg = d.pop("lagg", UNSET)
        lagg: InterfaceDescriptorsInfoLagg | Unset
        if isinstance(_lagg, Unset):
            lagg = UNSET
        else:
            lagg = InterfaceDescriptorsInfoLagg.from_dict(_lagg)

        _qinq = d.pop("qinq", UNSET)
        qinq: InterfaceDescriptorsInfoQinq | Unset
        if isinstance(_qinq, Unset):
            qinq = UNSET
        else:
            qinq = InterfaceDescriptorsInfoQinq.from_dict(_qinq)

        _ppp = d.pop("ppp", UNSET)
        ppp: InterfaceDescriptorsInfoPpp | Unset
        if isinstance(_ppp, Unset):
            ppp = UNSET
        else:
            ppp = InterfaceDescriptorsInfoPpp.from_dict(_ppp)

        _bridges = d.pop("bridges", UNSET)
        bridges: InterfaceDescriptorsInfoBridges | Unset
        if isinstance(_bridges, Unset):
            bridges = UNSET
        else:
            bridges = InterfaceDescriptorsInfoBridges.from_dict(_bridges)

        _vlan = d.pop("vlan", UNSET)
        vlan: InterfaceDescriptorsInfoVlan | Unset
        if isinstance(_vlan, Unset):
            vlan = UNSET
        else:
            vlan = InterfaceDescriptorsInfoVlan.from_dict(_vlan)

        _vxlan = d.pop("vxlan", UNSET)
        vxlan: InterfaceDescriptorsInfoVxlan | Unset
        if isinstance(_vxlan, Unset):
            vxlan = UNSET
        else:
            vxlan = InterfaceDescriptorsInfoVxlan.from_dict(_vxlan)

        _physical = d.pop("physical", UNSET)
        physical: InterfaceDescriptorsInfoPhysical | Unset
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
            vxlan=vxlan,
            physical=physical,
        )

        interface_descriptors_info.additional_properties = d
        return interface_descriptors_info

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
