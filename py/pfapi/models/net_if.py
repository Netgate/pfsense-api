from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.net_if_addr import NetIfAddr
    from ..models.net_if_dev_config import NetIfDevConfig
    from ..models.net_if_dhcp import NetIfDhcp
    from ..models.net_if_info import NetIfInfo
    from ..models.net_if_ipv_6rd import NetIfIpv6RD
    from ..models.net_if_options import NetIfOptions
    from ..models.net_if_owner import NetIfOwner


T = TypeVar("T", bound="NetIf")


@_attrs_define
class NetIf:
    """Network interface descriptor. By default, the assigned name of the interface
    is the same as the identity. Both the assigned and identity names can be
    changed in the configuration. The device_name can be changed if the driver
    supports it.

        Attributes:
            assigned_name (str): user assigned name, e.g. MYLAN
            device_name (str): host device name, e.g. ix1
            identity (str): identity of device, e.g. opt1
            descr (str): user provided interface description
            enable (bool): interface is enabled
            pseudo (bool): logical interface, such as a PPP tunnel
            addr_type (str): one of (dhcp, ipaddr)
            addr6_type (str): one of (slaac, dhcp6, 6to4, 6rd, ipaddrv6, none)
            options (NetIfOptions):
            addr (NetIfAddr):
            dhcp (NetIfDhcp):
            ipv6rd (NetIfIpv6RD):
            ownership (NetIfOwner): An interface can be owned by different OS subsystems: host, vpp,
                container or vm (virtual machine). Other than a host-owner, each
                owner has a unique ID and linked to its associated configuraton.
            device_config (NetIfDevConfig):
            info (NetIfInfo): Information about the interface as identified on the host
    """

    assigned_name: str
    device_name: str
    identity: str
    descr: str
    enable: bool
    pseudo: bool
    addr_type: str
    addr6_type: str
    options: "NetIfOptions"
    addr: "NetIfAddr"
    dhcp: "NetIfDhcp"
    ipv6rd: "NetIfIpv6RD"
    ownership: "NetIfOwner"
    device_config: "NetIfDevConfig"
    info: "NetIfInfo"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        assigned_name = self.assigned_name

        device_name = self.device_name

        identity = self.identity

        descr = self.descr

        enable = self.enable

        pseudo = self.pseudo

        addr_type = self.addr_type

        addr6_type = self.addr6_type

        options = self.options.to_dict()

        addr = self.addr.to_dict()

        dhcp = self.dhcp.to_dict()

        ipv6rd = self.ipv6rd.to_dict()

        ownership = self.ownership.to_dict()

        device_config = self.device_config.to_dict()

        info = self.info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assigned_name": assigned_name,
                "device_name": device_name,
                "identity": identity,
                "descr": descr,
                "enable": enable,
                "pseudo": pseudo,
                "addr_type": addr_type,
                "addr6_type": addr6_type,
                "options": options,
                "addr": addr,
                "dhcp": dhcp,
                "ipv6rd": ipv6rd,
                "ownership": ownership,
                "device_config": device_config,
                "info": info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.net_if_addr import NetIfAddr
        from ..models.net_if_dev_config import NetIfDevConfig
        from ..models.net_if_dhcp import NetIfDhcp
        from ..models.net_if_info import NetIfInfo
        from ..models.net_if_ipv_6rd import NetIfIpv6RD
        from ..models.net_if_options import NetIfOptions
        from ..models.net_if_owner import NetIfOwner

        d = src_dict.copy()
        assigned_name = d.pop("assigned_name")

        device_name = d.pop("device_name")

        identity = d.pop("identity")

        descr = d.pop("descr")

        enable = d.pop("enable")

        pseudo = d.pop("pseudo")

        addr_type = d.pop("addr_type")

        addr6_type = d.pop("addr6_type")

        options = NetIfOptions.from_dict(d.pop("options"))

        addr = NetIfAddr.from_dict(d.pop("addr"))

        dhcp = NetIfDhcp.from_dict(d.pop("dhcp"))

        ipv6rd = NetIfIpv6RD.from_dict(d.pop("ipv6rd"))

        ownership = NetIfOwner.from_dict(d.pop("ownership"))

        device_config = NetIfDevConfig.from_dict(d.pop("device_config"))

        info = NetIfInfo.from_dict(d.pop("info"))

        net_if = cls(
            assigned_name=assigned_name,
            device_name=device_name,
            identity=identity,
            descr=descr,
            enable=enable,
            pseudo=pseudo,
            addr_type=addr_type,
            addr6_type=addr6_type,
            options=options,
            addr=addr,
            dhcp=dhcp,
            ipv6rd=ipv6rd,
            ownership=ownership,
            device_config=device_config,
            info=info,
        )

        net_if.additional_properties = d
        return net_if

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
