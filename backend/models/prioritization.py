import pandas as pd

def prioritize_locations(population_csv, services_csv, top_n=5):
    pop_df = pd.read_csv(population_csv)
    svc_df = pd.read_csv(services_csv)
    # Count services per grid cell (nearest grid by lat/lon, mock logic)
    svc_counts = svc_df.groupby(['lat', 'lon']).size().reset_index(name='service_count')
    merged = pd.merge(pop_df, svc_counts, how='left', on=['lat', 'lon'])
    merged['service_count'] = merged['service_count'].fillna(0)
    # Score: high population, low service
    merged['score'] = merged['population'] / (merged['service_count'] + 1)
    top = merged.sort_values('score', ascending=False).head(top_n)
    return top[['grid_id', 'lat', 'lon', 'population', 'service_count', 'score']].to_dict(orient='records') 