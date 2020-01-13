import unittest
from sample_input import my_sql_dict, sql_server_dict, aurora_dict
from enhanced_rds.lambda_script import pull_metric_names, parse_logs


class TestLambdaComponents(unittest.TestCase):

    STANDARD_METRICS_CHECK = [
        'cpuUtilization.total',
        'loadAverageMinute.one',
        'memory.cached',
        'tasks.total',
        'swap.free',
        'network.tx',
        'diskIO.await',
        'fileSys.total',
        'OSprocesses.cpuUsedPc'
    ]

    SQL_SERVER_METRICS_CHECK = [
        'cpuUtilization.kern',
        'memory.kernPagedKb',
        'system.handles',
        'disks.availPc',
        'network.rdBytesPS',
        'RDSprocesses.workingSetPrivKb'
    ]

    AURORA_METRICS_CHECK = [
        'cpuUtilization.steal',
        'loadAverageMinute.fifteen',
        'memory.slab',
        'tasks.sleeping',
        'swap.total',
        'network.rx',
        'diskIO.writeThroughput',
        'fileSys.maxFiles',
        'OSprocesses.vss'
    ]

    def check_common_elements_standard(self, entry):
        dimensions = entry['dimensions']
        self.assertEqual(
            dimensions['instanceResourceID'],
            'db-H4UK4SA7E62QPMAYTMPK5XWETQ',
            'Incorrect instance resource id'
        )
        self.assertEqual(
            dimensions['AWSUniqueId'],
            'rds_ppr9b9oge80i99_us-east-1_1',
            'Incorrect AWSUniqueId dimension'
        )
        self.assertEqual(
            dimensions['Namespace'],
            'AWS/RDS',
            'Incorrect namespace dimension'
        )
        self.assertEqual(
            dimensions['EngineName'],
            'MYSQL',
            'Incorrect db engine name'
        )
        self.assertIsInstance(
            entry['timestamp'],
            int,
            'Timestamp not an integer'
        )

    def check_common_elements_sql_server(self, entry):
        dimensions = entry['dimensions']
        self.assertEqual(
            dimensions['instanceResourceID'],
            'db-YWCA2G6UQEA3NYZ54IS6XEBGUE',
            'Incorrect instance resource id'
        )
        self.assertEqual(
            dimensions['AWSUniqueId'],
            'rds_trevor_us-west-2_1',
            'Incorrect AWSUniqueId dimension'
        )
        self.assertEqual(
            dimensions['Namespace'],
            'AWS/RDS',
            'Incorrect namespace dimension'
        )
        self.assertEqual(
            dimensions['EngineName'],
            'SqlServer',
            'Incorrect db engine name'
        )
        self.assertIsInstance(
            entry['timestamp'],
            int,
            'Timestamp not an integer'
        )

    def check_common_elements_aurora(self, entry):
        dimensions = entry['dimensions']
        self.assertEqual(
            dimensions['instanceResourceID'],
            'db-F3AZGY5JTAS65TT4E7U3CDS6AM',
            'Incorrect instance resource id'
        )
        self.assertEqual(
            dimensions['AWSUniqueId'],
            'rds_trevor_eu-west-1_1234',
            'Incorrect AWSUniqueId dimension'
        )
        self.assertEqual(
            dimensions['Namespace'],
            'AWS/RDS',
            'Incorrect namespace dimension'
        )
        self.assertEqual(
            dimensions['EngineName'],
            'Aurora',
            'Incorrect db engine name'
        )
        self.assertIsInstance(
            entry['timestamp'],
            int,
            'Timestamp not an integer'
        )

    def grab_metrics(self, entries, checklist):
        entry_dict = {}

        for entry in entries:
            metric_name = entry['metric']
            if metric_name in checklist:
                entry_dict[metric_name] = entry

            if len(entry_dict.keys()) == len(checklist):
                return entry_dict

    def test_standard_parsing(self):
        desired_metrics_info = pull_metric_names(my_sql_dict['engine'])
        metric_entries = parse_logs(
            '1',
            'arn:aws:lambda:us-east-1:946288580872:function:testRDSLambda',
            my_sql_dict,
            *desired_metrics_info
        )

        first_entry = metric_entries[0]
        self.check_common_elements_standard(first_entry)

        # Grab the metrics we want
        metrics_to_check = self.grab_metrics(
            metric_entries,
            self.STANDARD_METRICS_CHECK
        )

        # Check each for the desired specifics
        cpu_util = metrics_to_check['cpuUtilization.total']
        self.check_common_elements_standard(cpu_util)
        self.assertEqual(cpu_util['value'], 21.01, 'Incorrect cpuUtil.total')

        load_avg = metrics_to_check['loadAverageMinute.one']
        self.check_common_elements_standard(load_avg)
        self.assertEqual(load_avg['value'], 0.29,
                         'Incorrect loadAverageMinute.one')

        memory_cached = metrics_to_check['memory.cached']
        self.check_common_elements_standard(memory_cached)
        self.assertEqual(
            memory_cached['value'],
            3288068,
            'Incorrect memory.cached'
        )

        tasks_total = metrics_to_check['tasks.total']
        self.check_common_elements_standard(tasks_total)
        self.assertEqual(tasks_total['value'], 262, 'Incorrect tasks.total')

        swap_free = metrics_to_check['swap.free']
        self.check_common_elements_standard(swap_free)
        self.assertEqual(swap_free['value'], 7703160, 'Incorrect swap.free')

        network_tx = metrics_to_check['network.tx']
        self.check_common_elements_standard(network_tx)
        self.assertEqual(network_tx['value'], 2856222, 'Incorrect network.tx')
        self.assertEqual(
            network_tx['dimensions']['interface'],
            'eth0',
            'Incorrectly parsed network metrics'
        )

        diskio_await = metrics_to_check['diskIO.await']
        self.check_common_elements_standard(diskio_await)
        self.assertEqual(diskio_await['value'], 1.6, 'Incorrect diskIO.await')
        self.assertEqual(
            diskio_await['dimensions']['device'],
            'rdsdev',
            'Incorrectly parsed diskIO metrics'
        )

        filesys_total = metrics_to_check['fileSys.total']
        self.check_common_elements_standard(filesys_total)
        self.assertEqual(
            filesys_total['value'],
            103053476,
            'Incorrect fileSys.total'
        )
        self.assertEqual(
            filesys_total['dimensions']['name'],
            'rdsfilesys',
            'Incorrectly parsed filesys metrics'
        )
        self.assertEqual(
            filesys_total['dimensions']['mountPoint'],
            '/rdsdbdata',
            'Incorrectly parsed filesys metrics'
        )

        os_processes_cpu = metrics_to_check['OSprocesses.cpuUsedPc']
        self.check_common_elements_standard(os_processes_cpu)
        self.assertEqual(
            os_processes_cpu['value'],
            0.5,
            'Incorrectly parsed process metrics'
        )

    def test_sql_server_parsing(self):
        desired_metrics_info = pull_metric_names(sql_server_dict['engine'])
        metric_entries = parse_logs(
            '1',
            'arn:aws:lambda:us-west-2:845296:function:testSqlServer',
            sql_server_dict,
            *desired_metrics_info
        )

        first_entry = metric_entries[0]
        self.check_common_elements_sql_server(first_entry)

        # Grab the metrics we want
        metrics_to_check = self.grab_metrics(
            metric_entries,
            self.SQL_SERVER_METRICS_CHECK
        )

        # Check each for the desired specifics
        cpu_util = metrics_to_check['cpuUtilization.kern']
        self.check_common_elements_sql_server(cpu_util)
        self.assertEqual(cpu_util['value'], 11.85, 'Incorrect cpuUtil.kern')

        memory_kern_paged_kb = metrics_to_check['memory.kernPagedKb']
        self.check_common_elements_sql_server(memory_kern_paged_kb)
        self.assertEqual(
            memory_kern_paged_kb['value'],
            136120,
            'Incorrect memory.kernPagedKb'
        )

        system_handles = metrics_to_check['system.handles']
        self.check_common_elements_sql_server(system_handles)
        self.assertEqual(
            system_handles['value'],
            14874,
            'Incorrect system.handles'
        )

        disks_avail_pc = metrics_to_check['disks.availPc']
        self.check_common_elements_sql_server(disks_avail_pc)
        self.assertEqual(
            disks_avail_pc['value'],
            99.22,
            'Incorrect disks.availPc'
        )
        self.assertEqual(
            disks_avail_pc['dimensions']['name'],
            'rdsdbdata',
            'Incorrectly parsed disks metrics'
        )

        network_rd_bytes_ps = metrics_to_check['network.rdBytesPS']
        self.check_common_elements_sql_server(network_rd_bytes_ps)
        self.assertEqual(
            network_rd_bytes_ps['value'],
            0,
            'Incorrect network.rdBytesPS'
        )
        self.assertEqual(
            network_rd_bytes_ps['dimensions']['interface'],
            'Ethernet 2',
            'Incorrectly parsed network metrics'
        )

        rds_processes_working_set_priv_kb =\
            metrics_to_check['RDSprocesses.workingSetPrivKb']
        self.check_common_elements_sql_server(
            rds_processes_working_set_priv_kb
        )
        self.assertEqual(
            rds_processes_working_set_priv_kb['value'],
            215996,
            'Incorrect RDSprocesses.workingSetPrivKb'
        )

    def test_aurora_parsing(self):
        desired_metrics_info = pull_metric_names(aurora_dict['engine'])
        metric_entries = parse_logs(
            '1234',
            'arn:aws:lambda:eu-west-1:098712340987:function:testAurora',
            aurora_dict,
            *desired_metrics_info
        )

        first_entry = metric_entries[0]
        self.check_common_elements_aurora(first_entry)

        # Grab the metrics we want
        metrics_to_check = self.grab_metrics(
            metric_entries,
            self.AURORA_METRICS_CHECK
        )

        # Check each for the desired specifics
        cpu_util = metrics_to_check['cpuUtilization.steal']
        self.check_common_elements_aurora(cpu_util)
        self.assertEqual(cpu_util['value'], 0.36, 'Incorrect cpuUtil.steal')

        load_average_minute_fifteen =\
            metrics_to_check['loadAverageMinute.fifteen']
        self.check_common_elements_aurora(load_average_minute_fifteen)
        self.assertEqual(
            load_average_minute_fifteen['value'],
            0.13,
            'Incorrect loadAverageMinute.fifteen'
        )

        memory_slab = metrics_to_check['memory.slab']
        self.check_common_elements_aurora(memory_slab)
        self.assertEqual(memory_slab['value'], 38916, 'Incorrect memory.slab')

        tasks_sleeping = metrics_to_check['tasks.sleeping']
        self.check_common_elements_aurora(tasks_sleeping)
        self.assertEqual(
            tasks_sleeping['value'],
            233,
            'Incorrect tasks.sleeping'
        )

        swap_total = metrics_to_check['swap.total']
        self.check_common_elements_aurora(swap_total)
        self.assertEqual(swap_total['value'], 0, 'Incorrect swap.total')

        network_rx = metrics_to_check['network.rx']
        self.check_common_elements_aurora(network_rx)
        self.assertEqual(
            network_rx['value'],
            58724202.3,
            'Incorrect network.rx'
        )
        self.assertEqual(
            network_rx['dimensions']['interface'],
            'eth0',
            'Incorrectly parsed network metrics'
        )

        diskio_write_throughput = metrics_to_check['diskIO.writeThroughput']
        self.check_common_elements_aurora(diskio_write_throughput)
        self.assertEqual(
            diskio_write_throughput['value'],
            476409.8,
            'Incorrect diskIO.writeThroughput'
        )
        self.assertEqual(
            len(diskio_write_throughput['dimensions'].keys()),
            4,
            'Incorrectly parsed diskIO metrics'
        )

        filesys_max_files = metrics_to_check['fileSys.maxFiles']
        self.check_common_elements_aurora(filesys_max_files)
        self.assertEqual(
            filesys_max_files['value'],
            2097152,
            'Incorrect fileSys.maxFiles'
        )
        self.assertEqual(
            filesys_max_files['dimensions']['name'],
            'rdsfilesys',
            'Incorrectly parsed fileSys metrics'
        )
        self.assertEqual(
            filesys_max_files['dimensions']['mountPoint'],
            '/rdsdbdata',
            'Incorrectly parsed fileSys metrics'
        )

        os_processes_vss = metrics_to_check['OSprocesses.vss']
        self.check_common_elements_aurora(os_processes_vss)
        self.assertEqual(
            os_processes_vss['value'],
            691648,
            'Incorrect OSprocesses.vss'
        )


if __name__ == '__main__':
    unittest.main()
