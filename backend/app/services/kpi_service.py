from tqdm import tqdm
from app.utils.fastf1_helper import *
import pandas as pd

GP_LIST = {
    2020: [
        "Red Bull Ring", "Red Bull Ring", "Hungaroring", "Silverstone", "Silverstone", "Circuit de Barcelona-Catalunya",
        "Circuit de Spa-Francorchamps", "Autodromo Nazionale Monza", "Autodromo Internazionale del Mugello",
        "Sochi Autodrom", "Nürburgring", "Autódromo Internacional do Algarve", "Autodromo Enzo e Dino Ferrari",
        "Istanbul Park", "Bahrain International Circuit", "Bahrain International Circuit (Sakhir)", "Yas Marina Circuit"
    ],
    2021: [
        "Bahrain International Circuit", "Autodromo Enzo e Dino Ferrari", "Autódromo Internacional do Algarve",
        "Circuit de Barcelona-Catalunya", "Circuit de Monaco", "Baku City Circuit", "Circuit Paul Ricard", "Red Bull Ring",
        "Red Bull Ring", "Silverstone Circuit", "Hungaroring", "Circuit de Spa-Francorchamps", "Circuit Zandvoort",
        "Autodromo Nazionale Monza", "Sochi Autodrom", "Istanbul Park", "Circuit of the Americas", "Autódromo Hermanos Rodríguez",
        "Interlagos", "Losail International Circuit", "Jeddah Street Circuit", "Yas Marina Circuit"
    ],
    2022: [
        "Bahrain International Circuit", "Jeddah Street Circuit", "Melbourne Grand Prix Circuit", "Imola Circuit",
        "Circuit de Barcelona-Catalunya", "Circuit de Monaco", "Baku City Circuit", "Circuit de Spa-Francorchamps",
        "Circuit Zandvoort", "Autodromo Nazionale Monza", "Sochi Autodrom", "Marina Bay Street Circuit", "Circuit of the Americas",
        "Autodromo Hermanos Rodríguez", "Interlagos", "Las Vegas Grand Prix Circuit", "Yas Marina Circuit"
    ],
    2023: [
        "Bahrain International Circuit", "Jeddah Street Circuit", "Melbourne Grand Prix Circuit", "Azerbaijan Grand Prix Circuit",
        "Circuit de Barcelona-Catalunya", "Circuit de Monaco", "Baku City Circuit", "Circuit de Spa-Francorchamps",
        "Circuit Zandvoort", "Autodromo Nazionale Monza", "Sochi Autodrom", "Marina Bay Street Circuit", "Circuit of the Americas",
        "Autodromo Hermanos Rodríguez", "Interlagos", "Las Vegas Grand Prix Circuit", "Yas Marina Circuit"
    ],
    2024: [
        "Bahrain International Circuit", "Jeddah Street Circuit", "Melbourne Grand Prix Circuit", "Azerbaijan Grand Prix Circuit",
        "Circuit de Barcelona-Catalunya", "Circuit de Monaco", "Baku City Circuit", "Circuit de Spa-Francorchamps",
        "Circuit Zandvoort", "Autodromo Nazionale Monza", "Sochi Autodrom", "Marina Bay Street Circuit", "Circuit of the Americas",
        "Autodromo Hermanos Rodríguez", "Interlagos", "Las Vegas Grand Prix Circuit", "Yas Marina Circuit"
    ],
    2025: [
        "Bahrain International Circuit", "Jeddah Street Circuit", "Melbourne Grand Prix Circuit", "Azerbaijan Grand Prix Circuit",
        "Circuit de Barcelona-Catalunya", "Circuit de Monaco", "Baku City Circuit", "Circuit de Spa-Francorchamps",
        "Circuit Zandvoort", "Autodromo Nazionale Monza", "Sochi Autodrom", "Marina Bay Street Circuit", "Circuit of the Americas",
        "Autodromo Hermanos Rodríguez", "Interlagos", "Las Vegas Grand Prix Circuit", "Yas Marina Circuit"
    ]
}

def get_classification(season: int, by: str ='team'):
    all_Points = []

    if by not in ['team', 'driver']:
        raise TypeError('By must be either "team" or "driver"')

    if by == 'team':
        key = 'TeamName'
        get_result = get_race_results_by_team
    else:
        key = 'FullName'
        get_result = get_race_results_by_driver

    for gp in tqdm(GP_LIST.get(season), desc=f"Processing season {season}"):
        results = get_result(season, gp)
        all_Points.append(results)

    result = (pd
        .concat(all_Points)
        .groupby(key, as_index=False)
        .agg(
            total_Points=("Points", "sum"),
            avg_Points=("Points", "mean"),
            min_Points=("Points", "min"),
            max_Points=("Points", "max")
        )
        .reset_index(drop=True)
        .sort_values('total_Points', ascending=False)
    )\
    .rename(columns={key: "name"})\
    .to_dict(orient='records')

    return result


