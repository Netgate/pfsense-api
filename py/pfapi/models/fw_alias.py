from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fw_alias_type import FWAliasType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_target import FWTarget


T = TypeVar("T", bound="FWAlias")


@_attrs_define
class FWAlias:
    """
    Attributes:
        name (str):
        address (str):
        type (FWAliasType):
        truncated (bool):
        targets (Union[Unset, List['FWTarget']]):
        descr (Union[Unset, str]):
        detail (Union[Unset, str]):
        updatefreq (Union[Unset, str]):
    """

    name: str
    address: str
    type: FWAliasType
    truncated: bool
    targets: Union[Unset, List["FWTarget"]] = UNSET
    descr: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    updatefreq: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        address = self.address

        type = self.type.value

        truncated = self.truncated

        targets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        descr = self.descr

        detail = self.detail

        updatefreq = self.updatefreq

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "address": address,
                "type": type,
                "truncated": truncated,
            }
        )
        if targets is not UNSET:
            field_dict["targets"] = targets
        if descr is not UNSET:
            field_dict["descr"] = descr
        if detail is not UNSET:
            field_dict["detail"] = detail
        if updatefreq is not UNSET:
            field_dict["updatefreq"] = updatefreq

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_target import FWTarget

        d = src_dict.copy()
        name = d.pop("name")

        address = d.pop("address")

        type = FWAliasType(d.pop("type"))

        truncated = d.pop("truncated")

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = FWTarget.from_dict(targets_item_data)

            targets.append(targets_item)

        descr = d.pop("descr", UNSET)

        detail = d.pop("detail", UNSET)

        updatefreq = d.pop("updatefreq", UNSET)

        fw_alias = cls(
            name=name,
            address=address,
            type=type,
            truncated=truncated,
            targets=targets,
            descr=descr,
            detail=detail,
            updatefreq=updatefreq,
        )

        fw_alias.additional_properties = d
        return fw_alias

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
