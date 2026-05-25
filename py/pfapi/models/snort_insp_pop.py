from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnortInspPop")


@_attrs_define
class SnortInspPop:
    """
    Attributes:
        b64_decode_depth (int | Unset): base64 decoding depth (-1 no limit) { -1:65535 }; default -1
        bitenc_decode_depth (int | Unset): Non-Encoded MIME attachment extraction depth (-1 no limit) { -1:65535 };
            default -1
        decompress_pdf (bool | Unset): decompress pdf files in MIME attachments; default false
        decompress_swf (bool | Unset): decompress swf files in MIME attachments; default false
        decompress_zip (bool | Unset): decompress zip files in MIME attachments; default false
        decompress_vba (bool | Unset): decompress MS Office Visual Basic for Applications macro files in MIME
            attachments; default false
        qp_decode_depth (int | Unset): Quoted Printable decoding depth (-1 no limit) { -1:65535 }; default -1
        uu_decode_depth (int | Unset): Unix-to-Unix decoding depth (-1 no limit) { -1:65535 }; default -1
    """

    b64_decode_depth: int | Unset = UNSET
    bitenc_decode_depth: int | Unset = UNSET
    decompress_pdf: bool | Unset = UNSET
    decompress_swf: bool | Unset = UNSET
    decompress_zip: bool | Unset = UNSET
    decompress_vba: bool | Unset = UNSET
    qp_decode_depth: int | Unset = UNSET
    uu_decode_depth: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        b64_decode_depth = self.b64_decode_depth

        bitenc_decode_depth = self.bitenc_decode_depth

        decompress_pdf = self.decompress_pdf

        decompress_swf = self.decompress_swf

        decompress_zip = self.decompress_zip

        decompress_vba = self.decompress_vba

        qp_decode_depth = self.qp_decode_depth

        uu_decode_depth = self.uu_decode_depth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if b64_decode_depth is not UNSET:
            field_dict["b64_decode_depth"] = b64_decode_depth
        if bitenc_decode_depth is not UNSET:
            field_dict["bitenc_decode_depth"] = bitenc_decode_depth
        if decompress_pdf is not UNSET:
            field_dict["decompress_pdf"] = decompress_pdf
        if decompress_swf is not UNSET:
            field_dict["decompress_swf"] = decompress_swf
        if decompress_zip is not UNSET:
            field_dict["decompress_zip"] = decompress_zip
        if decompress_vba is not UNSET:
            field_dict["decompress_vba"] = decompress_vba
        if qp_decode_depth is not UNSET:
            field_dict["qp_decode_depth"] = qp_decode_depth
        if uu_decode_depth is not UNSET:
            field_dict["uu_decode_depth"] = uu_decode_depth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        b64_decode_depth = d.pop("b64_decode_depth", UNSET)

        bitenc_decode_depth = d.pop("bitenc_decode_depth", UNSET)

        decompress_pdf = d.pop("decompress_pdf", UNSET)

        decompress_swf = d.pop("decompress_swf", UNSET)

        decompress_zip = d.pop("decompress_zip", UNSET)

        decompress_vba = d.pop("decompress_vba", UNSET)

        qp_decode_depth = d.pop("qp_decode_depth", UNSET)

        uu_decode_depth = d.pop("uu_decode_depth", UNSET)

        snort_insp_pop = cls(
            b64_decode_depth=b64_decode_depth,
            bitenc_decode_depth=bitenc_decode_depth,
            decompress_pdf=decompress_pdf,
            decompress_swf=decompress_swf,
            decompress_zip=decompress_zip,
            decompress_vba=decompress_vba,
            qp_decode_depth=qp_decode_depth,
            uu_decode_depth=uu_decode_depth,
        )

        snort_insp_pop.additional_properties = d
        return snort_insp_pop

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
