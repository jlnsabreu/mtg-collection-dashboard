# MTG Collection Dashboard

Analysis of my personal Magic: The Gathering collection using ManaBox export data enriched with the Scryfall API.

## Stack

Python · Pandas · PostgreSQL · Tableau (in progress)

## Pipeline

1. `01_cleanup.ipynb` — loads and standardizes ManaBox CSV exports
2. `scryfall.py` — fetches card data from the Scryfall API by ID
3. `02_transform.ipynb` — merges, transforms, and loads into PostgreSQL

## Setup

1. Clone the repo
2. Create a `.env` file based on `.env.example`
3. Add your ManaBox CSV exports to `data/raw/`
4. Run the notebooks in order

## Data

Collection data exported from [ManaBox](https://manabox.app).  
Card metadata from the [Scryfall API](https://scryfall.com/docs/api)
