#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zhoubangtao'

import wx
import wx.lib.buttons
import cPickle
import os
import config.settings

class MassMailer(wx.App):
  def OnInit(self):
    self.file = ''
    self.width = 600
    self.height = 480
    self.frame = wx.Frame(parent=None, title='MassMailer', size=(self.width, self.height))
    self.panel = wx.Panel(self.frame, -1)
    self.menu = MenuBar(self.frame)
    self.text = wx.TextCtrl(self.panel, -1, pos=(2, 2), size=(self.width - 10, self.height - 50),
                            style=wx.HSCROLL | wx.TE_MULTILINE)
    self.Bind(wx.EVT_MENU, self.OnOpen, self.menu.open)
    self.Bind(wx.EVT_MENU, self.OnSave, self.menu.save)
    self.Bind(wx.EVT_MENU, self.OnSaveAs, self.menu.saveas)
    self.Bind(wx.EVT_MENU, self.OnClose, self.menu.close)
    self.Bind(wx.EVT_MENU, self.OnUndo, self.menu.undo)
    self.Bind(wx.EVT_MENU, self.OnRedo, self.menu.redo)
    self.Bind(wx.EVT_MENU, self.OnCut, self.menu.cut)
    self.Bind(wx.EVT_MENU, self.OnCopy, self.menu.copy)
    self.Bind(wx.EVT_MENU, self.OnPaste, self.menu.paste)
    self.Bind(wx.EVT_MENU, self.OnSelectAll, self.menu.selectall)
    self.Bind(wx.EVT_MENU, self.OnColor, self.menu.color)
    self.Bind(wx.EVT_MENU, self.OnTrans, self.menu.trans)
    self.Bind(wx.EVT_MENU, self.OnAbout, self.menu.about)
    self.Bind(wx.EVT_RIGHT_DOWN, self.OnRClick)
    self.Bind(wx.EVT_SIZE, self.Resize)
    self.frame.Show()
    return True

class MenuBar(wx.Frame):
  def __init__(self, parent):
    self.menuBar = wx.MenuBar()
    self.file = wx.Menu()
    self.open = self.file.Append(-1, u'打开')
    self.save = self.file.Append(-1, u'保存')
    self.saveas = self.file.Append(-1, u'另存为')
    self.file.AppendSeparator()
    self.close = self.file.Append(-1, u'退出')
    self.menuBar.Append(self.file, u'文件(&F)')
    self.edit = wx.Menu()
    self.undo = self.edit.Append(-1, u'撤销')
    self.redo = self.edit.Append(-1, u'重做')
    self.edit.AppendSeparator()
    self.cut = self.edit.Append(-1, u'剪切')
    self.copy = self.edit.Append(-1, u'复制')
    self.paste = self.edit.Append(-1, u'粘贴')
    self.edit.AppendSeparator()
    self.selectall = self.edit.Append(-1, u'全选')
    self.menuBar.Append(self.edit, u'编辑(&E)')
    self.view = wx.Menu()
    self.color = self.view.AppendCheckItem(1051, u'设为黑色')
    self.trans = self.view.Append(-1, u'设置透明度')
    self.menuBar.Append(self.view, u'查看(&V)')
    self.help = wx.Menu()
    self.about = self.help.Append(-1, u'关于')
    self.menuBar.Append(self.help, u'帮助(&H)')
    parent.SetMenuBar(self.menuBar)

class ToolBar(wx.Panel):
    def __int__(self, parent, id, paint):



