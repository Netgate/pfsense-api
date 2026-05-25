from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_binder_l_use import SnortInspBinderLUse
    from ..models.snort_insp_binder_l_when import SnortInspBinderLWhen


T = TypeVar("T", bound="SnortInspBinder")


@_attrs_define
class SnortInspBinder:
    """
    Attributes:
        when (SnortInspBinderLWhen | Unset):
        use (SnortInspBinderLUse | Unset):
    """

    when: SnortInspBinderLWhen | Unset = UNSET
    use: SnortInspBinderLUse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        when: dict[str, Any] | Unset = UNSET
        if not isinstance(self.when, Unset):
            when = self.when.to_dict()

        use: dict[str, Any] | Unset = UNSET
        if not isinstance(self.use, Unset):
            use = self.use.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if when is not UNSET:
            field_dict["when"] = when
        if use is not UNSET:
            field_dict["use"] = use

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_binder_l_use import SnortInspBinderLUse
        from ..models.snort_insp_binder_l_when import SnortInspBinderLWhen

        d = dict(src_dict)
        _when = d.pop("when", UNSET)
        when: SnortInspBinderLWhen | Unset
        if isinstance(_when, Unset):
            when = UNSET
        else:
            when = SnortInspBinderLWhen.from_dict(_when)

        _use = d.pop("use", UNSET)
        use: SnortInspBinderLUse | Unset
        if isinstance(_use, Unset):
            use = UNSET
        else:
            use = SnortInspBinderLUse.from_dict(_use)

        snort_insp_binder = cls(
            when=when,
            use=use,
        )

        snort_insp_binder.additional_properties = d
        return snort_insp_binder

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
