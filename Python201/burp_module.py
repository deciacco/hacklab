from burp import IBurpExtender, ITab

from java.io import PrintWriter
from java.lang import RuntimeException
from javax import swing
from java.awt import BorderLayout

import sys, time, socket, threading, sys


class BurpExtender(IBurpExtender, ITab):
     
    def registerExtenderCallbacks(self, callbacks):
        self._clicked = False
        self._response_data = None
        self._kill_threads = False

        sys.stdout = callbacks.getStdout()

        self._callbacks = callbacks
        self._callbacks.setExtensionName("Bind shell")

        self._tab = swing.JPanel(BorderLayout())

        text_panel = swing.JPanel()
        box_vertical = swing.Box.createVerticalBox()

        #---------------------------------------------------------
        #IP Address

        box_horizontal = swing.Box.createHorizontalBox()
        self._ipaddress = swing.JTextArea('', 2, 100)
        self._ipaddress.setLineWrap(True)
        self._ipaddress.border = swing.BorderFactory.createTitledBorder("IP Address:")
        box_horizontal.add(self._ipaddress)
        box_vertical.add(box_horizontal)

        #---------------------------------------------------------
        #User Commands

        box_horizontal = swing.Box.createHorizontalBox()
        self._usercommand = swing.JTextArea('', 2, 100)
        self._usercommand.setLineWrap(True)
        self._usercommand.border = swing.BorderFactory.createTitledBorder("Command:")
        box_horizontal.add(self._usercommand)
        box_vertical.add(box_horizontal)

        #---------------------------------------------------------
        #Buttons

        box_horizontal = swing.Box.createHorizontalBox()
        button_panel = swing.JPanel()

        self._connectbtn = swing.JButton('[ -- Connect -- ]',actionPerformed=self._connect)
        self._sendbtn = swing.JButton('[ -- Send -- ]',actionPerformed=self._send)
        self._disconnectbtn = swing.JButton('[ -- Disconnect -- ]',actionPerformed=self._disconnect)

        self._disconnectbtn.enabled = False
        self._sendbtn.enabled = False

        button_panel.add(self._connectbtn)
        button_panel.add(self._sendbtn)
        button_panel.add(self._disconnectbtn)

        box_horizontal.add(button_panel)
        box_vertical.add(box_horizontal)

        #---------------------------------------------------------
        #Text Area

        box_horizontal = swing.Box.createHorizontalBox()
        self._output = swing.JTextArea('', 25, 100)
        self._output.setLineWrap(True)
        self._output.setEditable(False)

        scroll = swing.JScrollPane(self._output)

        box_horizontal.add(scroll)
        box_vertical.add(box_horizontal)

        #---------------------------------------------------------
        #Add to screen

        text_panel.add(box_vertical) 
        self._tab.add(text_panel)

        callbacks.addSuiteTab(self)
        return

    def getTabCaption(self):
        return "Bind shell"

    def getUiComponent(self):
        return self._tab

    def _send(self, event):
        return

    def _connect(self, event):
        return

    def _disconnect(self, event):
        return