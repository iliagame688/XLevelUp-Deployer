
import os

# XLEVELUP REAL OVERRIDE
os.environ["XLEVELUP_MODE"] = "REAL"
os.environ["XDEPLOY_REAL"] = "1"


from Core.main import start


start()
