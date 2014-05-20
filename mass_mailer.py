#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zhoubangtao'

import wx
import wx.lib.buttons
import cPickle
import os


class MassMailer(wx.Window):
  def __init__(self, parent, id):
    wx.Window.__init__(self, parent, id)
    #self.SetBackgroundColour("Red")
    self.color = "Green"
    self.thickness = 10

    #创建一个画笔
    self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)
    self.lines = []
    self.curLine = []
    self.pos = (0, 0)
    self.InitBuffer()

    #连接事件
    self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
    self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
    self.Bind(wx.EVT_MOTION, self.OnMotion)
    self.Bind(wx.EVT_SIZE, self.OnSize)
    self.Bind(wx.EVT_IDLE, self.OnIdle)
    self.Bind(wx.EVT_PAINT, self.OnPaint)


