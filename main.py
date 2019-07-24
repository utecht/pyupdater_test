#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk

from pyupdater.client import Client
from client_config import ClientConfig

APP_NAME = 'TKTest'
APP_VERSION = '0.0.7'

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.client = Client(ClientConfig())
        self.client.refresh()
        self.client.add_progress_hook(self.print_status_info)
        self.master = master
        self.pack(side="top", fill="both", expand=True)
        ttk.Label(self, text='Did you restart?').pack(side="top")
        self.version_number = ttk.Label(self, text=APP_VERSION)
        self.version_number.pack(side="top")
        self.status = ttk.Label(self, text='')
        self.status.pack(side="top")
        ttk.Button(self, text="Check for update", command=self.check_for_update).pack(side="top")
        self.update()

    def check_for_update(self):
        self.version_number['text'] = "Checking for update...."
        self.update()
        app_update = self.client.update_check(APP_NAME, APP_VERSION)
        if app_update is not None:
            self.version_number['text'] = "Update found, downloading...."
            self.update()
            app_update.download()
            if app_update.is_downloaded():
                app_update.extract_restart()
        else:
            self.version_number['text'] = "No update found"
            self.update()

    def print_status_info(self, info):
        total = info.get('total')
        download = info.get('download')
        status = info.get('status')
        self.status['text'] = "{}\n{}\n{}".format(download, total, status)
        self.update()
        print(download, total, status)


r = tk.Tk()
app = Application(master=r)
app.mainloop()
