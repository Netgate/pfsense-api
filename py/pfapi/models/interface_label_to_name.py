from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="InterfaceLabelToName")


@_attrs_define
class InterfaceLabelToName:
    """Mapping of friendly interface label to the configuration name
    and the underlying device name. For example:

    friendly: LANOPT
    name:     lanopt (assigned)
    ident:    opt1
    if:       eth0

        Attributes:
            friendly (str):
            name (str):
            ident (str):
            if_ (str):
    """

    friendly: str
    name: str
    ident: str
    if_: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        friendly = self.friendly

        name = self.name

        ident = self.ident

        if_ = self.if_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "friendly": friendly,
                "name": name,
                "ident": ident,
                "if": if_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        friendly = d.pop("friendly")

        name = d.pop("name")

        ident = d.pop("ident")

        if_ = d.pop("if")

        interface_label_to_name = cls(
            friendly=friendly,
            name=name,
            ident=ident,
            if_=if_,
        )

        interface_label_to_name.additional_properties = d
        return interface_label_to_name

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
