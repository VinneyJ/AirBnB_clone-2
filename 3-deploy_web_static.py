#!/usr/bin/python3
from fabric.api import *
import time
import os.path

env.hosts = ['35.243.204.121', '35.237.251.153']


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


def do_deploy(archive_path):
    """
       upload the compressed file and
       unzip it in the particular server remove
       unwated directories and create a symlink
    """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        archived = archive_path.split("/")[-1]
        new_path = ("/data/web_static/releases/" + archived.split(".")[0])
        put(archive_path, "/tmp/")

        run("sudo mkdir -p {}".format(new_path))

        run("sudo tar -xzf /tmp/{} -C {}".format(archived, new_path))
        run("sudo rm -rf /tmp/{}".format(archived))
        run("sudo mv {}/web_static/* {}/".format(new_path, new_path))
        run("sudo rm -rf {}/web_static".format(new_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_path))

        return True
    except:
        return False


def deploy():
    try:
        archive_path = do_pack()
        value = do_deploy(archive_path)
        return value
    except:
        return False
