from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.p_flow_exporter import PFlowExporter
    from ..models.p_flow_global_options_src_ip_address import PFlowGlobalOptionsSrcIpAddress
    from ..models.p_flow_options import PFlowOptions


T = TypeVar("T", bound="PFlowGlobalOptions")


@_attrs_define
class PFlowGlobalOptions:
    """
    Attributes:
        options (PFlowOptions | Unset):
        exporters (list[PFlowExporter] | Unset):
        src_ip_address (PFlowGlobalOptionsSrcIpAddress | Unset):
    """

    options: PFlowOptions | Unset = UNSET
    exporters: list[PFlowExporter] | Unset = UNSET
    src_ip_address: PFlowGlobalOptionsSrcIpAddress | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        exporters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exporters, Unset):
            exporters = []
            for exporters_item_data in self.exporters:
                exporters_item = exporters_item_data.to_dict()
                exporters.append(exporters_item)

        src_ip_address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.src_ip_address, Unset):
            src_ip_address = self.src_ip_address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if options is not UNSET:
            field_dict["options"] = options
        if exporters is not UNSET:
            field_dict["exporters"] = exporters
        if src_ip_address is not UNSET:
            field_dict["src_ip_address"] = src_ip_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.p_flow_exporter import PFlowExporter
        from ..models.p_flow_global_options_src_ip_address import PFlowGlobalOptionsSrcIpAddress
        from ..models.p_flow_options import PFlowOptions

        d = dict(src_dict)
        _options = d.pop("options", UNSET)
        options: PFlowOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = PFlowOptions.from_dict(_options)

        _exporters = d.pop("exporters", UNSET)
        exporters: list[PFlowExporter] | Unset = UNSET
        if _exporters is not UNSET:
            exporters = []
            for exporters_item_data in _exporters:
                exporters_item = PFlowExporter.from_dict(exporters_item_data)

                exporters.append(exporters_item)

        _src_ip_address = d.pop("src_ip_address", UNSET)
        src_ip_address: PFlowGlobalOptionsSrcIpAddress | Unset
        if isinstance(_src_ip_address, Unset):
            src_ip_address = UNSET
        else:
            src_ip_address = PFlowGlobalOptionsSrcIpAddress.from_dict(_src_ip_address)

        p_flow_global_options = cls(
            options=options,
            exporters=exporters,
            src_ip_address=src_ip_address,
        )

        p_flow_global_options.additional_properties = d
        return p_flow_global_options

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
