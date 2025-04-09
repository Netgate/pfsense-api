from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tunable import Tunable


T = TypeVar("T", bound="TunableRequest")


@_attrs_define
class TunableRequest:
    """
    Attributes:
        tunable (Union[Unset, Tunable]):
        id (Union[Unset, int]):
    """

    tunable: Union[Unset, "Tunable"] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tunable: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tunable, Unset):
            tunable = self.tunable.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tunable is not UNSET:
            field_dict["tunable"] = tunable
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tunable import Tunable

        d = src_dict.copy()
        _tunable = d.pop("tunable", UNSET)
        tunable: Union[Unset, Tunable]
        if isinstance(_tunable, Unset):
            tunable = UNSET
        else:
            tunable = Tunable.from_dict(_tunable)

        id = d.pop("id", UNSET)

        tunable_request = cls(
            tunable=tunable,
            id=id,
        )

        tunable_request.additional_properties = d
        return tunable_request

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
