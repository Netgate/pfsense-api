from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        setup (Union[Unset, SetupWizardOptions]):
    """

    setup: Union[Unset, "SetupWizardOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        setup: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.setup, Unset):
            setup = self.setup.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if setup is not UNSET:
            field_dict["setup"] = setup

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.setup_wizard_options import SetupWizardOptions

        d = src_dict.copy()
        _setup = d.pop("setup", UNSET)
        setup: Union[Unset, SetupWizardOptions]
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
