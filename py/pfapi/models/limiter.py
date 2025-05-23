from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.limiter_aqm import LimiterAqm
from ..models.limiter_mask import LimiterMask
from ..models.limiter_sched import LimiterSched
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.limiter_bandwidth import LimiterBandwidth
    from ..models.limiter_queue import LimiterQueue


T = TypeVar("T", bound="Limiter")


@_attrs_define
class Limiter:
    """
    Attributes:
        name (str): name of the limiter, it will appear for selection on firewall rules
        enabled (Union[Unset, bool]):
        number (Union[Unset, int]): generated by system when create limiter
        bandwidth (Union[Unset, List['LimiterBandwidth']]):
        mask (Union[Unset, LimiterMask]): controls how the limiter will mask addresses in the limiter
            valid values = none, srcaddress, dstaddress
        maskbits (Union[Unset, int]): address masking for ipv4
        maskbitsv6 (Union[Unset, int]): address masking for ipv6
        description (Union[Unset, str]):
        aqm (Union[Unset, LimiterAqm]): active queue management (AQM) algorithm
            valid values = droptail, codel, pie, red, gred
        sched (Union[Unset, LimiterSched]): scheduler manages the sequence of network packets in the limiter's queue
            valid values = wf2q+, fifo, qfq, rr, prio, fq_codel, fq_pie
        qlimit (Union[Unset, int]): specifies the length of the limiter's queue, which the scheduler and AQM are
            responsible for
        ecn (Union[Unset, bool]): explicit congestion Notification (ECN) sets a reserved TCP flag when the queue is
            nearing or exceeding capacity
        delay (Union[Unset, int]): introduces an artificial delay (latency), specified in milliseconds
        plr (Union[Unset, float]): packet loss rate can be configured to drop a certain fraction of packets that enter
            the limiter
            valid value between 0 and 1
            a value of 0.001 means one packet in 1000 gets dropped
        buckets (Union[Unset, int]): bucket Size, specified in slots, sets the size of the hash table used for queue
            storage
        queue (Union[Unset, List['LimiterQueue']]):
    """

    name: str
    enabled: Union[Unset, bool] = UNSET
    number: Union[Unset, int] = UNSET
    bandwidth: Union[Unset, List["LimiterBandwidth"]] = UNSET
    mask: Union[Unset, LimiterMask] = UNSET
    maskbits: Union[Unset, int] = UNSET
    maskbitsv6: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    aqm: Union[Unset, LimiterAqm] = UNSET
    sched: Union[Unset, LimiterSched] = UNSET
    qlimit: Union[Unset, int] = UNSET
    ecn: Union[Unset, bool] = UNSET
    delay: Union[Unset, int] = UNSET
    plr: Union[Unset, float] = UNSET
    buckets: Union[Unset, int] = UNSET
    queue: Union[Unset, List["LimiterQueue"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        enabled = self.enabled

        number = self.number

        bandwidth: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bandwidth, Unset):
            bandwidth = []
            for bandwidth_item_data in self.bandwidth:
                bandwidth_item = bandwidth_item_data.to_dict()
                bandwidth.append(bandwidth_item)

        mask: Union[Unset, str] = UNSET
        if not isinstance(self.mask, Unset):
            mask = self.mask.value

        maskbits = self.maskbits

        maskbitsv6 = self.maskbitsv6

        description = self.description

        aqm: Union[Unset, str] = UNSET
        if not isinstance(self.aqm, Unset):
            aqm = self.aqm.value

        sched: Union[Unset, str] = UNSET
        if not isinstance(self.sched, Unset):
            sched = self.sched.value

        qlimit = self.qlimit

        ecn = self.ecn

        delay = self.delay

        plr = self.plr

        buckets = self.buckets

        queue: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.queue, Unset):
            queue = []
            for queue_item_data in self.queue:
                queue_item = queue_item_data.to_dict()
                queue.append(queue_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if number is not UNSET:
            field_dict["number"] = number
        if bandwidth is not UNSET:
            field_dict["bandwidth"] = bandwidth
        if mask is not UNSET:
            field_dict["mask"] = mask
        if maskbits is not UNSET:
            field_dict["maskbits"] = maskbits
        if maskbitsv6 is not UNSET:
            field_dict["maskbitsv6"] = maskbitsv6
        if description is not UNSET:
            field_dict["description"] = description
        if aqm is not UNSET:
            field_dict["aqm"] = aqm
        if sched is not UNSET:
            field_dict["sched"] = sched
        if qlimit is not UNSET:
            field_dict["qlimit"] = qlimit
        if ecn is not UNSET:
            field_dict["ecn"] = ecn
        if delay is not UNSET:
            field_dict["delay"] = delay
        if plr is not UNSET:
            field_dict["plr"] = plr
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if queue is not UNSET:
            field_dict["queue"] = queue

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.limiter_bandwidth import LimiterBandwidth
        from ..models.limiter_queue import LimiterQueue

        d = src_dict.copy()
        name = d.pop("name")

        enabled = d.pop("enabled", UNSET)

        number = d.pop("number", UNSET)

        bandwidth = []
        _bandwidth = d.pop("bandwidth", UNSET)
        for bandwidth_item_data in _bandwidth or []:
            bandwidth_item = LimiterBandwidth.from_dict(bandwidth_item_data)

            bandwidth.append(bandwidth_item)

        _mask = d.pop("mask", UNSET)
        mask: Union[Unset, LimiterMask]
        if isinstance(_mask, Unset):
            mask = UNSET
        else:
            mask = LimiterMask(_mask)

        maskbits = d.pop("maskbits", UNSET)

        maskbitsv6 = d.pop("maskbitsv6", UNSET)

        description = d.pop("description", UNSET)

        _aqm = d.pop("aqm", UNSET)
        aqm: Union[Unset, LimiterAqm]
        if isinstance(_aqm, Unset):
            aqm = UNSET
        else:
            aqm = LimiterAqm(_aqm)

        _sched = d.pop("sched", UNSET)
        sched: Union[Unset, LimiterSched]
        if isinstance(_sched, Unset):
            sched = UNSET
        else:
            sched = LimiterSched(_sched)

        qlimit = d.pop("qlimit", UNSET)

        ecn = d.pop("ecn", UNSET)

        delay = d.pop("delay", UNSET)

        plr = d.pop("plr", UNSET)

        buckets = d.pop("buckets", UNSET)

        queue = []
        _queue = d.pop("queue", UNSET)
        for queue_item_data in _queue or []:
            queue_item = LimiterQueue.from_dict(queue_item_data)

            queue.append(queue_item)

        limiter = cls(
            name=name,
            enabled=enabled,
            number=number,
            bandwidth=bandwidth,
            mask=mask,
            maskbits=maskbits,
            maskbitsv6=maskbitsv6,
            description=description,
            aqm=aqm,
            sched=sched,
            qlimit=qlimit,
            ecn=ecn,
            delay=delay,
            plr=plr,
            buckets=buckets,
            queue=queue,
        )

        limiter.additional_properties = d
        return limiter

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
