from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.all_software_packages_software_packages import AllSoftwarePackagesSoftwarePackages


T = TypeVar("T", bound="AllSoftwarePackages")


@_attrs_define
class AllSoftwarePackages:
    """Example:

    {
      "software_packages": {
        "plus": {
          "24.03": {
            "packages": [
              { "name": "snort", "category": "security", "local_version": "1.0.1", "avail_version": "1.0.2" },
              ...
            ]
          }
        },
        "free": {
          "2.8.0": {
            "packages": [
              { "name": "tinyproxy", "category": "net", "local_version": "1.1", "avail_version": "1.1" },
              ...
            ]
          }
        }
      }
    }

        Attributes:
            software_packages (Union[Unset, AllSoftwarePackagesSoftwarePackages]):
    """

    software_packages: Union[Unset, "AllSoftwarePackagesSoftwarePackages"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        software_packages: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.software_packages, Unset):
            software_packages = self.software_packages.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if software_packages is not UNSET:
            field_dict["software_packages"] = software_packages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.all_software_packages_software_packages import AllSoftwarePackagesSoftwarePackages

        d = src_dict.copy()
        _software_packages = d.pop("software_packages", UNSET)
        software_packages: Union[Unset, AllSoftwarePackagesSoftwarePackages]
        if isinstance(_software_packages, Unset):
            software_packages = UNSET
        else:
            software_packages = AllSoftwarePackagesSoftwarePackages.from_dict(_software_packages)

        all_software_packages = cls(
            software_packages=software_packages,
        )

        all_software_packages.additional_properties = d
        return all_software_packages

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
