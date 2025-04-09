from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
            assigned_name (Union[Unset, str]): user assigned name, e.g. MYLAN
            device_name (Union[Unset, str]): host device name, e.g. ix1
            identity (Union[Unset, str]): identity of device, e.g. opt1
            descr (Union[Unset, str]): user provided interface description
            enable (Union[Unset, bool]): interface is enabled
            pseudo (Union[Unset, bool]): logical interface, such as a PPP tunnel
            addr_type (Union[Unset, str]): one of (dhcp, ipaddr)
            addr6_type (Union[Unset, str]): one of (slaac, dhcp6, 6to4, 6rd, ipaddrv6, none)
            options (Union[Unset, NetIfOptions]):
            addr (Union[Unset, NetIfAddr]):
            dhcp (Union[Unset, NetIfDhcp]):
            ipv6rd (Union[Unset, NetIfIpv6RD]):
            ownership (Union[Unset, NetIfOwner]): An interface can be owned by different OS subsystems: host, vpp,
                container or vm (virtual machine). Other than a host-owner, each
                owner has a unique ID and linked to its associated configuraton.
            device_config (Union[Unset, NetIfDevConfig]):
            info (Union[Unset, NetIfInfo]): Information about the interface as identified on the host
    """

    assigned_name: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    identity: Union[Unset, str] = UNSET
    descr: Union[Unset, str] = UNSET
    enable: Union[Unset, bool] = UNSET
    pseudo: Union[Unset, bool] = UNSET
    addr_type: Union[Unset, str] = UNSET
    addr6_type: Union[Unset, str] = UNSET
    options: Union[Unset, "NetIfOptions"] = UNSET
    addr: Union[Unset, "NetIfAddr"] = UNSET
    dhcp: Union[Unset, "NetIfDhcp"] = UNSET
    ipv6rd: Union[Unset, "NetIfIpv6RD"] = UNSET
    ownership: Union[Unset, "NetIfOwner"] = UNSET
    device_config: Union[Unset, "NetIfDevConfig"] = UNSET
    info: Union[Unset, "NetIfInfo"] = UNSET
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

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        addr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.addr, Unset):
            addr = self.addr.to_dict()

        dhcp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dhcp, Unset):
            dhcp = self.dhcp.to_dict()

        ipv6rd: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ipv6rd, Unset):
            ipv6rd = self.ipv6rd.to_dict()

        ownership: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ownership, Unset):
            ownership = self.ownership.to_dict()

        device_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.device_config, Unset):
            device_config = self.device_config.to_dict()

        info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.info, Unset):
            info = self.info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assigned_name is not UNSET:
            field_dict["assigned_name"] = assigned_name
        if device_name is not UNSET:
            field_dict["device_name"] = device_name
        if identity is not UNSET:
            field_dict["identity"] = identity
        if descr is not UNSET:
            field_dict["descr"] = descr
        if enable is not UNSET:
            field_dict["enable"] = enable
        if pseudo is not UNSET:
            field_dict["pseudo"] = pseudo
        if addr_type is not UNSET:
            field_dict["addr_type"] = addr_type
        if addr6_type is not UNSET:
            field_dict["addr6_type"] = addr6_type
        if options is not UNSET:
            field_dict["options"] = options
        if addr is not UNSET:
            field_dict["addr"] = addr
        if dhcp is not UNSET:
            field_dict["dhcp"] = dhcp
        if ipv6rd is not UNSET:
            field_dict["ipv6rd"] = ipv6rd
        if ownership is not UNSET:
            field_dict["ownership"] = ownership
        if device_config is not UNSET:
            field_dict["device_config"] = device_config
        if info is not UNSET:
            field_dict["info"] = info

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
        assigned_name = d.pop("assigned_name", UNSET)

        device_name = d.pop("device_name", UNSET)

        identity = d.pop("identity", UNSET)

        descr = d.pop("descr", UNSET)

        enable = d.pop("enable", UNSET)

        pseudo = d.pop("pseudo", UNSET)

        addr_type = d.pop("addr_type", UNSET)

        addr6_type = d.pop("addr6_type", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, NetIfOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = NetIfOptions.from_dict(_options)

        _addr = d.pop("addr", UNSET)
        addr: Union[Unset, NetIfAddr]
        if isinstance(_addr, Unset):
            addr = UNSET
        else:
            addr = NetIfAddr.from_dict(_addr)

        _dhcp = d.pop("dhcp", UNSET)
        dhcp: Union[Unset, NetIfDhcp]
        if isinstance(_dhcp, Unset):
            dhcp = UNSET
        else:
            dhcp = NetIfDhcp.from_dict(_dhcp)

        _ipv6rd = d.pop("ipv6rd", UNSET)
        ipv6rd: Union[Unset, NetIfIpv6RD]
        if isinstance(_ipv6rd, Unset):
            ipv6rd = UNSET
        else:
            ipv6rd = NetIfIpv6RD.from_dict(_ipv6rd)

        _ownership = d.pop("ownership", UNSET)
        ownership: Union[Unset, NetIfOwner]
        if isinstance(_ownership, Unset):
            ownership = UNSET
        else:
            ownership = NetIfOwner.from_dict(_ownership)

        _device_config = d.pop("device_config", UNSET)
        device_config: Union[Unset, NetIfDevConfig]
        if isinstance(_device_config, Unset):
            device_config = UNSET
        else:
            device_config = NetIfDevConfig.from_dict(_device_config)

        _info = d.pop("info", UNSET)
        info: Union[Unset, NetIfInfo]
        if isinstance(_info, Unset):
            info = UNSET
        else:
            info = NetIfInfo.from_dict(_info)

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
