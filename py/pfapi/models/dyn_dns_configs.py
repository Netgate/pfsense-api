from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_ip_service import CheckIPService
    from ..models.dyn_dns_config import DynDNSConfig
    from ..models.rfc_item import RFCItem


T = TypeVar("T", bound="DynDNSConfigs")


@_attrs_define
class DynDNSConfigs:
    """
    Attributes:
        dyndnses (Union[Unset, List['DynDNSConfig']]):
        dnsupdate (Union[Unset, List['RFCItem']]):
        checkipservice (Union[Unset, List['CheckIPService']]):
    """

    dyndnses: Union[Unset, List["DynDNSConfig"]] = UNSET
    dnsupdate: Union[Unset, List["RFCItem"]] = UNSET
    checkipservice: Union[Unset, List["CheckIPService"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dyndnses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dyndnses, Unset):
            dyndnses = []
            for dyndnses_item_data in self.dyndnses:
                dyndnses_item = dyndnses_item_data.to_dict()
                dyndnses.append(dyndnses_item)

        dnsupdate: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dnsupdate, Unset):
            dnsupdate = []
            for dnsupdate_item_data in self.dnsupdate:
                dnsupdate_item = dnsupdate_item_data.to_dict()
                dnsupdate.append(dnsupdate_item)

        checkipservice: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.checkipservice, Unset):
            checkipservice = []
            for checkipservice_item_data in self.checkipservice:
                checkipservice_item = checkipservice_item_data.to_dict()
                checkipservice.append(checkipservice_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dyndnses is not UNSET:
            field_dict["dyndnses"] = dyndnses
        if dnsupdate is not UNSET:
            field_dict["dnsupdate"] = dnsupdate
        if checkipservice is not UNSET:
            field_dict["checkipservice"] = checkipservice

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.check_ip_service import CheckIPService
        from ..models.dyn_dns_config import DynDNSConfig
        from ..models.rfc_item import RFCItem

        d = src_dict.copy()
        dyndnses = []
        _dyndnses = d.pop("dyndnses", UNSET)
        for dyndnses_item_data in _dyndnses or []:
            dyndnses_item = DynDNSConfig.from_dict(dyndnses_item_data)

            dyndnses.append(dyndnses_item)

        dnsupdate = []
        _dnsupdate = d.pop("dnsupdate", UNSET)
        for dnsupdate_item_data in _dnsupdate or []:
            dnsupdate_item = RFCItem.from_dict(dnsupdate_item_data)

            dnsupdate.append(dnsupdate_item)

        checkipservice = []
        _checkipservice = d.pop("checkipservice", UNSET)
        for checkipservice_item_data in _checkipservice or []:
            checkipservice_item = CheckIPService.from_dict(checkipservice_item_data)

            checkipservice.append(checkipservice_item)

        dyn_dns_configs = cls(
            dyndnses=dyndnses,
            dnsupdate=dnsupdate,
            checkipservice=checkipservice,
        )

        dyn_dns_configs.additional_properties = d
        return dyn_dns_configs

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
