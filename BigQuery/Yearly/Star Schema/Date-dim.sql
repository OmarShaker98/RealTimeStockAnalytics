-- Create the DimDate Table
CREATE OR REPLACE TABLE realtimepiplineproject.Stock_DWH.DimDate AS (
  WITH UniqueDates AS (
    SELECT DISTINCT
      CAST(DATE(TIMESTAMP(Date)) AS DATE) AS DateValue
    FROM
      realtimepiplineproject.Stock_Pipline.Years
    WHERE
      Date IS NOT NULL  
  )
  SELECT
    CAST(FORMAT_DATE('%Y%m%d', DateValue) AS INT64) AS date_id, -- Surrogate key 
    DateValue AS date,  -- Include the date here
    EXTRACT(YEAR FROM DateValue) AS year, 
    EXTRACT(MONTH FROM DateValue) AS month, 
    CASE EXTRACT(MONTH FROM DateValue)  
      WHEN 1 THEN 'January'
      WHEN 2 THEN 'February'
      WHEN 3 THEN 'March'
      WHEN 4 THEN 'April'
      WHEN 5 THEN 'May'
      WHEN 6 THEN 'June'
      WHEN 7 THEN 'July'
      WHEN 8 THEN 'August'
      WHEN 9 THEN 'September'
      WHEN 10 THEN 'October'
      WHEN 11 THEN 'November'
      ELSE 'December'
    END AS month_name,
    EXTRACT(DAY FROM DateValue) AS day, 
    EXTRACT(DAYOFWEEK FROM DateValue) AS day_of_week, 
    CASE EXTRACT(DAYOFWEEK FROM DateValue)  
      WHEN 1 THEN 'Sunday'
      WHEN 2 THEN 'Monday'
      WHEN 3 THEN 'Tuesday'
      WHEN 4 THEN 'Wednesday'
      WHEN 5 THEN 'Thursday'
      WHEN 6 THEN 'Friday'
      ELSE 'Saturday'
    END AS day_name,
    EXTRACT(WEEK FROM DateValue) AS week_of_year, 
    CASE  
      WHEN EXTRACT(MONTH FROM DateValue) IN (1, 2, 3) THEN 1
      WHEN EXTRACT(MONTH FROM DateValue) IN (4, 5, 6) THEN 2
      WHEN EXTRACT(MONTH FROM DateValue) IN (7, 8, 9) THEN 3
      ELSE 4
    END AS quarter 
  FROM
    UniqueDates
);
