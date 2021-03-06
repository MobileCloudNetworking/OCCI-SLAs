#!/usr/bin/env python
#
# Copyright (c) 2015 Intel Innovation and Research Ireland Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import threading
import logging
from wsgiref.simple_server import make_server

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

class OcciServer(threading.Thread):

    def __init__(self, api):
        super(OcciServer, self ).__init__()
        self.httpd = make_server('127.0.0.1', 8888, api)

    def run(self):
        LOG.info("Starting OCCI server on port 8888")
        self.httpd.serve_forever(poll_interval=0.5)

    def stop(self):
        self.httpd.shutdown()
        self.httpd.server_close()
