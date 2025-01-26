#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of web_static
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of web_static folder
    """
    try:
        # Create versions directory if it doesn't exist
        if not os.path.exists("versions"):
            local("mkdir -p versions")

        # Create archive name using current timestamp
        now = datetime.now()
        archive_name = "versions/web_static_{}.tgz".format(
            now.strftime("%Y%m%d%H%M%S"))

        # Create archive
        local("tar -cvzf {} web_static".format(archive_name))

        # Return archive path if successful
        return archive_name
    except:
        return None