from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fw_filter_rule import FWFilterRule
    from ..models.nat1_to_1_rule import NAT1To1Rule
    from ..models.nat_npt_rule import NATNptRule
    from ..models.nat_outbound_rule import NATOutboundRule
    from ..models.nat_rule import NATRule
    from ..models.separator import Separator


T = TypeVar("T", bound="FirewallEvent")


@_attrs_define
class FirewallEvent:
    """
    Attributes:
        intf_name (Union[Unset, str]): friendly network interface name
        action (Union[Unset, str]): activity on the rule - added, updated, deleted, moved
        rule_type (Union[Unset, str]): filter, separator, nat, nat1to1, natout, npt
        filter_ (Union[Unset, FWFilterRule]):
        nat (Union[Unset, NATRule]):
        nat1to1 (Union[Unset, NAT1To1Rule]):
        natout (Union[Unset, NATOutboundRule]):
        npt (Union[Unset, NATNptRule]):
        separator (Union[Unset, Separator]):
    """

    intf_name: Union[Unset, str] = UNSET
    action: Union[Unset, str] = UNSET
    rule_type: Union[Unset, str] = UNSET
    filter_: Union[Unset, "FWFilterRule"] = UNSET
    nat: Union[Unset, "NATRule"] = UNSET
    nat1to1: Union[Unset, "NAT1To1Rule"] = UNSET
    natout: Union[Unset, "NATOutboundRule"] = UNSET
    npt: Union[Unset, "NATNptRule"] = UNSET
    separator: Union[Unset, "Separator"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        intf_name = self.intf_name

        action = self.action

        rule_type = self.rule_type

        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        nat: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nat, Unset):
            nat = self.nat.to_dict()

        nat1to1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nat1to1, Unset):
            nat1to1 = self.nat1to1.to_dict()

        natout: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.natout, Unset):
            natout = self.natout.to_dict()

        npt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.npt, Unset):
            npt = self.npt.to_dict()

        separator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.separator, Unset):
            separator = self.separator.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if intf_name is not UNSET:
            field_dict["intf_name"] = intf_name
        if action is not UNSET:
            field_dict["action"] = action
        if rule_type is not UNSET:
            field_dict["rule_type"] = rule_type
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if nat is not UNSET:
            field_dict["nat"] = nat
        if nat1to1 is not UNSET:
            field_dict["nat1to1"] = nat1to1
        if natout is not UNSET:
            field_dict["natout"] = natout
        if npt is not UNSET:
            field_dict["npt"] = npt
        if separator is not UNSET:
            field_dict["separator"] = separator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fw_filter_rule import FWFilterRule
        from ..models.nat1_to_1_rule import NAT1To1Rule
        from ..models.nat_npt_rule import NATNptRule
        from ..models.nat_outbound_rule import NATOutboundRule
        from ..models.nat_rule import NATRule
        from ..models.separator import Separator

        d = src_dict.copy()
        intf_name = d.pop("intf_name", UNSET)

        action = d.pop("action", UNSET)

        rule_type = d.pop("rule_type", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, FWFilterRule]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = FWFilterRule.from_dict(_filter_)

        _nat = d.pop("nat", UNSET)
        nat: Union[Unset, NATRule]
        if isinstance(_nat, Unset):
            nat = UNSET
        else:
            nat = NATRule.from_dict(_nat)

        _nat1to1 = d.pop("nat1to1", UNSET)
        nat1to1: Union[Unset, NAT1To1Rule]
        if isinstance(_nat1to1, Unset):
            nat1to1 = UNSET
        else:
            nat1to1 = NAT1To1Rule.from_dict(_nat1to1)

        _natout = d.pop("natout", UNSET)
        natout: Union[Unset, NATOutboundRule]
        if isinstance(_natout, Unset):
            natout = UNSET
        else:
            natout = NATOutboundRule.from_dict(_natout)

        _npt = d.pop("npt", UNSET)
        npt: Union[Unset, NATNptRule]
        if isinstance(_npt, Unset):
            npt = UNSET
        else:
            npt = NATNptRule.from_dict(_npt)

        _separator = d.pop("separator", UNSET)
        separator: Union[Unset, Separator]
        if isinstance(_separator, Unset):
            separator = UNSET
        else:
            separator = Separator.from_dict(_separator)

        firewall_event = cls(
            intf_name=intf_name,
            action=action,
            rule_type=rule_type,
            filter_=filter_,
            nat=nat,
            nat1to1=nat1to1,
            natout=natout,
            npt=npt,
            separator=separator,
        )

        firewall_event.additional_properties = d
        return firewall_event

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
