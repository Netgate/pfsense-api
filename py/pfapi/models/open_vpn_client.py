from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_vpn_client_config import OpenVPNClientConfig


T = TypeVar("T", bound="OpenVPNClient")


@_attrs_define
class OpenVPNClient:
    """
    Attributes:
        client (Union[Unset, OpenVPNClientConfig]):
    """

    client: Union[Unset, "OpenVPNClientConfig"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client is not UNSET:
            field_dict["client"] = client

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.open_vpn_client_config import OpenVPNClientConfig

        d = src_dict.copy()
        _client = d.pop("client", UNSET)
        client: Union[Unset, OpenVPNClientConfig]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = OpenVPNClientConfig.from_dict(_client)

        open_vpn_client = cls(
            client=client,
        )

        open_vpn_client.additional_properties = d
        return open_vpn_client

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
