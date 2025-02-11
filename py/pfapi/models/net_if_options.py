from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NetIfOptions")


@_attrs_define
class NetIfOptions:
    """
    Attributes:
        blockbogons (bool):
        blockpriv (bool):
        mtu (int):
        mss (int):
        pcp (int):
        promisc (bool):
        member (str):
        mac (str):
        mediaopt (str):
        spoofmac (str):
        tag (int):
    """

    blockbogons: bool
    blockpriv: bool
    mtu: int
    mss: int
    pcp: int
    promisc: bool
    member: str
    mac: str
    mediaopt: str
    spoofmac: str
    tag: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        blockbogons = self.blockbogons

        blockpriv = self.blockpriv

        mtu = self.mtu

        mss = self.mss

        pcp = self.pcp

        promisc = self.promisc

        member = self.member

        mac = self.mac

        mediaopt = self.mediaopt

        spoofmac = self.spoofmac

        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blockbogons": blockbogons,
                "blockpriv": blockpriv,
                "mtu": mtu,
                "mss": mss,
                "pcp": pcp,
                "promisc": promisc,
                "member": member,
                "mac": mac,
                "mediaopt": mediaopt,
                "spoofmac": spoofmac,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        blockbogons = d.pop("blockbogons")

        blockpriv = d.pop("blockpriv")

        mtu = d.pop("mtu")

        mss = d.pop("mss")

        pcp = d.pop("pcp")

        promisc = d.pop("promisc")

        member = d.pop("member")

        mac = d.pop("mac")

        mediaopt = d.pop("mediaopt")

        spoofmac = d.pop("spoofmac")

        tag = d.pop("tag")

        net_if_options = cls(
            blockbogons=blockbogons,
            blockpriv=blockpriv,
            mtu=mtu,
            mss=mss,
            pcp=pcp,
            promisc=promisc,
            member=member,
            mac=mac,
            mediaopt=mediaopt,
            spoofmac=spoofmac,
            tag=tag,
        )

        net_if_options.additional_properties = d
        return net_if_options

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
