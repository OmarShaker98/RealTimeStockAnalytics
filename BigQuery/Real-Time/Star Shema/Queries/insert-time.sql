INSERT INTO realtimepiplineproject.Stock_DWH.DimTime (time_id, time, hour, minute, second, AmPm, full_time)
WITH source_data AS (
  SELECT
    TIME(TIMESTAMP(Datetime)) AS time_value,  
    EXTRACT(HOUR FROM TIMESTAMP(Datetime)) AS hour,
    EXTRACT(MINUTE FROM TIMESTAMP(Datetime)) AS minute,
    EXTRACT(SECOND FROM TIMESTAMP(Datetime)) AS second
  FROM realtimepiplineproject.Stock_DWH.Realtime_Stock
  WHERE Datetime >= '2020-01-01' 
  GROUP BY time_value, hour, minute, second
)
SELECT 
  CONCAT(CAST(hour AS STRING), LPAD(CAST(minute AS STRING), 2, '0'), LPAD(CAST(second AS STRING), 2, '0')) AS time_id,
  time_value AS time,
  hour,
  minute,
  second,
  CASE 
    WHEN hour < 12 THEN 'AM'
    ELSE 'PM'
  END AS AmPm,
  FORMAT("%02d:%02d:%02d %s", MOD(hour, 12), minute, second, CASE WHEN hour < 12 THEN 'AM' ELSE 'PM' END) AS full_time
FROM source_data;
