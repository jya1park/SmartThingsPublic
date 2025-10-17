# Auction Simulator for Hwaseong Properties

This folder contains a lightweight Python 3 script that can be used to explore
fictional foreclosure auction scenarios for apartments and detached houses in
Hwaseong-si, Gyeonggi-do.

## Features

* List sample apartment and detached house properties that are currently in the
  simulated auction catalog.
* Run a price distribution simulation for a property to estimate which creditor
  receives priority and how the auction proceeds might be distributed on the
  auction decision date.

## Usage

> **Python requirement**: The CLI is written for Python 3.9+ and relies only on
> the standard library. Activate your Python environment before running the
> commands below.

```bash
# List apartments or houses in the built-in dataset
python auction_simulator.py list --type apartment
python auction_simulator.py list --type house

# Simulate how a predicted winning bid distributes among liens
python auction_simulator.py simulate APT-001 --price 325000000
```

## Notes

* The dataset is fictional and is intended for demonstration and educational
  purposes only. Real auction data requires consulting an official court auction
  system or a licensed appraisal office.
* The priority order used in the simulation reflects a typical lien order but is
  simplified for clarity.
```
