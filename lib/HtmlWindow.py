#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'zhoubangtao'

import wx.html

class MyHtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self,parent,-1,title)
        html = wx.html.HtmlWindow(self)
        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()
        html.SetPage(
            "Here is some <b>formatted</b>   <i><u>text</u></i>"
            "loaded from a <font color=\"red\"> string </font>."
            "<script>"
            "alert('h');"
            "</script>"
        )

app = wx.PySimpleApp()
frm = MyHtmlFrame(None, "Simple HTML")
frm.Show()
app.MainLoop()

# 从一个WEB页装载HTML，examples:
#
# import wx
# import wx.html
#
# class MyHtmlFrame(wx.Frame):
#     def __init__(self, parent, title):
#         wx.Frame.__init__(self, parent, -1, title, size=(600,400))
#         html = wx.html.HtmlWindow(self)
#         if "gtk2" in wx.PlatformInfo:
#             html.SetStandardFonts()
#         wx.CallAfter(html.LoadPage,"")
# app = wx.PySimpleApp()
# frm = MyHtmlFrame(None, "Simple HTML Browser")
# frm.Show()
# app.MainLoop()
#
# 带有状态栏和标题栏的HTML窗口，examples:
#
# import wx
# import wx.html
#
# class MyHtmlFrame(wx.Frame):
#     def __init__(self, parent, title):
#         wx.Frame.__init__(self, parent, -1, title, size=(600,400))
#         self.CreateStatusBar()
#         html = wx.html.HtmlWindow(self)
#         if "gtk2" in wx.PlatformInfo:
#             html.SetStandardFonts()
#         html.SetRelatedFrame(self,self.GetTitle() + " -- %s")
#         #关联HTML到框架
#         html.SetRelatedStatusBar(0) #关联HTML到状态栏
#         wx.CallAfter(html.LoadPage, "")
#
# app = wx.PySimpleApp()
# frm = MyHtmlFrame(None, "Simple HTML Browser")
# frm.Show()
# app.MainLoop()
#
# 如何增加对新标记的支持（略）
#
# 第十七章 wxPython的打印构架
#
# （略）
#
# 第十八章 其它应用
#
# 剪贴板应用
#
# examples:
#
# import wx
#
# t1_text = "test1"
# t2_text = "test2"
# class MyFrame(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self,None,title="Clipboard",size=(500,300))
#         p = wx.Panel(self)
#         # create the controls
#         self.t1 = wx.TextCtrl(p,-1,t1_text,style=wx.TE_MULTILINE|wx.HSCROLL)
#         self.t2 = wx.TextCtrl(p,-1,t2_text,style=wx.TE_MULTILINE|wx.HSCROLL)
#         copy = wx.Button(p, -1, "Copy")
#         paste = wx.Button(p, -1, "Paste")
#         # setup the layout with sizers
#         fgs = wx.FlexGridSizer(2, 2, 5, 5)
#         fgs.AddGrowableRow(0)
#         fgs.AddGrowableCol(0)
#         fgs.AddGrowableCol(1)
#         fgs.Add(self.t1, 0, wx.EXPAND)
#         fgs.Add(self.t2, 0, wx.EXPAND)
#         fgs.Add(copy, 0, wx.EXPAND)
#         fgs.Add(paste, 0, wx.EXPAND)
#         border = wx.BoxSizer()
#         border.Add(fgs, 1, wx.EXPAND|wx.ALL, 5)
#         p.SetSizer(border)
#         # Bind events
#         self.Bind(wx.EVT_BUTTON, self.OnDoCopy, copy)
#         self.Bind(wx.EVT_BUTTON, self.OnDoPaste, paste)
#     def OnDoCopy(self, evt):
#         #Copy按钮的事件处理函数
#         data = wx.TextDataObject()
#         data.SetText(self.t1.GetValue())
#         if wx.TheClipboard.Open():
#             wx.TheClipboard.SetData(data)
#             #将数据放置到剪贴板上
#             wx.TheClipboard.Close()
#         else:
#             wx.MessageBox("Unable to open the clipboard", "Error")
#     def OnDoPaste(self, evt):
#         #Paste按钮的事件处理函数
#         success = False
#         data = wx.TextDataObject()
#         if wx.TheClipboard.Open():
#             success = wx.TheClipboard.GetData(data)
#             #从剪贴板得到数据
#             wx.TheClipboard.Close()
#         if success:
#             self.t2.SetValue(data.GetText())
#             #更新文本控件
#         else:
#             wx.MessageBox(
#                 "There is no data in the clipboard in the required format",
#                 "Error")
# app = wx.PySimpleApp()
# frm = MyFrame()
# frm.Show()
# app.MainLoop()
#
# 简单的一个拖放源，examples:
#
# import wx
# class DragController(wx.Control):
#     """
#     Just a little control to handle dragging the text from a text
#     control.We use a separate control so as to not interfere with
#     the native drag-select functionality of the native text control.
#     """
#     def __init__(self, parent, source, size=(25,25)):
#         wx.Control.__init__(self,parent,-1,size=size,style=wx.SIMPLE_BORDER)
#         self.source = source
#         self.SetMinSize(size)
#         self.Bind(wx.EVT_PAINT, self.OnPaint)
#         self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
#     def OnPaint(self, evt):
#         # draw a simple arrow
#         dc = wx.BufferedPaintDC(self)
#         dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
#         dc.Clear()
#         w, h = dc.GetSize()
#         y = h/2
#         dc.SetPen(wx.Pen("dark blue", 2))
#         dc.DrawLine(w/8,   y, w-w/8, y)
#         dc.DrawLine(w-w/8, y, w/2,   h/4)
#         dc.DrawLine(w-w/8, y, w/2,   3*h/4)
#     def OnLeftDown(self, evt):
#         text = self.source.GetValue()
#         data = wx.TextDataObject(text)
#         dropSource = wx.DropSource(self)#创建释放源
#         dropSource.SetData(data)#设置数据
#         result = dropSource.DoDragDrop(wx.Drag_AllowMove)#执行释放
#         # if the user wants to move the data then we should delete it
#         # from the source
#         if result == wx.DragMove:
#             self.source.SetValue("")#如果需要的话，删除源中的数据
# class MyFrame(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self, None, title="Drop Source")
#         p = wx.Panel(self)
#         # create the controls
#         label1 = wx.StaticText(p, -1, "Put some text in this control:")
#         label2 = wx.StaticText(p, -1,
#            "Then drag from the neighboring bitmap and\n"
#            "drop in an application that accepts dropped\n"
#            "text, such as MS Word.")
#         text = wx.TextCtrl(p, -1, "sillycat")
#         dragctl = DragController(p, text)
#         # setup the layout with sizers
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(label1, 0, wx.ALL, 5)
#         hrow = wx.BoxSizer(wx.HORIZONTAL)
#         hrow.Add(text, 1, wx.RIGHT, 5)
#         hrow.Add(dragctl, 0)
#         sizer.Add(hrow, 0, wx.EXPAND|wx.ALL, 5)
#         sizer.Add(label2, 0, wx.ALL, 5)
#         p.SetSizer(sizer)
#         sizer.Fit(self)
# app = wx.PySimpleApp()
# frm = MyFrame()
# frm.Show()
# app.MainLoop()
#
# 文件拖放到目标的代码示例，examples:
#
# import wx
# class MyFileDropTarget(wx.FileDropTarget):
#     #声明释放到的目标
#     def __init__(self, window):
#         wx.FileDropTarget.__init__(self)
#         self.window = window
#     def OnDropFiles(self, x, y, filenames):#释放文件处理函数数据
#         self.window.AppendText("\n%d file(s) dropped at (%d,%d):\n" % (len(filenames),x,y))
#         for file in filenames:
#             self.window.AppendText("\t%s\n" % file)
# class MyFrame(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self,None,title="DropTarget",size=(500,300))
#         p = wx.Panel(self)
#         # create the controls
#         label = wx.StaticText(p,-1,"Drop some files here:")
#         text = wx.TextCtrl(p,-1,"",style=wx.TE_MULTILINE|wx.HSCROLL)
#         # setup the layout with sizers
#         sizer = wx.BoxSizer(wx.VERTICAL)
#         sizer.Add(label, 0, wx.ALL, 5)
#         sizer.Add(text, 1, wx.EXPAND|wx.ALL, 5)
#         p.SetSizer(sizer)
#         # make the text control be a drop target
#         dt = MyFileDropTarget(text)#将文本控件作为释放到的目标
#         text.SetDropTarget(dt)
# app = wx.PySimpleApp()
# frm = MyFrame()
# frm.Show()
# app.MainLoop()
#
# 定时器应用
# 简单的数据时钟，examples:
#
# import wx
# import time
# class ClockWindow(wx.Window):
#     def __init__(self, parent):
#         wx.Window.__init__(self, parent)
#         self.Bind(wx.EVT_PAINT,self.OnPaint)
#         self.timer = wx.Timer(self)
#         #创建定时器
#         self.Bind(wx.EVT_TIMER,self.OnTimer,self.timer)
#         #绑定一个定时器事件
#         self.timer.Start(1000)#设定时间间隔
#     def Draw(self, dc):
#         #绘制当前时间
#         t = time.localtime(time.time())
#         st = time.strftime("%I:%M:%S", t)
#         w, h = self.GetClientSize()
#         dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
#         dc.Clear()
#         dc.SetFont(wx.Font(30, wx.SWISS, wx.NORMAL, wx.NORMAL))
#         tw, th = dc.GetTextExtent(st)
#         dc.DrawText(st, (w-tw)/2, (h)/2 - th/2)
#     def OnTimer(self, evt):
#         #显示时间事件处理函数
#         dc = wx.BufferedDC(wx.ClientDC(self))
#         self.Draw(dc)
#     def OnPaint(self, evt):
#         dc = wx.BufferedPaintDC(self)
#         self.Draw(dc)
# class MyFrame(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self, None, title="wx.Timer")
#         ClockWindow(self)
#
#
# app = wx.PySimpleApp()
# frm = MyFrame()
# frm.Show()
# app.MainLoop()
#
# 多线程应用，examples:
#
# import wx
# import threading
# import random
# class WorkerThread(threading.Thread):
#     """
#     This just simulates some long-running task that periodically sends
#     a message to the GUI thread.
#     """
#     def __init__(self, threadNum, window):
#         threading.Thread.__init__(self)
#         self.threadNum = threadNum
#         self.window = window
#         self.timeToQuit = threading.Event()
#         self.timeToQuit.clear()
#         self.messageCount = random.randint(10,20)
#         self.messageDelay = 0.1 + 2.0 * random.random()
#     def stop(self):
#         self.timeToQuit.set()
#     def run(self):#运行一个线程
#         msg = "Thread %d iterating %d times with a delay of %1.4f\n" \
#               % (self.threadNum, self.messageCount, self.messageDelay)
#         wx.CallAfter(self.window.LogMessage, msg)
#         for i in range(1, self.messageCount+1):
#             self.timeToQuit.wait(self.messageDelay)
#             if self.timeToQuit.isSet():
#                 break
#             msg = "Message %d from thread %d\n" % (i, self.threadNum)
#             wx.CallAfter(self.window.LogMessage, msg)
#         else:#这里不懂，为啥要用else
#             wx.CallAfter(self.window.ThreadFinished, self)
#         #当循环“自然”终结（循环条件为假）时 else 从句会被执行一次，
#         #而当循环是由 break 语句中断时，else从句就不被执行。
# class MyFrame(wx.Frame):
#     def __init__(self):
#         wx.Frame.__init__(self, None, title="Multi-threaded GUI")
#         self.threads = []
#         self.count = 0
#         panel = wx.Panel(self)
#         startBtn = wx.Button(panel, -1, "Start a thread")
#         stopBtn = wx.Button(panel, -1, "Stop all threads")
#         self.tc = wx.StaticText(panel, -1, "Worker Threads: 00")
#         self.log = wx.TextCtrl(panel,-1,"",style=wx.TE_RICH|wx.TE_MULTILINE)
#
#         inner = wx.BoxSizer(wx.HORIZONTAL)
#         inner.Add(startBtn, 0, wx.RIGHT, 15)
#         inner.Add(stopBtn, 0, wx.RIGHT, 15)
#         inner.Add(self.tc, 0, wx.ALIGN_CENTER_VERTICAL)
#         main = wx.BoxSizer(wx.VERTICAL)
#         main.Add(inner, 0, wx.ALL, 5)
#         main.Add(self.log, 1, wx.EXPAND|wx.ALL, 5)
#         panel.SetSizer(main)
#         self.Bind(wx.EVT_BUTTON, self.OnStartButton, startBtn)
#         self.Bind(wx.EVT_BUTTON, self.OnStopButton, stopBtn)
#         self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
#         self.UpdateCount()
#     def OnStartButton(self, evt):
#         self.count += 1
#         thread = WorkerThread(self.count, self)#创建一个线程
#         self.threads.append(thread)
#         self.UpdateCount()
#         thread.start()#启动线程
#     def OnStopButton(self, evt):
#         self.StopThreads()
#         self.UpdateCount()
#     def OnCloseWindow(self, evt):
#         self.StopThreads()
#         self.Destroy()
#     def StopThreads(self):#从池中删除线程
#         while self.threads:
#             thread = self.threads[0]
#             thread.stop()
#             self.threads.remove(thread)
#     def UpdateCount(self):
#         self.tc.SetLabel("Worker Threads: %d" % len(self.threads))
#     def LogMessage(self, msg):#注册一个消息
#         self.log.AppendText(msg)
#     def ThreadFinished(self, thread):#删除线程
#         self.threads.remove(thread)
#         self.UpdateCount()
# app = wx.PySimpleApp()
# frm = MyFrame()
# frm.Show()
# app.MainLoop()