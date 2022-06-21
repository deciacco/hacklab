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
        self._clicked = True
        time.sleep(1)
        self._output.text = self._response_data

    def _send_thread(self):
        while True:
            if self._kill_threads:
                sys.exit()

            if self._clicked:
                self._clicked = False
                self._s.send(self._usercommand.text)

    def _recv_thread(self):
        while True:
            if self._kill_threads:
                sys.exit()

            data = self._s.recv(4096).replace("Enter Command> ", "")

            if data:
                self._response_data = data

    def _connect(self, event):
        try:
            self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._s.connect((self._ipaddress.text, 1234))
            self._kill_threads = False

            threading.Thread(target=self._send_thread).start()
            threading.Thread(target=self._recv_thread).start()

            self._connectbtn.enabled = False
            self._disconnectbtn.enabled = True
            self._sendbtn.enabled = True
            self._ipaddress.enabled = False

            self._output.text = "Connected to bind shell!"
        except:
            self._output.text = "Could not connect, try again!"

    def _disconnect(self, event):
        self._s.send("exit")
        self._s.close()
        self._kill_threads = True

        self._connectbtn.enabled = True
        self._disconnectbtn.enabled = False
        self._sendbtn.enabled = False
        self._ipaddress.enabled = True

        self._output.text = "Disconnected from bind shell!"