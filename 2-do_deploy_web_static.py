#!/usr/bin/python3

from fabric.api import *
import os.path
from fabric.operations import run, put, sudo

#env.user = 'ubuntu'

env.hosts = ['35.243.204.121', '35.237.251.153' ]
def do_deploy(archive_path):
    if (os.path.isfile(archive_path) is False):
        print("path doesnt exist!")
        return False

    try:
        archived = archive_path.split("/")[:-1]
        new_path = ("/data/web_static/releases/" + archived.split(".")[0])
        put(archive_path, "/tmp/")
            
        run("sudo mkdir {}".format(new_path))
            
        run('sudo tar -xzf /tmp/{} -C {}'.format(archived, new_path))
        run('sudo rm -rf /tmp/{}'.format(archived))
            
        run("sudo mv {}/web_static/* {}/".format(new_path, new_path))
        run("sudo rm -rf {}/web_static".format(new_path))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(new_path))

        print("success!")
        return True
    except:
        print("Failed!")
        return False
