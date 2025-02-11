from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.phase_1 import Phase1
    from ..models.phase_2 import Phase2


T = TypeVar("T", bound="IPSecPhaseList")


@_attrs_define
class IPSecPhaseList:
    """
    Attributes:
        phase1 (List['Phase1']):
        phase2 (List['Phase2']):
    """

    phase1: List["Phase1"]
    phase2: List["Phase2"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phase1 = []
        for phase1_item_data in self.phase1:
            phase1_item = phase1_item_data.to_dict()
            phase1.append(phase1_item)

        phase2 = []
        for phase2_item_data in self.phase2:
            phase2_item = phase2_item_data.to_dict()
            phase2.append(phase2_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phase1": phase1,
                "phase2": phase2,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.phase_1 import Phase1
        from ..models.phase_2 import Phase2

        d = src_dict.copy()
        phase1 = []
        _phase1 = d.pop("phase1")
        for phase1_item_data in _phase1:
            phase1_item = Phase1.from_dict(phase1_item_data)

            phase1.append(phase1_item)

        phase2 = []
        _phase2 = d.pop("phase2")
        for phase2_item_data in _phase2:
            phase2_item = Phase2.from_dict(phase2_item_data)

            phase2.append(phase2_item)

        ip_sec_phase_list = cls(
            phase1=phase1,
            phase2=phase2,
        )

        ip_sec_phase_list.additional_properties = d
        return ip_sec_phase_list

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
