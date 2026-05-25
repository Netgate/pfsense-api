from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frr_row import FrrRow
    from ..models.text_value import TextValue


T = TypeVar("T", bound="Frr")


@_attrs_define
class Frr:
    """
    Attributes:
        enable (bool | Unset): Enable

            Enable FRR
        routerid (str | Unset): Default Router ID

            Specify the default Router ID. RID is the highest logical (loopback) IP address configured on a router.
            For more information on router identifiers see http://en.wikipedia.org/wiki/Open_Shortest_Path_First.
            Per-daemon configuration will take precedence over this setting.
        password (str | Unset): Master Password

            Password to access the management daemons. Required.
        passwordencrypt (bool | Unset): Encrypt Password

            Enable password encryption service.
        ignoreipsecrestart (bool | Unset): Ignore IPsec Restart

            Ignore IPsec restart events.
            When unchecked, IPsec VTI interfaces will be reset in FRR when IPsec restarts.
            This reset can prevent routes from becoming inactive in the routing table after interface events.
        carpstatusvid (str | Unset): CARP Status IP

            Used to determine the CARP status. When the CARP vhid is in BACKUP status, FRR will not be started.
        logging (bool | Unset): (Logging) Syslog Logging

            If set to yes, FRR daemon Logs will be written via syslog.
        pkgloglevel (str | Unset): (Logging) Package Logging Level (0, 1)

            Set the log level for package scripts
        enablesnmpagentx (bool | Unset): (Modules) Enable SNMP AgentX

            Enable agentx support for accessing FRR Zebra data via SNMP with the net-snmp package.
        row (list[FrrRow] | Unset):
        nht (str | Unset): (Next hop Tracking) Resolve via default route (none, ipv4, ipv6, both)

            By default, next hop tracking does not resolve next hops via the default route. Allowing this behavior can be
            useful, for example, so BGP can peer across the default route.
        carpstatusvid_options (list[TextValue] | Unset):
        routetarget_options (list[TextValue] | Unset):
    """

    enable: bool | Unset = UNSET
    routerid: str | Unset = UNSET
    password: str | Unset = UNSET
    passwordencrypt: bool | Unset = UNSET
    ignoreipsecrestart: bool | Unset = UNSET
    carpstatusvid: str | Unset = UNSET
    logging: bool | Unset = UNSET
    pkgloglevel: str | Unset = UNSET
    enablesnmpagentx: bool | Unset = UNSET
    row: list[FrrRow] | Unset = UNSET
    nht: str | Unset = UNSET
    carpstatusvid_options: list[TextValue] | Unset = UNSET
    routetarget_options: list[TextValue] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        routerid = self.routerid

        password = self.password

        passwordencrypt = self.passwordencrypt

        ignoreipsecrestart = self.ignoreipsecrestart

        carpstatusvid = self.carpstatusvid

        logging = self.logging

        pkgloglevel = self.pkgloglevel

        enablesnmpagentx = self.enablesnmpagentx

        row: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.row, Unset):
            row = []
            for row_item_data in self.row:
                row_item = row_item_data.to_dict()
                row.append(row_item)

        nht = self.nht

        carpstatusvid_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.carpstatusvid_options, Unset):
            carpstatusvid_options = []
            for carpstatusvid_options_item_data in self.carpstatusvid_options:
                carpstatusvid_options_item = carpstatusvid_options_item_data.to_dict()
                carpstatusvid_options.append(carpstatusvid_options_item)

        routetarget_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.routetarget_options, Unset):
            routetarget_options = []
            for routetarget_options_item_data in self.routetarget_options:
                routetarget_options_item = routetarget_options_item_data.to_dict()
                routetarget_options.append(routetarget_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if routerid is not UNSET:
            field_dict["routerid"] = routerid
        if password is not UNSET:
            field_dict["password"] = password
        if passwordencrypt is not UNSET:
            field_dict["passwordencrypt"] = passwordencrypt
        if ignoreipsecrestart is not UNSET:
            field_dict["ignoreipsecrestart"] = ignoreipsecrestart
        if carpstatusvid is not UNSET:
            field_dict["carpstatusvid"] = carpstatusvid
        if logging is not UNSET:
            field_dict["logging"] = logging
        if pkgloglevel is not UNSET:
            field_dict["pkgloglevel"] = pkgloglevel
        if enablesnmpagentx is not UNSET:
            field_dict["enablesnmpagentx"] = enablesnmpagentx
        if row is not UNSET:
            field_dict["row"] = row
        if nht is not UNSET:
            field_dict["nht"] = nht
        if carpstatusvid_options is not UNSET:
            field_dict["carpstatusvid_options"] = carpstatusvid_options
        if routetarget_options is not UNSET:
            field_dict["routetarget_options"] = routetarget_options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frr_row import FrrRow
        from ..models.text_value import TextValue

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        routerid = d.pop("routerid", UNSET)

        password = d.pop("password", UNSET)

        passwordencrypt = d.pop("passwordencrypt", UNSET)

        ignoreipsecrestart = d.pop("ignoreipsecrestart", UNSET)

        carpstatusvid = d.pop("carpstatusvid", UNSET)

        logging = d.pop("logging", UNSET)

        pkgloglevel = d.pop("pkgloglevel", UNSET)

        enablesnmpagentx = d.pop("enablesnmpagentx", UNSET)

        _row = d.pop("row", UNSET)
        row: list[FrrRow] | Unset = UNSET
        if _row is not UNSET:
            row = []
            for row_item_data in _row:
                row_item = FrrRow.from_dict(row_item_data)

                row.append(row_item)

        nht = d.pop("nht", UNSET)

        _carpstatusvid_options = d.pop("carpstatusvid_options", UNSET)
        carpstatusvid_options: list[TextValue] | Unset = UNSET
        if _carpstatusvid_options is not UNSET:
            carpstatusvid_options = []
            for carpstatusvid_options_item_data in _carpstatusvid_options:
                carpstatusvid_options_item = TextValue.from_dict(carpstatusvid_options_item_data)

                carpstatusvid_options.append(carpstatusvid_options_item)

        _routetarget_options = d.pop("routetarget_options", UNSET)
        routetarget_options: list[TextValue] | Unset = UNSET
        if _routetarget_options is not UNSET:
            routetarget_options = []
            for routetarget_options_item_data in _routetarget_options:
                routetarget_options_item = TextValue.from_dict(routetarget_options_item_data)

                routetarget_options.append(routetarget_options_item)

        frr = cls(
            enable=enable,
            routerid=routerid,
            password=password,
            passwordencrypt=passwordencrypt,
            ignoreipsecrestart=ignoreipsecrestart,
            carpstatusvid=carpstatusvid,
            logging=logging,
            pkgloglevel=pkgloglevel,
            enablesnmpagentx=enablesnmpagentx,
            row=row,
            nht=nht,
            carpstatusvid_options=carpstatusvid_options,
            routetarget_options=routetarget_options,
        )

        frr.additional_properties = d
        return frr

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
