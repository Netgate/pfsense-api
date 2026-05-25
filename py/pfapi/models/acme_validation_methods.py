from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acme_validation_methods_methods import ACMEValidationMethodsMethods


T = TypeVar("T", bound="ACMEValidationMethods")


@_attrs_define
class ACMEValidationMethods:
    """
    Attributes:
        methods (ACMEValidationMethodsMethods | Unset):
    """

    methods: ACMEValidationMethodsMethods | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        methods: dict[str, Any] | Unset = UNSET
        if not isinstance(self.methods, Unset):
            methods = self.methods.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if methods is not UNSET:
            field_dict["methods"] = methods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acme_validation_methods_methods import ACMEValidationMethodsMethods

        d = dict(src_dict)
        _methods = d.pop("methods", UNSET)
        methods: ACMEValidationMethodsMethods | Unset
        if isinstance(_methods, Unset):
            methods = UNSET
        else:
            methods = ACMEValidationMethodsMethods.from_dict(_methods)

        acme_validation_methods = cls(
            methods=methods,
        )

        acme_validation_methods.additional_properties = d
        return acme_validation_methods

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
