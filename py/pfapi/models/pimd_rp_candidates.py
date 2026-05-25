from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pimd_rp_candidate import PimdRpCandidate
    from ..models.text_value import TextValue


T = TypeVar("T", bound="PimdRpCandidates")


@_attrs_define
class PimdRpCandidates:
    """
    Attributes:
        candidates (list[PimdRpCandidate] | Unset):
        intf_options (list[TextValue] | Unset):
    """

    candidates: list[PimdRpCandidate] | Unset = UNSET
    intf_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        candidates: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.candidates, Unset):
            candidates = []
            for candidates_item_data in self.candidates:
                candidates_item = candidates_item_data.to_dict()
                candidates.append(candidates_item)

        intf_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intf_options, Unset):
            intf_options = []
            for intf_options_item_data in self.intf_options:
                intf_options_item = intf_options_item_data.to_dict()
                intf_options.append(intf_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if candidates is not UNSET:
            field_dict["candidates"] = candidates
        if intf_options is not UNSET:
            field_dict["intf_options"] = intf_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pimd_rp_candidate import PimdRpCandidate
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _candidates = d.pop("candidates", UNSET)
        candidates: list[PimdRpCandidate] | Unset = UNSET
        if _candidates is not UNSET:
            candidates = []
            for candidates_item_data in _candidates:
                candidates_item = PimdRpCandidate.from_dict(candidates_item_data)

                candidates.append(candidates_item)

        _intf_options = d.pop("intf_options", UNSET)
        intf_options: list[TextValue] | Unset = UNSET
        if _intf_options is not UNSET:
            intf_options = []
            for intf_options_item_data in _intf_options:
                intf_options_item = TextValue.from_dict(intf_options_item_data)

                intf_options.append(intf_options_item)

        pimd_rp_candidates = cls(
            candidates=candidates,
            intf_options=intf_options,
        )

        pimd_rp_candidates.additional_properties = d
        return pimd_rp_candidates

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
