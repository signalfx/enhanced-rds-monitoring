"""
    The default structure(s) of the metric payloads delivered to the Lambda. Note that the Aurora section only contains
    the structures in which there is meaningful difference from the standard version.
"""

# Standard set of metric info
METRICS = [
    u'cpuUtilization',
    u'diskIO',
    u'fileSys',
    u'loadAverageMinute',
    u'memory',
    u'network',
    u'swap',
    u'tasks',
    u'OSprocesses',
    u'RDSprocesses'
]

PROCESS_METRICS = [
    u'vss',
    u'rss',
    u'memoryUsedPc',
    u'cpuUsedPc'
]

METRICS_DIMS = {
    u'diskIO': [u'device'],
    u'fileSys': [u'name', u'mountPoint'],
    u'network': [u'interface']
}

# Metric info for Aurora instances.
METRICS_AURORA_DIMS = {
    u'diskIO': [],  # This is a workaround to account for the way Aurora sends diskIO metrics (which isn't even listed on their offered metrics)
    u'fileSys': [u'name', u'mountPoint'],
    u'network': [u'interface']
}

# Metric info for Microsoft SQL instances.
METRICS_MICROSOFT = [
    u'cpuUtilization',
    u'disks',
    u'memory',
    u'network',
    u'OSprocesses',
    u'RDSprocesses',
    u'system'
]

PROCESS_METRICS_MICROSOFT = [
    u'cpuUsedPc',
    u'memUsedPc',
    u'workingSetKb',
    u'workingSetPrivKb',
    u'workingSetShareableKb',
    u'virtKb'
]

METRICS_MICROSOFT_DIMS = {
    u'disks': [u'name'],
    u'network': [u'interface']
}
