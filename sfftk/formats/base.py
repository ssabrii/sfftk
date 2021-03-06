# -*- coding: utf-8 -*-
# base.py
"""
sfftk.formats.base
==================

Generic application-specific segmentation file format (GAS-SFF)

Keep it as simple as possible. Assignment to attributes is done directly. Uses 
basic data structures (lists, dicts, tuples). Defines global attributes and methods.

We define a single segmentation container consisting of two top-level containers:

- a header container that holds all top-level non-segment data

- a list of segment containers

Each segment container has two main parts:

- an annotation container that lists all non-geometric descriptions i.e. textual, logical descriptions

- the actual geometric container that can either be meshes, contours, a volume or shapes

"""
from __future__ import division

__author__ = "Paul K. Korir, PhD"
__email__ = "pkorir@ebi.ac.uk, paul.korir@gmail.com"
__date__ = "2017-03-28"
__updated__ = '2018-02-14'


class SegmentationType(object):
    """Base class for all segmentation classes"""

    def convert(self, *args, **kwargs):
        """Method to implement conversion to EMDB-SFF using the intermediary API.
        
        :param str name: optional name of the segmentation used in <name/>
        :param str softwareVersion: optional software version for Amira use in <software><version/></software>
        :param str processingDetails: optional processings used in Amira used in <software><processingDetails/></software>
        :param str details: optional details associated with this segmentation used in <details/> 
        
        Implementations of this method within converters can do only two things:
        
        - use objects in the schema API
        - call objects locally extended from the formats API
        """
        raise NotImplementedError

    def __repr__(self):
        return str(self.__class__)

    def __str__(self):
        return str(self.__class__)


class SegmentFormat(SegmentationType):
    """Base class for all segmentation geometrical representation formats"""
    format = None

    def __init__(self, *args, **kwargs):
        super(SegmentFormat, self).__init__(*args, **kwargs)


class Mesh(SegmentFormat):
    """``meshList`` segmentation"""
    format = 'mesh'

    def __init__(self, *args, **kwargs):
        super(Mesh, self).__init__(*args, **kwargs)


class Contours(SegmentFormat):
    """``contourList`` segmentation"""
    format = 'contours'

    def __init__(self, *args, **kwargs):
        super(Contours, self).__init__(*args, **kwargs)


class Shapes(SegmentFormat):
    """``shapePrimitiveList`` segmentation"""
    format = 'shapes'

    def __init__(self, *args, **kwargs):
        super(Shapes, self).__init__(*args, **kwargs)


class Volume(SegmentFormat):
    """``threeDVolume`` segmentation"""
    format = 'volume'

    def __init__(self, *args, **kwargs):
        super(Volume, self).__init__(*args, **kwargs)


class Segment(SegmentationType):
    """Base class for segment classes"""
    annotation = None
    meshes = None
    contours = None
    volume = None
    shapes = None

    def __repr__(self):
        formats = list()
        if self.meshes: formats.append(self.meshes.format)
        if self.contours: formats.append(self.contours.format)
        if self.volume: formats.append(self.volume.format)
        if self.shapes: formats.append(self.shapes.format)
        return "Segment of format(s): {}".format(', '.join(formats))


class Annotation(SegmentationType):
    """Base class for all biological annotation classes"""
    pass


class Header(SegmentationType):
    """Base class for all header classes (for metadata)"""
    pass


class Segmentation(SegmentationType):
    """Base class for a segmentation"""
    header = None
    segments = list()
