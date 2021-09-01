#!/usr/bin/python3
"""
compress the webstatic
"""
from fabric.api import local
import time


def do_pack():
    ''' creates a .tgz archive '''
    
    timestmp = time.strftime("%Y%m%d%H%M%S")
    try:
        local('mkdir -p versions')
        local('tar -cvzf versions/web_static_{}.tgz web_static/'
              .format(timestmp))
        return ('versions/web_static_{}.tgz'.format(timestmp))
    except:
        return None
