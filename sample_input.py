# Sample RDSOS output from a MySQL instance
my_sql_dict = {
    u"engine": u"MYSQL",
    u"instanceID": u"ppr9b9oge80i99",
    u"instanceResourceID": u"db-H4UK4SA7E62QPMAYTMPK5XWETQ",
    u"timestamp": u"2017-09-19T00:21:07Z",
    u"version": 1,
    u"uptime": u"272 days, 1:28:18",
    u"numVCPUs": 2,
    u"cpuUtilization": {
        u"guest": 0,
        u"irq": 0.72,
        u"system": 7.25,
        u"wait": 4.35,
        u"idle": 78.99,
        u"user": 3.62,
        u"total": 21.01,
        u"steal": 1.45,
        u"nice": 3.62
    },
    u"loadAverageMinute": {
        u"fifteen": 0.4,
        u"five": 0.3,
        u"one": 0.29
    },
    u"memory": {
        u"writeback": 0,
        u"hugePagesFree": 0,
        u"hugePagesRsvd": 0,
        u"hugePagesSurp": 0,
        u"cached": 3288068,
        u"hugePagesSize": 2048,
        u"free": 2746028,
        u"hugePagesTotal": 0,
        u"inactive": 838368,
        u"pageTables": 5448,
        u"dirty": 144,
        u"mapped": 25548,
        u"active": 3766972,
        u"total": 7697596,
        u"slab": 239772,
        u"buffers": 301616
    },
    u"tasks": {
        u"sleeping": 256,
        u"zombie": 0,
        u"running": 4,
        u"stopped": 0,
        u"total": 262,
        u"blocked": 2
    },
    u"swap": {
        u"cached": 0,
        u"total": 7703160,
        u"free": 7703160
    },
    u"network": [
        {
            u"interface": u"eth0",
            u"rx": 821640,
            u"tx": 2856222
        }
    ],
    u"diskIO": [
        {
            u"writeKbPS": 20,
            u"readIOsPS": 0,
            u"await": 1.6,
            u"readKbPS": 0,
            u"rrqmPS": 0,
            u"util": 0.8,
            u"avgQueueLen": 0.01,
            u"tps": 5,
            u"readKb": 0,
            u"device": u"rdsdev",
            u"writeKb": 20,
            u"avgReqSz": 4,
            u"wrqmPS": 0,
            u"writeIOsPS": 5
        }
    ],
    u"fileSys": [
        {
            u"used": 626316,
            u"name": u"rdsfilesys",
            u"usedFiles": 523,
            u"usedFilePercent": 0.01,
            u"maxFiles": 6553600,
            u"mountPoint": u"/rdsdbdata",
            u"total": 103053476,
            u"usedPercent": 0.61
        }
    ],
    u"processList": [
        {
            u"vss": 6365136,
            u"name": u"mysqld",
            u"tgid": 3305,
            u"parentID": 1,
            u"memoryUsedPc": 9.14,
            u"cpuUsedPc": 0,
            u"id": 765,
            u"rss": 703620
        },
        {
            u"vss": 6365136,
            u"name": u"mysqld",
            u"tgid": 3305,
            u"parentID": 1,
            u"memoryUsedPc": 9.14,
            u"cpuUsedPc": 5.5,
            u"id": 766,
            u"rss": 703620
        },
        {
            u"vss": 6365136,
            u"name": u"mysqld",
            u"tgid": 3305,
            u"parentID": 1,
            u"memoryUsedPc": 9.14,
            u"cpuUsedPc": 0,
            u"id": 780,
            u"rss": 703620
        },
        {
            u"vss": 6365136,
            u"name": u"mysqld",
            u"tgid": 3305,
            u"parentID": 1,
            u"memoryUsedPc": 9.14,
            u"cpuUsedPc": 0,
            u"id": 781,
            u"rss": 703620
        },
        {
            u"vss": 6365136,
            u"name": u"mysqld",
            u"tgid": 3305,
            u"parentID": 1,
            u"memoryUsedPc": 9.14,
            u"cpuUsedPc": 0,
            u"id": 3305,
            u"rss": 703620
        },
        {
            u"vss": 6365136,
            u"name": u"mysqld",
            u"tgid": 3305,
            u"parentID": 1,
            u"memoryUsedPc": 9.14,
            u"cpuUsedPc": 6,
            u"id": 4111,
            u"rss": 703620
        },
        {
            u"vss": 6365136,
            u"name": u"mysqld",
            u"tgid": 3305,
            u"parentID": 1,
            u"memoryUsedPc": 9.14,
            u"cpuUsedPc": 5.5,
            u"id": 10888,
            u"rss": 703620
        },
        {
            u"vss": 6365136,
            u"name": u"mysqld",
            u"tgid": 3305,
            u"parentID": 1,
            u"memoryUsedPc": 9.14,
            u"cpuUsedPc": 6,
            u"id": 19825,
            u"rss": 703620
        },
        {
            u"vss": 6365136,
            u"name": u"mysqld",
            u"tgid": 3305,
            u"parentID": 1,
            u"memoryUsedPc": 9.14,
            u"cpuUsedPc": 5.5,
            u"id": 31951,
            u"rss": 703620
        },
        {
            u"vss": 6365136,
            u"name": u"mysqld",
            u"tgid": 3305,
            u"parentID": 1,
            u"memoryUsedPc": 9.14,
            u"cpuUsedPc": 5.5,
            u"id": 32015,
            u"rss": 703620
        },
        {
            u"vss": 935380,
            u"name": u"OS processes",
            u"tgid": 0,
            u"parentID": 0,
            u"memoryUsedPc": 0.35,
            u"cpuUsedPc": 0.5,
            u"id": 0,
            u"rss": 27824
        },
        {
            u"vss": 1293204,
            u"name": u"RDS processes",
            u"tgid": 0,
            u"parentID": 0,
            u"memoryUsedPc": 4.27,
            u"cpuUsedPc": 4,
            u"id": 0,
            u"rss": 329184
        }
    ]
}

# Sample RDSOS output from a SQL Server instance
sql_server_dict = {
    u"engine": u"SqlServer",
    u"instanceID": u"trevor",
    u"instanceResourceID": u"db-YWCA2G6UQEA3NYZ54IS6XEBGUE",
    u"timestamp": u"2017-09-12T23:58:59Z",
    u"version": 1,
    u"uptime": u"0 days, 00:10:43",
    u"numVCPUs": 1,
    u"cpuUtilization": {
        u"idle": 64.13,
        u"kern": 11.85,
        u"user": 24.01
    },
    u"memory": {
        u"commitTotKb": 1073308,
        u"commitLimitKb": 1572464,
        u"commitPeakKb": 1109112,
        u"physTotKb": 1048176,
        u"physAvailKb": 125072,
        u"sysCacheKb": 182448,
        u"kernTotKb": 192596,
        u"kernPagedKb": 136120,
        u"kernNonpagedKb": 56476,
        u"sqlServerTotKb": 123432,
        u"pageSize": 4096
    },
    u"system": {
        u"handles": 14874,
        u"threads": 634,
        u"processes": 44
    },
    u"disks": [
        {
            u"name": u"rdsdbdata",
            u"totalKb": 20838336,
            u"usedKb": 162752,
            u"usedPc": 0.78,
            u"availKb": 20675584,
            u"availPc": 99.22,
            u"rdCountPS": 0,
            u"rdBytesPS": 0,
            u"wrCountPS": 0,
            u"wrBytesPS": 0
        }
    ],
    u"network": [
        {
            u"interface": "Ethernet 2",
            u"rdBytesPS": 0,
            u"wrBytesPS": 0
        }
    ],
    u"processList": [
        {
            u"name": u"OS processes",
            u"cpuUsedPc": 0.3,
            u"memUsedPc": 8.46,
            u"workingSetKb": 249908,
            u"workingSetPrivKb": 88728,
            u"workingSetShareableKb": 161180,
            u"virtKb": 57985212532
        },
        {
            u"name": u"RDS processes",
            u"cpuUsedPc": 1.52,
            u"memUsedPc": 20.61,
            u"workingSetKb": 367720,
            u"workingSetPrivKb": 215996,
            u"workingSetShareableKb": 151724,
            u"virtKb": 4331792332
        },
        {
            u"name": u"sqlwriter.exe",
            u"pid": 1736,
            u"cpuUsedPc": 0,
            u"memUsedPc": 0.1,
            u"workingSetKb": 5876,
            u"workingSetPrivKb": 1020,
            u"workingSetShareableKb": 4856,
            u"virtKb": 38280
        },
        {
            u"name": u"fdlauncher.exe",
            u"pid": 2436,
            u"cpuUsedPc": 0,
            u"memUsedPc": 0.05,
            u"workingSetKb": 3576,
            u"workingSetPrivKb": 568,
            u"workingSetShareableKb": 3008,
            u"virtKb": 26776
        },
        {
            u"name": u"sqlservr.exe",
            u"pid": 3624,
            u"cpuUsedPc": 32.22,
            u"memUsedPc": 11.12,
            u"workingSetKb": 158676,
            u"workingSetPrivKb": 116608,
            u"workingSetShareableKb": 42068,
            u"virtKb": 2694704
        },
        {
            u"name": u"sqlservr.exe",
            u"pid": 3624,
            u"tid": 3628,
            u"cpuUsedPc": 0
        },
        {
            u"name": u"sqlservr.exe",
            u"pid": 3624,
            u"tid": 3636,
            u"cpuUsedPc": 0
        },
        {
            u"name": u"sqlservr.exe",
            u"pid": 3624,
            u"tid": 3644,
            u"cpuUsedPc": 0
        },
        {
            u"name": u"sqlservr.exe",
            u"pid": 3624,
            u"tid": 3648,
            u"cpuUsedPc": 0
        },
        {
            u"name": u"sqlservr.exe",
            u"pid": 3624,
            u"tid": 3660,
            u"cpuUsedPc": 0
        },
        {
            u"name": u"sqlservr.exe",
            u"pid": 3624,
            u"tid": 3664,
            u"cpuUsedPc": 0
        },
        {
            u"name": u"sqlservr.exe",
            u"pid": 3624,
            u"tid": 3668,
            u"cpuUsedPc": 0
        },
        {
            u'name': u"sqlservr.exe",
            u"pid": 3624,
            u"tid": 3672,
            u"cpuUsedPc": 32.22
        },
        {
            u"name": u"sqlservr.exe",
            u"pid": 3624,
            u"tid": 3676,
            u"cpuUsedPc": 0
        },
        {
            u"name": u"sqlservr.exe",
            u"pid": 3624,
            u"tid": 3680,
            u"cpuUsedPc": 0
        },
    ]
}

# Sample RDSOS output for an Aurora instance
aurora_dict = {
    u"engine": u"Aurora",
    u"instanceID": u"trevor",
    u"instanceResourceID": u"db-F3AZGY5JTAS65TT4E7U3CDS6AM",
    u"timestamp": u"2017-09-12T23:02:53Z",
    u"version": 1,
    u"uptime": u"0:44:23",
    u"numVCPUs": 1,
    u"cpuUtilization": {
        u"guest": 0,
        u"irq": 0.04,
        u"system": 1.86,
        u"wait": 2.61,
        u"idle": 90.08,
        u"user": 5.01,
        u"total": 9.92,
        u"steal": 0.36,
        u"nice": 0.04
    },
    u"loadAverageMinute": {
        u"fifteen": 0.13,
        u"five": 0.1,
        u"one": 0.3
    },
    u"memory": {
        u"writeback": 0,
        u"hugePagesFree": 1024,
        u"hugePagesRsvd": 0,
        u"hugePagesSurp": 0,
        u"cached": 489508,
        u"hugePagesSize": 2048,
        u"free": 99192,
        u"hugePagesTotal": 367616,
        u"inactive": 260216,
        u"pageTables": 6244,
        u"dirty": 1400,
        u"mapped": 84816,
        u"active": 890436,
        u"total": 2052380,
        u"slab": 38916,
        u"buffers": 67024
    },
    u"tasks": {
        u"sleeping": 233,
        u"zombie": 0,
        u"running": 2,
        u"stopped": 0,
        u"total": 235,
        u"blocked": 0
    },
    u"swap": {
        u"cached": 0,
        u"total": 0,
        u"free": 0
    },
    u"network": [
        {
            u"interface": u"eth0",
            u"rx": 58724202.3,
            u"tx": 2613197.9
        }
    ],
    u"diskIO": [
        {
            u"readLatency": 2.74,
            u"writeLatency": 1.5,
            u"writeThroughput": 476409.8,
            u"readThroughput": 665190.4,
            u"readIOsPS": 40.6,
            u"diskQueueDepth": 0,
            u"writeIOsPS": 1426.8
        }
    ],
    u"fileSys": [
        {
            u"used": 68956,
            u"name": u"rdsfilesys",
            u"usedFiles": 211,
            u"usedFilePercent": 0.01,
            u"maxFiles": 2097152,
            u"mountPoint": u"/rdsdbdata",
            u"total": 32890736,
            u"usedPercent": 0.21
        }
    ],
    u"processList": [
        {
            u"vss": 1232180,
            u"name": u"aurora",
            u"tgid": 5439,
            u"vmlimit": 2052380,
            u"parentID": 1,
            u"memoryUsedPc": 12.47,
            u"cpuUsedPc": 0,
            u"id": 5439,
            u"rss": 255908
        },
        {
            u"vss": 691648,
            u"name": u"OS processes",
            u"tgid": 0,
            u"vmlimit": u"",
            u"parentID": 0,
            u"memoryUsedPc": 1.15,
            u"cpuUsedPc": 0,
            u"id": 0,
            u"rss": 23888
        },
        {
            u"vss": 3247344,
            u"name": u"RDS processes",
            u"tgid": 0,
            u"vmlimit": u"",
            u"parentID": 0,
            u"memoryUsedPc": 20.91,
            u"cpuUsedPc": 0,
            u"id": 0,
            u"rss": 429908
        }
    ]
}
