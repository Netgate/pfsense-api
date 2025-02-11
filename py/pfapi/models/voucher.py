from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.voucher_roll import VoucherRoll


T = TypeVar("T", bound="Voucher")


@_attrs_define
class Voucher:
    """
    Attributes:
        charset (str):
        rollbits (int):
        ticketbits (int):
        checksumbits (int):
        magic (int):
        exponent (int):
        publickey (str):
        privatekey (str):
        descrmsgnoaccess (str):
        descrmsgexpired (str):
        enable (bool):
        roll (Union[Unset, List['VoucherRoll']]):
    """

    charset: str
    rollbits: int
    ticketbits: int
    checksumbits: int
    magic: int
    exponent: int
    publickey: str
    privatekey: str
    descrmsgnoaccess: str
    descrmsgexpired: str
    enable: bool
    roll: Union[Unset, List["VoucherRoll"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        charset = self.charset

        rollbits = self.rollbits

        ticketbits = self.ticketbits

        checksumbits = self.checksumbits

        magic = self.magic

        exponent = self.exponent

        publickey = self.publickey

        privatekey = self.privatekey

        descrmsgnoaccess = self.descrmsgnoaccess

        descrmsgexpired = self.descrmsgexpired

        enable = self.enable

        roll: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roll, Unset):
            roll = []
            for roll_item_data in self.roll:
                roll_item = roll_item_data.to_dict()
                roll.append(roll_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "charset": charset,
                "rollbits": rollbits,
                "ticketbits": ticketbits,
                "checksumbits": checksumbits,
                "magic": magic,
                "exponent": exponent,
                "publickey": publickey,
                "privatekey": privatekey,
                "descrmsgnoaccess": descrmsgnoaccess,
                "descrmsgexpired": descrmsgexpired,
                "enable": enable,
            }
        )
        if roll is not UNSET:
            field_dict["roll"] = roll

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.voucher_roll import VoucherRoll

        d = src_dict.copy()
        charset = d.pop("charset")

        rollbits = d.pop("rollbits")

        ticketbits = d.pop("ticketbits")

        checksumbits = d.pop("checksumbits")

        magic = d.pop("magic")

        exponent = d.pop("exponent")

        publickey = d.pop("publickey")

        privatekey = d.pop("privatekey")

        descrmsgnoaccess = d.pop("descrmsgnoaccess")

        descrmsgexpired = d.pop("descrmsgexpired")

        enable = d.pop("enable")

        roll = []
        _roll = d.pop("roll", UNSET)
        for roll_item_data in _roll or []:
            roll_item = VoucherRoll.from_dict(roll_item_data)

            roll.append(roll_item)

        voucher = cls(
            charset=charset,
            rollbits=rollbits,
            ticketbits=ticketbits,
            checksumbits=checksumbits,
            magic=magic,
            exponent=exponent,
            publickey=publickey,
            privatekey=privatekey,
            descrmsgnoaccess=descrmsgnoaccess,
            descrmsgexpired=descrmsgexpired,
            enable=enable,
            roll=roll,
        )

        voucher.additional_properties = d
        return voucher

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
