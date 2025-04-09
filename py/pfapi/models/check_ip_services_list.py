from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_ip_service import CheckIPService


T = TypeVar("T", bound="CheckIPServicesList")


@_attrs_define
class CheckIPServicesList:
    """
    Attributes:
        checkipservice (Union[Unset, List['CheckIPService']]):
    """

    checkipservice: Union[Unset, List["CheckIPService"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        checkipservice: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.checkipservice, Unset):
            checkipservice = []
            for checkipservice_item_data in self.checkipservice:
                checkipservice_item = checkipservice_item_data.to_dict()
                checkipservice.append(checkipservice_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checkipservice is not UNSET:
            field_dict["checkipservice"] = checkipservice

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.check_ip_service import CheckIPService

        d = src_dict.copy()
        checkipservice = []
        _checkipservice = d.pop("checkipservice", UNSET)
        for checkipservice_item_data in _checkipservice or []:
            checkipservice_item = CheckIPService.from_dict(checkipservice_item_data)

            checkipservice.append(checkipservice_item)

        check_ip_services_list = cls(
            checkipservice=checkipservice,
        )

        check_ip_services_list.additional_properties = d
        return check_ip_services_list

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
