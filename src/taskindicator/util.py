# encoding=utf-8

from __future__ import print_function

import calendar
import datetime
import json
import subprocess
import sys

import pygtk
pygtk.require("2.0")
import gtk

from taskindicator import taskw


def run_command(command):
    print("> %s" % " ".join(command), file=sys.stderr)
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    return p.communicate()[0]


def find_tasks(args):
    return taskw.Tasks()


def strip_description(text):
    if text.startswith("(bw)"):
        words = text.split(" ")
        text = " ".join(words[2:-2])
    return text


def get_icon_path(icon_name):
    theme = gtk.icon_theme_get_default()

    icon = theme.lookup_icon(icon_name, 0, 0)
    if icon:
        print("Found icon %s: %s" % (icon_name, icon.get_filename()),
            file=sys.stderr)
        return icon.get_filename()

    print("No icon named %s" % icon_name, file=sys.stderr)


def get_task_info(uuid):
    return taskw.Tasks()[uuid]


class UTC(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return datetime.timedelta(0)


def now():
    return datetime.datetime.now(UTC())
