from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Package")


@_attrs_define
class Package:
    """
    Attributes:
        name (str):
        internal_name (str):
        info_link (str):
        descr (str):
        version (str):
        config_file (str):
        include_file (str):
        category (str):
        depedencies (Union[Unset, List[str]]):
    """

    name: str
    internal_name: str
    info_link: str
    descr: str
    version: str
    config_file: str
    include_file: str
    category: str
    depedencies: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        internal_name = self.internal_name

        info_link = self.info_link

        descr = self.descr

        version = self.version

        config_file = self.config_file

        include_file = self.include_file

        category = self.category

        depedencies: Union[Unset, List[str]] = UNSET
        if not isinstance(self.depedencies, Unset):
            depedencies = self.depedencies

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "internal_name": internal_name,
                "info_link": info_link,
                "descr": descr,
                "version": version,
                "config_file": config_file,
                "include_file": include_file,
                "category": category,
            }
        )
        if depedencies is not UNSET:
            field_dict["depedencies"] = depedencies

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        internal_name = d.pop("internal_name")

        info_link = d.pop("info_link")

        descr = d.pop("descr")

        version = d.pop("version")

        config_file = d.pop("config_file")

        include_file = d.pop("include_file")

        category = d.pop("category")

        depedencies = cast(List[str], d.pop("depedencies", UNSET))

        package = cls(
            name=name,
            internal_name=internal_name,
            info_link=info_link,
            descr=descr,
            version=version,
            config_file=config_file,
            include_file=include_file,
            category=category,
            depedencies=depedencies,
        )

        package.additional_properties = d
        return package

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
