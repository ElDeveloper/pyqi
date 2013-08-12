#!/usr/bin/env python

#-----------------------------------------------------------------------------
# Copyright (c) 2013, The BiPy Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------
from __future__ import division

__author__ = "Daniel McDonald"
__copyright__ = "Copyright 2013, The pyqi project"
__credits__ = ["Greg Caporaso", "Daniel McDonald", "Doug Wendel",
               "Jai Ram Rideout"]
__license__ = "BSD"
__version__ = "0.1.0-dev"
__maintainer__ = "Daniel McDonald"
__email__ = "wasade@gmail.com"

from unittest import TestCase, main
from pyqi.core.command import Parameter, ParameterCollection, Command
from pyqi.core.exception import IncompetentDeveloperError, UnknownParameter

class CommandTests(TestCase):
    def test_init(self):
        """Jog the init"""
        c = Command()
        self.assertEqual(len(c.Parameters), 0)
        with self.assertRaises(NotImplementedError):
            _ = c()

    def test_subclass_init(self):
        """Exercise the subclassing"""
        class foo(Command):
            Parameters = ParameterCollection([Parameter('a', str, 'help1',
                                                        Required=True),
                                              Parameter('b', str, 'help2',
                                                        Required=False)])
            def run(self, **kwargs):
                return {}

        obs = foo()

        self.assertEqual(len(obs.Parameters), 2)
        self.assertEqual(obs.run(bar={'a':10}), {})

class ParameterTests(TestCase):
    def test_init(self):
        """Jog the init"""
        obj = Parameter('a', str, 'help', Required=False)
        self.assertEqual(obj.Name, 'a')
        self.assertEqual(obj.DataType, str)
        self.assertEqual(obj.Description, 'help')
        self.assertEqual(obj.Required, False)
        self.assertEqual(obj.Default, None)
        self.assertEqual(obj.DefaultDescription, None)
        self.assertRaises(IncompetentDeveloperError, Parameter, 'a', str,
                          'help', True, 'x')


class ParameterCollectionTests(TestCase):
    def test_getattr(self):
        pc = ParameterCollection([Parameter('foo',str, 'help')])
        self.assertRaises(UnknownParameter, pc.__getitem__, 'bar')
        self.assertEqual(pc['foo'].Name, 'foo') # make sure we can getitem
        self.assertRaises(TypeError, pc.__setitem__, 'bar', 10)

    def test_setattr(self):
        pass
if __name__ == '__main__':
    main()
