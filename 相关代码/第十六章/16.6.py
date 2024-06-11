# 重构
mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
titles = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]

print(mags[:10]) 
print(titles[:2]) 
print(lons[:5]) 
print(lats[:5])

