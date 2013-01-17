from pyanaconda.ui.gui import QuitDialog, GUIObject, GraphicalUserInterface
#from .product import productName, productVersion
from .hubs import InitalSetupMainHub
from pyanaconda.ui.gui.spokes import StandaloneSpoke
import pyanaconda.ui.gui.spokes
from pyanaconda.ui.common import collect, FirstbootSpokeMixIn
import os
from gi.repository import Gdk
import logging
from di import inject, usesclassinject

# localization
_ = lambda t: t
N_ = lambda t: t

productTitle = lambda: "Inital Setup of Fedora"
isFinal = lambda: False

class InitalSetupQuitDialog(QuitDialog):
    MESSAGE = N_("Are you sure you want to quit the configuration process?\n"
                 "You might end up with unusable system if you do.")

@inject(Gdk, productTitle = productTitle, isFinal = isFinal)
class InitalSetupGraphicalUserInterface(GraphicalUserInterface):
    """This is the main Gtk based firstboot interface. It inherits from
       anaconda to make the look & feel as similar as possible.
    """

    screenshots_directory = "/tmp/initial-setup-screenshots"
    
    @usesclassinject
    def __init__(self, storage, payload, instclass):
        GraphicalUserInterface.__init__(self, storage, payload, instclass,
                                        productTitle, isFinal,
                                        quitDialog = InitalSetupQuitDialog)
        
    def _list_hubs(self):
        return [InitalSetupMainHub]

    basemask = "firstboot.gui"
    basepath = os.path.dirname(__file__)
    paths = GraphicalUserInterface.paths + {
        "spokes": [(basemask + ".spokes.%s", os.path.join(basepath, "spokes"))],
        "categories": [(basemask + ".categories.%s", os.path.join(basepath, "categories"))],
        }
