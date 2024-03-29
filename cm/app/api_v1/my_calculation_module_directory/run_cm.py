from .load_profile.load_profile import load_profile_gen


def main(res_heating_share, industry_share, tertiary_share, nuts2_id, heat_density_raster_total, heat_density_raster_res, heat_density_raster_nonres, gfa_res_curr_density, gfa_nonres_curr_density, nuts_id_number, output_directory):
    industry_profile_monthly,res_heating_profile_monthly, res_shw_profile_monthly, ter_heating_profile_monthly,\
    ter_shw_profile_monthly, effective_profile_monthly =\
        load_profile_gen(res_heating_share, industry_share, tertiary_share, nuts2_id, heat_density_raster_total,
                         heat_density_raster_res, heat_density_raster_nonres, gfa_res_curr_density, gfa_nonres_curr_density, nuts_id_number, output_directory)

    graphics = [{
            "type": "line",
            "xLabel": "Month",
            "yLabel": "Load",
            "data": {
                "labels": ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                           "October", "November", "December"],
                "datasets": [{
                    "label": "Industry",
                    "borderColor": "#3CA879",
                    "backgroundColor": "rgba(62, 149, 205, 0)",
                    "data": industry_profile_monthly
                    },
                    {
                    "label": "Residential heating",
                    "borderColor": "#3CAEA7",
                    "backgroundColor": "rgba(254, 124, 96, 0)",
                    "data": res_heating_profile_monthly
                    },
                    {
                    "label": "Residential warm water supply",
                    "borderColor": "#3CAEA7",
                    "backgroundColor": "rgba(254, 124, 96, 0)",
                    "data": res_shw_profile_monthly
                    },
                    {
                    "label": "Tertiary heating",
                    "borderColor": "##3C8EB4",
                    "backgroundColor": "rgba(254, 124, 96, 0)",
                    "data": ter_heating_profile_monthly
                    },
                    {
                    "label": "Tertiary warm water supply",
                    "borderColor": "##3C8EB4",
                    "backgroundColor": "rgba(254, 124, 96, 0)",
                    "data": ter_shw_profile_monthly
                    },
                    {
                    "label": "Effective",
                    "borderColor": "#3C63BA",
                    "backgroundColor": "rgba(254, 124, 96, 0)",
                    "data": effective_profile_monthly
                    }
                    ]
            }
        }]
    return graphics
