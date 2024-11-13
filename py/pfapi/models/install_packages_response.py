from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.package_install_progress import PackageInstallProgress


T = TypeVar("T", bound="InstallPackagesResponse")


@_attrs_define
class InstallPackagesResponse:
    """Current progress of package (re)installation. A transaction ID can be used to resume querying of status.

    Attributes:
        transaction (Union[Unset, str]):
        progress (Union[Unset, List['PackageInstallProgress']]):
    """

    transaction: Union[Unset, str] = UNSET
    progress: Union[Unset, List["PackageInstallProgress"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction = self.transaction

        progress: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = []
            for progress_item_data in self.progress:
                progress_item = progress_item_data.to_dict()
                progress.append(progress_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction is not UNSET:
            field_dict["transaction"] = transaction
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.package_install_progress import PackageInstallProgress

        d = src_dict.copy()
        transaction = d.pop("transaction", UNSET)

        progress = []
        _progress = d.pop("progress", UNSET)
        for progress_item_data in _progress or []:
            progress_item = PackageInstallProgress.from_dict(progress_item_data)

            progress.append(progress_item)

        install_packages_response = cls(
            transaction=transaction,
            progress=progress,
        )

        install_packages_response.additional_properties = d
        return install_packages_response

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
