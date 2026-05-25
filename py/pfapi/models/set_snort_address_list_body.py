from __future__ import annotations

import json
from collections.abc import Mapping
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, FileTypes, Unset

if TYPE_CHECKING:
    from ..models.snort_address_list import SnortAddressList


T = TypeVar("T", bound="SetSnortAddressListBody")


@_attrs_define
class SetSnortAddressListBody:
    """
    Attributes:
        req (SnortAddressList | Unset):
        addresslist (File | Unset):
    """

    req: SnortAddressList | Unset = UNSET
    addresslist: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        req: dict[str, Any] | Unset = UNSET
        if not isinstance(self.req, Unset):
            req = self.req.to_dict()

        addresslist: FileTypes | Unset = UNSET
        if not isinstance(self.addresslist, Unset):
            addresslist = self.addresslist.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if req is not UNSET:
            field_dict["req"] = req
        if addresslist is not UNSET:
            field_dict["addresslist"] = addresslist

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.req, Unset):
            files.append(("req", (None, json.dumps(self.req.to_dict()).encode(), "application/json")))

        if not isinstance(self.addresslist, Unset):
            files.append(("addresslist", self.addresslist.to_tuple()))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_address_list import SnortAddressList

        d = dict(src_dict)
        _req = d.pop("req", UNSET)
        req: SnortAddressList | Unset
        if isinstance(_req, Unset):
            req = UNSET
        else:
            req = SnortAddressList.from_dict(_req)

        _addresslist = d.pop("addresslist", UNSET)
        addresslist: File | Unset
        if isinstance(_addresslist, Unset):
            addresslist = UNSET
        else:
            addresslist = File(payload=BytesIO(_addresslist))

        set_snort_address_list_body = cls(
            req=req,
            addresslist=addresslist,
        )

        set_snort_address_list_body.additional_properties = d
        return set_snort_address_list_body

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
