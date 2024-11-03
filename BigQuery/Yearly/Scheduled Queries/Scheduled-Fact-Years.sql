-- Insert new records into fact_stock_data from STOCK_DATA
INSERT INTO `realtimepiplineproject.Stock_DWH.fact_stock_data` (
  fact_id,
  company_id,
  date_id,
  price_cat_id,
  Open,
  High,
  Low,
  Close,
  Adj_Close,
  Volume,
  Price_Range,
  Daily_Return,
  Volatility_percentage
)
WITH NewData AS (
  SELECT
    ROW_NUMBER() OVER() + COALESCE(( 
      SELECT MAX(fact_id) FROM `realtimepiplineproject.Stock_DWH.fact_stock_data`
    ), 0) AS fact_id,  -- Ensure surrogate key continues from the last max fact_id
    company.company_id,
    dim_date.date_id,
    price.price_cat_id,  
    stock.Open,
    stock.High,
    stock.Low,
    stock.Close,
    stock.Adj_Close,
    stock.Volume,
    stock.Price_Range,
    stock.Daily_Return,
    stock.Volatility_percentage
  FROM `realtimepiplineproject.Stock_Pipline.Years` AS stock
  INNER JOIN `realtimepiplineproject.Stock_DWH.dim_company` AS company
    ON company.Company = stock.Company 
    AND company.industry = stock.Industry 
    AND company.sector = stock.Sector
  INNER JOIN `realtimepiplineproject.Stock_DWH.DimDate` AS dim_date
    ON dim_date.date = CAST(stock.Date AS DATE)
  INNER JOIN `realtimepiplineproject.Stock_DWH.dim_price` AS price
    ON price.price_category = stock.Price_Category
)
-- Insert only new records that do not already exist in the fact table
SELECT
  NewData.fact_id,
  NewData.company_id,
  NewData.date_id,
  NewData.price_cat_id,
  NewData.Open,
  NewData.High,
  NewData.Low,
  NewData.Close,
  NewData.Adj_Close,
  NewData.Volume,
  NewData.Price_Range,
  NewData.Daily_Return,
  NewData.Volatility_percentage
FROM NewData
LEFT JOIN `realtimepiplineproject.Stock_DWH.fact_stock_data` AS fact
  ON NewData.company_id = fact.company_id
  AND NewData.date_id = fact.date_id
WHERE fact.company_id IS NULL AND fact.date_id IS NULL;  