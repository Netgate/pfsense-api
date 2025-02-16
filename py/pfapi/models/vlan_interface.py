from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VLANInterface")


@_attrs_define
class VLANInterface:
    """
    Attributes:
        if_device (str): parent interface of the VLAN
        tag (int): 802.1Q VLAN tag (between 1 and 4094)
        pcp (int): 802.1Q VLAN Priority (between 0 and 7)
        descr (str): description
        vlanif (str): generated by system when a VLAN is created
    """

    if_device: str
    tag: int
    pcp: int
    descr: str
    vlanif: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if_device = self.if_device

        tag = self.tag

        pcp = self.pcp

        descr = self.descr

        vlanif = self.vlanif

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "if_device": if_device,
                "tag": tag,
                "pcp": pcp,
                "descr": descr,
                "vlanif": vlanif,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        if_device = d.pop("if_device")

        tag = d.pop("tag")

        pcp = d.pop("pcp")

        descr = d.pop("descr")

        vlanif = d.pop("vlanif")

        vlan_interface = cls(
            if_device=if_device,
            tag=tag,
            pcp=pcp,
            descr=descr,
            vlanif=vlanif,
        )

        vlan_interface.additional_properties = d
        return vlan_interface

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
