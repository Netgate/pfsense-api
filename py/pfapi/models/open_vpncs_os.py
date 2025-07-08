from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpncso_config import OpenVPNCSOConfig
    from ..models.text_value import TextValue


T = TypeVar("T", bound="OpenVPNCSOs")


@_attrs_define
class OpenVPNCSOs:
    """
    Attributes:
        cscs (Union[Unset, List['OpenVPNCSOConfig']]):
        removable_options (Union[Unset, List['TextValue']]):
    """

    cscs: Union[Unset, List["OpenVPNCSOConfig"]] = UNSET
    removable_options: Union[Unset, List["TextValue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cscs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cscs, Unset):
            cscs = []
            for cscs_item_data in self.cscs:
                cscs_item = cscs_item_data.to_dict()
                cscs.append(cscs_item)

        removable_options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.removable_options, Unset):
            removable_options = []
            for removable_options_item_data in self.removable_options:
                removable_options_item = removable_options_item_data.to_dict()
                removable_options.append(removable_options_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cscs is not UNSET:
            field_dict["cscs"] = cscs
        if removable_options is not UNSET:
            field_dict["removable_options"] = removable_options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_vpncso_config import OpenVPNCSOConfig
        from ..models.text_value import TextValue

        d = src_dict.copy()
        cscs = []
        _cscs = d.pop("cscs", UNSET)
        for cscs_item_data in _cscs or []:
            cscs_item = OpenVPNCSOConfig.from_dict(cscs_item_data)

            cscs.append(cscs_item)

        removable_options = []
        _removable_options = d.pop("removable_options", UNSET)
        for removable_options_item_data in _removable_options or []:
            removable_options_item = TextValue.from_dict(removable_options_item_data)

            removable_options.append(removable_options_item)

        open_vpncs_os = cls(
            cscs=cscs,
            removable_options=removable_options,
        )

        open_vpncs_os.additional_properties = d
        return open_vpncs_os

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
