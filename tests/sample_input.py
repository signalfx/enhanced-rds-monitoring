# Sample RDSOS output from a MySQL instance
my_sql_dict = {
    "engine": "MYSQL",
    "instanceID": "ppr9b9oge80i99",
    "instanceResourceID": "db-H4UK4SA7E62QPMAYTMPK5XWETQ",
    "timestamp": "2017-09-19T00:21:07Z",
    "version": 1,
    "uptime": "272 days, 1:28:18",
    "numVCPUs": 2,
    "cpuUtilization": {
        "guest": 0,
        "irq": 0.72,
        "system": 7.25,
        "wait": 4.35,
        "idle": 78.99,
        "user": 3.62,
        "total": 21.01,
        "steal": 1.45,
        "nice": 3.62
    },
    "loadAverageMinute": {
        "fifteen": 0.4,
        "five": 0.3,
        "one": 0.29
    },
    "memory": {
        "writeback": 0,
        "hugePagesFree": 0,
        "hugePagesRsvd": 0,
        "hugePagesSurp": 0,
        "cached": 3288068,
        "hugePagesSize": 2048,
        "free": 2746028,
        "hugePagesTotal": 0,
        "inactive": 838368,
        "pageTables": 5448,
        "dirty": 144,
        "mapped": 25548,
        "active": 3766972,
        "total": 7697596,
        "slab": 239772,
        "buffers": 301616
    },
    "tasks": {
        "sleeping": 256,
        "zombie": 0,
        "running": 4,
        "stopped": 0,
        "total": 262,
        "blocked": 2
    },
    "swap": {
        "cached": 0,
        "total": 7703160,
        "free": 7703160
    },
    "network": [
        {
            "interface": "eth0",
            "rx": 821640,
            "tx": 2856222
        }
    ],
    "diskIO": [
        {
            "writeKbPS": 20,
            "readIOsPS": 0,
            "await": 1.6,
            "readKbPS": 0,
            "rrqmPS": 0,
            "util": 0.8,
            "avgQueueLen": 0.01,
            "tps": 5,
            "readKb": 0,
            "device": "rdsdev",
            "writeKb": 20,
            "avgReqSz": 4,
            "wrqmPS": 0,
            "writeIOsPS": 5
        }
    ],
    "fileSys": [
        {
            "used": 626316,
            "name": "rdsfilesys",
            "usedFiles": 523,
            "usedFilePercent": 0.01,
            "maxFiles": 6553600,
            "mountPoint": "/rdsdbdata",
            "total": 103053476,
            "usedPercent": 0.61
        }
    ],
    "processList": [
        {
            "vss": 6365136,
            "name": "mysqld",
            "tgid": 3305,
            "parentID": 1,
            "memoryUsedPc": 9.14,
            "cpuUsedPc": 0,
            "id": 765,
            "rss": 703620
        },
        {
            "vss": 6365136,
            "name": "mysqld",
            "tgid": 3305,
            "parentID": 1,
            "memoryUsedPc": 9.14,
            "cpuUsedPc": 5.5,
            "id": 766,
            "rss": 703620
        },
        {
            "vss": 6365136,
            "name": "mysqld",
            "tgid": 3305,
            "parentID": 1,
            "memoryUsedPc": 9.14,
            "cpuUsedPc": 0,
            "id": 780,
            "rss": 703620
        },
        {
            "vss": 6365136,
            "name": "mysqld",
            "tgid": 3305,
            "parentID": 1,
            "memoryUsedPc": 9.14,
            "cpuUsedPc": 0,
            "id": 781,
            "rss": 703620
        },
        {
            "vss": 6365136,
            "name": "mysqld",
            "tgid": 3305,
            "parentID": 1,
            "memoryUsedPc": 9.14,
            "cpuUsedPc": 0,
            "id": 3305,
            "rss": 703620
        },
        {
            "vss": 6365136,
            "name": "mysqld",
            "tgid": 3305,
            "parentID": 1,
            "memoryUsedPc": 9.14,
            "cpuUsedPc": 6,
            "id": 4111,
            "rss": 703620
        },
        {
            "vss": 6365136,
            "name": "mysqld",
            "tgid": 3305,
            "parentID": 1,
            "memoryUsedPc": 9.14,
            "cpuUsedPc": 5.5,
            "id": 10888,
            "rss": 703620
        },
        {
            "vss": 6365136,
            "name": "mysqld",
            "tgid": 3305,
            "parentID": 1,
            "memoryUsedPc": 9.14,
            "cpuUsedPc": 6,
            "id": 19825,
            "rss": 703620
        },
        {
            "vss": 6365136,
            "name": "mysqld",
            "tgid": 3305,
            "parentID": 1,
            "memoryUsedPc": 9.14,
            "cpuUsedPc": 5.5,
            "id": 31951,
            "rss": 703620
        },
        {
            "vss": 6365136,
            "name": "mysqld",
            "tgid": 3305,
            "parentID": 1,
            "memoryUsedPc": 9.14,
            "cpuUsedPc": 5.5,
            "id": 32015,
            "rss": 703620
        },
        {
            "vss": 935380,
            "name": "OS processes",
            "tgid": 0,
            "parentID": 0,
            "memoryUsedPc": 0.35,
            "cpuUsedPc": 0.5,
            "id": 0,
            "rss": 27824
        },
        {
            "vss": 1293204,
            "name": "RDS processes",
            "tgid": 0,
            "parentID": 0,
            "memoryUsedPc": 4.27,
            "cpuUsedPc": 4,
            "id": 0,
            "rss": 329184
        }
    ]
}

# Sample RDSOS output from a SQL Server instance
sql_server_dict = {
    "engine": "SqlServer",
    "instanceID": "trevor",
    "instanceResourceID": "db-YWCA2G6UQEA3NYZ54IS6XEBGUE",
    "timestamp": "2017-09-12T23:58:59Z",
    "version": 1,
    "uptime": "0 days, 00:10:43",
    "numVCPUs": 1,
    "cpuUtilization": {
        "idle": 64.13,
        "kern": 11.85,
        "user": 24.01
    },
    "memory": {
        "commitTotKb": 1073308,
        "commitLimitKb": 1572464,
        "commitPeakKb": 1109112,
        "physTotKb": 1048176,
        "physAvailKb": 125072,
        "sysCacheKb": 182448,
        "kernTotKb": 192596,
        "kernPagedKb": 136120,
        "kernNonpagedKb": 56476,
        "sqlServerTotKb": 123432,
        "pageSize": 4096
    },
    "system": {
        "handles": 14874,
        "threads": 634,
        "processes": 44
    },
    "disks": [
        {
            "name": "rdsdbdata",
            "totalKb": 20838336,
            "usedKb": 162752,
            "usedPc": 0.78,
            "availKb": 20675584,
            "availPc": 99.22,
            "rdCountPS": 0,
            "rdBytesPS": 0,
            "wrCountPS": 0,
            "wrBytesPS": 0
        }
    ],
    "network": [
        {
            "interface": "Ethernet 2",
            "rdBytesPS": 0,
            "wrBytesPS": 0
        }
    ],
    "processList": [
        {
            "name": "OS processes",
            "cpuUsedPc": 0.3,
            "memUsedPc": 8.46,
            "workingSetKb": 249908,
            "workingSetPrivKb": 88728,
            "workingSetShareableKb": 161180,
            "virtKb": 57985212532
        },
        {
            "name": "RDS processes",
            "cpuUsedPc": 1.52,
            "memUsedPc": 20.61,
            "workingSetKb": 367720,
            "workingSetPrivKb": 215996,
            "workingSetShareableKb": 151724,
            "virtKb": 4331792332
        },
        {
            "name": "sqlwriter.exe",
            "pid": 1736,
            "cpuUsedPc": 0,
            "memUsedPc": 0.1,
            "workingSetKb": 5876,
            "workingSetPrivKb": 1020,
            "workingSetShareableKb": 4856,
            "virtKb": 38280
        },
        {
            "name": "fdlauncher.exe",
            "pid": 2436,
            "cpuUsedPc": 0,
            "memUsedPc": 0.05,
            "workingSetKb": 3576,
            "workingSetPrivKb": 568,
            "workingSetShareableKb": 3008,
            "virtKb": 26776
        },
        {
            "name": "sqlservr.exe",
            "pid": 3624,
            "cpuUsedPc": 32.22,
            "memUsedPc": 11.12,
            "workingSetKb": 158676,
            "workingSetPrivKb": 116608,
            "workingSetShareableKb": 42068,
            "virtKb": 2694704
        },
        {
            "name": "sqlservr.exe",
            "pid": 3624,
            "tid": 3628,
            "cpuUsedPc": 0
        },
        {
            "name": "sqlservr.exe",
            "pid": 3624,
            "tid": 3636,
            "cpuUsedPc": 0
        },
        {
            "name": "sqlservr.exe",
            "pid": 3624,
            "tid": 3644,
            "cpuUsedPc": 0
        },
        {
            "name": "sqlservr.exe",
            "pid": 3624,
            "tid": 3648,
            "cpuUsedPc": 0
        },
        {
            "name": "sqlservr.exe",
            "pid": 3624,
            "tid": 3660,
            "cpuUsedPc": 0
        },
        {
            "name": "sqlservr.exe",
            "pid": 3624,
            "tid": 3664,
            "cpuUsedPc": 0
        },
        {
            "name": "sqlservr.exe",
            "pid": 3624,
            "tid": 3668,
            "cpuUsedPc": 0
        },
        {
            'name': "sqlservr.exe",
            "pid": 3624,
            "tid": 3672,
            "cpuUsedPc": 32.22
        },
        {
            "name": "sqlservr.exe",
            "pid": 3624,
            "tid": 3676,
            "cpuUsedPc": 0
        },
        {
            "name": "sqlservr.exe",
            "pid": 3624,
            "tid": 3680,
            "cpuUsedPc": 0
        },
    ]
}

# Sample RDSOS output for an Aurora instance
aurora_dict = {
    "engine": "Aurora",
    "instanceID": "trevor",
    "instanceResourceID": "db-F3AZGY5JTAS65TT4E7U3CDS6AM",
    "timestamp": "2017-09-12T23:02:53Z",
    "version": 1,
    "uptime": "0:44:23",
    "numVCPUs": 1,
    "cpuUtilization": {
        "guest": 0,
        "irq": 0.04,
        "system": 1.86,
        "wait": 2.61,
        "idle": 90.08,
        "user": 5.01,
        "total": 9.92,
        "steal": 0.36,
        "nice": 0.04
    },
    "loadAverageMinute": {
        "fifteen": 0.13,
        "five": 0.1,
        "one": 0.3
    },
    "memory": {
        "writeback": 0,
        "hugePagesFree": 1024,
        "hugePagesRsvd": 0,
        "hugePagesSurp": 0,
        "cached": 489508,
        "hugePagesSize": 2048,
        "free": 99192,
        "hugePagesTotal": 367616,
        "inactive": 260216,
        "pageTables": 6244,
        "dirty": 1400,
        "mapped": 84816,
        "active": 890436,
        "total": 2052380,
        "slab": 38916,
        "buffers": 67024
    },
    "tasks": {
        "sleeping": 233,
        "zombie": 0,
        "running": 2,
        "stopped": 0,
        "total": 235,
        "blocked": 0
    },
    "swap": {
        "cached": 0,
        "total": 0,
        "free": 0
    },
    "network": [
        {
            "interface": "eth0",
            "rx": 58724202.3,
            "tx": 2613197.9
        }
    ],
    "diskIO": [
        {
            "readLatency": 2.74,
            "writeLatency": 1.5,
            "writeThroughput": 476409.8,
            "readThroughput": 665190.4,
            "readIOsPS": 40.6,
            "diskQueueDepth": 0,
            "writeIOsPS": 1426.8
        }
    ],
    "fileSys": [
        {
            "used": 68956,
            "name": "rdsfilesys",
            "usedFiles": 211,
            "usedFilePercent": 0.01,
            "maxFiles": 2097152,
            "mountPoint": "/rdsdbdata",
            "total": 32890736,
            "usedPercent": 0.21
        }
    ],
    "processList": [
        {
            "vss": 1232180,
            "name": "aurora",
            "tgid": 5439,
            "vmlimit": 2052380,
            "parentID": 1,
            "memoryUsedPc": 12.47,
            "cpuUsedPc": 0,
            "id": 5439,
            "rss": 255908
        },
        {
            "vss": 691648,
            "name": "OS processes",
            "tgid": 0,
            "vmlimit": "",
            "parentID": 0,
            "memoryUsedPc": 1.15,
            "cpuUsedPc": 0,
            "id": 0,
            "rss": 23888
        },
        {
            "vss": 3247344,
            "name": "RDS processes",
            "tgid": 0,
            "vmlimit": "",
            "parentID": 0,
            "memoryUsedPc": 20.91,
            "cpuUsedPc": 0,
            "id": 0,
            "rss": 429908
        }
    ]
}
