#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""
from fabric.api import env, local, put, run
from datetime import datetime
import os.path

env.hosts = ['<IP web-01>', 'IP web-02']  # Replace with your server IPs


def do_pack():
    """
    Generates a .tgz archive from the contents of web_static folder
    """
    try:
        if not os.path.exists("versions"):
            local("mkdir -p versions")
        now = datetime.now()
        archive_name = "versions/web_static_{}.tgz".format(
            now.strftime("%Y%m%d%H%M%S"))
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        name_without_ext = file_name.split('.')[0]
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p /data/web_static/releases/{}/".format(name_without_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, name_without_ext))
        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name_without_ext, name_without_ext))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(name_without_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name_without_ext))
        return True
    except:
        return False


def deploy():
    """
    Creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)