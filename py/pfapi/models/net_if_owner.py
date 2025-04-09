from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.net_if_owner_container import NetIfOwnerContainer
    from ..models.net_if_owner_host import NetIfOwnerHost
    from ..models.net_if_owner_vm import NetIfOwnerVM
    from ..models.net_if_owner_vpp import NetIfOwnerVPP


T = TypeVar("T", bound="NetIfOwner")


@_attrs_define
class NetIfOwner:
    """An interface can be owned by different OS subsystems: host, vpp,
    container or vm (virtual machine). Other than a host-owner, each
    owner has a unique ID and linked to its associated configuraton.

        Attributes:
            owner_type (Union[Unset, str]):
            owner_id (Union[Unset, str]):
            host_config (Union[Unset, NetIfOwnerHost]):
            vpp_config (Union[Unset, NetIfOwnerVPP]):
            container_config (Union[Unset, NetIfOwnerContainer]):
            vm_config (Union[Unset, NetIfOwnerVM]):
    """

    owner_type: Union[Unset, str] = UNSET
    owner_id: Union[Unset, str] = UNSET
    host_config: Union[Unset, "NetIfOwnerHost"] = UNSET
    vpp_config: Union[Unset, "NetIfOwnerVPP"] = UNSET
    container_config: Union[Unset, "NetIfOwnerContainer"] = UNSET
    vm_config: Union[Unset, "NetIfOwnerVM"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        owner_type = self.owner_type

        owner_id = self.owner_id

        host_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.host_config, Unset):
            host_config = self.host_config.to_dict()

        vpp_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vpp_config, Unset):
            vpp_config = self.vpp_config.to_dict()

        container_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.container_config, Unset):
            container_config = self.container_config.to_dict()

        vm_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vm_config, Unset):
            vm_config = self.vm_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner_type is not UNSET:
            field_dict["owner_type"] = owner_type
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id
        if host_config is not UNSET:
            field_dict["host_config"] = host_config
        if vpp_config is not UNSET:
            field_dict["vpp_config"] = vpp_config
        if container_config is not UNSET:
            field_dict["container_config"] = container_config
        if vm_config is not UNSET:
            field_dict["vm_config"] = vm_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.net_if_owner_container import NetIfOwnerContainer
        from ..models.net_if_owner_host import NetIfOwnerHost
        from ..models.net_if_owner_vm import NetIfOwnerVM
        from ..models.net_if_owner_vpp import NetIfOwnerVPP

        d = src_dict.copy()
        owner_type = d.pop("owner_type", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        _host_config = d.pop("host_config", UNSET)
        host_config: Union[Unset, NetIfOwnerHost]
        if isinstance(_host_config, Unset):
            host_config = UNSET
        else:
            host_config = NetIfOwnerHost.from_dict(_host_config)

        _vpp_config = d.pop("vpp_config", UNSET)
        vpp_config: Union[Unset, NetIfOwnerVPP]
        if isinstance(_vpp_config, Unset):
            vpp_config = UNSET
        else:
            vpp_config = NetIfOwnerVPP.from_dict(_vpp_config)

        _container_config = d.pop("container_config", UNSET)
        container_config: Union[Unset, NetIfOwnerContainer]
        if isinstance(_container_config, Unset):
            container_config = UNSET
        else:
            container_config = NetIfOwnerContainer.from_dict(_container_config)

        _vm_config = d.pop("vm_config", UNSET)
        vm_config: Union[Unset, NetIfOwnerVM]
        if isinstance(_vm_config, Unset):
            vm_config = UNSET
        else:
            vm_config = NetIfOwnerVM.from_dict(_vm_config)

        net_if_owner = cls(
            owner_type=owner_type,
            owner_id=owner_id,
            host_config=host_config,
            vpp_config=vpp_config,
            container_config=container_config,
            vm_config=vm_config,
        )

        net_if_owner.additional_properties = d
        return net_if_owner

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
