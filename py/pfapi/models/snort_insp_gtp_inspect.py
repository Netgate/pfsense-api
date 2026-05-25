from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_gtp_inspect_l_infos import SnortInspGtpInspectLInfos
    from ..models.snort_insp_gtp_inspect_l_messages import SnortInspGtpInspectLMessages


T = TypeVar("T", bound="SnortInspGtpInspect")


@_attrs_define
class SnortInspGtpInspect:
    """
    Attributes:
        version (int | Unset): GTP version { 0:2 }; default 2
        messages (list[SnortInspGtpInspectLMessages] | Unset):
        infos (list[SnortInspGtpInspectLInfos] | Unset):
    """

    version: int | Unset = UNSET
    messages: list[SnortInspGtpInspectLMessages] | Unset = UNSET
    infos: list[SnortInspGtpInspectLInfos] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.infos, Unset):
            infos = []
            for infos_item_data in self.infos:
                infos_item = infos_item_data.to_dict()
                infos.append(infos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if messages is not UNSET:
            field_dict["messages"] = messages
        if infos is not UNSET:
            field_dict["infos"] = infos

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_gtp_inspect_l_infos import SnortInspGtpInspectLInfos
        from ..models.snort_insp_gtp_inspect_l_messages import SnortInspGtpInspectLMessages

        d = dict(src_dict)
        version = d.pop("version", UNSET)

        _messages = d.pop("messages", UNSET)
        messages: list[SnortInspGtpInspectLMessages] | Unset = UNSET
        if _messages is not UNSET:
            messages = []
            for messages_item_data in _messages:
                messages_item = SnortInspGtpInspectLMessages.from_dict(messages_item_data)

                messages.append(messages_item)

        _infos = d.pop("infos", UNSET)
        infos: list[SnortInspGtpInspectLInfos] | Unset = UNSET
        if _infos is not UNSET:
            infos = []
            for infos_item_data in _infos:
                infos_item = SnortInspGtpInspectLInfos.from_dict(infos_item_data)

                infos.append(infos_item)

        snort_insp_gtp_inspect = cls(
            version=version,
            messages=messages,
            infos=infos,
        )

        snort_insp_gtp_inspect.additional_properties = d
        return snort_insp_gtp_inspect

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
