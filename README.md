# Ontario Natural Gas Pipe Sizing Calculator (CSA B149.1 basis)

Sizes natural gas piping by the longest-length method for Schedule 40 metallic pipe at 0.60 specific gravity, on both standard pressure-drop bases (0.5 in. w.c. and 3.0 in. w.c.), with the full capacity grids published in the data file for verification.

**Live web tool:** https://dust2engineering.github.io/ontario-gas-pipe-sizing-calculator/web/

## How it works

- Enter the total connected load and the longest run; the run is rounded up to the next table length and the smallest adequate pipe size is returned with every size's capacity shown.
- Capacities are in CFH; at 1,000 Btu/ft³, CFH numerically equals MBH, so a 300,000 Btu/h load is entered as 300.
- Propane is deliberately not covered: published reproductions of the propane table conflict on units.

## Data in this repository

- `gas-pipe-data.json` — both complete capacity grids with their sourcing note. CSA B149.1 Annex A is paywalled; these are the standard North American Schedule 40 tables on the same 0.60 SG basis, cross-checked numeral-by-numeral across Rheem (NFPA 54), Noritz and IFGC reproductions, 2026-11-15.
- `gas_pipe.py` — command-line sizer using the same JSON.

## Command line

```bash
python3 gas_pipe.py 300 60
```

## Worked examples

- [furnace-boiler-300mbh.md](examples/furnace-boiler-300mbh.md)
- [higher-drop-180mbh.md](examples/higher-drop-180mbh.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: HVAC / mechanical. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
