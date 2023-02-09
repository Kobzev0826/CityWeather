create table if not exists cities(
    city_id integer primary key,
    name_city varchar(256) not null
);

create table if not exists cityweather(
    id integer primary key,
    city_id integer not null,
    temperature decimal(4,2),
    wind_speed decimal(8,2),
    atmosphere_pressure integer,
    dttm datetime
)