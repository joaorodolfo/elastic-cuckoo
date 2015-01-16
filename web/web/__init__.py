# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import sys
import os
from django.conf import settings

sys.path.append(settings.CUCKOO_PATH)

from lib.cuckoo.common.constants import CUCKOO_ROOT
from lib.cuckoo.common.config import Config

cfg = Config("reporting").elastic

# Checks if mongo reporting is enabled in Cuckoo.
if not cfg.get("enabled"):
    raise Exception("Elastic reporting module is not enabled in cuckoo, aborting!")

# Get connection options from reporting.conf.
settings.ELASTIC_HOST = cfg.get("host", "127.0.0.1")
settings.ELASTIC_PORT = cfg.get("port", 9200)
