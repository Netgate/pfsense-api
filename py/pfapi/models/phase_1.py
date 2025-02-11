from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.phase_1_encryption import Phase1Encryption


T = TypeVar("T", bound="Phase1")


@_attrs_define
class Phase1:
    """
    Attributes:
        ikeid (str):
        iketype (str):
        interface (str):
        remote_gateway (str):
        protocol (str):
        myid_type (str):
        myid_data (str):
        peerid_type (str):
        peerid_data (str):
        encryption (Phase1Encryption):
        lifetime (int):
        rekey_time (int):
        reauth_time (int):
        rand_time (int):
        pre_shared_key (str):
        private_key (str):
        certref (str):
        pkcs11certref (str):
        pkcs11pin (str):
        caref (str):
        authentication_method (str):
        descr (str):
        nat_traversal (str):
        mobike (str):
        startaction (str):
        closeaction (str):
        dpd_delay (int):
        dpd_maxfail (int):
        prfselect_enable (bool):
        gw_duplicates (bool):
        mobile (bool):
        disabled (bool):
    """

    ikeid: str
    iketype: str
    interface: str
    remote_gateway: str
    protocol: str
    myid_type: str
    myid_data: str
    peerid_type: str
    peerid_data: str
    encryption: "Phase1Encryption"
    lifetime: int
    rekey_time: int
    reauth_time: int
    rand_time: int
    pre_shared_key: str
    private_key: str
    certref: str
    pkcs11certref: str
    pkcs11pin: str
    caref: str
    authentication_method: str
    descr: str
    nat_traversal: str
    mobike: str
    startaction: str
    closeaction: str
    dpd_delay: int
    dpd_maxfail: int
    prfselect_enable: bool
    gw_duplicates: bool
    mobile: bool
    disabled: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ikeid = self.ikeid

        iketype = self.iketype

        interface = self.interface

        remote_gateway = self.remote_gateway

        protocol = self.protocol

        myid_type = self.myid_type

        myid_data = self.myid_data

        peerid_type = self.peerid_type

        peerid_data = self.peerid_data

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ikeid": ikeid,
                "iketype": iketype,
                "interface": interface,
                "remote_gateway": remote_gateway,
                "protocol": protocol,
                "myid_type": myid_type,
                "myid_data": myid_data,
                "peerid_type": peerid_type,
                "peerid_data": peerid_data,
                "encryption": encryption,
                "lifetime": lifetime,
                "rekey_time": rekey_time,
                "reauth_time": reauth_time,
                "rand_time": rand_time,
                "pre_shared_key": pre_shared_key,
                "private_key": private_key,
                "certref": certref,
                "pkcs11certref": pkcs11certref,
                "pkcs11pin": pkcs11pin,
                "caref": caref,
                "authentication_method": authentication_method,
                "descr": descr,
                "nat_traversal": nat_traversal,
                "mobike": mobike,
                "startaction": startaction,
                "closeaction": closeaction,
                "dpd_delay": dpd_delay,
                "dpd_maxfail": dpd_maxfail,
                "prfselect_enable": prfselect_enable,
                "gw_duplicates": gw_duplicates,
                "mobile": mobile,
                "disabled": disabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.phase_1_encryption import Phase1Encryption

        d = src_dict.copy()
        ikeid = d.pop("ikeid")

        iketype = d.pop("iketype")

        interface = d.pop("interface")

        remote_gateway = d.pop("remote_gateway")

        protocol = d.pop("protocol")

        myid_type = d.pop("myid_type")

        myid_data = d.pop("myid_data")

        peerid_type = d.pop("peerid_type")

        peerid_data = d.pop("peerid_data")

        encryption = Phase1Encryption.from_dict(d.pop("encryption"))

        lifetime = d.pop("lifetime")

        rekey_time = d.pop("rekey_time")

        reauth_time = d.pop("reauth_time")

        rand_time = d.pop("rand_time")

        pre_shared_key = d.pop("pre_shared_key")

        private_key = d.pop("private_key")

        certref = d.pop("certref")

        pkcs11certref = d.pop("pkcs11certref")

        pkcs11pin = d.pop("pkcs11pin")

        caref = d.pop("caref")

        authentication_method = d.pop("authentication_method")

        descr = d.pop("descr")

        nat_traversal = d.pop("nat_traversal")

        mobike = d.pop("mobike")

        startaction = d.pop("startaction")

        closeaction = d.pop("closeaction")

        dpd_delay = d.pop("dpd_delay")

        dpd_maxfail = d.pop("dpd_maxfail")

        prfselect_enable = d.pop("prfselect_enable")

        gw_duplicates = d.pop("gw_duplicates")

        mobile = d.pop("mobile")

        disabled = d.pop("disabled")

        phase_1 = cls(
            ikeid=ikeid,
            iketype=iketype,
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
