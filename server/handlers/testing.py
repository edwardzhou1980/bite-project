# Copyright 2010 Google Inc. All Rights Reserved.
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

"""Testing handlers for the HUD project.

Used to expose some of the server internal contructs to facilitate manual
testing and debugging.
"""

__author__ = 'alexto@google.com (Alexis O. Torres)'

import sys
import webapp2

from google.appengine.api import memcache

from common.handlers import base


class FlushCacheHandler(base.BaseHandler):
  """Flushes memcache."""

  # Disable 'Invalid method name' lint error.
  # pylint: disable-msg=C6409
  def get(self):
    result = memcache.flush_all()
    self.response.out.write('Flush success status: <b>%s</b>' % result)


app = webapp2.WSGIApplication(
    [('/testing/flush_cache', FlushCacheHandler)],
    debug=True)

