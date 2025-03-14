#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""
from fabric.api import env, put, run
import os.path

env.hosts = ['<IP web-01>', 'IP web-02']  # Replace with your server IPs


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload archive
        file_name = os.path.basename(archive_path)
        name_without_ext = file_name.split('.')[0]
        put(archive_path, "/tmp/{}".format(file_name))

        # Create target directory
        run("mkdir -p /data/web_static/releases/{}/".format(name_without_ext))

        # Uncompress archive
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, name_without_ext))

        # Remove archive
        run("rm /tmp/{}".format(file_name))

        # Move files up one level
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name_without_ext, name_without_ext))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(name_without_ext))

        # Remove old symbolic link and create new one
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name_without_ext))

        return True
    except:
        return False