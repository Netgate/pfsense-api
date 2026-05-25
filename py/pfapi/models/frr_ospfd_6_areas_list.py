from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_ospfd_6_area import FrrOspfd6Area
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrOspfd6AreasList")


@_attrs_define
class FrrOspfd6AreasList:
    """
    Attributes:
        ospfd6areas (list[FrrOspfd6Area] | Unset):
        exportlist_options (list[TextValue] | Unset):
        importlist_options (list[TextValue] | Unset):
        filterlist_out_options (list[TextValue] | Unset):
        filterlist_in_options (list[TextValue] | Unset):
    """

    ospfd6areas: list[FrrOspfd6Area] | Unset = UNSET
    exportlist_options: list[TextValue] | Unset = UNSET
    importlist_options: list[TextValue] | Unset = UNSET
    filterlist_out_options: list[TextValue] | Unset = UNSET
    filterlist_in_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ospfd6areas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ospfd6areas, Unset):
            ospfd6areas = []
            for ospfd6areas_item_data in self.ospfd6areas:
                ospfd6areas_item = ospfd6areas_item_data.to_dict()
                ospfd6areas.append(ospfd6areas_item)

        exportlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exportlist_options, Unset):
            exportlist_options = []
            for exportlist_options_item_data in self.exportlist_options:
                exportlist_options_item = exportlist_options_item_data.to_dict()
                exportlist_options.append(exportlist_options_item)

        importlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.importlist_options, Unset):
            importlist_options = []
            for importlist_options_item_data in self.importlist_options:
                importlist_options_item = importlist_options_item_data.to_dict()
                importlist_options.append(importlist_options_item)

        filterlist_out_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filterlist_out_options, Unset):
            filterlist_out_options = []
            for filterlist_out_options_item_data in self.filterlist_out_options:
                filterlist_out_options_item = filterlist_out_options_item_data.to_dict()
                filterlist_out_options.append(filterlist_out_options_item)

        filterlist_in_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filterlist_in_options, Unset):
            filterlist_in_options = []
            for filterlist_in_options_item_data in self.filterlist_in_options:
                filterlist_in_options_item = filterlist_in_options_item_data.to_dict()
                filterlist_in_options.append(filterlist_in_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ospfd6areas is not UNSET:
            field_dict["ospfd6areas"] = ospfd6areas
        if exportlist_options is not UNSET:
            field_dict["exportlist_options"] = exportlist_options
        if importlist_options is not UNSET:
            field_dict["importlist_options"] = importlist_options
        if filterlist_out_options is not UNSET:
            field_dict["filterlist_out_options"] = filterlist_out_options
        if filterlist_in_options is not UNSET:
            field_dict["filterlist_in_options"] = filterlist_in_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_ospfd_6_area import FrrOspfd6Area
        from ..models.text_value import TextValue

        d = dict(src_dict)
        _ospfd6areas = d.pop("ospfd6areas", UNSET)
        ospfd6areas: list[FrrOspfd6Area] | Unset = UNSET
        if _ospfd6areas is not UNSET:
            ospfd6areas = []
            for ospfd6areas_item_data in _ospfd6areas:
                ospfd6areas_item = FrrOspfd6Area.from_dict(ospfd6areas_item_data)

                ospfd6areas.append(ospfd6areas_item)

        _exportlist_options = d.pop("exportlist_options", UNSET)
        exportlist_options: list[TextValue] | Unset = UNSET
        if _exportlist_options is not UNSET:
            exportlist_options = []
            for exportlist_options_item_data in _exportlist_options:
                exportlist_options_item = TextValue.from_dict(exportlist_options_item_data)

                exportlist_options.append(exportlist_options_item)

        _importlist_options = d.pop("importlist_options", UNSET)
        importlist_options: list[TextValue] | Unset = UNSET
        if _importlist_options is not UNSET:
            importlist_options = []
            for importlist_options_item_data in _importlist_options:
                importlist_options_item = TextValue.from_dict(importlist_options_item_data)

                importlist_options.append(importlist_options_item)

        _filterlist_out_options = d.pop("filterlist_out_options", UNSET)
        filterlist_out_options: list[TextValue] | Unset = UNSET
        if _filterlist_out_options is not UNSET:
            filterlist_out_options = []
            for filterlist_out_options_item_data in _filterlist_out_options:
                filterlist_out_options_item = TextValue.from_dict(filterlist_out_options_item_data)

                filterlist_out_options.append(filterlist_out_options_item)

        _filterlist_in_options = d.pop("filterlist_in_options", UNSET)
        filterlist_in_options: list[TextValue] | Unset = UNSET
        if _filterlist_in_options is not UNSET:
            filterlist_in_options = []
            for filterlist_in_options_item_data in _filterlist_in_options:
                filterlist_in_options_item = TextValue.from_dict(filterlist_in_options_item_data)

                filterlist_in_options.append(filterlist_in_options_item)

        frr_ospfd_6_areas_list = cls(
            ospfd6areas=ospfd6areas,
            exportlist_options=exportlist_options,
            importlist_options=importlist_options,
            filterlist_out_options=filterlist_out_options,
            filterlist_in_options=filterlist_in_options,
        )

        frr_ospfd_6_areas_list.additional_properties = d
        return frr_ospfd_6_areas_list

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
