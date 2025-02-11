from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

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
        options (PFlowOptions):
        src_ip_address (PFlowGlobalOptionsSrcIpAddress):
        exporters (Union[Unset, List['PFlowExporter']]):
    """

    options: "PFlowOptions"
    src_ip_address: "PFlowGlobalOptionsSrcIpAddress"
    exporters: Union[Unset, List["PFlowExporter"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        options = self.options.to_dict()

        src_ip_address = self.src_ip_address.to_dict()

        exporters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exporters, Unset):
            exporters = []
            for exporters_item_data in self.exporters:
                exporters_item = exporters_item_data.to_dict()
                exporters.append(exporters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "options": options,
                "src_ip_address": src_ip_address,
            }
        )
        if exporters is not UNSET:
            field_dict["exporters"] = exporters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.p_flow_exporter import PFlowExporter
        from ..models.p_flow_global_options_src_ip_address import PFlowGlobalOptionsSrcIpAddress
        from ..models.p_flow_options import PFlowOptions

        d = src_dict.copy()
        options = PFlowOptions.from_dict(d.pop("options"))

        src_ip_address = PFlowGlobalOptionsSrcIpAddress.from_dict(d.pop("src_ip_address"))

        exporters = []
        _exporters = d.pop("exporters", UNSET)
        for exporters_item_data in _exporters or []:
            exporters_item = PFlowExporter.from_dict(exporters_item_data)

            exporters.append(exporters_item)

        p_flow_global_options = cls(
            options=options,
            src_ip_address=src_ip_address,
            exporters=exporters,
        )

        p_flow_global_options.additional_properties = d
        return p_flow_global_options

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
