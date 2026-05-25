from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.aws_wizard_create_vpn_req_routing import AwsWizardCreateVpnReqRouting
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.aws_wizard_cred import AwsWizardCred
    from ..models.aws_wizard_vpc import AwsWizardVpc


T = TypeVar("T", bound="AwsWizardCreateVpnReq")


@_attrs_define
class AwsWizardCreateVpnReq:
    """
    Attributes:
        cred (AwsWizardCred | Unset):
        vpc (AwsWizardVpc | Unset):
        vp_gw_id (str | Unset): virtual private gateway id
        routing (AwsWizardCreateVpnReqRouting | Unset): routing type
        bgpasn (str | Unset): bgp as number. Defaults to 65000
        locpubip (str | Unset): local public ip address
        loccidrs (list[str] | Unset):
        updatesecgroups (bool | Unset): update security groups
        max_wait_time (int | Unset): maximum number of minute to wait for the vpn to be created. default 15 mintues
    """

    cred: AwsWizardCred | Unset = UNSET
    vpc: AwsWizardVpc | Unset = UNSET
    vp_gw_id: str | Unset = UNSET
    routing: AwsWizardCreateVpnReqRouting | Unset = UNSET
    bgpasn: str | Unset = UNSET
    locpubip: str | Unset = UNSET
    loccidrs: list[str] | Unset = UNSET
    updatesecgroups: bool | Unset = UNSET
    max_wait_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cred: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cred, Unset):
            cred = self.cred.to_dict()

        vpc: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vpc, Unset):
            vpc = self.vpc.to_dict()

        vp_gw_id = self.vp_gw_id

        routing: str | Unset = UNSET
        if not isinstance(self.routing, Unset):
            routing = self.routing.value

        bgpasn = self.bgpasn

        locpubip = self.locpubip

        loccidrs: list[str] | Unset = UNSET
        if not isinstance(self.loccidrs, Unset):
            loccidrs = self.loccidrs

        updatesecgroups = self.updatesecgroups

        max_wait_time = self.max_wait_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cred is not UNSET:
            field_dict["cred"] = cred
        if vpc is not UNSET:
            field_dict["vpc"] = vpc
        if vp_gw_id is not UNSET:
            field_dict["vp_gw_id"] = vp_gw_id
        if routing is not UNSET:
            field_dict["routing"] = routing
        if bgpasn is not UNSET:
            field_dict["bgpasn"] = bgpasn
        if locpubip is not UNSET:
            field_dict["locpubip"] = locpubip
        if loccidrs is not UNSET:
            field_dict["loccidrs"] = loccidrs
        if updatesecgroups is not UNSET:
            field_dict["updatesecgroups"] = updatesecgroups
        if max_wait_time is not UNSET:
            field_dict["max_wait_time"] = max_wait_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_wizard_cred import AwsWizardCred
        from ..models.aws_wizard_vpc import AwsWizardVpc

        d = dict(src_dict)
        _cred = d.pop("cred", UNSET)
        cred: AwsWizardCred | Unset
        if isinstance(_cred, Unset):
            cred = UNSET
        else:
            cred = AwsWizardCred.from_dict(_cred)

        _vpc = d.pop("vpc", UNSET)
        vpc: AwsWizardVpc | Unset
        if isinstance(_vpc, Unset):
            vpc = UNSET
        else:
            vpc = AwsWizardVpc.from_dict(_vpc)

        vp_gw_id = d.pop("vp_gw_id", UNSET)

        _routing = d.pop("routing", UNSET)
        routing: AwsWizardCreateVpnReqRouting | Unset
        if isinstance(_routing, Unset):
            routing = UNSET
        else:
            routing = AwsWizardCreateVpnReqRouting(_routing)

        bgpasn = d.pop("bgpasn", UNSET)

        locpubip = d.pop("locpubip", UNSET)

        loccidrs = cast(list[str], d.pop("loccidrs", UNSET))

        updatesecgroups = d.pop("updatesecgroups", UNSET)

        max_wait_time = d.pop("max_wait_time", UNSET)

        aws_wizard_create_vpn_req = cls(
            cred=cred,
            vpc=vpc,
            vp_gw_id=vp_gw_id,
            routing=routing,
            bgpasn=bgpasn,
            locpubip=locpubip,
            loccidrs=loccidrs,
            updatesecgroups=updatesecgroups,
            max_wait_time=max_wait_time,
        )

        aws_wizard_create_vpn_req.additional_properties = d
        return aws_wizard_create_vpn_req

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
