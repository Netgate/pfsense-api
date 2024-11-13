from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_v_address import GatewayVAddress


T = TypeVar("T", bound="GatewayPInfo")


@_attrs_define
class GatewayPInfo:
    """
    Attributes:
        name (Union[Unset, str]):
        vaddress (Union[Unset, List['GatewayVAddress']]):
        descr (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    vaddress: Union[Unset, List["GatewayVAddress"]] = UNSET
    descr: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        vaddress: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vaddress, Unset):
            vaddress = []
            for vaddress_item_data in self.vaddress:
                vaddress_item = vaddress_item_data.to_dict()
                vaddress.append(vaddress_item)

        descr = self.descr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if vaddress is not UNSET:
            field_dict["vaddress"] = vaddress
        if descr is not UNSET:
            field_dict["descr"] = descr

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.gateway_v_address import GatewayVAddress

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        vaddress = []
        _vaddress = d.pop("vaddress", UNSET)
        for vaddress_item_data in _vaddress or []:
            vaddress_item = GatewayVAddress.from_dict(vaddress_item_data)

            vaddress.append(vaddress_item)

        descr = d.pop("descr", UNSET)

        gateway_p_info = cls(
            name=name,
            vaddress=vaddress,
            descr=descr,
        )

        gateway_p_info.additional_properties = d
        return gateway_p_info

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
