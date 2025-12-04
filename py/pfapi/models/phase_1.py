from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.phase_1_encryption import Phase1Encryption


T = TypeVar("T", bound="Phase1")


@_attrs_define
class Phase1:
    """
    Attributes:
        iketype (str):
        ikeid (str | Unset):
        interface (str | Unset):
        remote_gateway (str | Unset):
        protocol (str | Unset):
        myid_type (str | Unset):
        myid_data (str | Unset):
        peerid_type (str | Unset):
        peerid_data (str | Unset):
        encryption (Phase1Encryption | Unset):
        lifetime (int | Unset):
        rekey_time (int | Unset):
        reauth_time (int | Unset):
        rand_time (int | Unset):
        pre_shared_key (str | Unset):
        private_key (str | Unset):
        certref (str | Unset):
        pkcs11certref (str | Unset):
        pkcs11pin (str | Unset):
        caref (str | Unset):
        authentication_method (str | Unset):
        descr (str | Unset):
        nat_traversal (str | Unset):
        mobike (str | Unset):
        startaction (str | Unset):
        closeaction (str | Unset):
        dpd_delay (int | Unset):
        dpd_maxfail (int | Unset):
        prfselect_enable (bool | Unset):
        gw_duplicates (bool | Unset):
        mobile (bool | Unset):
        disabled (bool | Unset):
    """

    iketype: str
    ikeid: str | Unset = UNSET
    interface: str | Unset = UNSET
    remote_gateway: str | Unset = UNSET
    protocol: str | Unset = UNSET
    myid_type: str | Unset = UNSET
    myid_data: str | Unset = UNSET
    peerid_type: str | Unset = UNSET
    peerid_data: str | Unset = UNSET
    encryption: Phase1Encryption | Unset = UNSET
    lifetime: int | Unset = UNSET
    rekey_time: int | Unset = UNSET
    reauth_time: int | Unset = UNSET
    rand_time: int | Unset = UNSET
    pre_shared_key: str | Unset = UNSET
    private_key: str | Unset = UNSET
    certref: str | Unset = UNSET
    pkcs11certref: str | Unset = UNSET
    pkcs11pin: str | Unset = UNSET
    caref: str | Unset = UNSET
    authentication_method: str | Unset = UNSET
    descr: str | Unset = UNSET
    nat_traversal: str | Unset = UNSET
    mobike: str | Unset = UNSET
    startaction: str | Unset = UNSET
    closeaction: str | Unset = UNSET
    dpd_delay: int | Unset = UNSET
    dpd_maxfail: int | Unset = UNSET
    prfselect_enable: bool | Unset = UNSET
    gw_duplicates: bool | Unset = UNSET
    mobile: bool | Unset = UNSET
    disabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        iketype = self.iketype

        ikeid = self.ikeid

        interface = self.interface

        remote_gateway = self.remote_gateway

        protocol = self.protocol

        myid_type = self.myid_type

        myid_data = self.myid_data

        peerid_type = self.peerid_type

        peerid_data = self.peerid_data

        encryption: dict[str, Any] | Unset = UNSET
        if not isinstance(self.encryption, Unset):
            encryption = self.encryption.to_dict()

        lifetime = self.lifetime

        rekey_time = self.rekey_time

        reauth_time = self.reauth_time

        rand_time = self.rand_time

        pre_shared_key = self.pre_shared_key

        private_key = self.private_key

        certref = self.certref

        pkcs11certref = self.pkcs11certref

        pkcs11pin = self.pkcs11pin

        caref = self.caref

        authentication_method = self.authentication_method

        descr = self.descr

        nat_traversal = self.nat_traversal

        mobike = self.mobike

        startaction = self.startaction

        closeaction = self.closeaction

        dpd_delay = self.dpd_delay

        dpd_maxfail = self.dpd_maxfail

        prfselect_enable = self.prfselect_enable

        gw_duplicates = self.gw_duplicates

        mobile = self.mobile

        disabled = self.disabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "iketype": iketype,
            }
        )
        if ikeid is not UNSET:
            field_dict["ikeid"] = ikeid
        if interface is not UNSET:
            field_dict["interface"] = interface
        if remote_gateway is not UNSET:
            field_dict["remote_gateway"] = remote_gateway
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if myid_type is not UNSET:
            field_dict["myid_type"] = myid_type
        if myid_data is not UNSET:
            field_dict["myid_data"] = myid_data
        if peerid_type is not UNSET:
            field_dict["peerid_type"] = peerid_type
        if peerid_data is not UNSET:
            field_dict["peerid_data"] = peerid_data
        if encryption is not UNSET:
            field_dict["encryption"] = encryption
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if rekey_time is not UNSET:
            field_dict["rekey_time"] = rekey_time
        if reauth_time is not UNSET:
            field_dict["reauth_time"] = reauth_time
        if rand_time is not UNSET:
            field_dict["rand_time"] = rand_time
        if pre_shared_key is not UNSET:
            field_dict["pre_shared_key"] = pre_shared_key
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if certref is not UNSET:
            field_dict["certref"] = certref
        if pkcs11certref is not UNSET:
            field_dict["pkcs11certref"] = pkcs11certref
        if pkcs11pin is not UNSET:
            field_dict["pkcs11pin"] = pkcs11pin
        if caref is not UNSET:
            field_dict["caref"] = caref
        if authentication_method is not UNSET:
            field_dict["authentication_method"] = authentication_method
        if descr is not UNSET:
            field_dict["descr"] = descr
        if nat_traversal is not UNSET:
            field_dict["nat_traversal"] = nat_traversal
        if mobike is not UNSET:
            field_dict["mobike"] = mobike
        if startaction is not UNSET:
            field_dict["startaction"] = startaction
        if closeaction is not UNSET:
            field_dict["closeaction"] = closeaction
        if dpd_delay is not UNSET:
            field_dict["dpd_delay"] = dpd_delay
        if dpd_maxfail is not UNSET:
            field_dict["dpd_maxfail"] = dpd_maxfail
        if prfselect_enable is not UNSET:
            field_dict["prfselect_enable"] = prfselect_enable
        if gw_duplicates is not UNSET:
            field_dict["gw_duplicates"] = gw_duplicates
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.phase_1_encryption import Phase1Encryption

        d = dict(src_dict)
        iketype = d.pop("iketype")

        ikeid = d.pop("ikeid", UNSET)

        interface = d.pop("interface", UNSET)

        remote_gateway = d.pop("remote_gateway", UNSET)

        protocol = d.pop("protocol", UNSET)

        myid_type = d.pop("myid_type", UNSET)

        myid_data = d.pop("myid_data", UNSET)

        peerid_type = d.pop("peerid_type", UNSET)

        peerid_data = d.pop("peerid_data", UNSET)

        _encryption = d.pop("encryption", UNSET)
        encryption: Phase1Encryption | Unset
        if isinstance(_encryption, Unset):
            encryption = UNSET
        else:
            encryption = Phase1Encryption.from_dict(_encryption)

        lifetime = d.pop("lifetime", UNSET)

        rekey_time = d.pop("rekey_time", UNSET)

        reauth_time = d.pop("reauth_time", UNSET)

        rand_time = d.pop("rand_time", UNSET)

        pre_shared_key = d.pop("pre_shared_key", UNSET)

        private_key = d.pop("private_key", UNSET)

        certref = d.pop("certref", UNSET)

        pkcs11certref = d.pop("pkcs11certref", UNSET)

        pkcs11pin = d.pop("pkcs11pin", UNSET)

        caref = d.pop("caref", UNSET)

        authentication_method = d.pop("authentication_method", UNSET)

        descr = d.pop("descr", UNSET)

        nat_traversal = d.pop("nat_traversal", UNSET)

        mobike = d.pop("mobike", UNSET)

        startaction = d.pop("startaction", UNSET)

        closeaction = d.pop("closeaction", UNSET)

        dpd_delay = d.pop("dpd_delay", UNSET)

        dpd_maxfail = d.pop("dpd_maxfail", UNSET)

        prfselect_enable = d.pop("prfselect_enable", UNSET)

        gw_duplicates = d.pop("gw_duplicates", UNSET)

        mobile = d.pop("mobile", UNSET)

        disabled = d.pop("disabled", UNSET)

        phase_1 = cls(
            iketype=iketype,
            ikeid=ikeid,
            interface=interface,
            remote_gateway=remote_gateway,
            protocol=protocol,
            myid_type=myid_type,
            myid_data=myid_data,
            peerid_type=peerid_type,
            peerid_data=peerid_data,
            encryption=encryption,
            lifetime=lifetime,
            rekey_time=rekey_time,
            reauth_time=reauth_time,
            rand_time=rand_time,
            pre_shared_key=pre_shared_key,
            private_key=private_key,
            certref=certref,
            pkcs11certref=pkcs11certref,
            pkcs11pin=pkcs11pin,
            caref=caref,
            authentication_method=authentication_method,
            descr=descr,
            nat_traversal=nat_traversal,
            mobike=mobike,
            startaction=startaction,
            closeaction=closeaction,
            dpd_delay=dpd_delay,
            dpd_maxfail=dpd_maxfail,
            prfselect_enable=prfselect_enable,
            gw_duplicates=gw_duplicates,
            mobile=mobile,
            disabled=disabled,
        )

        phase_1.additional_properties = d
        return phase_1

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
