-- Insert new records into fact_stock_data from STOCK_DATA
INSERT INTO `realtimepiplineproject.Stock_DWH.fact_stock_data_time` (
  fact_id,
  company_id,
  date_id,
  time_id,
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
      SELECT MAX(fact_id) FROM `realtimepiplineproject.Stock_DWH.fact_stock_data_time`
    ), 0) AS fact_id,  -- Ensure surrogate key continues from the last max fact_id
    company.company_id,
    dim_date.date_id,
    dim_time.time_id,
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
  FROM `realtimepiplineproject.Stock_DWH.Realtime_Stock` AS stock
  INNER JOIN `realtimepiplineproject.Stock_DWH.dim_company_time` AS company
    ON company.Company = stock.Company 
    AND company.industry = stock.Industry 
    AND company.sector = stock.Sector
  INNER JOIN `realtimepiplineproject.Stock_DWH.dim_date` AS dim_date
    ON dim_date.date = CAST(stock.Datetime AS DATE)
  INNER JOIN `realtimepiplineproject.Stock_DWH.DimTime` AS dim_time
    ON dim_time.time = CAST(stock.Datetime AS TIME)
  INNER JOIN `realtimepiplineproject.Stock_DWH.dim_price` AS price
    ON price.price_category = stock.Price_Category
    WHERE stock.Datetime >= '2020-01-01' 
)
-- Insert only new records that do not already exist in the fact table
SELECT
  NewData.fact_id,
  NewData.company_id,
  NewData.date_id,
  NewData.time_id,
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
LEFT JOIN `realtimepiplineproject.Stock_DWH.fact_stock_data_time` AS fact
  ON NewData.company_id = fact.company_id
  AND NewData.date_id = fact.date_id
  AND NewData.time_id = fact.time_id
WHERE fact.company_id IS NULL AND fact.date_id IS NULL AND fact.time_id IS NULL;  