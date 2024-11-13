from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pp_po_e_server import PPPoEServer


T = TypeVar("T", bound="PPPoEConfig")


@_attrs_define
class PPPoEConfig:
    """
    Attributes:
        pppoe (Union[Unset, List['PPPoEServer']]):
        interfaces (Union[Unset, List[str]]):
    """

    pppoe: Union[Unset, List["PPPoEServer"]] = UNSET
    interfaces: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pppoe: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pppoe, Unset):
            pppoe = []
            for pppoe_item_data in self.pppoe:
                pppoe_item = pppoe_item_data.to_dict()
                pppoe.append(pppoe_item)

        interfaces: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interfaces, Unset):
            interfaces = self.interfaces

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pppoe is not UNSET:
            field_dict["pppoe"] = pppoe
        if interfaces is not UNSET:
            field_dict["interfaces"] = interfaces

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pp_po_e_server import PPPoEServer

        d = src_dict.copy()
        pppoe = []
        _pppoe = d.pop("pppoe", UNSET)
        for pppoe_item_data in _pppoe or []:
            pppoe_item = PPPoEServer.from_dict(pppoe_item_data)

            pppoe.append(pppoe_item)

        interfaces = cast(List[str], d.pop("interfaces", UNSET))

        pp_po_e_config = cls(
            pppoe=pppoe,
            interfaces=interfaces,
        )

        pp_po_e_config.additional_properties = d
        return pp_po_e_config

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
