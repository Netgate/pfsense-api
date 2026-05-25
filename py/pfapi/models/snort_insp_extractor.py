from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_extractor_protocols import SnortInspExtractorProtocols


T = TypeVar("T", bound="SnortInspExtractor")


@_attrs_define
class SnortInspExtractor:
    """
    Attributes:
        formatting (str | Unset): output format for extractor { csv | tsv | json }; default csv
        connector (str | Unset): output destination for extractor
        time (str | Unset): output format for timestamp values { snort | snort_yy | unix | unix_s | unix_us }; default
            unix
        default_filter (str | Unset): default action for protocol with no filter provided { pick | skip }; default pick
        protocols (list[SnortInspExtractorProtocols] | Unset):
    """

    formatting: str | Unset = UNSET
    connector: str | Unset = UNSET
    time: str | Unset = UNSET
    default_filter: str | Unset = UNSET
    protocols: list[SnortInspExtractorProtocols] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        formatting = self.formatting

        connector = self.connector

        time = self.time

        default_filter = self.default_filter

        protocols: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.protocols, Unset):
            protocols = []
            for protocols_item_data in self.protocols:
                protocols_item = protocols_item_data.to_dict()
                protocols.append(protocols_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if formatting is not UNSET:
            field_dict["formatting"] = formatting
        if connector is not UNSET:
            field_dict["connector"] = connector
        if time is not UNSET:
            field_dict["time"] = time
        if default_filter is not UNSET:
            field_dict["default_filter"] = default_filter
        if protocols is not UNSET:
            field_dict["protocols"] = protocols

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_extractor_protocols import SnortInspExtractorProtocols

        d = dict(src_dict)
        formatting = d.pop("formatting", UNSET)

        connector = d.pop("connector", UNSET)

        time = d.pop("time", UNSET)

        default_filter = d.pop("default_filter", UNSET)

        _protocols = d.pop("protocols", UNSET)
        protocols: list[SnortInspExtractorProtocols] | Unset = UNSET
        if _protocols is not UNSET:
            protocols = []
            for protocols_item_data in _protocols:
                protocols_item = SnortInspExtractorProtocols.from_dict(protocols_item_data)

                protocols.append(protocols_item)

        snort_insp_extractor = cls(
            formatting=formatting,
            connector=connector,
            time=time,
            default_filter=default_filter,
            protocols=protocols,
        )

        snort_insp_extractor.additional_properties = d
        return snort_insp_extractor

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
