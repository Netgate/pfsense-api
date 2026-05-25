from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_ripd_row import FrrRipdRow
    from ..models.text_value import TextValue


T = TypeVar("T", bound="FrrRipd")


@_attrs_define
class FrrRipd:
    """
    Attributes:
        enable (bool | Unset): Enable

            Enable RIP Routing
        row (list[FrrRipdRow] | Unset):
        redistributeconnectedsubnets (bool | Unset): (Route Redistribution) Connected Networks

            Redistribute Connected Networks
        redistributeconnectedsubnets_metric (str | Unset): (Route Redistribution) Metric (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 11, 12, 13, 14, 15, 16)

            Metric
        redistributeconnectedsubnets_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributeconnectedsubnets_distlist (str | Unset): (Route Redistribution) Distribute List

            Distribute List
        redistributekernel (bool | Unset): (Route Redistribution) pfSense Kernel Routes

            Redistribute pfSense Kernel
        redistributekernel_metric (str | Unset): (Route Redistribution) Metric (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
            12, 13, 14, 15, 16)

            Metric
        redistributekernel_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributekernel_distlist (str | Unset): (Route Redistribution) Distribute List

            Distribute List
        redistributebgp (bool | Unset): (Route Redistribution) BGP Routes

            Redistribute BGP
        redistributebgp_metric (str | Unset): (Route Redistribution) Metric (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16)

            Metric
        redistributebgp_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributebgp_distlist (str | Unset): (Route Redistribution) Distribute List

            Distribute List
        redistributeospf (bool | Unset): (Route Redistribution) OSPF Routes

            Redistribute OSPF
        redistributeospf_metric (str | Unset): (Route Redistribution) Metric (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
            13, 14, 15, 16)

            Metric
        redistributeospf_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributeospf_distlist (str | Unset): (Route Redistribution) Distribute List

            Distribute List
        redistributestatic (bool | Unset): (Route Redistribution) FRR Static Routes

            Redistribute FRR Static
        redistributestatic_metric (str | Unset): (Route Redistribution) Metric (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
            12, 13, 14, 15, 16)

            Metric
        redistributestatic_routemap (str | Unset): (Route Redistribution)

            Route Map
        redistributestatic_distlist (str | Unset): (Route Redistribution) Distribute List

            Distribute List
        redistributedefaultroute (bool | Unset): (Default Route Redistribution) Redistribute Default

            Redistribute a Default route to neighbors
        ripversion (str | Unset): (Advanced) RIP Version (2, 1)

            Defines RIP version.
        inoffsetlist (str | Unset): (Advanced) Incoming Offset List

            Incoming Updates Offset List
        inmetricvalue (str | Unset): (Advanced) Metric Value (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

            In Offset Metric Value
        outoffsetlist (str | Unset): (Advanced) Outgoing Offset List

            Outgoing Updates Offset List
        outmetricvalue (str | Unset): (Advanced) Metric Value (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)

            In Offset Metric Value
        redistributeconnectedsubnets_routemap_options (list[TextValue] | Unset):
        redistributeconnectedsubnets_distlist_options (list[TextValue] | Unset):
        redistributekernel_routemap_options (list[TextValue] | Unset):
        redistributekernel_distlist_options (list[TextValue] | Unset):
        redistributebgp_routemap_options (list[TextValue] | Unset):
        redistributebgp_distlist_options (list[TextValue] | Unset):
        redistributeospf_routemap_options (list[TextValue] | Unset):
        redistributeospf_distlist_options (list[TextValue] | Unset):
        redistributestatic_routemap_options (list[TextValue] | Unset):
        redistributestatic_distlist_options (list[TextValue] | Unset):
        inoffsetlist_options (list[TextValue] | Unset):
        outoffsetlist_options (list[TextValue] | Unset):
    """

    enable: bool | Unset = UNSET
    row: list[FrrRipdRow] | Unset = UNSET
    redistributeconnectedsubnets: bool | Unset = UNSET
    redistributeconnectedsubnets_metric: str | Unset = UNSET
    redistributeconnectedsubnets_routemap: str | Unset = UNSET
    redistributeconnectedsubnets_distlist: str | Unset = UNSET
    redistributekernel: bool | Unset = UNSET
    redistributekernel_metric: str | Unset = UNSET
    redistributekernel_routemap: str | Unset = UNSET
    redistributekernel_distlist: str | Unset = UNSET
    redistributebgp: bool | Unset = UNSET
    redistributebgp_metric: str | Unset = UNSET
    redistributebgp_routemap: str | Unset = UNSET
    redistributebgp_distlist: str | Unset = UNSET
    redistributeospf: bool | Unset = UNSET
    redistributeospf_metric: str | Unset = UNSET
    redistributeospf_routemap: str | Unset = UNSET
    redistributeospf_distlist: str | Unset = UNSET
    redistributestatic: bool | Unset = UNSET
    redistributestatic_metric: str | Unset = UNSET
    redistributestatic_routemap: str | Unset = UNSET
    redistributestatic_distlist: str | Unset = UNSET
    redistributedefaultroute: bool | Unset = UNSET
    ripversion: str | Unset = UNSET
    inoffsetlist: str | Unset = UNSET
    inmetricvalue: str | Unset = UNSET
    outoffsetlist: str | Unset = UNSET
    outmetricvalue: str | Unset = UNSET
    redistributeconnectedsubnets_routemap_options: list[TextValue] | Unset = UNSET
    redistributeconnectedsubnets_distlist_options: list[TextValue] | Unset = UNSET
    redistributekernel_routemap_options: list[TextValue] | Unset = UNSET
    redistributekernel_distlist_options: list[TextValue] | Unset = UNSET
    redistributebgp_routemap_options: list[TextValue] | Unset = UNSET
    redistributebgp_distlist_options: list[TextValue] | Unset = UNSET
    redistributeospf_routemap_options: list[TextValue] | Unset = UNSET
    redistributeospf_distlist_options: list[TextValue] | Unset = UNSET
    redistributestatic_routemap_options: list[TextValue] | Unset = UNSET
    redistributestatic_distlist_options: list[TextValue] | Unset = UNSET
    inoffsetlist_options: list[TextValue] | Unset = UNSET
    outoffsetlist_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        row: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        redistributeconnectedsubnets = self.redistributeconnectedsubnets

        redistributeconnectedsubnets_metric = self.redistributeconnectedsubnets_metric

        redistributeconnectedsubnets_routemap = self.redistributeconnectedsubnets_routemap

        redistributeconnectedsubnets_distlist = self.redistributeconnectedsubnets_distlist

        redistributekernel = self.redistributekernel

        redistributekernel_metric = self.redistributekernel_metric

        redistributekernel_routemap = self.redistributekernel_routemap

        redistributekernel_distlist = self.redistributekernel_distlist

        redistributebgp = self.redistributebgp

        redistributebgp_metric = self.redistributebgp_metric

        redistributebgp_routemap = self.redistributebgp_routemap

        redistributebgp_distlist = self.redistributebgp_distlist

        redistributeospf = self.redistributeospf

        redistributeospf_metric = self.redistributeospf_metric

        redistributeospf_routemap = self.redistributeospf_routemap

        redistributeospf_distlist = self.redistributeospf_distlist

        redistributestatic = self.redistributestatic

        redistributestatic_metric = self.redistributestatic_metric

        redistributestatic_routemap = self.redistributestatic_routemap

        redistributestatic_distlist = self.redistributestatic_distlist

        redistributedefaultroute = self.redistributedefaultroute

        ripversion = self.ripversion

        inoffsetlist = self.inoffsetlist

        inmetricvalue = self.inmetricvalue

        outoffsetlist = self.outoffsetlist

        outmetricvalue = self.outmetricvalue

        redistributeconnectedsubnets_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributeconnectedsubnets_routemap_options, Unset):
            redistributeconnectedsubnets_routemap_options = []
            for (
                redistributeconnectedsubnets_routemap_options_item_data
            ) in self.redistributeconnectedsubnets_routemap_options:
                redistributeconnectedsubnets_routemap_options_item = (
                    redistributeconnectedsubnets_routemap_options_item_data.to_dict()
                )
                redistributeconnectedsubnets_routemap_options.append(redistributeconnectedsubnets_routemap_options_item)

        redistributeconnectedsubnets_distlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributeconnectedsubnets_distlist_options, Unset):
            redistributeconnectedsubnets_distlist_options = []
            for (
                redistributeconnectedsubnets_distlist_options_item_data
            ) in self.redistributeconnectedsubnets_distlist_options:
                redistributeconnectedsubnets_distlist_options_item = (
                    redistributeconnectedsubnets_distlist_options_item_data.to_dict()
                )
                redistributeconnectedsubnets_distlist_options.append(redistributeconnectedsubnets_distlist_options_item)

        redistributekernel_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributekernel_routemap_options, Unset):
            redistributekernel_routemap_options = []
            for redistributekernel_routemap_options_item_data in self.redistributekernel_routemap_options:
                redistributekernel_routemap_options_item = redistributekernel_routemap_options_item_data.to_dict()
                redistributekernel_routemap_options.append(redistributekernel_routemap_options_item)

        redistributekernel_distlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributekernel_distlist_options, Unset):
            redistributekernel_distlist_options = []
            for redistributekernel_distlist_options_item_data in self.redistributekernel_distlist_options:
                redistributekernel_distlist_options_item = redistributekernel_distlist_options_item_data.to_dict()
                redistributekernel_distlist_options.append(redistributekernel_distlist_options_item)

        redistributebgp_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributebgp_routemap_options, Unset):
            redistributebgp_routemap_options = []
            for redistributebgp_routemap_options_item_data in self.redistributebgp_routemap_options:
                redistributebgp_routemap_options_item = redistributebgp_routemap_options_item_data.to_dict()
                redistributebgp_routemap_options.append(redistributebgp_routemap_options_item)

        redistributebgp_distlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributebgp_distlist_options, Unset):
            redistributebgp_distlist_options = []
            for redistributebgp_distlist_options_item_data in self.redistributebgp_distlist_options:
                redistributebgp_distlist_options_item = redistributebgp_distlist_options_item_data.to_dict()
                redistributebgp_distlist_options.append(redistributebgp_distlist_options_item)

        redistributeospf_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributeospf_routemap_options, Unset):
            redistributeospf_routemap_options = []
            for redistributeospf_routemap_options_item_data in self.redistributeospf_routemap_options:
                redistributeospf_routemap_options_item = redistributeospf_routemap_options_item_data.to_dict()
                redistributeospf_routemap_options.append(redistributeospf_routemap_options_item)

        redistributeospf_distlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributeospf_distlist_options, Unset):
            redistributeospf_distlist_options = []
            for redistributeospf_distlist_options_item_data in self.redistributeospf_distlist_options:
                redistributeospf_distlist_options_item = redistributeospf_distlist_options_item_data.to_dict()
                redistributeospf_distlist_options.append(redistributeospf_distlist_options_item)

        redistributestatic_routemap_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributestatic_routemap_options, Unset):
            redistributestatic_routemap_options = []
            for redistributestatic_routemap_options_item_data in self.redistributestatic_routemap_options:
                redistributestatic_routemap_options_item = redistributestatic_routemap_options_item_data.to_dict()
                redistributestatic_routemap_options.append(redistributestatic_routemap_options_item)

        redistributestatic_distlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.redistributestatic_distlist_options, Unset):
            redistributestatic_distlist_options = []
            for redistributestatic_distlist_options_item_data in self.redistributestatic_distlist_options:
                redistributestatic_distlist_options_item = redistributestatic_distlist_options_item_data.to_dict()
                redistributestatic_distlist_options.append(redistributestatic_distlist_options_item)

        inoffsetlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inoffsetlist_options, Unset):
            inoffsetlist_options = []
            for inoffsetlist_options_item_data in self.inoffsetlist_options:
                inoffsetlist_options_item = inoffsetlist_options_item_data.to_dict()
                inoffsetlist_options.append(inoffsetlist_options_item)

        outoffsetlist_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.outoffsetlist_options, Unset):
            outoffsetlist_options = []
            for outoffsetlist_options_item_data in self.outoffsetlist_options:
                outoffsetlist_options_item = outoffsetlist_options_item_data.to_dict()
                outoffsetlist_options.append(outoffsetlist_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if row is not UNSET:
            field_dict["row"] = row
        if redistributeconnectedsubnets is not UNSET:
            field_dict["redistributeconnectedsubnets"] = redistributeconnectedsubnets
        if redistributeconnectedsubnets_metric is not UNSET:
            field_dict["redistributeconnectedsubnets_metric"] = redistributeconnectedsubnets_metric
        if redistributeconnectedsubnets_routemap is not UNSET:
            field_dict["redistributeconnectedsubnets_routemap"] = redistributeconnectedsubnets_routemap
        if redistributeconnectedsubnets_distlist is not UNSET:
            field_dict["redistributeconnectedsubnets_distlist"] = redistributeconnectedsubnets_distlist
        if redistributekernel is not UNSET:
            field_dict["redistributekernel"] = redistributekernel
        if redistributekernel_metric is not UNSET:
            field_dict["redistributekernel_metric"] = redistributekernel_metric
        if redistributekernel_routemap is not UNSET:
            field_dict["redistributekernel_routemap"] = redistributekernel_routemap
        if redistributekernel_distlist is not UNSET:
            field_dict["redistributekernel_distlist"] = redistributekernel_distlist
        if redistributebgp is not UNSET:
            field_dict["redistributebgp"] = redistributebgp
        if redistributebgp_metric is not UNSET:
            field_dict["redistributebgp_metric"] = redistributebgp_metric
        if redistributebgp_routemap is not UNSET:
            field_dict["redistributebgp_routemap"] = redistributebgp_routemap
        if redistributebgp_distlist is not UNSET:
            field_dict["redistributebgp_distlist"] = redistributebgp_distlist
        if redistributeospf is not UNSET:
            field_dict["redistributeospf"] = redistributeospf
        if redistributeospf_metric is not UNSET:
            field_dict["redistributeospf_metric"] = redistributeospf_metric
        if redistributeospf_routemap is not UNSET:
            field_dict["redistributeospf_routemap"] = redistributeospf_routemap
        if redistributeospf_distlist is not UNSET:
            field_dict["redistributeospf_distlist"] = redistributeospf_distlist
        if redistributestatic is not UNSET:
            field_dict["redistributestatic"] = redistributestatic
        if redistributestatic_metric is not UNSET:
            field_dict["redistributestatic_metric"] = redistributestatic_metric
        if redistributestatic_routemap is not UNSET:
            field_dict["redistributestatic_routemap"] = redistributestatic_routemap
        if redistributestatic_distlist is not UNSET:
            field_dict["redistributestatic_distlist"] = redistributestatic_distlist
        if redistributedefaultroute is not UNSET:
            field_dict["redistributedefaultroute"] = redistributedefaultroute
        if ripversion is not UNSET:
            field_dict["ripversion"] = ripversion
        if inoffsetlist is not UNSET:
            field_dict["inoffsetlist"] = inoffsetlist
        if inmetricvalue is not UNSET:
            field_dict["inmetricvalue"] = inmetricvalue
        if outoffsetlist is not UNSET:
            field_dict["outoffsetlist"] = outoffsetlist
        if outmetricvalue is not UNSET:
            field_dict["outmetricvalue"] = outmetricvalue
        if redistributeconnectedsubnets_routemap_options is not UNSET:
            field_dict["redistributeconnectedsubnets_routemap_options"] = redistributeconnectedsubnets_routemap_options
        if redistributeconnectedsubnets_distlist_options is not UNSET:
            field_dict["redistributeconnectedsubnets_distlist_options"] = redistributeconnectedsubnets_distlist_options
        if redistributekernel_routemap_options is not UNSET:
            field_dict["redistributekernel_routemap_options"] = redistributekernel_routemap_options
        if redistributekernel_distlist_options is not UNSET:
            field_dict["redistributekernel_distlist_options"] = redistributekernel_distlist_options
        if redistributebgp_routemap_options is not UNSET:
            field_dict["redistributebgp_routemap_options"] = redistributebgp_routemap_options
        if redistributebgp_distlist_options is not UNSET:
            field_dict["redistributebgp_distlist_options"] = redistributebgp_distlist_options
        if redistributeospf_routemap_options is not UNSET:
            field_dict["redistributeospf_routemap_options"] = redistributeospf_routemap_options
        if redistributeospf_distlist_options is not UNSET:
            field_dict["redistributeospf_distlist_options"] = redistributeospf_distlist_options
        if redistributestatic_routemap_options is not UNSET:
            field_dict["redistributestatic_routemap_options"] = redistributestatic_routemap_options
        if redistributestatic_distlist_options is not UNSET:
            field_dict["redistributestatic_distlist_options"] = redistributestatic_distlist_options
        if inoffsetlist_options is not UNSET:
            field_dict["inoffsetlist_options"] = inoffsetlist_options
        if outoffsetlist_options is not UNSET:
            field_dict["outoffsetlist_options"] = outoffsetlist_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_ripd_row import FrrRipdRow
        from ..models.text_value import TextValue

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        _row = d.pop("row", UNSET)
        row: list[FrrRipdRow] | Unset = UNSET
        if _row is not UNSET:
            row = []
            for row_item_data in _row:
                row_item = FrrRipdRow.from_dict(row_item_data)

                row.append(row_item)

        redistributeconnectedsubnets = d.pop("redistributeconnectedsubnets", UNSET)

        redistributeconnectedsubnets_metric = d.pop("redistributeconnectedsubnets_metric", UNSET)

        redistributeconnectedsubnets_routemap = d.pop("redistributeconnectedsubnets_routemap", UNSET)

        redistributeconnectedsubnets_distlist = d.pop("redistributeconnectedsubnets_distlist", UNSET)

        redistributekernel = d.pop("redistributekernel", UNSET)

        redistributekernel_metric = d.pop("redistributekernel_metric", UNSET)

        redistributekernel_routemap = d.pop("redistributekernel_routemap", UNSET)

        redistributekernel_distlist = d.pop("redistributekernel_distlist", UNSET)

        redistributebgp = d.pop("redistributebgp", UNSET)

        redistributebgp_metric = d.pop("redistributebgp_metric", UNSET)

        redistributebgp_routemap = d.pop("redistributebgp_routemap", UNSET)

        redistributebgp_distlist = d.pop("redistributebgp_distlist", UNSET)

        redistributeospf = d.pop("redistributeospf", UNSET)

        redistributeospf_metric = d.pop("redistributeospf_metric", UNSET)

        redistributeospf_routemap = d.pop("redistributeospf_routemap", UNSET)

        redistributeospf_distlist = d.pop("redistributeospf_distlist", UNSET)

        redistributestatic = d.pop("redistributestatic", UNSET)

        redistributestatic_metric = d.pop("redistributestatic_metric", UNSET)

        redistributestatic_routemap = d.pop("redistributestatic_routemap", UNSET)

        redistributestatic_distlist = d.pop("redistributestatic_distlist", UNSET)

        redistributedefaultroute = d.pop("redistributedefaultroute", UNSET)

        ripversion = d.pop("ripversion", UNSET)

        inoffsetlist = d.pop("inoffsetlist", UNSET)

        inmetricvalue = d.pop("inmetricvalue", UNSET)

        outoffsetlist = d.pop("outoffsetlist", UNSET)

        outmetricvalue = d.pop("outmetricvalue", UNSET)

        _redistributeconnectedsubnets_routemap_options = d.pop("redistributeconnectedsubnets_routemap_options", UNSET)
        redistributeconnectedsubnets_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributeconnectedsubnets_routemap_options is not UNSET:
            redistributeconnectedsubnets_routemap_options = []
            for (
                redistributeconnectedsubnets_routemap_options_item_data
            ) in _redistributeconnectedsubnets_routemap_options:
                redistributeconnectedsubnets_routemap_options_item = TextValue.from_dict(
                    redistributeconnectedsubnets_routemap_options_item_data
                )

                redistributeconnectedsubnets_routemap_options.append(redistributeconnectedsubnets_routemap_options_item)

        _redistributeconnectedsubnets_distlist_options = d.pop("redistributeconnectedsubnets_distlist_options", UNSET)
        redistributeconnectedsubnets_distlist_options: list[TextValue] | Unset = UNSET
        if _redistributeconnectedsubnets_distlist_options is not UNSET:
            redistributeconnectedsubnets_distlist_options = []
            for (
                redistributeconnectedsubnets_distlist_options_item_data
            ) in _redistributeconnectedsubnets_distlist_options:
                redistributeconnectedsubnets_distlist_options_item = TextValue.from_dict(
                    redistributeconnectedsubnets_distlist_options_item_data
                )

                redistributeconnectedsubnets_distlist_options.append(redistributeconnectedsubnets_distlist_options_item)

        _redistributekernel_routemap_options = d.pop("redistributekernel_routemap_options", UNSET)
        redistributekernel_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributekernel_routemap_options is not UNSET:
            redistributekernel_routemap_options = []
            for redistributekernel_routemap_options_item_data in _redistributekernel_routemap_options:
                redistributekernel_routemap_options_item = TextValue.from_dict(
                    redistributekernel_routemap_options_item_data
                )

                redistributekernel_routemap_options.append(redistributekernel_routemap_options_item)

        _redistributekernel_distlist_options = d.pop("redistributekernel_distlist_options", UNSET)
        redistributekernel_distlist_options: list[TextValue] | Unset = UNSET
        if _redistributekernel_distlist_options is not UNSET:
            redistributekernel_distlist_options = []
            for redistributekernel_distlist_options_item_data in _redistributekernel_distlist_options:
                redistributekernel_distlist_options_item = TextValue.from_dict(
                    redistributekernel_distlist_options_item_data
                )

                redistributekernel_distlist_options.append(redistributekernel_distlist_options_item)

        _redistributebgp_routemap_options = d.pop("redistributebgp_routemap_options", UNSET)
        redistributebgp_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributebgp_routemap_options is not UNSET:
            redistributebgp_routemap_options = []
            for redistributebgp_routemap_options_item_data in _redistributebgp_routemap_options:
                redistributebgp_routemap_options_item = TextValue.from_dict(redistributebgp_routemap_options_item_data)

                redistributebgp_routemap_options.append(redistributebgp_routemap_options_item)

        _redistributebgp_distlist_options = d.pop("redistributebgp_distlist_options", UNSET)
        redistributebgp_distlist_options: list[TextValue] | Unset = UNSET
        if _redistributebgp_distlist_options is not UNSET:
            redistributebgp_distlist_options = []
            for redistributebgp_distlist_options_item_data in _redistributebgp_distlist_options:
                redistributebgp_distlist_options_item = TextValue.from_dict(redistributebgp_distlist_options_item_data)

                redistributebgp_distlist_options.append(redistributebgp_distlist_options_item)

        _redistributeospf_routemap_options = d.pop("redistributeospf_routemap_options", UNSET)
        redistributeospf_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributeospf_routemap_options is not UNSET:
            redistributeospf_routemap_options = []
            for redistributeospf_routemap_options_item_data in _redistributeospf_routemap_options:
                redistributeospf_routemap_options_item = TextValue.from_dict(
                    redistributeospf_routemap_options_item_data
                )

                redistributeospf_routemap_options.append(redistributeospf_routemap_options_item)

        _redistributeospf_distlist_options = d.pop("redistributeospf_distlist_options", UNSET)
        redistributeospf_distlist_options: list[TextValue] | Unset = UNSET
        if _redistributeospf_distlist_options is not UNSET:
            redistributeospf_distlist_options = []
            for redistributeospf_distlist_options_item_data in _redistributeospf_distlist_options:
                redistributeospf_distlist_options_item = TextValue.from_dict(
                    redistributeospf_distlist_options_item_data
                )

                redistributeospf_distlist_options.append(redistributeospf_distlist_options_item)

        _redistributestatic_routemap_options = d.pop("redistributestatic_routemap_options", UNSET)
        redistributestatic_routemap_options: list[TextValue] | Unset = UNSET
        if _redistributestatic_routemap_options is not UNSET:
            redistributestatic_routemap_options = []
            for redistributestatic_routemap_options_item_data in _redistributestatic_routemap_options:
                redistributestatic_routemap_options_item = TextValue.from_dict(
                    redistributestatic_routemap_options_item_data
                )

                redistributestatic_routemap_options.append(redistributestatic_routemap_options_item)

        _redistributestatic_distlist_options = d.pop("redistributestatic_distlist_options", UNSET)
        redistributestatic_distlist_options: list[TextValue] | Unset = UNSET
        if _redistributestatic_distlist_options is not UNSET:
            redistributestatic_distlist_options = []
            for redistributestatic_distlist_options_item_data in _redistributestatic_distlist_options:
                redistributestatic_distlist_options_item = TextValue.from_dict(
                    redistributestatic_distlist_options_item_data
                )

                redistributestatic_distlist_options.append(redistributestatic_distlist_options_item)

        _inoffsetlist_options = d.pop("inoffsetlist_options", UNSET)
        inoffsetlist_options: list[TextValue] | Unset = UNSET
        if _inoffsetlist_options is not UNSET:
            inoffsetlist_options = []
            for inoffsetlist_options_item_data in _inoffsetlist_options:
                inoffsetlist_options_item = TextValue.from_dict(inoffsetlist_options_item_data)

                inoffsetlist_options.append(inoffsetlist_options_item)

        _outoffsetlist_options = d.pop("outoffsetlist_options", UNSET)
        outoffsetlist_options: list[TextValue] | Unset = UNSET
        if _outoffsetlist_options is not UNSET:
            outoffsetlist_options = []
            for outoffsetlist_options_item_data in _outoffsetlist_options:
                outoffsetlist_options_item = TextValue.from_dict(outoffsetlist_options_item_data)

                outoffsetlist_options.append(outoffsetlist_options_item)

        frr_ripd = cls(
            enable=enable,
            row=row,
            redistributeconnectedsubnets=redistributeconnectedsubnets,
            redistributeconnectedsubnets_metric=redistributeconnectedsubnets_metric,
            redistributeconnectedsubnets_routemap=redistributeconnectedsubnets_routemap,
            redistributeconnectedsubnets_distlist=redistributeconnectedsubnets_distlist,
            redistributekernel=redistributekernel,
            redistributekernel_metric=redistributekernel_metric,
            redistributekernel_routemap=redistributekernel_routemap,
            redistributekernel_distlist=redistributekernel_distlist,
            redistributebgp=redistributebgp,
            redistributebgp_metric=redistributebgp_metric,
            redistributebgp_routemap=redistributebgp_routemap,
            redistributebgp_distlist=redistributebgp_distlist,
            redistributeospf=redistributeospf,
            redistributeospf_metric=redistributeospf_metric,
            redistributeospf_routemap=redistributeospf_routemap,
            redistributeospf_distlist=redistributeospf_distlist,
            redistributestatic=redistributestatic,
            redistributestatic_metric=redistributestatic_metric,
            redistributestatic_routemap=redistributestatic_routemap,
            redistributestatic_distlist=redistributestatic_distlist,
            redistributedefaultroute=redistributedefaultroute,
            ripversion=ripversion,
            inoffsetlist=inoffsetlist,
            inmetricvalue=inmetricvalue,
            outoffsetlist=outoffsetlist,
            outmetricvalue=outmetricvalue,
            redistributeconnectedsubnets_routemap_options=redistributeconnectedsubnets_routemap_options,
            redistributeconnectedsubnets_distlist_options=redistributeconnectedsubnets_distlist_options,
            redistributekernel_routemap_options=redistributekernel_routemap_options,
            redistributekernel_distlist_options=redistributekernel_distlist_options,
            redistributebgp_routemap_options=redistributebgp_routemap_options,
            redistributebgp_distlist_options=redistributebgp_distlist_options,
            redistributeospf_routemap_options=redistributeospf_routemap_options,
            redistributeospf_distlist_options=redistributeospf_distlist_options,
            redistributestatic_routemap_options=redistributestatic_routemap_options,
            redistributestatic_distlist_options=redistributestatic_distlist_options,
            inoffsetlist_options=inoffsetlist_options,
            outoffsetlist_options=outoffsetlist_options,
        )

        frr_ripd.additional_properties = d
        return frr_ripd

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
