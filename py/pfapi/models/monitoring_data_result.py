from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.monitoring_data_request import MonitoringDataRequest


T = TypeVar("T", bound="MonitoringDataResult")


@_attrs_define
class MonitoringDataResult:
    """Data returned is a set of CSV values for the series.

    Attributes:
        request (MonitoringDataRequest | Unset):
        dataseries (list[str] | Unset):
        data_format (str | Unset):
        data (list[str] | Unset):
    """

    request: MonitoringDataRequest | Unset = UNSET
    dataseries: list[str] | Unset = UNSET
    data_format: str | Unset = UNSET
    data: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request: dict[str, Any] | Unset = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        dataseries: list[str] | Unset = UNSET
        if not isinstance(self.dataseries, Unset):
            dataseries = self.dataseries

        data_format = self.data_format

        data: list[str] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request is not UNSET:
            field_dict["request"] = request
        if dataseries is not UNSET:
            field_dict["dataseries"] = dataseries
        if data_format is not UNSET:
            field_dict["data_format"] = data_format
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.monitoring_data_request import MonitoringDataRequest

        d = dict(src_dict)
        _request = d.pop("request", UNSET)
        request: MonitoringDataRequest | Unset
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = MonitoringDataRequest.from_dict(_request)

        dataseries = cast(list[str], d.pop("dataseries", UNSET))

        data_format = d.pop("data_format", UNSET)

        data = cast(list[str], d.pop("data", UNSET))

        monitoring_data_result = cls(
            request=request,
            dataseries=dataseries,
            data_format=data_format,
            data=data,
        )

        monitoring_data_result.additional_properties = d
        return monitoring_data_result

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
