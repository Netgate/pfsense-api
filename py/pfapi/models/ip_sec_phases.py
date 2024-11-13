from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_phase_list import IPSecPhaseList


T = TypeVar("T", bound="IPSecPhases")


@_attrs_define
class IPSecPhases:
    """
    Attributes:
        phases (Union[Unset, IPSecPhaseList]):
    """

    phases: Union[Unset, "IPSecPhaseList"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phases: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.phases, Unset):
            phases = self.phases.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phases is not UNSET:
            field_dict["phases"] = phases

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_sec_phase_list import IPSecPhaseList

        d = src_dict.copy()
        _phases = d.pop("phases", UNSET)
        phases: Union[Unset, IPSecPhaseList]
        if isinstance(_phases, Unset):
            phases = UNSET
        else:
            phases = IPSecPhaseList.from_dict(_phases)

        ip_sec_phases = cls(
            phases=phases,
        )

        ip_sec_phases.additional_properties = d
        return ip_sec_phases

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
