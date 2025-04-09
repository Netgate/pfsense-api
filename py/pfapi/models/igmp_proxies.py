from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.igmp_proxy import IGMPProxy
    from ..models.simple_interface import SimpleInterface


T = TypeVar("T", bound="IGMPProxies")


@_attrs_define
class IGMPProxies:
    """
    Attributes:
        igmpentries (Union[Unset, List['IGMPProxy']]):
        enable (Union[Unset, bool]):
        verbose (Union[Unset, bool]):
        interfaces (Union[Unset, List['SimpleInterface']]):
    """

    igmpentries: Union[Unset, List["IGMPProxy"]] = UNSET
    enable: Union[Unset, bool] = UNSET
    verbose: Union[Unset, bool] = UNSET
    interfaces: Union[Unset, List["SimpleInterface"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        igmpentries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.igmpentries, Unset):
            igmpentries = []
            for igmpentries_item_data in self.igmpentries:
                igmpentries_item = igmpentries_item_data.to_dict()
                igmpentries.append(igmpentries_item)

        enable = self.enable

        verbose = self.verbose

        interfaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = []
            for interfaces_item_data in self.interfaces:
                interfaces_item = interfaces_item_data.to_dict()
                interfaces.append(interfaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if igmpentries is not UNSET:
            field_dict["igmpentries"] = igmpentries
        if enable is not UNSET:
            field_dict["enable"] = enable
        if verbose is not UNSET:
            field_dict["verbose"] = verbose
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.igmp_proxy import IGMPProxy
        from ..models.simple_interface import SimpleInterface

        d = src_dict.copy()
        igmpentries = []
        _igmpentries = d.pop("igmpentries", UNSET)
        for igmpentries_item_data in _igmpentries or []:
            igmpentries_item = IGMPProxy.from_dict(igmpentries_item_data)

            igmpentries.append(igmpentries_item)

        enable = d.pop("enable", UNSET)

        verbose = d.pop("verbose", UNSET)

        interfaces = []
        _interfaces = d.pop("interfaces", UNSET)
        for interfaces_item_data in _interfaces or []:
            interfaces_item = SimpleInterface.from_dict(interfaces_item_data)

            interfaces.append(interfaces_item)

        igmp_proxies = cls(
            igmpentries=igmpentries,
            enable=enable,
            verbose=verbose,
            interfaces=interfaces,
        )

        igmp_proxies.additional_properties = d
        return igmp_proxies

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
