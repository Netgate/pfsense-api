from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.interface_ports_lists import InterfacePortsLists


T = TypeVar("T", bound="InterfacePorts")


@_attrs_define
class InterfacePorts:
    """
    Attributes:
        ports (InterfacePortsLists):
        modems (List[str]):
    """

    ports: "InterfacePortsLists"
    modems: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ports = self.ports.to_dict()

        modems = self.modems

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ports": ports,
                "modems": modems,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.interface_ports_lists import InterfacePortsLists

        d = src_dict.copy()
        ports = InterfacePortsLists.from_dict(d.pop("ports"))

        modems = cast(List[str], d.pop("modems"))

        interface_ports = cls(
            ports=ports,
            modems=modems,
        )

        interface_ports.additional_properties = d
        return interface_ports

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
