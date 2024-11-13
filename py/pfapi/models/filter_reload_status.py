from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FilterReloadStatus")


@_attrs_define
class FilterReloadStatus:
    """
    Attributes:
        ongoing (Union[Unset, bool]):
        done (Union[Unset, bool]):
        status_lines (Union[Unset, List[str]]):
    """

    ongoing: Union[Unset, bool] = UNSET
    done: Union[Unset, bool] = UNSET
    status_lines: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ongoing = self.ongoing

        done = self.done

        status_lines: Union[Unset, List[str]] = UNSET
        if not isinstance(self.status_lines, Unset):
            status_lines = self.status_lines

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ongoing is not UNSET:
            field_dict["ongoing"] = ongoing
        if done is not UNSET:
            field_dict["done"] = done
        if status_lines is not UNSET:
            field_dict["status_lines"] = status_lines

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ongoing = d.pop("ongoing", UNSET)

        done = d.pop("done", UNSET)

        status_lines = cast(List[str], d.pop("status_lines", UNSET))

        filter_reload_status = cls(
            ongoing=ongoing,
            done=done,
            status_lines=status_lines,
        )

        filter_reload_status.additional_properties = d
        return filter_reload_status

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
