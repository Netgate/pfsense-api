from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_alias import FWAlias


T = TypeVar("T", bound="FWUpdateAliasreq")


@_attrs_define
class FWUpdateAliasreq:
    """
    Attributes:
        alias (Union[Unset, FWAlias]):
        id (Union[Unset, str]):
    """

    alias: Union[Unset, "FWAlias"] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alias: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alias, Unset):
            alias = self.alias.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_alias import FWAlias

        d = src_dict.copy()
        _alias = d.pop("alias", UNSET)
        alias: Union[Unset, FWAlias]
        if isinstance(_alias, Unset):
            alias = UNSET
        else:
            alias = FWAlias.from_dict(_alias)

        id = d.pop("id", UNSET)

        fw_update_aliasreq = cls(
            alias=alias,
            id=id,
        )

        fw_update_aliasreq.additional_properties = d
        return fw_update_aliasreq

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
