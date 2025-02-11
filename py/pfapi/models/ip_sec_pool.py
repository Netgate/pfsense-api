from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_pool_lease import IPSecPoolLease


T = TypeVar("T", bound="IPSecPool")


@_attrs_define
class IPSecPool:
    """
    Attributes:
        name (str):
        base (str):
        online (str):
        offline (str):
        size (str):
        lease (Union[Unset, List['IPSecPoolLease']]):
    """

    name: str
    base: str
    online: str
    offline: str
    size: str
    lease: Union[Unset, List["IPSecPoolLease"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        base = self.base

        online = self.online

        offline = self.offline

        size = self.size

        lease: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lease, Unset):
            lease = []
            for lease_item_data in self.lease:
                lease_item = lease_item_data.to_dict()
                lease.append(lease_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "base": base,
                "online": online,
                "offline": offline,
                "size": size,
            }
        )
        if lease is not UNSET:
            field_dict["lease"] = lease

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_sec_pool_lease import IPSecPoolLease

        d = src_dict.copy()
        name = d.pop("name")

        base = d.pop("base")

        online = d.pop("online")

        offline = d.pop("offline")

        size = d.pop("size")

        lease = []
        _lease = d.pop("lease", UNSET)
        for lease_item_data in _lease or []:
            lease_item = IPSecPoolLease.from_dict(lease_item_data)

            lease.append(lease_item)

        ip_sec_pool = cls(
            name=name,
            base=base,
            online=online,
            offline=offline,
            size=size,
            lease=lease,
        )

        ip_sec_pool.additional_properties = d
        return ip_sec_pool

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
