from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.igmp_proxy import IGMPProxy


T = TypeVar("T", bound="IGMPProxies")


@_attrs_define
class IGMPProxies:
    """
    Attributes:
        igmpentry (Union[Unset, List['IGMPProxy']]):
        enable (Union[Unset, bool]):
        verbose (Union[Unset, bool]):
        interfaces (Union[Unset, str]):
    """

    igmpentry: Union[Unset, List["IGMPProxy"]] = UNSET
    enable: Union[Unset, bool] = UNSET
    verbose: Union[Unset, bool] = UNSET
    interfaces: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        igmpentry: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.igmpentry, Unset):
            igmpentry = []
            for igmpentry_item_data in self.igmpentry:
                igmpentry_item = igmpentry_item_data.to_dict()
                igmpentry.append(igmpentry_item)

        enable = self.enable

        verbose = self.verbose

        interfaces = self.interfaces

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if igmpentry is not UNSET:
            field_dict["igmpentry"] = igmpentry
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

        d = src_dict.copy()
        igmpentry = []
        _igmpentry = d.pop("igmpentry", UNSET)
        for igmpentry_item_data in _igmpentry or []:
            igmpentry_item = IGMPProxy.from_dict(igmpentry_item_data)

            igmpentry.append(igmpentry_item)

        enable = d.pop("enable", UNSET)

        verbose = d.pop("verbose", UNSET)

        interfaces = d.pop("interfaces", UNSET)

        igmp_proxies = cls(
            igmpentry=igmpentry,
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
