-- Create dim_date table from the start of the year 2024 to the end of the year 2024
CREATE OR REPLACE TABLE `realtimepiplineproject.Stock_DWH.dim_date` AS
WITH DateTable AS (
  -- Generate a list of dates from January 1, 2024 to December 31, 2024
  SELECT
    DATE AS date,
    EXTRACT(YEAR FROM DATE) AS year,
    EXTRACT(MONTH FROM DATE) AS month,
    FORMAT_DATE('%B', DATE) AS month_name,  -- Get month name like 'January'
    EXTRACT(DAY FROM DATE) AS day,
    EXTRACT(DAYOFWEEK FROM DATE) AS day_of_week,  -- 1=Sunday, 7=Saturday
    FORMAT_DATE('%A', DATE) AS day_name,  -- Get day name like 'Monday'
    EXTRACT(WEEK FROM DATE) AS week_of_year,
    EXTRACT(QUARTER FROM DATE) AS quarter
  FROM
    UNNEST(GENERATE_DATE_ARRAY('2024-01-01', '2024-12-31')) AS DATE
)

SELECT
  -- Create a surrogate key for each date in the format YYYYMMDD
  CAST(FORMAT_DATE('%Y%m%d', date) AS INT64) AS date_id,
  date,
  year,
  month,
  month_name,
  day,
  day_of_week,
  day_name,
  week_of_year,
  quarter
FROM DateTable
ORDER BY date;
