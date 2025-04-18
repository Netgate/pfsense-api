from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lagg_interface_lacptimeout import LAGGInterfaceLacptimeout
from ..models.lagg_interface_proto import LAGGInterfaceProto
from ..types import UNSET, Unset

T = TypeVar("T", bound="LAGGInterface")


@_attrs_define
class LAGGInterface:
    """
    Attributes:
        members (List[str]):
        descr (Union[Unset, str]): description
        laggif_device (Union[Unset, str]): generated by system when create lagg
        proto (Union[Unset, LAGGInterfaceProto]): lagg protocol
            valid value = none, lacp, failover, loadbalance, roundrobin
        failovermaster (Union[Unset, str]): (for proto=failover only) failover master interface
        lacptimeout (Union[Unset, LAGGInterfaceLacptimeout]): (for proto=lacp only) LACP Timeout Mode
            valid value = slow, fast
        lagghash (Union[Unset, str]): (for proto=lacp or loadbalance) hash algorithms for the packet layers
            valid value = "l2,l3,l4", "l2", "l3", "l4", "l2,l3", "l3,l4", "l2,l4"
    """

    members: List[str]
    descr: Union[Unset, str] = UNSET
    laggif_device: Union[Unset, str] = UNSET
    proto: Union[Unset, LAGGInterfaceProto] = UNSET
    failovermaster: Union[Unset, str] = UNSET
    lacptimeout: Union[Unset, LAGGInterfaceLacptimeout] = UNSET
    lagghash: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        members = self.members

        descr = self.descr

        laggif_device = self.laggif_device

        proto: Union[Unset, str] = UNSET
        if not isinstance(self.proto, Unset):
            proto = self.proto.value

        failovermaster = self.failovermaster

        lacptimeout: Union[Unset, str] = UNSET
        if not isinstance(self.lacptimeout, Unset):
            lacptimeout = self.lacptimeout.value

        lagghash = self.lagghash

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "members": members,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if laggif_device is not UNSET:
            field_dict["laggif_device"] = laggif_device
        if proto is not UNSET:
            field_dict["proto"] = proto
        if failovermaster is not UNSET:
            field_dict["failovermaster"] = failovermaster
        if lacptimeout is not UNSET:
            field_dict["lacptimeout"] = lacptimeout
        if lagghash is not UNSET:
            field_dict["lagghash"] = lagghash

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        members = cast(List[str], d.pop("members"))

        descr = d.pop("descr", UNSET)

        laggif_device = d.pop("laggif_device", UNSET)

        _proto = d.pop("proto", UNSET)
        proto: Union[Unset, LAGGInterfaceProto]
        if isinstance(_proto, Unset):
            proto = UNSET
        else:
            proto = LAGGInterfaceProto(_proto)

        failovermaster = d.pop("failovermaster", UNSET)

        _lacptimeout = d.pop("lacptimeout", UNSET)
        lacptimeout: Union[Unset, LAGGInterfaceLacptimeout]
        if isinstance(_lacptimeout, Unset):
            lacptimeout = UNSET
        else:
            lacptimeout = LAGGInterfaceLacptimeout(_lacptimeout)

        lagghash = d.pop("lagghash", UNSET)

        lagg_interface = cls(
            members=members,
            descr=descr,
            laggif_device=laggif_device,
            proto=proto,
            failovermaster=failovermaster,
            lacptimeout=lacptimeout,
            lagghash=lagghash,
        )

        lagg_interface.additional_properties = d
        return lagg_interface

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
