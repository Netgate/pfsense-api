from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

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
            owner_type (str | Unset):
            owner_id (str | Unset):
            host_config (NetIfOwnerHost | Unset):
            vpp_config (NetIfOwnerVPP | Unset):
            container_config (NetIfOwnerContainer | Unset):
            vm_config (NetIfOwnerVM | Unset):
    """

    owner_type: str | Unset = UNSET
    owner_id: str | Unset = UNSET
    host_config: NetIfOwnerHost | Unset = UNSET
    vpp_config: NetIfOwnerVPP | Unset = UNSET
    container_config: NetIfOwnerContainer | Unset = UNSET
    vm_config: NetIfOwnerVM | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        owner_type = self.owner_type

        owner_id = self.owner_id

        host_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.host_config, Unset):
            host_config = self.host_config.to_dict()

        vpp_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vpp_config, Unset):
            vpp_config = self.vpp_config.to_dict()

        container_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.container_config, Unset):
            container_config = self.container_config.to_dict()

        vm_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vm_config, Unset):
            vm_config = self.vm_config.to_dict()

        field_dict: dict[str, Any] = {}
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
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.net_if_owner_container import NetIfOwnerContainer
        from ..models.net_if_owner_host import NetIfOwnerHost
        from ..models.net_if_owner_vm import NetIfOwnerVM
        from ..models.net_if_owner_vpp import NetIfOwnerVPP

        d = dict(src_dict)
        owner_type = d.pop("owner_type", UNSET)

        owner_id = d.pop("owner_id", UNSET)

        _host_config = d.pop("host_config", UNSET)
        host_config: NetIfOwnerHost | Unset
        if isinstance(_host_config, Unset):
            host_config = UNSET
        else:
            host_config = NetIfOwnerHost.from_dict(_host_config)

        _vpp_config = d.pop("vpp_config", UNSET)
        vpp_config: NetIfOwnerVPP | Unset
        if isinstance(_vpp_config, Unset):
            vpp_config = UNSET
        else:
            vpp_config = NetIfOwnerVPP.from_dict(_vpp_config)

        _container_config = d.pop("container_config", UNSET)
        container_config: NetIfOwnerContainer | Unset
        if isinstance(_container_config, Unset):
            container_config = UNSET
        else:
            container_config = NetIfOwnerContainer.from_dict(_container_config)

        _vm_config = d.pop("vm_config", UNSET)
        vm_config: NetIfOwnerVM | Unset
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
