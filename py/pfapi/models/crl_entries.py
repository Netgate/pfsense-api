from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crl_config import CRLConfig


T = TypeVar("T", bound="CRLEntries")


@_attrs_define
class CRLEntries:
    """
    Attributes:
        crls (Union[Unset, List['CRLConfig']]):
        refid (Union[Unset, str]): for new and update CRL functions, the refid of the CRL that was changed
    """

    crls: Union[Unset, List["CRLConfig"]] = UNSET
    refid: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        crls: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.crls, Unset):
            crls = []
            for crls_item_data in self.crls:
                crls_item = crls_item_data.to_dict()
                crls.append(crls_item)

        refid = self.refid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crls is not UNSET:
            field_dict["crls"] = crls
        if refid is not UNSET:
            field_dict["refid"] = refid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.crl_config import CRLConfig

        d = src_dict.copy()
        crls = []
        _crls = d.pop("crls", UNSET)
        for crls_item_data in _crls or []:
            crls_item = CRLConfig.from_dict(crls_item_data)

            crls.append(crls_item)

        refid = d.pop("refid", UNSET)

        crl_entries = cls(
            crls=crls,
            refid=refid,
        )

        crl_entries.additional_properties = d
        return crl_entries

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
