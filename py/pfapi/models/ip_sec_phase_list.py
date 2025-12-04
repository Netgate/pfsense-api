from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_sec_capable_interface import IPSecCapableInterface
    from ..models.phase_1 import Phase1
    from ..models.phase_2 import Phase2


T = TypeVar("T", bound="IPSecPhaseList")


@_attrs_define
class IPSecPhaseList:
    """
    Attributes:
        phase1 (list[Phase1] | Unset):
        phase2 (list[Phase2] | Unset):
        ipsec_capable_ifs (list[IPSecCapableInterface] | Unset):
    """

    phase1: list[Phase1] | Unset = UNSET
    phase2: list[Phase2] | Unset = UNSET
    ipsec_capable_ifs: list[IPSecCapableInterface] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phase1: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phase1, Unset):
            phase1 = []
            for phase1_item_data in self.phase1:
                phase1_item = phase1_item_data.to_dict()
                phase1.append(phase1_item)

        phase2: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.phase2, Unset):
            phase2 = []
            for phase2_item_data in self.phase2:
                phase2_item = phase2_item_data.to_dict()
                phase2.append(phase2_item)

        ipsec_capable_ifs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ipsec_capable_ifs, Unset):
            ipsec_capable_ifs = []
            for ipsec_capable_ifs_item_data in self.ipsec_capable_ifs:
                ipsec_capable_ifs_item = ipsec_capable_ifs_item_data.to_dict()
                ipsec_capable_ifs.append(ipsec_capable_ifs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phase1 is not UNSET:
            field_dict["phase1"] = phase1
        if phase2 is not UNSET:
            field_dict["phase2"] = phase2
        if ipsec_capable_ifs is not UNSET:
            field_dict["ipsec_capable_ifs"] = ipsec_capable_ifs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ip_sec_capable_interface import IPSecCapableInterface
        from ..models.phase_1 import Phase1
        from ..models.phase_2 import Phase2

        d = dict(src_dict)
        _phase1 = d.pop("phase1", UNSET)
        phase1: list[Phase1] | Unset = UNSET
        if _phase1 is not UNSET:
            phase1 = []
            for phase1_item_data in _phase1:
                phase1_item = Phase1.from_dict(phase1_item_data)

                phase1.append(phase1_item)

        _phase2 = d.pop("phase2", UNSET)
        phase2: list[Phase2] | Unset = UNSET
        if _phase2 is not UNSET:
            phase2 = []
            for phase2_item_data in _phase2:
                phase2_item = Phase2.from_dict(phase2_item_data)

                phase2.append(phase2_item)

        _ipsec_capable_ifs = d.pop("ipsec_capable_ifs", UNSET)
        ipsec_capable_ifs: list[IPSecCapableInterface] | Unset = UNSET
        if _ipsec_capable_ifs is not UNSET:
            ipsec_capable_ifs = []
            for ipsec_capable_ifs_item_data in _ipsec_capable_ifs:
                ipsec_capable_ifs_item = IPSecCapableInterface.from_dict(ipsec_capable_ifs_item_data)

                ipsec_capable_ifs.append(ipsec_capable_ifs_item)

        ip_sec_phase_list = cls(
            phase1=phase1,
            phase2=phase2,
            ipsec_capable_ifs=ipsec_capable_ifs,
        )

        ip_sec_phase_list.additional_properties = d
        return ip_sec_phase_list

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
