from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpncso_config import OpenVPNCSOConfig


T = TypeVar("T", bound="OpenVPNCSO")


@_attrs_define
class OpenVPNCSO:
    """
    Attributes:
        csc (Union[Unset, OpenVPNCSOConfig]):
    """

    csc: Union[Unset, "OpenVPNCSOConfig"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        csc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.csc, Unset):
            csc = self.csc.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if csc is not UNSET:
            field_dict["csc"] = csc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_vpncso_config import OpenVPNCSOConfig

        d = src_dict.copy()
        _csc = d.pop("csc", UNSET)
        csc: Union[Unset, OpenVPNCSOConfig]
        if isinstance(_csc, Unset):
            csc = UNSET
        else:
            csc = OpenVPNCSOConfig.from_dict(_csc)

        open_vpncso = cls(
            csc=csc,
        )

        open_vpncso.additional_properties = d
        return open_vpncso

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
