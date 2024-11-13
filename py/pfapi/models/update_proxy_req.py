from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.igmp_proxy import IGMPProxy


T = TypeVar("T", bound="UpdateProxyReq")


@_attrs_define
class UpdateProxyReq:
    """
    Attributes:
        proxy (Union[Unset, IGMPProxy]):
    """

    proxy: Union[Unset, "IGMPProxy"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        proxy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proxy, Unset):
            proxy = self.proxy.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proxy is not UNSET:
            field_dict["proxy"] = proxy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.igmp_proxy import IGMPProxy

        d = src_dict.copy()
        _proxy = d.pop("proxy", UNSET)
        proxy: Union[Unset, IGMPProxy]
        if isinstance(_proxy, Unset):
            proxy = UNSET
        else:
            proxy = IGMPProxy.from_dict(_proxy)

        update_proxy_req = cls(
            proxy=proxy,
        )

        update_proxy_req.additional_properties = d
        return update_proxy_req

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
