#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
import caesar
import string

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = "Hello world!"
        encrypted_message = caesar.encrypt("Hello world",13)

        self.response.write(encrypted_message)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
