from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aws_wizard_create_tunnels_req_routing import AwsWizardCreateTunnelsReqRouting
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_wizard_vpc import AwsWizardVpc


T = TypeVar("T", bound="AwsWizardCreateTunnelsReq")


@_attrs_define
class AwsWizardCreateTunnelsReq:
    """
    Attributes:
        vpc (AwsWizardVpc | Unset):
        loc_if_ident (str | Unset): interface for the local endpoint of the tunnels
        loccidrs (list[str] | Unset):
        routing (AwsWizardCreateTunnelsReqRouting | Unset): routing type
        custgwcfg (str | Unset): base64 encoded customer gateway configuration
    """

    vpc: AwsWizardVpc | Unset = UNSET
    loc_if_ident: str | Unset = UNSET
    loccidrs: list[str] | Unset = UNSET
    routing: AwsWizardCreateTunnelsReqRouting | Unset = UNSET
    custgwcfg: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vpc, Unset):
            vpc = self.vpc.to_dict()

        loc_if_ident = self.loc_if_ident

        loccidrs: list[str] | Unset = UNSET
        if not isinstance(self.loccidrs, Unset):
            loccidrs = self.loccidrs

        routing: str | Unset = UNSET
        if not isinstance(self.routing, Unset):
            routing = self.routing.value

        custgwcfg = self.custgwcfg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpc is not UNSET:
            field_dict["vpc"] = vpc
        if loc_if_ident is not UNSET:
            field_dict["loc_if_ident"] = loc_if_ident
        if loccidrs is not UNSET:
            field_dict["loccidrs"] = loccidrs
        if routing is not UNSET:
            field_dict["routing"] = routing
        if custgwcfg is not UNSET:
            field_dict["custgwcfg"] = custgwcfg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_wizard_vpc import AwsWizardVpc

        d = dict(src_dict)
        _vpc = d.pop("vpc", UNSET)
        vpc: AwsWizardVpc | Unset
        if isinstance(_vpc, Unset):
            vpc = UNSET
        else:
            vpc = AwsWizardVpc.from_dict(_vpc)

        loc_if_ident = d.pop("loc_if_ident", UNSET)

        loccidrs = cast(list[str], d.pop("loccidrs", UNSET))

        _routing = d.pop("routing", UNSET)
        routing: AwsWizardCreateTunnelsReqRouting | Unset
        if isinstance(_routing, Unset):
            routing = UNSET
        else:
            routing = AwsWizardCreateTunnelsReqRouting(_routing)

        custgwcfg = d.pop("custgwcfg", UNSET)

        aws_wizard_create_tunnels_req = cls(
            vpc=vpc,
            loc_if_ident=loc_if_ident,
            loccidrs=loccidrs,
            routing=routing,
            custgwcfg=custgwcfg,
        )

        aws_wizard_create_tunnels_req.additional_properties = d
        return aws_wizard_create_tunnels_req

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
