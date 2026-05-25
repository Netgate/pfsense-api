from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.snort_insp_ftp_server_cmd_validity import SnortInspFtpServerCmdValidity
    from ..models.snort_insp_ftp_server_directory_cmds import SnortInspFtpServerDirectoryCmds


T = TypeVar("T", bound="SnortInspFtpServer")


@_attrs_define
class SnortInspFtpServer:
    """
    Attributes:
        chk_str_fmt (str | Unset): check the formatting of the given commands
        data_chan_cmds (str | Unset): check the formatting of the given commands
        data_rest_cmds (str | Unset): check the formatting of the given commands
        data_xfer_cmds (str | Unset): check the formatting of the given commands
        directory_cmds (list[SnortInspFtpServerDirectoryCmds] | Unset):
        file_put_cmds (str | Unset): check the formatting of the given commands
        file_get_cmds (str | Unset): check the formatting of the given commands
        encr_cmds (str | Unset): check the formatting of the given commands
        login_cmds (str | Unset): check the formatting of the given commands
        check_encrypted (bool | Unset): check for end of encryption; default false
        cmd_validity (list[SnortInspFtpServerCmdValidity] | Unset):
        def_max_param_len (int | Unset): default maximum length of commands handled by server; 0 is unlimited { 1:max32
            }; default 100
        encrypted_traffic (bool | Unset): check for encrypted Telnet and FTP; default false
        ftp_cmds (str | Unset): specify additional commands supported by server beyond RFC 959
        ignore_data_chan (bool | Unset): do not inspect FTP data channels; default false
        ignore_telnet_erase_cmds (bool | Unset): ignore erase character and erase line commands when normalizing;
            default false
        print_cmds (bool | Unset): print command configurations on start up; default false
        telnet_cmds (bool | Unset): detect Telnet escape sequences of FTP control channel; default false
    """

    chk_str_fmt: str | Unset = UNSET
    data_chan_cmds: str | Unset = UNSET
    data_rest_cmds: str | Unset = UNSET
    data_xfer_cmds: str | Unset = UNSET
    directory_cmds: list[SnortInspFtpServerDirectoryCmds] | Unset = UNSET
    file_put_cmds: str | Unset = UNSET
    file_get_cmds: str | Unset = UNSET
    encr_cmds: str | Unset = UNSET
    login_cmds: str | Unset = UNSET
    check_encrypted: bool | Unset = UNSET
    cmd_validity: list[SnortInspFtpServerCmdValidity] | Unset = UNSET
    def_max_param_len: int | Unset = UNSET
    encrypted_traffic: bool | Unset = UNSET
    ftp_cmds: str | Unset = UNSET
    ignore_data_chan: bool | Unset = UNSET
    ignore_telnet_erase_cmds: bool | Unset = UNSET
    print_cmds: bool | Unset = UNSET
    telnet_cmds: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        chk_str_fmt = self.chk_str_fmt

        data_chan_cmds = self.data_chan_cmds

        data_rest_cmds = self.data_rest_cmds

        data_xfer_cmds = self.data_xfer_cmds

        directory_cmds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.directory_cmds, Unset):
            directory_cmds = []
            for directory_cmds_item_data in self.directory_cmds:
                directory_cmds_item = directory_cmds_item_data.to_dict()
                directory_cmds.append(directory_cmds_item)

        file_put_cmds = self.file_put_cmds

        file_get_cmds = self.file_get_cmds

        encr_cmds = self.encr_cmds

        login_cmds = self.login_cmds

        check_encrypted = self.check_encrypted

        cmd_validity: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cmd_validity, Unset):
            cmd_validity = []
            for cmd_validity_item_data in self.cmd_validity:
                cmd_validity_item = cmd_validity_item_data.to_dict()
                cmd_validity.append(cmd_validity_item)

        def_max_param_len = self.def_max_param_len

        encrypted_traffic = self.encrypted_traffic

        ftp_cmds = self.ftp_cmds

        ignore_data_chan = self.ignore_data_chan

        ignore_telnet_erase_cmds = self.ignore_telnet_erase_cmds

        print_cmds = self.print_cmds

        telnet_cmds = self.telnet_cmds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if chk_str_fmt is not UNSET:
            field_dict["chk_str_fmt"] = chk_str_fmt
        if data_chan_cmds is not UNSET:
            field_dict["data_chan_cmds"] = data_chan_cmds
        if data_rest_cmds is not UNSET:
            field_dict["data_rest_cmds"] = data_rest_cmds
        if data_xfer_cmds is not UNSET:
            field_dict["data_xfer_cmds"] = data_xfer_cmds
        if directory_cmds is not UNSET:
            field_dict["directory_cmds"] = directory_cmds
        if file_put_cmds is not UNSET:
            field_dict["file_put_cmds"] = file_put_cmds
        if file_get_cmds is not UNSET:
            field_dict["file_get_cmds"] = file_get_cmds
        if encr_cmds is not UNSET:
            field_dict["encr_cmds"] = encr_cmds
        if login_cmds is not UNSET:
            field_dict["login_cmds"] = login_cmds
        if check_encrypted is not UNSET:
            field_dict["check_encrypted"] = check_encrypted
        if cmd_validity is not UNSET:
            field_dict["cmd_validity"] = cmd_validity
        if def_max_param_len is not UNSET:
            field_dict["def_max_param_len"] = def_max_param_len
        if encrypted_traffic is not UNSET:
            field_dict["encrypted_traffic"] = encrypted_traffic
        if ftp_cmds is not UNSET:
            field_dict["ftp_cmds"] = ftp_cmds
        if ignore_data_chan is not UNSET:
            field_dict["ignore_data_chan"] = ignore_data_chan
        if ignore_telnet_erase_cmds is not UNSET:
            field_dict["ignore_telnet_erase_cmds"] = ignore_telnet_erase_cmds
        if print_cmds is not UNSET:
            field_dict["print_cmds"] = print_cmds
        if telnet_cmds is not UNSET:
            field_dict["telnet_cmds"] = telnet_cmds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snort_insp_ftp_server_cmd_validity import SnortInspFtpServerCmdValidity
        from ..models.snort_insp_ftp_server_directory_cmds import SnortInspFtpServerDirectoryCmds

        d = dict(src_dict)
        chk_str_fmt = d.pop("chk_str_fmt", UNSET)

        data_chan_cmds = d.pop("data_chan_cmds", UNSET)

        data_rest_cmds = d.pop("data_rest_cmds", UNSET)

        data_xfer_cmds = d.pop("data_xfer_cmds", UNSET)

        _directory_cmds = d.pop("directory_cmds", UNSET)
        directory_cmds: list[SnortInspFtpServerDirectoryCmds] | Unset = UNSET
        if _directory_cmds is not UNSET:
            directory_cmds = []
            for directory_cmds_item_data in _directory_cmds:
                directory_cmds_item = SnortInspFtpServerDirectoryCmds.from_dict(directory_cmds_item_data)

                directory_cmds.append(directory_cmds_item)

        file_put_cmds = d.pop("file_put_cmds", UNSET)

        file_get_cmds = d.pop("file_get_cmds", UNSET)

        encr_cmds = d.pop("encr_cmds", UNSET)

        login_cmds = d.pop("login_cmds", UNSET)

        check_encrypted = d.pop("check_encrypted", UNSET)

        _cmd_validity = d.pop("cmd_validity", UNSET)
        cmd_validity: list[SnortInspFtpServerCmdValidity] | Unset = UNSET
        if _cmd_validity is not UNSET:
            cmd_validity = []
            for cmd_validity_item_data in _cmd_validity:
                cmd_validity_item = SnortInspFtpServerCmdValidity.from_dict(cmd_validity_item_data)

                cmd_validity.append(cmd_validity_item)

        def_max_param_len = d.pop("def_max_param_len", UNSET)

        encrypted_traffic = d.pop("encrypted_traffic", UNSET)

        ftp_cmds = d.pop("ftp_cmds", UNSET)

        ignore_data_chan = d.pop("ignore_data_chan", UNSET)

        ignore_telnet_erase_cmds = d.pop("ignore_telnet_erase_cmds", UNSET)

        print_cmds = d.pop("print_cmds", UNSET)

        telnet_cmds = d.pop("telnet_cmds", UNSET)

        snort_insp_ftp_server = cls(
            chk_str_fmt=chk_str_fmt,
            data_chan_cmds=data_chan_cmds,
            data_rest_cmds=data_rest_cmds,
            data_xfer_cmds=data_xfer_cmds,
            directory_cmds=directory_cmds,
            file_put_cmds=file_put_cmds,
            file_get_cmds=file_get_cmds,
            encr_cmds=encr_cmds,
            login_cmds=login_cmds,
            check_encrypted=check_encrypted,
            cmd_validity=cmd_validity,
            def_max_param_len=def_max_param_len,
            encrypted_traffic=encrypted_traffic,
            ftp_cmds=ftp_cmds,
            ignore_data_chan=ignore_data_chan,
            ignore_telnet_erase_cmds=ignore_telnet_erase_cmds,
            print_cmds=print_cmds,
            telnet_cmds=telnet_cmds,
        )

        snort_insp_ftp_server.additional_properties = d
        return snort_insp_ftp_server

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
