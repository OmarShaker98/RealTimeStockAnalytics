-- Insert new price categories into dim_price table
INSERT INTO `realtimepiplineproject.Stock_DWH.dim_price` (price_cat_id, price_category)
WITH NewPriceCategories AS (
  SELECT
    ROW_NUMBER() OVER (ORDER BY Price_Category) + (SELECT MAX(price_cat_id) FROM `realtimepiplineproject.Stock_DWH.dim_price`) AS price_cat_id,  -- Generate new surrogate keys
    Price_Category AS price_category  -- Ensure unique price category
  FROM `realtimepiplineproject.Stock_Pipline.Years` AS stock
  GROUP BY Price_Category
)
-- Insert only new price categories not already present in dim_price
SELECT
  price_cat_id,
  price_category
FROM NewPriceCategories
WHERE price_category NOT IN (SELECT price_category FROM `realtimepiplineproject.Stock_DWH.dim_price`);