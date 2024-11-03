-- Create the dim_price table 
CREATE OR REPLACE TABLE `realtimepiplineproject.Stock_DWH.dim_price_time` AS
WITH PriceCategoryTable AS (
  SELECT
    ROW_NUMBER() OVER () AS price_cat_id,  -- Surrogate key, auto-incremented
    Price_Category AS price_category        -- Unique price category
  FROM `realtimepiplineproject.Stock_DWH.Realtime_Stock`
  WHERE Datetime >= '2020-01-01' 
  GROUP BY Price_Category  
)
SELECT
    price_cat_id,
    price_category
FROM PriceCategoryTable
order by price_cat_id
