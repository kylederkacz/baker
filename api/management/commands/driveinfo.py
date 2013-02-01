import subprocess
import re

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    fdisk_regex = '''
(?:Disk\s+(?P<disk>[^:]*)\:\s+(?P<size>[\w\.\ ]+),\s+(?P<bytes>\d+)\s+bytes
\s+(?P<heads>\d+)\sheads,\s+(?P<sectors_per_track>\d+)\s+sectors/track,\s+(?P<cylinders>\d+)\s+cylinders,\s+total\s+(?P<total_sectors>\d+)\s+sectors
\s+.*
\s+.*
\s+.*
\s+.*
\s*
(?:.+)+\s+
(?P<partitions>(?:.+\s)+))+
'''

    partition_regex = r'''
(?P<device>\S+)\s+
(?P<is_boot>[\*]{0,1})\s+
(?P<start_sector>\d+)\s+
(?P<end_sector>\d+)\s+
(?P<total_blocks>[\d\+]+)\s+
(?P<fs_type>\w+)\s+
(?P<system>.+)\s*
'''

    def handle(self, *args, **options):
        return self.execute(*args, **options)

    def execute(self, *args, **options):
        blkid_output = subprocess.check_output('/Users/kylederkacz/blkid')
        partitions = self._parse_blkid_output(blkid_output)
        df_output = subprocess.check_output(['/Users/kylederkacz/df', '-k'])
        partitions = self._parse_df_output(df_output, partitions)

        fdisk = re.compile(self.fdisk_regex, flags=re.MULTILINE | re.VERBOSE)
        partition = re.compile(self.partition_regex, flags=re.MULTILINE | re.VERBOSE)
        drives = {}
        for match in fdisk.finditer(subprocess.check_output(['/Users/kylederkacz/fdisk', '-l'])):
            data = match.groupdict()
            parts = []
            if 'partitions' in data.keys() and data['partitions']:
                for p in partition.finditer(data['partitions']):
                    p_data = p.groupdict()
                    if p_data['device'] in partitions.keys():
                        p_data.update(partitions[p_data['device']])
                    parts.append(p_data)
            data['partitions'] = parts
            drives[data['disk']] = data

        import pprint
        pprint.pprint(drives)

        return drives

    def _parse_df_output(self, output, drives):
        for line in output.splitlines()[1:]:
            drive = {}
            parts = line.split()
            drive['mount_point'] = parts.pop()
            drive['usage'] = parts.pop()
            drive['available_space'] = parts.pop()
            drive['used_space'] = parts.pop()
            drive['total_size'] = parts.pop()
            drive['file_system'] = ' '.join(parts)
            if drive['file_system'] in drives.keys():
                drives[drive['file_system']].update(drive)
        return drives

    def _parse_blkid_output(self, output):
        drives = {}
        for line in output.splitlines():
            parts = line.split(':', 1)
            values = [value.split('=') for value in parts[1].strip().replace('"', '').split()]
            values = [(key.lower(), value) for key, value in values]
            drives[parts[0]] = dict(values)
        return drives
