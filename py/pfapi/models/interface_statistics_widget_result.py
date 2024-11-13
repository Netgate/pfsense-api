from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.interface_statistics_widget_result_interfaces import InterfaceStatisticsWidgetResultInterfaces


T = TypeVar("T", bound="InterfaceStatisticsWidgetResult")


@_attrs_define
class InterfaceStatisticsWidgetResult:
    """
    Attributes:
        interfaces (Union[Unset, InterfaceStatisticsWidgetResultInterfaces]):
    """

    interfaces: Union[Unset, "InterfaceStatisticsWidgetResultInterfaces"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        interfaces: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interface_statistics_widget_result_interfaces import InterfaceStatisticsWidgetResultInterfaces

        d = src_dict.copy()
        _interfaces = d.pop("interfaces", UNSET)
        interfaces: Union[Unset, InterfaceStatisticsWidgetResultInterfaces]
        if isinstance(_interfaces, Unset):
            interfaces = UNSET
        else:
            interfaces = InterfaceStatisticsWidgetResultInterfaces.from_dict(_interfaces)

        interface_statistics_widget_result = cls(
            interfaces=interfaces,
        )

        interface_statistics_widget_result.additional_properties = d
        return interface_statistics_widget_result

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
