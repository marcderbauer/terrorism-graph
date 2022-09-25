# Interpol Terrorism Knowledge Graph

## Intent
This repo serves to create a knowledge graph of Individuals wanted by Interpol and Terrorist organisations and their associated members.

The main sources are: 
- https://www.interpol.int/en/How-we-work/Notices 
- https://en.wikipedia.org/wiki/List_of_designated_terrorist_groups 

## Technology
- Streamlit, Neo4j, Python

## Status
This repo is currently in it's earliest stages. I intend to focus on some other projects first, but wanted to capture the idea well, so I could continue on it at a later point. `main.py` includes a proof of concept MVP. In order to run it you need to complete two steps:

### Install the required dependencies
    pip install -r requirements.txt  

### Run the MVP
    streamlit run mvp.py 

## Long-Term
It would be nice to join this with a database of terrorist incidents.   
The [Global Terrorism Database](https://www.start.umd.edu/gtd/) and Our World In Data's [Terrorism]("https://ourworldindata.org/terrorism") page would be a good start for that. However, the Global Terrorism database has approx 200k entries, which may cause some issues regarding visualisation. I will need to find a way to deal with that once the rest works.

## Contribution
I am happy about any feedback, collaboration or just thoughts in general.

 [![Hey](https://img.shields.io/badge/-Message%20me!-green)](mailto:hello@marcanthonybauer.com?subject=[GitHub%20--%20terrorism-graph])
