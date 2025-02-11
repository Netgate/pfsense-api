from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tunable import Tunable


T = TypeVar("T", bound="TunableRequest")


@_attrs_define
class TunableRequest:
    """
    Attributes:
        tunable (Tunable):
        id (int):
    """

    tunable: "Tunable"
    id: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tunable = self.tunable.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tunable": tunable,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.tunable import Tunable

        d = src_dict.copy()
        tunable = Tunable.from_dict(d.pop("tunable"))

        id = d.pop("id")

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
