#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by nirm03
# Copyright (c) 2013 nirm03
#
# License: MIT
#

"""This module exports the Cs162 plugin class."""

from SublimeLinter.lint import Linter
import sublime


class Cs162(Linter):

    """Provides an interface to clang."""

    syntax = ('c', 'c improved', 'c++', 'c++11')
    executable = 'curl'

    @property
    def regex(self):
        from re import compile, escape
        filename_full = sublime.active_window().active_view().file_name()
        filename_twoup =  '/'.join(filename_full.rsplit('/', 2)[-2:])
        return compile(r'.*' + escape(filename_twoup) + r':(?P<line>\d+):'
            r'((?P<col>\d*): )?'# column number, colon and space are only applicable for single line messages
            # several lines of anything followed by
            # either error/warning/note or newline (= irrelevant backtrace content)
            # (lazy quantifiers so we don’t skip what we seek)
            r'(.*?((?P<error>error)|(?P<warning>warning|note)|\r?\n))+?'
            r': (?P<message>.+)'# match the remaining content of the current line for output
        )


    multiline = True

    def cmd(self):
        """
        Return the command line to execute.

        We override this method, so we can add extra flags and include paths
        based on the 'include_dirs' and 'extra_flags' settings.

        """

        return 'curl -s http://192.168.162.162:16280'
