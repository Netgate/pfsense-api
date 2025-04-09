from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBootenv")


@_attrs_define
class CreateBootenv:
    """
    Attributes:
        name (str):
        from_ (str):
        descr (Union[Unset, str]):
        protect (Union[Unset, bool]):
    """

    name: str
    from_: str
    descr: Union[Unset, str] = UNSET
    protect: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        from_ = self.from_

        descr = self.descr

        protect = self.protect

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "from": from_,
            }
        )
        if descr is not UNSET:
            field_dict["descr"] = descr
        if protect is not UNSET:
            field_dict["protect"] = protect

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        from_ = d.pop("from")

        descr = d.pop("descr", UNSET)

        protect = d.pop("protect", UNSET)

        create_bootenv = cls(
            name=name,
            from_=from_,
            descr=descr,
            protect=protect,
        )

        create_bootenv.additional_properties = d
        return create_bootenv

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
