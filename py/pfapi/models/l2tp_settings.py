from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.l2tp_config import L2TPConfig


T = TypeVar("T", bound="L2TPSettings")


@_attrs_define
class L2TPSettings:
    """
    Attributes:
        l2tp (Union[Unset, L2TPConfig]):
        interfaces (Union[Unset, List[str]]):
    """

    l2tp: Union[Unset, "L2TPConfig"] = UNSET
    interfaces: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        l2tp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.l2tp, Unset):
            l2tp = self.l2tp.to_dict()

        interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if l2tp is not UNSET:
            field_dict["l2tp"] = l2tp
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.l2tp_config import L2TPConfig

        d = src_dict.copy()
        _l2tp = d.pop("l2tp", UNSET)
        l2tp: Union[Unset, L2TPConfig]
        if isinstance(_l2tp, Unset):
            l2tp = UNSET
        else:
            l2tp = L2TPConfig.from_dict(_l2tp)

        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        l2tp_settings = cls(
            l2tp=l2tp,
            interfaces=interfaces,
        )

        l2tp_settings.additional_properties = d
        return l2tp_settings

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
