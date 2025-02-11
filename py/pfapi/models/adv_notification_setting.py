from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdvNotificationSetting")


@_attrs_define
class AdvNotificationSetting:
    """
    Attributes:
        cert_enable_notify (bool):
        disablebeep (bool):
        disable_smtp (bool):
        enable_pushover (bool):
        enable_telegram (bool):
        smtpssl (bool):
        sslvalidate (bool):
        api (str):
        certexpiredays (int):
        chatid (str):
        pushoverapikey (str):
        pushoverexpire (int):
        pushoverpriority (str):
        pushoverretry (int):
        pushoversound (str):
        pushoveruserkey (str):
        smtpauthmech (str):
        smtpfromaddress (str):
        smtpipaddress (str):
        smtpnotifyemailaddress (str):
        smtppassword (str):
        smtppassword_confirm (str):
        smtpport (str):
        smtptimeout (int):
        smtpusername (str):
        save (bool):
        test_smtp (bool):
        test_telegram (bool):
        test_pushover (bool):
        revoked_cert_ignore_notify (bool):
        enable_slack (bool):
        slack_api (str):
        slack_channel (str):
    """

    cert_enable_notify: bool
    disablebeep: bool
    disable_smtp: bool
    enable_pushover: bool
    enable_telegram: bool
    smtpssl: bool
    sslvalidate: bool
    api: str
    certexpiredays: int
    chatid: str
    pushoverapikey: str
    pushoverexpire: int
    pushoverpriority: str
    pushoverretry: int
    pushoversound: str
    pushoveruserkey: str
    smtpauthmech: str
    smtpfromaddress: str
    smtpipaddress: str
    smtpnotifyemailaddress: str
    smtppassword: str
    smtppassword_confirm: str
    smtpport: str
    smtptimeout: int
    smtpusername: str
    save: bool
    test_smtp: bool
    test_telegram: bool
    test_pushover: bool
    revoked_cert_ignore_notify: bool
    enable_slack: bool
    slack_api: str
    slack_channel: str
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
        field_dict.update(
            {
                "cert_enable_notify": cert_enable_notify,
                "disablebeep": disablebeep,
                "disable_smtp": disable_smtp,
                "enable_pushover": enable_pushover,
                "enable_telegram": enable_telegram,
                "smtpssl": smtpssl,
                "sslvalidate": sslvalidate,
                "api": api,
                "certexpiredays": certexpiredays,
                "chatid": chatid,
                "pushoverapikey": pushoverapikey,
                "pushoverexpire": pushoverexpire,
                "pushoverpriority": pushoverpriority,
                "pushoverretry": pushoverretry,
                "pushoversound": pushoversound,
                "pushoveruserkey": pushoveruserkey,
                "smtpauthmech": smtpauthmech,
                "smtpfromaddress": smtpfromaddress,
                "smtpipaddress": smtpipaddress,
                "smtpnotifyemailaddress": smtpnotifyemailaddress,
                "smtppassword": smtppassword,
                "smtppassword_confirm": smtppassword_confirm,
                "smtpport": smtpport,
                "smtptimeout": smtptimeout,
                "smtpusername": smtpusername,
                "save": save,
                "test_smtp": test_smtp,
                "test_telegram": test_telegram,
                "test_pushover": test_pushover,
                "revoked_cert_ignore_notify": revoked_cert_ignore_notify,
                "enable_slack": enable_slack,
                "slack_api": slack_api,
                "slack_channel": slack_channel,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cert_enable_notify = d.pop("cert_enable_notify")

        disablebeep = d.pop("disablebeep")

        disable_smtp = d.pop("disable_smtp")

        enable_pushover = d.pop("enable_pushover")

        enable_telegram = d.pop("enable_telegram")

        smtpssl = d.pop("smtpssl")

        sslvalidate = d.pop("sslvalidate")

        api = d.pop("api")

        certexpiredays = d.pop("certexpiredays")

        chatid = d.pop("chatid")

        pushoverapikey = d.pop("pushoverapikey")

        pushoverexpire = d.pop("pushoverexpire")

        pushoverpriority = d.pop("pushoverpriority")

        pushoverretry = d.pop("pushoverretry")

        pushoversound = d.pop("pushoversound")

        pushoveruserkey = d.pop("pushoveruserkey")

        smtpauthmech = d.pop("smtpauthmech")

        smtpfromaddress = d.pop("smtpfromaddress")

        smtpipaddress = d.pop("smtpipaddress")

        smtpnotifyemailaddress = d.pop("smtpnotifyemailaddress")

        smtppassword = d.pop("smtppassword")

        smtppassword_confirm = d.pop("smtppassword_confirm")

        smtpport = d.pop("smtpport")

        smtptimeout = d.pop("smtptimeout")

        smtpusername = d.pop("smtpusername")

        save = d.pop("save")

        test_smtp = d.pop("test_smtp")

        test_telegram = d.pop("test_telegram")

        test_pushover = d.pop("test_pushover")

        revoked_cert_ignore_notify = d.pop("revoked_cert_ignore_notify")

        enable_slack = d.pop("enable_slack")

        slack_api = d.pop("slack_api")

        slack_channel = d.pop("slack_channel")

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
