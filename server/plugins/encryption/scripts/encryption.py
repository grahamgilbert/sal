#!/usr/bin/python

import subprocess
import sys
sys.path.append('/usr/local/munki')
from munkilib import FoundationPlist
from munkilib import munkicommon
import os

def get_status(cmd, checkstring):
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except Exception, e:
        output = str(e.output)
    if checkstring in output:
        return 'Enabled'
    else:
        return 'Disabled'

def fv_status():
    cmd = ['/usr/bin/fdesetup', 'status']
    return get_status(cmd, 'FileVault is On.')

def main():

    if os.path.exists('/usr/bin/fdesetup'):
        filevault = fv_status()
    else:
        filevault = 'Not Supported'

    plist_path = '/usr/local/sal/plugin_results.plist'

    if os.path.exists(plist_path):
        plist = FoundationPlist.readPlist(plist_path)
    else:
        plist = []
    result = {}
    result['plugin'] = 'Encryption'
    result['historical'] = False
    data = {}
    data['Filevault'] = filevault
    result['data'] = data
    plist.append(result)
    FoundationPlist.writePlist(plist, plist_path)

if __name__ == '__main__':
    main()
