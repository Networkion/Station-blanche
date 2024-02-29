#!usr/bin/env python3
# coding:utf-8

import os
from yara_scanner import YaraScanner


class Scanner(object):

    def __init__(self):
        self.scanner = YaraScanner()
        self.scanner.track_yara_dir('module/yara/rules')

    def load_rules(self):
        self.scanner.load_rules()
        return "Rules loaded"

    def scan_file(self, directory):
        directory = os.path.abspath(directory)

        if self.scanner.scan(directory):
            return self.scanner.scan_results
