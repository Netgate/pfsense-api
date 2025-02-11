from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TCPFlags")


@_attrs_define
class TCPFlags:
    """
    Attributes:
        fin (bool):
        syn (bool):
        rst (bool):
        psh (bool):
        ack (bool):
        urg (bool):
        ece (bool):
        cwr (bool):
    """

    fin: bool
    syn: bool
    rst: bool
    psh: bool
    ack: bool
    urg: bool
    ece: bool
    cwr: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fin = self.fin

        syn = self.syn

        rst = self.rst

        psh = self.psh

        ack = self.ack

        urg = self.urg

        ece = self.ece

        cwr = self.cwr

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fin": fin,
                "syn": syn,
                "rst": rst,
                "psh": psh,
                "ack": ack,
                "urg": urg,
                "ece": ece,
                "cwr": cwr,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fin = d.pop("fin")

        syn = d.pop("syn")

        rst = d.pop("rst")

        psh = d.pop("psh")

        ack = d.pop("ack")

        urg = d.pop("urg")

        ece = d.pop("ece")

        cwr = d.pop("cwr")

        tcp_flags = cls(
            fin=fin,
            syn=syn,
            rst=rst,
            psh=psh,
            ack=ack,
            urg=urg,
            ece=ece,
            cwr=cwr,
        )

        tcp_flags.additional_properties = d
        return tcp_flags

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
