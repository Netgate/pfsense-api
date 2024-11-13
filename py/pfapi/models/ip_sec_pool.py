from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IPSecPool")


@_attrs_define
class IPSecPool:
    """
    Attributes:
        name (Union[Unset, str]):
        base (Union[Unset, str]):
        online (Union[Unset, str]):
        offline (Union[Unset, str]):
        size (Union[Unset, str]):
        host (Union[Unset, str]):
        status (Union[Unset, str]):
        id (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    base: Union[Unset, str] = UNSET
    online: Union[Unset, str] = UNSET
    offline: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        base = self.base

        online = self.online

        offline = self.offline

        size = self.size

        host = self.host

        status = self.status

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if base is not UNSET:
            field_dict["base"] = base
        if online is not UNSET:
            field_dict["online"] = online
        if offline is not UNSET:
            field_dict["offline"] = offline
        if size is not UNSET:
            field_dict["size"] = size
        if host is not UNSET:
            field_dict["host"] = host
        if status is not UNSET:
            field_dict["status"] = status
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        base = d.pop("base", UNSET)

        online = d.pop("online", UNSET)

        offline = d.pop("offline", UNSET)

        size = d.pop("size", UNSET)

        host = d.pop("host", UNSET)

        status = d.pop("status", UNSET)

        id = d.pop("id", UNSET)

        ip_sec_pool = cls(
            name=name,
            base=base,
            online=online,
            offline=offline,
            size=size,
            host=host,
            status=status,
            id=id,
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
