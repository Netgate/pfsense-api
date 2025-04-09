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
        options (Union[Unset, PFlowOptions]):
        exporters (Union[Unset, List['PFlowExporter']]):
        src_ip_address (Union[Unset, PFlowGlobalOptionsSrcIpAddress]):
    """

    options: Union[Unset, "PFlowOptions"] = UNSET
    exporters: Union[Unset, List["PFlowExporter"]] = UNSET
    src_ip_address: Union[Unset, "PFlowGlobalOptionsSrcIpAddress"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        exporters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exporters, Unset):
            exporters = []
            for exporters_item_data in self.exporters:
                exporters_item = exporters_item_data.to_dict()
                exporters.append(exporters_item)

        src_ip_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.src_ip_address, Unset):
            src_ip_address = self.src_ip_address.to_dict()

        field_dict: Dict[str, Any] = {}
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
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.p_flow_exporter import PFlowExporter
        from ..models.p_flow_global_options_src_ip_address import PFlowGlobalOptionsSrcIpAddress
        from ..models.p_flow_options import PFlowOptions

        d = src_dict.copy()
        _options = d.pop("options", UNSET)
        options: Union[Unset, PFlowOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = PFlowOptions.from_dict(_options)

        exporters = []
        _exporters = d.pop("exporters", UNSET)
        for exporters_item_data in _exporters or []:
            exporters_item = PFlowExporter.from_dict(exporters_item_data)

            exporters.append(exporters_item)

        _src_ip_address = d.pop("src_ip_address", UNSET)
        src_ip_address: Union[Unset, PFlowGlobalOptionsSrcIpAddress]
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
