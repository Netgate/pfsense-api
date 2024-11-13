from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pf_info import PfInfo


T = TypeVar("T", bound="PfInfoResponse")


@_attrs_define
class PfInfoResponse:
    """
    Attributes:
        pfinfo (Union[Unset, PfInfo]):
    """

    pfinfo: Union[Unset, "PfInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pfinfo: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pfinfo, Unset):
            pfinfo = self.pfinfo.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pfinfo is not UNSET:
            field_dict["pfinfo"] = pfinfo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pf_info import PfInfo

        d = src_dict.copy()
        _pfinfo = d.pop("pfinfo", UNSET)
        pfinfo: Union[Unset, PfInfo]
        if isinstance(_pfinfo, Unset):
            pfinfo = UNSET
        else:
            pfinfo = PfInfo.from_dict(_pfinfo)

        pf_info_response = cls(
            pfinfo=pfinfo,
        )

        pf_info_response.additional_properties = d
        return pf_info_response

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
