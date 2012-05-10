# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2011, Martín Raúl Villalba
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
##############################################################################

import os
import codecs

ORG_ROOT = os.path.expanduser('~/nts/org/')
INBOX_NORMAL = ORG_ROOT + 'N-INBOX'
INBOX_URGENT = ORG_ROOT + 'U-INBOX'

#---------------------------#
# INBOX file spec:          #
# PRJ-SPC> Note line 1      #
#   Optional extra line     #
#   prepended with 2 or     #
#   more whitespaces        #
# [more notes or EOF]       #
#---------------------------#

class Inbox(object):
    path = ''
    notes = []

    def __init__(self, path=None, default_prjspec=u''):
        self.prjspec = default_prjspec
        if path:
            self.loadFile(path)

    def load(self, path):
        return self.loadFile(path)

    def loadFile(self, path):
        ibx = codecs.open(path, 'r', 'utf-8')
        data = ibx.read()
        ibx.close()
        self.loadString(data)
        self.path = path
        return self.notes

    def loadString(self, data):
        note = u''
        prjspec = u''
        notelist = []
        for line in (data + u"\n@#@EOF-MAGIC@#@").split("\n"):
            if line == u'' or line == u' ' or line[0:2] == u'  ':
                note += u'\n' + line.strip()
                continue
            if note.strip().strip(u'\n') != u'':
                notelist.append([prjspec, note.strip().strip(u'\n')])
            splits = line.split(u'>')
            if len(splits) == 1:
                splits = [self.prjspec] + splits
            if splits[0].strip().find(u' ') != -1 or splits[0] == u'':
                splits[0] = self.prjspec
            prjspec = splits[0].strip()
            note = line
        self.notes += notelist
        return self.notes

    def addNotes(self, data):
        self.notes += data

    def dump(self, path):
        return self.dumpFile(data)

    def dumpFile(self, path):
        pass

    def dumpString(self):
        pass
