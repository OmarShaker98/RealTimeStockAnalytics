INSERT INTO `realtimepiplineproject.Stock_DWH.DimTime` (time_id, time, hour, minute, second, AmPm, full_time)
SELECT DISTINCT 
    FORMAT_TIMESTAMP('%H%M%S', CAST(Datetime AS TIMESTAMP)) AS time_id,  -- Keep as STRING
    CAST(FORMAT_TIMESTAMP('%H:%M:%S', CAST(Datetime AS TIMESTAMP)) AS TIME) AS time,  -- Cast to TIME
    EXTRACT(HOUR FROM Datetime) AS hour,
    EXTRACT(MINUTE FROM Datetime) AS minute,
    EXTRACT(SECOND FROM Datetime) AS second,
    CASE WHEN EXTRACT(HOUR FROM Datetime) < 12 THEN 'AM' ELSE 'PM' END AS AmPm,
    FORMAT_TIMESTAMP('%I:%M:%S %p', CAST(Datetime AS TIMESTAMP)) AS full_time
FROM `realtimepiplineproject.Stock_DWH.Realtime_Stock`
WHERE Datetime >= '2023-01-01'  
AND FORMAT_TIMESTAMP('%H:%M:%S', CAST(Datetime AS TIMESTAMP)) NOT IN (
    SELECT FORMAT_TIME('%H:%M:%S', time) FROM `realtimepiplineproject.Stock_DWH.DimTime`
);
