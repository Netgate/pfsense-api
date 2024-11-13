from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_high_availability_advance_config import DhcpHighAvailabilityAdvanceConfig


T = TypeVar("T", bound="DhcpHighAvailabilityConfig")


@_attrs_define
class DhcpHighAvailabilityConfig:
    """High-availability configuration for Kea DHCP service.

    Attributes:
        enable (Union[Unset, bool]):
        role (Union[Unset, str]):
        local_name (Union[Unset, str]):
        local_address (Union[Unset, str]):
        remote_name (Union[Unset, str]):
        remote_address (Union[Unset, str]):
        advance_options (Union[Unset, DhcpHighAvailabilityAdvanceConfig]):
        enable_tls (Union[Unset, bool]):
        tls_server_cert_refid (Union[Unset, str]):
        enable_mutual_tls (Union[Unset, bool]):
        mutual_client_cert_refid (Union[Unset, str]):
        available_tls_server_certs (Union[Unset, List[str]]):
        available_mutual_client_certs (Union[Unset, List[str]]):
    """

    enable: Union[Unset, bool] = UNSET
    role: Union[Unset, str] = UNSET
    local_name: Union[Unset, str] = UNSET
    local_address: Union[Unset, str] = UNSET
    remote_name: Union[Unset, str] = UNSET
    remote_address: Union[Unset, str] = UNSET
    advance_options: Union[Unset, "DhcpHighAvailabilityAdvanceConfig"] = UNSET
    enable_tls: Union[Unset, bool] = UNSET
    tls_server_cert_refid: Union[Unset, str] = UNSET
    enable_mutual_tls: Union[Unset, bool] = UNSET
    mutual_client_cert_refid: Union[Unset, str] = UNSET
    available_tls_server_certs: Union[Unset, List[str]] = UNSET
    available_mutual_client_certs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enable = self.enable

        role = self.role

        local_name = self.local_name

        local_address = self.local_address

        remote_name = self.remote_name

        remote_address = self.remote_address

        advance_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.advance_options, Unset):
            advance_options = self.advance_options.to_dict()

        enable_tls = self.enable_tls

        tls_server_cert_refid = self.tls_server_cert_refid

        enable_mutual_tls = self.enable_mutual_tls

        mutual_client_cert_refid = self.mutual_client_cert_refid

        available_tls_server_certs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available_tls_server_certs, Unset):
            available_tls_server_certs = self.available_tls_server_certs

        available_mutual_client_certs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available_mutual_client_certs, Unset):
            available_mutual_client_certs = self.available_mutual_client_certs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if role is not UNSET:
            field_dict["role"] = role
        if local_name is not UNSET:
            field_dict["local_name"] = local_name
        if local_address is not UNSET:
            field_dict["local_address"] = local_address
        if remote_name is not UNSET:
            field_dict["remote_name"] = remote_name
        if remote_address is not UNSET:
            field_dict["remote_address"] = remote_address
        if advance_options is not UNSET:
            field_dict["advance_options"] = advance_options
        if enable_tls is not UNSET:
            field_dict["enable_tls"] = enable_tls
        if tls_server_cert_refid is not UNSET:
            field_dict["tls_server_cert_refid"] = tls_server_cert_refid
        if enable_mutual_tls is not UNSET:
            field_dict["enable_mutual_tls"] = enable_mutual_tls
        if mutual_client_cert_refid is not UNSET:
            field_dict["mutual_client_cert_refid"] = mutual_client_cert_refid
        if available_tls_server_certs is not UNSET:
            field_dict["available_tls_server_certs"] = available_tls_server_certs
        if available_mutual_client_certs is not UNSET:
            field_dict["available_mutual_client_certs"] = available_mutual_client_certs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dhcp_high_availability_advance_config import DhcpHighAvailabilityAdvanceConfig

        d = src_dict.copy()
        enable = d.pop("enable", UNSET)

        role = d.pop("role", UNSET)

        local_name = d.pop("local_name", UNSET)

        local_address = d.pop("local_address", UNSET)

        remote_name = d.pop("remote_name", UNSET)

        remote_address = d.pop("remote_address", UNSET)

        _advance_options = d.pop("advance_options", UNSET)
        advance_options: Union[Unset, DhcpHighAvailabilityAdvanceConfig]
        if isinstance(_advance_options, Unset):
            advance_options = UNSET
        else:
            advance_options = DhcpHighAvailabilityAdvanceConfig.from_dict(_advance_options)

        enable_tls = d.pop("enable_tls", UNSET)

        tls_server_cert_refid = d.pop("tls_server_cert_refid", UNSET)

        enable_mutual_tls = d.pop("enable_mutual_tls", UNSET)

        mutual_client_cert_refid = d.pop("mutual_client_cert_refid", UNSET)

        available_tls_server_certs = cast(List[str], d.pop("available_tls_server_certs", UNSET))

        available_mutual_client_certs = cast(List[str], d.pop("available_mutual_client_certs", UNSET))

        dhcp_high_availability_config = cls(
            enable=enable,
            role=role,
            local_name=local_name,
            local_address=local_address,
            remote_name=remote_name,
            remote_address=remote_address,
            advance_options=advance_options,
            enable_tls=enable_tls,
            tls_server_cert_refid=tls_server_cert_refid,
            enable_mutual_tls=enable_mutual_tls,
            mutual_client_cert_refid=mutual_client_cert_refid,
            available_tls_server_certs=available_tls_server_certs,
            available_mutual_client_certs=available_mutual_client_certs,
        )

        dhcp_high_availability_config.additional_properties = d
        return dhcp_high_availability_config

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
