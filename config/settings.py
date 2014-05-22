__author__ = 'zhoubangtao'

import sqlite3
import os
import sys

cx = sqlite3.connect("../db/mass_mailer.sqlite")
cu = cx.cursor()

MASS_MAILER_HOME = os.path.realpath("..")
sources = [os.path.join(MASS_MAILER_HOME,"lib")]

if __name__ == "__main__":
  print(MASS_MAILER_HOME)
  print(sources)
