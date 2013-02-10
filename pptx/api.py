# -*- coding: utf-8 -*-
#
# api.py
#
# Copyright (C) 2012, 2013 Steve Canny scanny@cisco.com
#
# This module is part of python-pptx and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""
Directly exposed API classes, Presentation for now. Provides some syntactic
sugar for interacting with the pptx.presentation.Package graph and also
provides some insulation so not so many classes in the other modules need to
be named as internal (leading underscore).
"""

from pptx.presentation import Package

class Presentation(object):
    """
    Return a |Presentation| instance loaded from ``.pptx`` file at *path*. If
    *path* is missing or ``None``, load the built-in default presentation
    template.
    """
    def __init__(self, path=None):
        super(Presentation, self).__init__()
        self.__package = Package(path)
        self.__presentation = self.__package.presentation
    
    @property
    def slidelayouts(self):
        """
        Tuple containing the :class:`SlideLayout` instances belonging to the
        first :class:`SlideMaster` of this presentation.
        """
        return tuple(self.__presentation.slidemasters[0].slidelayouts)
    
    @property
    def slidemaster(self):
        """
        First :class:`SlideMaster` object belonging to this presentation.
        """
        return self.__presentation.slidemasters[0]
    
    @property
    def slidemasters(self):
        """
        List of :class:`SlideMaster` objects belonging to this presentation.
        """
        return self.__presentation.slidemasters
    
    @property
    def slides(self):
        """
        :class:`SlideCollection` object containing the slides in this
        presentation.
        """
        return self.__presentation.slides
    
    def save(self, path):
        """
        Save this presentation at *path*.
        """
        return self.__package.save(path)
    


