from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.setup_settings import SetupSettings


T = TypeVar("T", bound="InitialSetup")


@_attrs_define
class InitialSetup:
    """
    Attributes:
        setup (Union[Unset, SetupSettings]):
    """

    setup: Union[Unset, "SetupSettings"] = UNSET
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
        from ..models.setup_settings import SetupSettings

        d = src_dict.copy()
        _setup = d.pop("setup", UNSET)
        setup: Union[Unset, SetupSettings]
        if isinstance(_setup, Unset):
            setup = UNSET
        else:
            setup = SetupSettings.from_dict(_setup)

        initial_setup = cls(
            setup=setup,
        )

        initial_setup.additional_properties = d
        return initial_setup

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
