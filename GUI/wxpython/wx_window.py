import wx

# Creates an App object which runs a loop to display the
# GUI on the screen
myapp = wx.App()

# Initialises a frame that the user would be able to
# interact with
init_frame = wx.Frame(parent=None, title='Word Play')

# Display the initialised frame on screen
init_frame.Show()

# Run a loop on the app object
myapp.MainLoop()