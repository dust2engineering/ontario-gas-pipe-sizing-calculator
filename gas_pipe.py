#!/usr/bin/env python3
"""Natural gas pipe sizing, longest-length method (Schedule 40, SG 0.60).
Usage: python3 gas_pipe.py LOAD_CFH LONGEST_RUN_FT [DROP]   DROP = 05 (default) or 30
Capacities in CFH; at 1,000 Btu/ft3, CFH numerically equals MBH.
Tables: 0.5 in. w.c. drop (inlet < 2 psi) and 3.0 in. w.c. drop (inlet >= 8 in. w.c., < 2 psi).
"""
import json, os, sys

DATA = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "gas-pipe-data.json")))

def main():
    if len(sys.argv) < 3:
        print(__doc__); return
    load, length = float(sys.argv[1]), float(sys.argv[2])
    drop = sys.argv[3] if len(sys.argv) > 3 else "05"
    t = DATA["table_0.5inwc"] if drop == "05" else DATA["table_3.0inwc"]
    lengths, grid = t["lengths_ft"], t["capacity_cfh"]
    col = next((i for i, L in enumerate(lengths) if L >= length), None)
    if col is None:
        print(f"Run longer than the table maximum ({lengths[-1]} ft). Use a detailed pressure-drop calculation."); return
    print(f"Design length (rounded up): {lengths[col]} ft; pressure drop {t['pressure_drop_in_wc']} in. w.c.")
    for s in ["1/2", "3/4", "1", "1-1/4", "1-1/2", "2"]:
        cap = grid[s][col]
        print(f"  NPS {s}: capacity {cap} CFH {'OK' if cap >= load else ''}")
        if cap >= load:
            print(f"RESULT: NPS {s} (capacity {cap} CFH >= load {load:g} CFH)"); return
    print("RESULT: load exceeds NPS 2 capacity at this length — split the load or use a detailed calculation.")

if __name__ == "__main__":
    main()
