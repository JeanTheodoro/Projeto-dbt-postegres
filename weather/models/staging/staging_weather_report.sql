with source as (
    select *
    from {{ source('weather_data', 'city_weather') }}
),
staging_weather_report as (
    select
        id,
        city,
        temperature,
        weather_description,
        wind_speed,
        time as weather_time_local,

        inserted_at,  -- <-- ADICIONE ESTA LINHA

        {{ convert_to_local('inserted_at', 'timezone') }} as inserted_at_local,
        timezone
    from source
)
select *
from staging_weather_report
