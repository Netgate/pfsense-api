from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.controller_info import ControllerInfo


T = TypeVar("T", bound="ControllersList")


@_attrs_define
class ControllersList:
    """
    Attributes:
        device_pubkey (str):
        controllers (List['ControllerInfo']):
    """

    device_pubkey: str
    controllers: List["ControllerInfo"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_pubkey = self.device_pubkey

        controllers = []
        for controllers_item_data in self.controllers:
            controllers_item = controllers_item_data.to_dict()
            controllers.append(controllers_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "device_pubkey": device_pubkey,
                "controllers": controllers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controller_info import ControllerInfo

        d = src_dict.copy()
        device_pubkey = d.pop("device_pubkey")

        controllers = []
        _controllers = d.pop("controllers")
        for controllers_item_data in _controllers:
            controllers_item = ControllerInfo.from_dict(controllers_item_data)

            controllers.append(controllers_item)

        controllers_list = cls(
            device_pubkey=device_pubkey,
            controllers=controllers,
        )

        controllers_list.additional_properties = d
        return controllers_list

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
