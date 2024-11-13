from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pfsense_result import PfsenseResult


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """
    Attributes:
        errcode (Union[Unset, int]): Error code
        errmsg (Union[Unset, str]): Error message
        alerts (Union[Unset, PfsenseResult]):
    """

    errcode: Union[Unset, int] = UNSET
    errmsg: Union[Unset, str] = UNSET
    alerts: Union[Unset, "PfsenseResult"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errcode = self.errcode

        errmsg = self.errmsg

        alerts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = self.alerts.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errcode is not UNSET:
            field_dict["errcode"] = errcode
        if errmsg is not UNSET:
            field_dict["errmsg"] = errmsg
        if alerts is not UNSET:
            field_dict["alerts"] = alerts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pfsense_result import PfsenseResult

        d = src_dict.copy()
        errcode = d.pop("errcode", UNSET)

        errmsg = d.pop("errmsg", UNSET)

        _alerts = d.pop("alerts", UNSET)
        alerts: Union[Unset, PfsenseResult]
        if isinstance(_alerts, Unset):
            alerts = UNSET
        else:
            alerts = PfsenseResult.from_dict(_alerts)

        error = cls(
            errcode=errcode,
            errmsg=errmsg,
            alerts=alerts,
        )

        error.additional_properties = d
        return error

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
