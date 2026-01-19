with base as (
    select *
    from {{ ref('staging_weather_report') }}
),
deduped as (
    select
        *,
        row_number() over (partition by id order by inserted_at desc) as rn
    from base
)
select *
from deduped
where rn = 1
