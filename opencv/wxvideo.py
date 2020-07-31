#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import wx  
import vlc

from os.path import basename, expanduser, isfile, join as joined
import sys

try:
    unicode       
except NameError:
    unicode = str  


class Player(wx.Frame):
    
    def __init__(self, title='', video=''):
        wx.Frame.__init__(self, None, -1, title=title or 'wxVLC',
                          pos=wx.DefaultPosition, size=(550, 500))

        self.video = video

        self.frame_menubar = wx.MenuBar()
        self.file_menu = wx.Menu()
        self.file_menu.Append(1, "&Open...", "Open from file...")
        self.file_menu.AppendSeparator()
        self.file_menu.Append(2, "&Close", "Quit")
        self.Bind(wx.EVT_MENU, self.OnOpen, id=1)
        self.Bind(wx.EVT_MENU, self.OnExit, id=2)
        self.frame_menubar.Append(self.file_menu, "File")
        self.SetMenuBar(self.frame_menubar)

        self.videopanel = wx.Panel(self, -1)
        self.videopanel.SetBackgroundColour(wx.BLACK)

        ctrlpanel = wx.Panel(self, -1)
        self.timeslider = wx.Slider(ctrlpanel, -1, 0, 0, 1000)
        self.timeslider.SetRange(0, 1000)
        self.pause = wx.Button(ctrlpanel, label="Pause")
        self.pause.Disable()
        self.play = wx.Button(ctrlpanel, label="Play")
        self.stop = wx.Button(ctrlpanel, label="Stop")
        self.stop.Disable()
        self.mute = wx.Button(ctrlpanel, label="Mute")
        self.volslider = wx.Slider(ctrlpanel, -1, 0, 0, 100, size=(100, -1))

        self.Bind(wx.EVT_BUTTON, self.OnPlay,   self.play)
        self.Bind(wx.EVT_BUTTON, self.OnPause,  self.pause)
        self.Bind(wx.EVT_BUTTON, self.OnStop,   self.stop)
        self.Bind(wx.EVT_BUTTON, self.OnMute,   self.mute)
        self.Bind(wx.EVT_SLIDER, self.OnVolume, self.volslider)

        ctrlbox = wx.BoxSizer(wx.VERTICAL)
        box1 = wx.BoxSizer(wx.HORIZONTAL)
        box2 = wx.BoxSizer(wx.HORIZONTAL)

        box1.Add(self.timeslider, 1)

        box2.Add(self.play, flag=wx.RIGHT, border=5)
        box2.Add(self.pause)
        box2.Add(self.stop)
        box2.Add((-1, -1), 1)
        box2.Add(self.mute)
        box2.Add(self.volslider, flag=wx.TOP | wx.LEFT, border=5)

        ctrlbox.Add(box1, flag=wx.EXPAND | wx.BOTTOM, border=10)
        ctrlbox.Add(box2, 1, wx.EXPAND)
        ctrlpanel.SetSizer(ctrlbox)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.videopanel, 1, flag=wx.EXPAND)
        sizer.Add(ctrlpanel, flag=wx.EXPAND | wx.BOTTOM | wx.TOP, border=10)
        self.SetSizer(sizer)
        self.SetMinSize((350, 300))

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)

        
        self.Instance = vlc.Instance()
        self.player = self.Instance.media_player_new()

    def OnExit(self, evt):
        
        self.Close()

    def OnOpen(self, evt):
        
        self.OnStop(None)

        video = self.video
        if video:
            self.video = ''
        else:  
            dlg = wx.FileDialog(self, "Choose a video file", expanduser('~'),
                                      "", "*.*", wx.FD_OPEN) 
            if dlg.ShowModal() == wx.ID_OK:
                video = joined(dlg.GetDirectory(), dlg.GetFilename())
            dlg.Destroy()

        if isfile(video):  
            self.Media = self.Instance.media_new(unicode(video))
            self.player.set_media(self.Media)
            
            title = self.player.get_title()
            self.SetTitle("%s - %s" % (title if title != -1 else 'wxVLC', basename(video)))

            handle = self.videopanel.GetHandle()
            if sys.platform.startswith('linux'):  
                self.player.set_xwindow(handle)
            elif sys.platform == "win32":  
                self.player.set_hwnd(handle)
            elif sys.platform == "darwin":
                self.player.set_nsobject(handle)
            self.OnPlay(None)

            self.volslider.SetValue(self.player.audio_get_volume() / 2)

    def OnPlay(self, evt):
        
        if not self.player.get_media():
            self.OnOpen(None)

        elif self.player.play():
            self.errorDialog("Unable to play.")
        else:
            self.timer.Start(1000)
            self.play.Disable()
            self.pause.Enable()
            self.stop.Enable()

    def OnPause(self, evt):
        
        if self.player.is_playing():
            self.play.Enable()
            self.pause.Disable()
        else:
            self.play.Disable()
            self.pause.Enable()
        self.player.pause()

    def OnStop(self, evt):
       
        self.player.stop()
       
        self.timeslider.SetValue(0)
        self.timer.Stop()
        self.play.Enable()
        self.pause.Disable()
        self.stop.Disable()

    def OnTimer(self, evt):
        
        length = self.player.get_length()
        self.timeslider.SetRange(-1, length)

        time = self.player.get_time()
        self.timeslider.SetValue(time)

    def OnMute(self, evt):
        
        muted = self.player.audio_get_mute()
        self.player.audio_set_mute(not muted)
        self.mute.SetLabel("Mute" if muted else "Unmute")
        

    def OnVolume(self, evt):
        
        volume = self.volslider.GetValue() * 2
        
        if self.player.audio_set_volume(volume) == -1:
            self.errorDialog("Failed to set volume")

    def errorDialog(self, errormessage):
        
        edialog = wx.MessageDialog(self, errormessage, 'Error', wx.OK|
                                                                wx.ICON_ERROR)
        edialog.ShowModal()

if __name__ == "__main__":

    _video = ''

    while len(sys.argv) > 1:
        arg = sys.argv.pop(1)
        if arg.lower() in ('-v', '--version'):
            
            c = basename(str(wx._core).split()[-1].rstrip('>').strip("'").strip('"'))
            print('%s: %s (%s %s %s)' % (basename(__file__), __version__,
                                         wx.__name__, wx.version(), c))
            try:
                vlc.print_version()
                vlc.print_python()
            except AttributeError:
                pass
            sys.exit(0)

        elif arg.startswith('-'):
            print('usage: %s  [-v | --version]  [<video_file_name>]' % (sys.argv[0],))
            sys.exit(1)

        elif arg:
            _video = expanduser(arg)
            if not isfile(_video):
                print('%s error: no such file: %r' % (sys.argv[0], arg))
                sys.exit(1)

    
app = wx.App()
player = Player(video=_video)
player.Centre()
player.Show()
app.MainLoop()