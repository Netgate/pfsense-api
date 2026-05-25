from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspNormalizerIp4")


@_attrs_define
class SnortInspNormalizerIp4:
    """
    Attributes:
        base (bool | Unset): clear options; default false
        df (bool | Unset): clear don’t frag flag; default false
        rf (bool | Unset): clear reserved flag; default false
        tos (bool | Unset): clear tos / differentiated services byte; default false
        trim (bool | Unset): truncate excess payload beyond datagram length; default false
    """

    base: bool | Unset = UNSET
    df: bool | Unset = UNSET
    rf: bool | Unset = UNSET
    tos: bool | Unset = UNSET
    trim: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base = self.base

        df = self.df

        rf = self.rf

        tos = self.tos

        trim = self.trim

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base is not UNSET:
            field_dict["base"] = base
        if df is not UNSET:
            field_dict["df"] = df
        if rf is not UNSET:
            field_dict["rf"] = rf
        if tos is not UNSET:
            field_dict["tos"] = tos
        if trim is not UNSET:
            field_dict["trim"] = trim

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base = d.pop("base", UNSET)

        df = d.pop("df", UNSET)

        rf = d.pop("rf", UNSET)

        tos = d.pop("tos", UNSET)

        trim = d.pop("trim", UNSET)

        snort_insp_normalizer_ip_4 = cls(
            base=base,
            df=df,
            rf=rf,
            tos=tos,
            trim=trim,
        )

        snort_insp_normalizer_ip_4.additional_properties = d
        return snort_insp_normalizer_ip_4

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
