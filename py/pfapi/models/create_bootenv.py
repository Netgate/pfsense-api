from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateBootenv")


@_attrs_define
class CreateBootenv:
    """
    Attributes:
        name (str):
        descr (str):
        from_ (str):
        protect (bool):
    """

    name: str
    descr: str
    from_: str
    protect: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        descr = self.descr

        from_ = self.from_

        protect = self.protect

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "descr": descr,
                "from": from_,
                "protect": protect,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        descr = d.pop("descr")

        from_ = d.pop("from")

        protect = d.pop("protect")

        create_bootenv = cls(
            name=name,
            descr=descr,
            from_=from_,
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
