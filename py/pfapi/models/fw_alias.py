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
        address (Union[Unset, str]): space separated list of addresses
        targets (Union[Unset, List['FWTarget']]):
        descr (Union[Unset, str]):
        type (Union[Unset, FWAliasType]): host, network, url, urltable, urltable_ports, port, or url_ports
        detail (Union[Unset, str]):
        updatefreq (Union[Unset, str]):
        truncated (Union[Unset, bool]):
    """

    name: str
    address: Union[Unset, str] = UNSET
    targets: Union[Unset, List["FWTarget"]] = UNSET
    descr: Union[Unset, str] = UNSET
    type: Union[Unset, FWAliasType] = UNSET
    detail: Union[Unset, str] = UNSET
    updatefreq: Union[Unset, str] = UNSET
    truncated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        address = self.address

        targets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        descr = self.descr

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        detail = self.detail

        updatefreq = self.updatefreq

        truncated = self.truncated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if targets is not UNSET:
            field_dict["targets"] = targets
        if descr is not UNSET:
            field_dict["descr"] = descr
        if type is not UNSET:
            field_dict["type"] = type
        if detail is not UNSET:
            field_dict["detail"] = detail
        if updatefreq is not UNSET:
            field_dict["updatefreq"] = updatefreq
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_target import FWTarget

        d = src_dict.copy()
        name = d.pop("name")

        address = d.pop("address", UNSET)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = FWTarget.from_dict(targets_item_data)

            targets.append(targets_item)

        descr = d.pop("descr", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FWAliasType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FWAliasType(_type)

        detail = d.pop("detail", UNSET)

        updatefreq = d.pop("updatefreq", UNSET)

        truncated = d.pop("truncated", UNSET)

        fw_alias = cls(
            name=name,
            address=address,
            targets=targets,
            descr=descr,
            type=type,
            detail=detail,
            updatefreq=updatefreq,
            truncated=truncated,
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
