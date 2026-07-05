"""Run this function to update the solar_cycle24.csv file"""
from sunpy.net import Fido
from sunpy.net import attrs as a


def get_flares():
    """
    Query HEK for flares > C1 from past solar cycle and save results to csv.
    
    """
    event_type = "FL"
    tstart = "2025-04-29"
    tend = "2025-08-29"
    result = Fido.search(
        a.Time(tstart, tend),
        a.hek.EventType(event_type),
        a.hek.OBS.Observatory == "GOES",
        a.hek.FL.GOESCls >= "C1.0",
    )

    new_table = result["hek"][
        "event_starttime", "event_peaktime", "event_endtime", "fl_goescls", "ar_noaanum"
    ]
    new_table.write("solar_cycle_flares_202504.csv", format="csv")


get_flares()
