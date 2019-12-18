"""
    The default structure(s) of the metric payloads delivered to the Lambda.
    Note that the Aurora section only contains the structures in which there is
    meaningful difference from the standard version.
"""

# Standard set of metric info
METRICS = [
    'cpuUtilization',
    'diskIO',
    'fileSys',
    'loadAverageMinute',
    'memory',
    'network',
    'swap',
    'tasks',
    'OSprocesses',
    'RDSprocesses'
]

PROCESS_METRICS = [
    'vss',
    'rss',
    'memoryUsedPc',
    'cpuUsedPc'
]

METRICS_DIMS = {
    'diskIO': ['device'],
    'fileSys': ['name', 'mountPoint'],
    'network': ['interface']
}

# Metric info for Aurora instances.
METRICS_AURORA_DIMS = {
    'diskIO': [],  # Workaround to account for Aurora diskIO metrics
    'fileSys': ['name', 'mountPoint'],
    'network': ['interface']
}

# Metric info for Microsoft SQL instances.
METRICS_MICROSOFT = [
    'cpuUtilization',
    'disks',
    'memory',
    'network',
    'OSprocesses',
    'RDSprocesses',
    'system'
]

PROCESS_METRICS_MICROSOFT = [
    'cpuUsedPc',
    'memUsedPc',
    'workingSetKb',
    'workingSetPrivKb',
    'workingSetShareableKb',
    'virtKb'
]

METRICS_MICROSOFT_DIMS = {
    'disks': ['name'],
    'network': ['interface']
}
