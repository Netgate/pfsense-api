from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Freeradiussqlconf")


@_attrs_define
class Freeradiussqlconf:
    """
    Attributes:
        sqlconfincludeenable (bool | Unset): (Enable SQL Database - Server 1) SQL Support
            Enable this to allow connections from FreeRADIUS to a SQL database. At least one of the following options must
            be enabled: Authorization, Accounting, Session, Post-Auth. (Default: Disabled)

            Enable SQL Support
        sqlconfenableauthorize (str | Unset): (Enable SQL Database - Server 1) Enable SQL Authorization (Disable,
            Enable)

            Enable this if usernames and passwords are stored on a SQL database.

            SQL support must be enabled for this to work.
            (Default: Disable)
        sqlconfenableaccounting (str | Unset): (Enable SQL Database - Server 1) Enable SQL Accounting (Disable, Enable)

            Enable this if accounting packets should be logged to a SQL database.


            SQL support must be enabled for this to work.
            (Default: Disable)
        sqlconfenablesession (str | Unset): (Enable SQL Database - Server 1) Enable SQL Session (Disable, Enable)

            Enable this to use the "rlm_sql" module (fast) to check for simultaneous connections instead of "radutmp"
            (slow).

            SQL support must be enabled for this to work.
            (Default: Disable)
        sqlconfenablepostauth (str | Unset): (Enable SQL Database - Server 1) Enable SQL Post-Auth (Disable, Enable)

            Enable this if you like to store post-authentication data on a SQL database.

            SQL support must be enabled for this to work.
            (Default: Disable)
        sqlconfdatabase (str | Unset): (SQL Database Configuration - Server 1) Database Type (mysql, postgresql)

            Choose the database type.
            (Default: MySQL)
        sqlconfserver (str | Unset): (SQL Database Configuration - Server 1) Server Address

            Database server FQDN or IP address.
            (Default: localhost)
        sqlconfport (str | Unset): (SQL Database Configuration - Server 1) Server Port

            Enter the port of the database server.
            (Default: 3306)
        sqlconflogin (str | Unset): (SQL Database Configuration - Server 1) Database Username

            Enter the username for the database server.
            (Default: radius)
        sqlconfpassword (str | Unset): (SQL Database Configuration - Server 1) Database Password

            Enter the password for the database server user.
            (Default: radpass)
        sqlconfradiusdb (str | Unset): (SQL Database Configuration - Server 1) Database Table Configuration

            Choose database table configuration.
            Click Info for details. (Default: radius)

            - For all DBs except Oracle choose:  radius

            - For Oracle, use the following template, adjusted according to your environment:

            (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=your_sid)))
        sqlconfaccttable1 (str | Unset): (SQL Database Configuration - Server 1) Accounting Table 1 (Start)

            This is the accounting "Start" table.
            Choose the same name for both if you want to log "Start" and "Stop" to the same table.
            (Default: radacct)
        sqlconfaccttable2 (str | Unset): (SQL Database Configuration - Server 1) Accounting Table 2 (Stop)

            This is the accounting "Stop" table.
            Choose the same name for both if you want to log "Start" and "Stop" to the same table.
            (Default: radacct)
        sqlconfpostauthtable (str | Unset): (SQL Database Configuration - Server 1) Post Auth Table

            Choose Post Auth Table.
            (Default: radpostauth)
        sqlconfauthchecktable (str | Unset): (SQL Database Configuration - Server 1) Auth Check Table

            Choose Auth Check Table.
            (Default: radcheck)
        sqlconfauthreplytable (str | Unset): (SQL Database Configuration - Server 1) Auth Reply Table

            Choose Auth Reply Table.
            (Default: radreply)
        sqlconfgroupchecktable (str | Unset): (SQL Database Configuration - Server 1) Group Check Table

            Choose Group Check Table.
            (Default: radgroupcheck)
        sqlconfgroupreplytable (str | Unset): (SQL Database Configuration - Server 1) Group Reply Table

            Choose Group Reply Table.
            (Default: radgroupreply)
        sqlconfusergrouptable (str | Unset): (SQL Database Configuration - Server 1) User Group Table

            Choose User Group Table.
            (Default: radusergroup)
        sqlconfreadgroups (str | Unset): (SQL Database Configuration - Server 1) Read the Group Tables (yes, no)

            If set to 'Yes', the group tables will be read.

            If set to 'No', the user must have Fall-Through = Yes in the radreply table.
            (Default: Yes)
        sqlconfdeletestalesessions (str | Unset): (SQL Database Configuration - Server 1) Delete Stale Sessions (yes,
            no)

            Remove stale session if checkrad does not see a double login.
            (Default: Yes)
        sqlconfsqltrace (str | Unset): (SQL Database Configuration - Server 1) Print all SQL Statements (yes, no)

            Print all SQL statements when in debug mode.
            (Default: No)
        sqlconfnumsqlsocks (str | Unset): (SQL Database Configuration - Server 1) Number of SQL Connections

            Number of SQL connections to make to the server.
            (Default: 5)
        sqlconfconnectfailureretrydelay (str | Unset): (SQL Database Configuration - Server 1) Failed Database
            Connection Delay

            Number of seconds before a retry after a failed database connection.
            (Default: 60)
        sqlconflifetime (str | Unset): (SQL Database Configuration - Server 1) SQL Socket Lifetime

            If you have network issues, such as TCP sessions expiring, you may need to set the socket lifetime.

            If set to non-zero, any open connections will be closed X seconds after they were first opened.
            (Default: 0)
        sqlconfmaxqueries (str | Unset): (SQL Database Configuration - Server 1) SQL Socket Maximum Queries

            If you have issues with SQL sockets lasting too long, you can limit the number of queries performed over one
            socket.

            After set number of queries, the socket will be closed. Use 0 for no limit.
            (Default: 0)
        sqlconfreadclients (str | Unset): (SQL Database Configuration - Server 1) Read Clients from Database (yes, no)

            Set to 'Yes' to read RADIUS clients from the database 'nas' table. Clients will only be read on server startup.
            (Default: Yes)
        sqlconfnastable (str | Unset): (SQL Database Configuration - Server 1) RADIUS Client Table

            Choose the table to keep RADIUS client info.
            (Default: nas)
        sqlconf2failover (str | Unset): (Enable Redundant SQL Database Support) Choose Failover/Load Balancing Mode
            (redundant, load-balance, redundant-load-balance)

            Choose the interaction of the two SQL databases.
            Click Info for details. (Default: Redundant)


            - Redundant: Failover to server2 if server1 fails.
            - Load-Balance: The load is balanced 50:50 between both databases.
            - Redundant-Load-Balance: The load is balanced 50:50 between both databases. If one is down, the other does
            100%.
        sqlconf2includeenable (bool | Unset): (Enable SQL Database - Server 2) SQL Support
            Enable this to allow connections from FreeRADIUS to a SQL database. At least one of the following options must
            be enabled: Authorization, Accounting, Session, Post-Auth. (Default: Disabled)

            Enable SQL Support (Default: unchecked)
        sqlconf2enableauthorize (str | Unset): (Enable SQL Database - Server 2) Enable SQL Authorization (Disable,
            Enable)

            Enable this if usernames and passwords are stored on a SQL database.

            SQL support must be enabled for this to work.
            (Default: Disable)
        sqlconf2enableaccounting (str | Unset): (Enable SQL Database - Server 2) Enable SQL Accounting (Disable, Enable)

            Enable this if accounting packets should be logged to a SQL database.

            SQL support must be enabled for this to work.
            (Default: Disable)
        sqlconf2enablesession (str | Unset): (Enable SQL Database - Server 2) Enable SQL Session (Disable, Enable)

            Enable this to use the "rlm_sql" module (fast) to check for simultaneous connections instead of "radutmp"
            (slow).

            SQL support must be enabled for this to work.
            (Default: Disable)
        sqlconf2enablepostauth (str | Unset): (Enable SQL Database - Server 2) Enable SQL Post-Auth (Disable, Enable)

            Enable this if you like to store post-authentication data on a SQL database.

            SQL support must be enabled for this to work.
            (Default: Disable)
        sqlconf2database (str | Unset): (SQL Database Configuration - Server 2) Database Type (mysql, postgresql)

            Choose the database type.
            (Default: MySQL)
        sqlconf2server (str | Unset): (SQL Database Configuration - Server 2) Server Address

            Database server FQDN or IP address.
            (Default: localhost)
        sqlconf2port (str | Unset): (SQL Database Configuration - Server 2) Server Port

            Enter the port of the database server.
            (Default: 3306)
        sqlconf2login (str | Unset): (SQL Database Configuration - Server 2) Database Username

            Enter the username for the database server.
            (Default: radius)
        sqlconf2password (str | Unset): (SQL Database Configuration - Server 2) Database Password

            Enter the password for the database server user.
            (Default: radpass)
        sqlconf2radiusdb (str | Unset): (SQL Database Configuration - Server 2) Database Table Configuration

            Choose database table configuration.
            Click Info for details. (Default: radius)

            - For all DBs except Oracle choose:  radius

            - For Oracle, use the following template, adjusted according to your environment:

            (DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SID=your_sid)))
        sqlconf2accttable1 (str | Unset): (SQL Database Configuration - Server 2) Accounting Table 1 (Start)

            This is the accounting "Start" table.
            Choose the same name for both if you want to log "Start" and "Stop" to the same table.
            (Default: radacct)
        sqlconf2accttable2 (str | Unset): (SQL Database Configuration - Server 2) Accounting Table 2 (Stop)

            This is the accounting "Stop" table.
            Choose the same name for both if you want to log "Start" and "Stop" to the same table.
            (Default: radacct)
        sqlconf2postauthtable (str | Unset): (SQL Database Configuration - Server 2) Post Auth Table

            Choose Post Auth Table.
            (Default: radpostauth)
        sqlconf2authchecktable (str | Unset): (SQL Database Configuration - Server 2) Auth Check Table

            Choose Auth Check Table.
            (Default: radcheck)
        sqlconf2authreplytable (str | Unset): (SQL Database Configuration - Server 2) Auth Reply Table

            Choose Auth Reply Table.
            (Default: radreply)
        sqlconf2groupchecktable (str | Unset): (SQL Database Configuration - Server 2) Group Check Table

            Choose Group Check Table.
            (Default: radgroupcheck)
        sqlconf2groupreplytable (str | Unset): (SQL Database Configuration - Server 2) Group Reply Table

            Choose Group Reply Table.
            (Default: radgroupreply)
        sqlconf2usergrouptable (str | Unset): (SQL Database Configuration - Server 2) User Group Table

            Choose User Group Table.
            (Default: radusergroup)
        sqlconf2readgroups (str | Unset): (SQL Database Configuration - Server 2) Read the Group Tables (yes, no)

            If set to 'Yes', the group tables will be read.

            If set to 'No', the user must have Fall-Through = Yes in the radreply table.
            (Default: Yes)
        sqlconf2deletestalesessions (str | Unset): (SQL Database Configuration - Server 2) Delete Stale Sessions (yes,
            no)

            Remove stale session if checkrad does not see a double login.
            (Default: Yes)
        sqlconf2sqltrace (str | Unset): (SQL Database Configuration - Server 2) Print all SQL Statements (yes, no)

            Print all SQL statements when in debug mode.
            (Default: No)
        sqlconf2numsqlsocks (str | Unset): (SQL Database Configuration - Server 2) Number of SQL Connections

            Number of SQL connections to make to the server.
            (Default: 5)
        sqlconf2connectfailureretrydelay (str | Unset): (SQL Database Configuration - Server 2) Failed Database
            Connection Delay

            Number of seconds before a retry after a failed database connection.
            (Default: 60)
        sqlconf2lifetime (str | Unset): (SQL Database Configuration - Server 2) SQL Socket Lifetime

            If you have network issues, such as TCP sessions expiring, you may need to set the socket lifetime.


            If set to non-zero, any open connections will be closed X seconds after they were first opened.
            (Default: 0)
        sqlconf2maxqueries (str | Unset): (SQL Database Configuration - Server 2) SQL Socket Maximum Queries

            If you have issues with SQL sockets lasting too long, you can limit the number of queries performed over one
            socket.


            After set number of queries, the socket will be closed. Use 0 for no limit.
            (Default: 0)
        sqlconf2readclients (str | Unset): (SQL Database Configuration - Server 2) Read Clients from Database (yes, no)

            Set to 'Yes' to read RADIUS clients from the database 'nas' table. Clients will only be read on server startup.
            (Default: Yes)
        sqlconf2nastable (str | Unset): (SQL Database Configuration - Server 2) RADIUS Client Table

            Choose the table to keep RADIUS client info.
            (Default: nas)
    """

    sqlconfincludeenable: bool | Unset = UNSET
    sqlconfenableauthorize: str | Unset = UNSET
    sqlconfenableaccounting: str | Unset = UNSET
    sqlconfenablesession: str | Unset = UNSET
    sqlconfenablepostauth: str | Unset = UNSET
    sqlconfdatabase: str | Unset = UNSET
    sqlconfserver: str | Unset = UNSET
    sqlconfport: str | Unset = UNSET
    sqlconflogin: str | Unset = UNSET
    sqlconfpassword: str | Unset = UNSET
    sqlconfradiusdb: str | Unset = UNSET
    sqlconfaccttable1: str | Unset = UNSET
    sqlconfaccttable2: str | Unset = UNSET
    sqlconfpostauthtable: str | Unset = UNSET
    sqlconfauthchecktable: str | Unset = UNSET
    sqlconfauthreplytable: str | Unset = UNSET
    sqlconfgroupchecktable: str | Unset = UNSET
    sqlconfgroupreplytable: str | Unset = UNSET
    sqlconfusergrouptable: str | Unset = UNSET
    sqlconfreadgroups: str | Unset = UNSET
    sqlconfdeletestalesessions: str | Unset = UNSET
    sqlconfsqltrace: str | Unset = UNSET
    sqlconfnumsqlsocks: str | Unset = UNSET
    sqlconfconnectfailureretrydelay: str | Unset = UNSET
    sqlconflifetime: str | Unset = UNSET
    sqlconfmaxqueries: str | Unset = UNSET
    sqlconfreadclients: str | Unset = UNSET
    sqlconfnastable: str | Unset = UNSET
    sqlconf2failover: str | Unset = UNSET
    sqlconf2includeenable: bool | Unset = UNSET
    sqlconf2enableauthorize: str | Unset = UNSET
    sqlconf2enableaccounting: str | Unset = UNSET
    sqlconf2enablesession: str | Unset = UNSET
    sqlconf2enablepostauth: str | Unset = UNSET
    sqlconf2database: str | Unset = UNSET
    sqlconf2server: str | Unset = UNSET
    sqlconf2port: str | Unset = UNSET
    sqlconf2login: str | Unset = UNSET
    sqlconf2password: str | Unset = UNSET
    sqlconf2radiusdb: str | Unset = UNSET
    sqlconf2accttable1: str | Unset = UNSET
    sqlconf2accttable2: str | Unset = UNSET
    sqlconf2postauthtable: str | Unset = UNSET
    sqlconf2authchecktable: str | Unset = UNSET
    sqlconf2authreplytable: str | Unset = UNSET
    sqlconf2groupchecktable: str | Unset = UNSET
    sqlconf2groupreplytable: str | Unset = UNSET
    sqlconf2usergrouptable: str | Unset = UNSET
    sqlconf2readgroups: str | Unset = UNSET
    sqlconf2deletestalesessions: str | Unset = UNSET
    sqlconf2sqltrace: str | Unset = UNSET
    sqlconf2numsqlsocks: str | Unset = UNSET
    sqlconf2connectfailureretrydelay: str | Unset = UNSET
    sqlconf2lifetime: str | Unset = UNSET
    sqlconf2maxqueries: str | Unset = UNSET
    sqlconf2readclients: str | Unset = UNSET
    sqlconf2nastable: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sqlconfincludeenable = self.sqlconfincludeenable

        sqlconfenableauthorize = self.sqlconfenableauthorize

        sqlconfenableaccounting = self.sqlconfenableaccounting

        sqlconfenablesession = self.sqlconfenablesession

        sqlconfenablepostauth = self.sqlconfenablepostauth

        sqlconfdatabase = self.sqlconfdatabase

        sqlconfserver = self.sqlconfserver

        sqlconfport = self.sqlconfport

        sqlconflogin = self.sqlconflogin

        sqlconfpassword = self.sqlconfpassword

        sqlconfradiusdb = self.sqlconfradiusdb

        sqlconfaccttable1 = self.sqlconfaccttable1

        sqlconfaccttable2 = self.sqlconfaccttable2

        sqlconfpostauthtable = self.sqlconfpostauthtable

        sqlconfauthchecktable = self.sqlconfauthchecktable

        sqlconfauthreplytable = self.sqlconfauthreplytable

        sqlconfgroupchecktable = self.sqlconfgroupchecktable

        sqlconfgroupreplytable = self.sqlconfgroupreplytable

        sqlconfusergrouptable = self.sqlconfusergrouptable

        sqlconfreadgroups = self.sqlconfreadgroups

        sqlconfdeletestalesessions = self.sqlconfdeletestalesessions

        sqlconfsqltrace = self.sqlconfsqltrace

        sqlconfnumsqlsocks = self.sqlconfnumsqlsocks

        sqlconfconnectfailureretrydelay = self.sqlconfconnectfailureretrydelay

        sqlconflifetime = self.sqlconflifetime

        sqlconfmaxqueries = self.sqlconfmaxqueries

        sqlconfreadclients = self.sqlconfreadclients

        sqlconfnastable = self.sqlconfnastable

        sqlconf2failover = self.sqlconf2failover

        sqlconf2includeenable = self.sqlconf2includeenable

        sqlconf2enableauthorize = self.sqlconf2enableauthorize

        sqlconf2enableaccounting = self.sqlconf2enableaccounting

        sqlconf2enablesession = self.sqlconf2enablesession

        sqlconf2enablepostauth = self.sqlconf2enablepostauth

        sqlconf2database = self.sqlconf2database

        sqlconf2server = self.sqlconf2server

        sqlconf2port = self.sqlconf2port

        sqlconf2login = self.sqlconf2login

        sqlconf2password = self.sqlconf2password

        sqlconf2radiusdb = self.sqlconf2radiusdb

        sqlconf2accttable1 = self.sqlconf2accttable1

        sqlconf2accttable2 = self.sqlconf2accttable2

        sqlconf2postauthtable = self.sqlconf2postauthtable

        sqlconf2authchecktable = self.sqlconf2authchecktable

        sqlconf2authreplytable = self.sqlconf2authreplytable

        sqlconf2groupchecktable = self.sqlconf2groupchecktable

        sqlconf2groupreplytable = self.sqlconf2groupreplytable

        sqlconf2usergrouptable = self.sqlconf2usergrouptable

        sqlconf2readgroups = self.sqlconf2readgroups

        sqlconf2deletestalesessions = self.sqlconf2deletestalesessions

        sqlconf2sqltrace = self.sqlconf2sqltrace

        sqlconf2numsqlsocks = self.sqlconf2numsqlsocks

        sqlconf2connectfailureretrydelay = self.sqlconf2connectfailureretrydelay

        sqlconf2lifetime = self.sqlconf2lifetime

        sqlconf2maxqueries = self.sqlconf2maxqueries

        sqlconf2readclients = self.sqlconf2readclients

        sqlconf2nastable = self.sqlconf2nastable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sqlconfincludeenable is not UNSET:
            field_dict["sqlconfincludeenable"] = sqlconfincludeenable
        if sqlconfenableauthorize is not UNSET:
            field_dict["sqlconfenableauthorize"] = sqlconfenableauthorize
        if sqlconfenableaccounting is not UNSET:
            field_dict["sqlconfenableaccounting"] = sqlconfenableaccounting
        if sqlconfenablesession is not UNSET:
            field_dict["sqlconfenablesession"] = sqlconfenablesession
        if sqlconfenablepostauth is not UNSET:
            field_dict["sqlconfenablepostauth"] = sqlconfenablepostauth
        if sqlconfdatabase is not UNSET:
            field_dict["sqlconfdatabase"] = sqlconfdatabase
        if sqlconfserver is not UNSET:
            field_dict["sqlconfserver"] = sqlconfserver
        if sqlconfport is not UNSET:
            field_dict["sqlconfport"] = sqlconfport
        if sqlconflogin is not UNSET:
            field_dict["sqlconflogin"] = sqlconflogin
        if sqlconfpassword is not UNSET:
            field_dict["sqlconfpassword"] = sqlconfpassword
        if sqlconfradiusdb is not UNSET:
            field_dict["sqlconfradiusdb"] = sqlconfradiusdb
        if sqlconfaccttable1 is not UNSET:
            field_dict["sqlconfaccttable1"] = sqlconfaccttable1
        if sqlconfaccttable2 is not UNSET:
            field_dict["sqlconfaccttable2"] = sqlconfaccttable2
        if sqlconfpostauthtable is not UNSET:
            field_dict["sqlconfpostauthtable"] = sqlconfpostauthtable
        if sqlconfauthchecktable is not UNSET:
            field_dict["sqlconfauthchecktable"] = sqlconfauthchecktable
        if sqlconfauthreplytable is not UNSET:
            field_dict["sqlconfauthreplytable"] = sqlconfauthreplytable
        if sqlconfgroupchecktable is not UNSET:
            field_dict["sqlconfgroupchecktable"] = sqlconfgroupchecktable
        if sqlconfgroupreplytable is not UNSET:
            field_dict["sqlconfgroupreplytable"] = sqlconfgroupreplytable
        if sqlconfusergrouptable is not UNSET:
            field_dict["sqlconfusergrouptable"] = sqlconfusergrouptable
        if sqlconfreadgroups is not UNSET:
            field_dict["sqlconfreadgroups"] = sqlconfreadgroups
        if sqlconfdeletestalesessions is not UNSET:
            field_dict["sqlconfdeletestalesessions"] = sqlconfdeletestalesessions
        if sqlconfsqltrace is not UNSET:
            field_dict["sqlconfsqltrace"] = sqlconfsqltrace
        if sqlconfnumsqlsocks is not UNSET:
            field_dict["sqlconfnumsqlsocks"] = sqlconfnumsqlsocks
        if sqlconfconnectfailureretrydelay is not UNSET:
            field_dict["sqlconfconnectfailureretrydelay"] = sqlconfconnectfailureretrydelay
        if sqlconflifetime is not UNSET:
            field_dict["sqlconflifetime"] = sqlconflifetime
        if sqlconfmaxqueries is not UNSET:
            field_dict["sqlconfmaxqueries"] = sqlconfmaxqueries
        if sqlconfreadclients is not UNSET:
            field_dict["sqlconfreadclients"] = sqlconfreadclients
        if sqlconfnastable is not UNSET:
            field_dict["sqlconfnastable"] = sqlconfnastable
        if sqlconf2failover is not UNSET:
            field_dict["sqlconf2failover"] = sqlconf2failover
        if sqlconf2includeenable is not UNSET:
            field_dict["sqlconf2includeenable"] = sqlconf2includeenable
        if sqlconf2enableauthorize is not UNSET:
            field_dict["sqlconf2enableauthorize"] = sqlconf2enableauthorize
        if sqlconf2enableaccounting is not UNSET:
            field_dict["sqlconf2enableaccounting"] = sqlconf2enableaccounting
        if sqlconf2enablesession is not UNSET:
            field_dict["sqlconf2enablesession"] = sqlconf2enablesession
        if sqlconf2enablepostauth is not UNSET:
            field_dict["sqlconf2enablepostauth"] = sqlconf2enablepostauth
        if sqlconf2database is not UNSET:
            field_dict["sqlconf2database"] = sqlconf2database
        if sqlconf2server is not UNSET:
            field_dict["sqlconf2server"] = sqlconf2server
        if sqlconf2port is not UNSET:
            field_dict["sqlconf2port"] = sqlconf2port
        if sqlconf2login is not UNSET:
            field_dict["sqlconf2login"] = sqlconf2login
        if sqlconf2password is not UNSET:
            field_dict["sqlconf2password"] = sqlconf2password
        if sqlconf2radiusdb is not UNSET:
            field_dict["sqlconf2radiusdb"] = sqlconf2radiusdb
        if sqlconf2accttable1 is not UNSET:
            field_dict["sqlconf2accttable1"] = sqlconf2accttable1
        if sqlconf2accttable2 is not UNSET:
            field_dict["sqlconf2accttable2"] = sqlconf2accttable2
        if sqlconf2postauthtable is not UNSET:
            field_dict["sqlconf2postauthtable"] = sqlconf2postauthtable
        if sqlconf2authchecktable is not UNSET:
            field_dict["sqlconf2authchecktable"] = sqlconf2authchecktable
        if sqlconf2authreplytable is not UNSET:
            field_dict["sqlconf2authreplytable"] = sqlconf2authreplytable
        if sqlconf2groupchecktable is not UNSET:
            field_dict["sqlconf2groupchecktable"] = sqlconf2groupchecktable
        if sqlconf2groupreplytable is not UNSET:
            field_dict["sqlconf2groupreplytable"] = sqlconf2groupreplytable
        if sqlconf2usergrouptable is not UNSET:
            field_dict["sqlconf2usergrouptable"] = sqlconf2usergrouptable
        if sqlconf2readgroups is not UNSET:
            field_dict["sqlconf2readgroups"] = sqlconf2readgroups
        if sqlconf2deletestalesessions is not UNSET:
            field_dict["sqlconf2deletestalesessions"] = sqlconf2deletestalesessions
        if sqlconf2sqltrace is not UNSET:
            field_dict["sqlconf2sqltrace"] = sqlconf2sqltrace
        if sqlconf2numsqlsocks is not UNSET:
            field_dict["sqlconf2numsqlsocks"] = sqlconf2numsqlsocks
        if sqlconf2connectfailureretrydelay is not UNSET:
            field_dict["sqlconf2connectfailureretrydelay"] = sqlconf2connectfailureretrydelay
        if sqlconf2lifetime is not UNSET:
            field_dict["sqlconf2lifetime"] = sqlconf2lifetime
        if sqlconf2maxqueries is not UNSET:
            field_dict["sqlconf2maxqueries"] = sqlconf2maxqueries
        if sqlconf2readclients is not UNSET:
            field_dict["sqlconf2readclients"] = sqlconf2readclients
        if sqlconf2nastable is not UNSET:
            field_dict["sqlconf2nastable"] = sqlconf2nastable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sqlconfincludeenable = d.pop("sqlconfincludeenable", UNSET)

        sqlconfenableauthorize = d.pop("sqlconfenableauthorize", UNSET)

        sqlconfenableaccounting = d.pop("sqlconfenableaccounting", UNSET)

        sqlconfenablesession = d.pop("sqlconfenablesession", UNSET)

        sqlconfenablepostauth = d.pop("sqlconfenablepostauth", UNSET)

        sqlconfdatabase = d.pop("sqlconfdatabase", UNSET)

        sqlconfserver = d.pop("sqlconfserver", UNSET)

        sqlconfport = d.pop("sqlconfport", UNSET)

        sqlconflogin = d.pop("sqlconflogin", UNSET)

        sqlconfpassword = d.pop("sqlconfpassword", UNSET)

        sqlconfradiusdb = d.pop("sqlconfradiusdb", UNSET)

        sqlconfaccttable1 = d.pop("sqlconfaccttable1", UNSET)

        sqlconfaccttable2 = d.pop("sqlconfaccttable2", UNSET)

        sqlconfpostauthtable = d.pop("sqlconfpostauthtable", UNSET)

        sqlconfauthchecktable = d.pop("sqlconfauthchecktable", UNSET)

        sqlconfauthreplytable = d.pop("sqlconfauthreplytable", UNSET)

        sqlconfgroupchecktable = d.pop("sqlconfgroupchecktable", UNSET)

        sqlconfgroupreplytable = d.pop("sqlconfgroupreplytable", UNSET)

        sqlconfusergrouptable = d.pop("sqlconfusergrouptable", UNSET)

        sqlconfreadgroups = d.pop("sqlconfreadgroups", UNSET)

        sqlconfdeletestalesessions = d.pop("sqlconfdeletestalesessions", UNSET)

        sqlconfsqltrace = d.pop("sqlconfsqltrace", UNSET)

        sqlconfnumsqlsocks = d.pop("sqlconfnumsqlsocks", UNSET)

        sqlconfconnectfailureretrydelay = d.pop("sqlconfconnectfailureretrydelay", UNSET)

        sqlconflifetime = d.pop("sqlconflifetime", UNSET)

        sqlconfmaxqueries = d.pop("sqlconfmaxqueries", UNSET)

        sqlconfreadclients = d.pop("sqlconfreadclients", UNSET)

        sqlconfnastable = d.pop("sqlconfnastable", UNSET)

        sqlconf2failover = d.pop("sqlconf2failover", UNSET)

        sqlconf2includeenable = d.pop("sqlconf2includeenable", UNSET)

        sqlconf2enableauthorize = d.pop("sqlconf2enableauthorize", UNSET)

        sqlconf2enableaccounting = d.pop("sqlconf2enableaccounting", UNSET)

        sqlconf2enablesession = d.pop("sqlconf2enablesession", UNSET)

        sqlconf2enablepostauth = d.pop("sqlconf2enablepostauth", UNSET)

        sqlconf2database = d.pop("sqlconf2database", UNSET)

        sqlconf2server = d.pop("sqlconf2server", UNSET)

        sqlconf2port = d.pop("sqlconf2port", UNSET)

        sqlconf2login = d.pop("sqlconf2login", UNSET)

        sqlconf2password = d.pop("sqlconf2password", UNSET)

        sqlconf2radiusdb = d.pop("sqlconf2radiusdb", UNSET)

        sqlconf2accttable1 = d.pop("sqlconf2accttable1", UNSET)

        sqlconf2accttable2 = d.pop("sqlconf2accttable2", UNSET)

        sqlconf2postauthtable = d.pop("sqlconf2postauthtable", UNSET)

        sqlconf2authchecktable = d.pop("sqlconf2authchecktable", UNSET)

        sqlconf2authreplytable = d.pop("sqlconf2authreplytable", UNSET)

        sqlconf2groupchecktable = d.pop("sqlconf2groupchecktable", UNSET)

        sqlconf2groupreplytable = d.pop("sqlconf2groupreplytable", UNSET)

        sqlconf2usergrouptable = d.pop("sqlconf2usergrouptable", UNSET)

        sqlconf2readgroups = d.pop("sqlconf2readgroups", UNSET)

        sqlconf2deletestalesessions = d.pop("sqlconf2deletestalesessions", UNSET)

        sqlconf2sqltrace = d.pop("sqlconf2sqltrace", UNSET)

        sqlconf2numsqlsocks = d.pop("sqlconf2numsqlsocks", UNSET)

        sqlconf2connectfailureretrydelay = d.pop("sqlconf2connectfailureretrydelay", UNSET)

        sqlconf2lifetime = d.pop("sqlconf2lifetime", UNSET)

        sqlconf2maxqueries = d.pop("sqlconf2maxqueries", UNSET)

        sqlconf2readclients = d.pop("sqlconf2readclients", UNSET)

        sqlconf2nastable = d.pop("sqlconf2nastable", UNSET)

        freeradiussqlconf = cls(
            sqlconfincludeenable=sqlconfincludeenable,
            sqlconfenableauthorize=sqlconfenableauthorize,
            sqlconfenableaccounting=sqlconfenableaccounting,
            sqlconfenablesession=sqlconfenablesession,
            sqlconfenablepostauth=sqlconfenablepostauth,
            sqlconfdatabase=sqlconfdatabase,
            sqlconfserver=sqlconfserver,
            sqlconfport=sqlconfport,
            sqlconflogin=sqlconflogin,
            sqlconfpassword=sqlconfpassword,
            sqlconfradiusdb=sqlconfradiusdb,
            sqlconfaccttable1=sqlconfaccttable1,
            sqlconfaccttable2=sqlconfaccttable2,
            sqlconfpostauthtable=sqlconfpostauthtable,
            sqlconfauthchecktable=sqlconfauthchecktable,
            sqlconfauthreplytable=sqlconfauthreplytable,
            sqlconfgroupchecktable=sqlconfgroupchecktable,
            sqlconfgroupreplytable=sqlconfgroupreplytable,
            sqlconfusergrouptable=sqlconfusergrouptable,
            sqlconfreadgroups=sqlconfreadgroups,
            sqlconfdeletestalesessions=sqlconfdeletestalesessions,
            sqlconfsqltrace=sqlconfsqltrace,
            sqlconfnumsqlsocks=sqlconfnumsqlsocks,
            sqlconfconnectfailureretrydelay=sqlconfconnectfailureretrydelay,
            sqlconflifetime=sqlconflifetime,
            sqlconfmaxqueries=sqlconfmaxqueries,
            sqlconfreadclients=sqlconfreadclients,
            sqlconfnastable=sqlconfnastable,
            sqlconf2failover=sqlconf2failover,
            sqlconf2includeenable=sqlconf2includeenable,
            sqlconf2enableauthorize=sqlconf2enableauthorize,
            sqlconf2enableaccounting=sqlconf2enableaccounting,
            sqlconf2enablesession=sqlconf2enablesession,
            sqlconf2enablepostauth=sqlconf2enablepostauth,
            sqlconf2database=sqlconf2database,
            sqlconf2server=sqlconf2server,
            sqlconf2port=sqlconf2port,
            sqlconf2login=sqlconf2login,
            sqlconf2password=sqlconf2password,
            sqlconf2radiusdb=sqlconf2radiusdb,
            sqlconf2accttable1=sqlconf2accttable1,
            sqlconf2accttable2=sqlconf2accttable2,
            sqlconf2postauthtable=sqlconf2postauthtable,
            sqlconf2authchecktable=sqlconf2authchecktable,
            sqlconf2authreplytable=sqlconf2authreplytable,
            sqlconf2groupchecktable=sqlconf2groupchecktable,
            sqlconf2groupreplytable=sqlconf2groupreplytable,
            sqlconf2usergrouptable=sqlconf2usergrouptable,
            sqlconf2readgroups=sqlconf2readgroups,
            sqlconf2deletestalesessions=sqlconf2deletestalesessions,
            sqlconf2sqltrace=sqlconf2sqltrace,
            sqlconf2numsqlsocks=sqlconf2numsqlsocks,
            sqlconf2connectfailureretrydelay=sqlconf2connectfailureretrydelay,
            sqlconf2lifetime=sqlconf2lifetime,
            sqlconf2maxqueries=sqlconf2maxqueries,
            sqlconf2readclients=sqlconf2readclients,
            sqlconf2nastable=sqlconf2nastable,
        )

        freeradiussqlconf.additional_properties = d
        return freeradiussqlconf

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
