import numpy as np
import pandas as pd


def site_find(str):
    web_id = 'https://'
    ind = str.find(web_id)
    site = str[ind:]
    return(ind,site)
