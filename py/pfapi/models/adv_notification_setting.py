from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvNotificationSetting")


@_attrs_define
class AdvNotificationSetting:
    """
    Attributes:
        cert_enable_notify (Union[Unset, bool]):
        disablebeep (Union[Unset, bool]):
        disable_smtp (Union[Unset, bool]):
        enable_pushover (Union[Unset, bool]):
        enable_telegram (Union[Unset, bool]):
        smtpssl (Union[Unset, bool]):
        sslvalidate (Union[Unset, bool]):
        api (Union[Unset, str]):
        certexpiredays (Union[Unset, int]):
        chatid (Union[Unset, str]):
        pushoverapikey (Union[Unset, str]):
        pushoverexpire (Union[Unset, int]):
        pushoverpriority (Union[Unset, str]):
        pushoverretry (Union[Unset, int]):
        pushoversound (Union[Unset, str]):
        pushoveruserkey (Union[Unset, str]):
        smtpauthmech (Union[Unset, str]):
        smtpfromaddress (Union[Unset, str]):
        smtpipaddress (Union[Unset, str]):
        smtpnotifyemailaddress (Union[Unset, str]):
        smtppassword (Union[Unset, str]):
        smtppassword_confirm (Union[Unset, str]):
        smtpport (Union[Unset, str]):
        smtptimeout (Union[Unset, int]):
        smtpusername (Union[Unset, str]):
        save (Union[Unset, bool]):
        test_smtp (Union[Unset, bool]):
        test_telegram (Union[Unset, bool]):
        test_pushover (Union[Unset, bool]):
        revoked_cert_ignore_notify (Union[Unset, bool]):
        enable_slack (Union[Unset, bool]):
        slack_api (Union[Unset, str]):
        slack_channel (Union[Unset, str]):
    """

    cert_enable_notify: Union[Unset, bool] = UNSET
    disablebeep: Union[Unset, bool] = UNSET
    disable_smtp: Union[Unset, bool] = UNSET
    enable_pushover: Union[Unset, bool] = UNSET
    enable_telegram: Union[Unset, bool] = UNSET
    smtpssl: Union[Unset, bool] = UNSET
    sslvalidate: Union[Unset, bool] = UNSET
    api: Union[Unset, str] = UNSET
    certexpiredays: Union[Unset, int] = UNSET
    chatid: Union[Unset, str] = UNSET
    pushoverapikey: Union[Unset, str] = UNSET
    pushoverexpire: Union[Unset, int] = UNSET
    pushoverpriority: Union[Unset, str] = UNSET
    pushoverretry: Union[Unset, int] = UNSET
    pushoversound: Union[Unset, str] = UNSET
    pushoveruserkey: Union[Unset, str] = UNSET
    smtpauthmech: Union[Unset, str] = UNSET
    smtpfromaddress: Union[Unset, str] = UNSET
    smtpipaddress: Union[Unset, str] = UNSET
    smtpnotifyemailaddress: Union[Unset, str] = UNSET
    smtppassword: Union[Unset, str] = UNSET
    smtppassword_confirm: Union[Unset, str] = UNSET
    smtpport: Union[Unset, str] = UNSET
    smtptimeout: Union[Unset, int] = UNSET
    smtpusername: Union[Unset, str] = UNSET
    save: Union[Unset, bool] = UNSET
    test_smtp: Union[Unset, bool] = UNSET
    test_telegram: Union[Unset, bool] = UNSET
    test_pushover: Union[Unset, bool] = UNSET
    revoked_cert_ignore_notify: Union[Unset, bool] = UNSET
    enable_slack: Union[Unset, bool] = UNSET
    slack_api: Union[Unset, str] = UNSET
    slack_channel: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cert_enable_notify = self.cert_enable_notify

        disablebeep = self.disablebeep

        disable_smtp = self.disable_smtp

        enable_pushover = self.enable_pushover

        enable_telegram = self.enable_telegram

        smtpssl = self.smtpssl

        sslvalidate = self.sslvalidate

        api = self.api

        certexpiredays = self.certexpiredays

        chatid = self.chatid

        pushoverapikey = self.pushoverapikey

        pushoverexpire = self.pushoverexpire

        pushoverpriority = self.pushoverpriority

        pushoverretry = self.pushoverretry

        pushoversound = self.pushoversound

        pushoveruserkey = self.pushoveruserkey

        smtpauthmech = self.smtpauthmech

        smtpfromaddress = self.smtpfromaddress

        smtpipaddress = self.smtpipaddress

        smtpnotifyemailaddress = self.smtpnotifyemailaddress

        smtppassword = self.smtppassword

        smtppassword_confirm = self.smtppassword_confirm

        smtpport = self.smtpport

        smtptimeout = self.smtptimeout

        smtpusername = self.smtpusername

        save = self.save

        test_smtp = self.test_smtp

        test_telegram = self.test_telegram

        test_pushover = self.test_pushover

        revoked_cert_ignore_notify = self.revoked_cert_ignore_notify

        enable_slack = self.enable_slack

        slack_api = self.slack_api

        slack_channel = self.slack_channel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert_enable_notify is not UNSET:
            field_dict["cert_enable_notify"] = cert_enable_notify
        if disablebeep is not UNSET:
            field_dict["disablebeep"] = disablebeep
        if disable_smtp is not UNSET:
            field_dict["disable_smtp"] = disable_smtp
        if enable_pushover is not UNSET:
            field_dict["enable_pushover"] = enable_pushover
        if enable_telegram is not UNSET:
            field_dict["enable_telegram"] = enable_telegram
        if smtpssl is not UNSET:
            field_dict["smtpssl"] = smtpssl
        if sslvalidate is not UNSET:
            field_dict["sslvalidate"] = sslvalidate
        if api is not UNSET:
            field_dict["api"] = api
        if certexpiredays is not UNSET:
            field_dict["certexpiredays"] = certexpiredays
        if chatid is not UNSET:
            field_dict["chatid"] = chatid
        if pushoverapikey is not UNSET:
            field_dict["pushoverapikey"] = pushoverapikey
        if pushoverexpire is not UNSET:
            field_dict["pushoverexpire"] = pushoverexpire
        if pushoverpriority is not UNSET:
            field_dict["pushoverpriority"] = pushoverpriority
        if pushoverretry is not UNSET:
            field_dict["pushoverretry"] = pushoverretry
        if pushoversound is not UNSET:
            field_dict["pushoversound"] = pushoversound
        if pushoveruserkey is not UNSET:
            field_dict["pushoveruserkey"] = pushoveruserkey
        if smtpauthmech is not UNSET:
            field_dict["smtpauthmech"] = smtpauthmech
        if smtpfromaddress is not UNSET:
            field_dict["smtpfromaddress"] = smtpfromaddress
        if smtpipaddress is not UNSET:
            field_dict["smtpipaddress"] = smtpipaddress
        if smtpnotifyemailaddress is not UNSET:
            field_dict["smtpnotifyemailaddress"] = smtpnotifyemailaddress
        if smtppassword is not UNSET:
            field_dict["smtppassword"] = smtppassword
        if smtppassword_confirm is not UNSET:
            field_dict["smtppassword_confirm"] = smtppassword_confirm
        if smtpport is not UNSET:
            field_dict["smtpport"] = smtpport
        if smtptimeout is not UNSET:
            field_dict["smtptimeout"] = smtptimeout
        if smtpusername is not UNSET:
            field_dict["smtpusername"] = smtpusername
        if save is not UNSET:
            field_dict["save"] = save
        if test_smtp is not UNSET:
            field_dict["test_smtp"] = test_smtp
        if test_telegram is not UNSET:
            field_dict["test_telegram"] = test_telegram
        if test_pushover is not UNSET:
            field_dict["test_pushover"] = test_pushover
        if revoked_cert_ignore_notify is not UNSET:
            field_dict["revoked_cert_ignore_notify"] = revoked_cert_ignore_notify
        if enable_slack is not UNSET:
            field_dict["enable_slack"] = enable_slack
        if slack_api is not UNSET:
            field_dict["slack_api"] = slack_api
        if slack_channel is not UNSET:
            field_dict["slack_channel"] = slack_channel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cert_enable_notify = d.pop("cert_enable_notify", UNSET)

        disablebeep = d.pop("disablebeep", UNSET)

        disable_smtp = d.pop("disable_smtp", UNSET)

        enable_pushover = d.pop("enable_pushover", UNSET)

        enable_telegram = d.pop("enable_telegram", UNSET)

        smtpssl = d.pop("smtpssl", UNSET)

        sslvalidate = d.pop("sslvalidate", UNSET)

        api = d.pop("api", UNSET)

        certexpiredays = d.pop("certexpiredays", UNSET)

        chatid = d.pop("chatid", UNSET)

        pushoverapikey = d.pop("pushoverapikey", UNSET)

        pushoverexpire = d.pop("pushoverexpire", UNSET)

        pushoverpriority = d.pop("pushoverpriority", UNSET)

        pushoverretry = d.pop("pushoverretry", UNSET)

        pushoversound = d.pop("pushoversound", UNSET)

        pushoveruserkey = d.pop("pushoveruserkey", UNSET)

        smtpauthmech = d.pop("smtpauthmech", UNSET)

        smtpfromaddress = d.pop("smtpfromaddress", UNSET)

        smtpipaddress = d.pop("smtpipaddress", UNSET)

        smtpnotifyemailaddress = d.pop("smtpnotifyemailaddress", UNSET)

        smtppassword = d.pop("smtppassword", UNSET)

        smtppassword_confirm = d.pop("smtppassword_confirm", UNSET)

        smtpport = d.pop("smtpport", UNSET)

        smtptimeout = d.pop("smtptimeout", UNSET)

        smtpusername = d.pop("smtpusername", UNSET)

        save = d.pop("save", UNSET)

        test_smtp = d.pop("test_smtp", UNSET)

        test_telegram = d.pop("test_telegram", UNSET)

        test_pushover = d.pop("test_pushover", UNSET)

        revoked_cert_ignore_notify = d.pop("revoked_cert_ignore_notify", UNSET)

        enable_slack = d.pop("enable_slack", UNSET)

        slack_api = d.pop("slack_api", UNSET)

        slack_channel = d.pop("slack_channel", UNSET)

        adv_notification_setting = cls(
            cert_enable_notify=cert_enable_notify,
            disablebeep=disablebeep,
            disable_smtp=disable_smtp,
            enable_pushover=enable_pushover,
            enable_telegram=enable_telegram,
            smtpssl=smtpssl,
            sslvalidate=sslvalidate,
            api=api,
            certexpiredays=certexpiredays,
            chatid=chatid,
            pushoverapikey=pushoverapikey,
            pushoverexpire=pushoverexpire,
            pushoverpriority=pushoverpriority,
            pushoverretry=pushoverretry,
            pushoversound=pushoversound,
            pushoveruserkey=pushoveruserkey,
            smtpauthmech=smtpauthmech,
            smtpfromaddress=smtpfromaddress,
            smtpipaddress=smtpipaddress,
            smtpnotifyemailaddress=smtpnotifyemailaddress,
            smtppassword=smtppassword,
            smtppassword_confirm=smtppassword_confirm,
            smtpport=smtpport,
            smtptimeout=smtptimeout,
            smtpusername=smtpusername,
            save=save,
            test_smtp=test_smtp,
            test_telegram=test_telegram,
            test_pushover=test_pushover,
            revoked_cert_ignore_notify=revoked_cert_ignore_notify,
            enable_slack=enable_slack,
            slack_api=slack_api,
            slack_channel=slack_channel,
        )

        adv_notification_setting.additional_properties = d
        return adv_notification_setting

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
