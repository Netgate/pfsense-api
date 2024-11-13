from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IGMPProxySettings")


@_attrs_define
class IGMPProxySettings:
    """
    Attributes:
        verbose (Union[Unset, bool]):
        enable (Union[Unset, bool]):
    """

    verbose: Union[Unset, bool] = UNSET
    enable: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        verbose = self.verbose

        enable = self.enable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if verbose is not UNSET:
            field_dict["verbose"] = verbose
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        verbose = d.pop("verbose", UNSET)

        enable = d.pop("enable", UNSET)

        igmp_proxy_settings = cls(
            verbose=verbose,
            enable=enable,
        )

        igmp_proxy_settings.additional_properties = d
        return igmp_proxy_settings

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
