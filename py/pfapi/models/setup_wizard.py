from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.setup_wizard_options import SetupWizardOptions


T = TypeVar("T", bound="SetupWizard")


@_attrs_define
class SetupWizard:
    """
    Attributes:
        setup (SetupWizardOptions | Unset):
    """

    setup: SetupWizardOptions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        setup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.setup, Unset):
            setup = self.setup.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if setup is not UNSET:
            field_dict["setup"] = setup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.setup_wizard_options import SetupWizardOptions

        d = dict(src_dict)
        _setup = d.pop("setup", UNSET)
        setup: SetupWizardOptions | Unset
        if isinstance(_setup, Unset):
            setup = UNSET
        else:
            setup = SetupWizardOptions.from_dict(_setup)

        setup_wizard = cls(
            setup=setup,
        )

        setup_wizard.additional_properties = d
        return setup_wizard

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
