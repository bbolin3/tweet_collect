import numpy as np
import pandas as pd


purchase_price = 488500

perc_down = .10

cancel_pmi = 0.2

loan = purchase_price*(1-perc_down)

cancel_price = (purchase_price*cancel_pmi - perc_down*purchase_price) + purchase_price