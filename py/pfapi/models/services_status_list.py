from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.services_status import ServicesStatus


T = TypeVar("T", bound="ServicesStatusList")


@_attrs_define
class ServicesStatusList:
    """
    Attributes:
        services (Union[Unset, List['ServicesStatus']]):
    """

    services: Union[Unset, List["ServicesStatus"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        services: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.services_status import ServicesStatus

        d = src_dict.copy()
        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = ServicesStatus.from_dict(services_item_data)

            services.append(services_item)

        services_status_list = cls(
            services=services,
        )

        services_status_list.additional_properties = d
        return services_status_list

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
