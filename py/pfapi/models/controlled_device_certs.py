from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.controlled_device_cert import ControlledDeviceCert


T = TypeVar("T", bound="ControlledDeviceCerts")


@_attrs_define
class ControlledDeviceCerts:
    """
    Attributes:
        certs (Union[Unset, List['ControlledDeviceCert']]):
    """

    certs: Union[Unset, List["ControlledDeviceCert"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certs, Unset):
            certs = []
            for certs_item_data in self.certs:
                certs_item = certs_item_data.to_dict()
                certs.append(certs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certs is not UNSET:
            field_dict["certs"] = certs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.controlled_device_cert import ControlledDeviceCert

        d = src_dict.copy()
        certs = []
        _certs = d.pop("certs", UNSET)
        for certs_item_data in _certs or []:
            certs_item = ControlledDeviceCert.from_dict(certs_item_data)

            certs.append(certs_item)

        controlled_device_certs = cls(
            certs=certs,
        )

        controlled_device_certs.additional_properties = d
        return controlled_device_certs

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
