CREATE OR REPLACE TABLE `realtimepiplineproject.Stock_DWH.fact_stock_data_time` AS
WITH FactTable AS (
  SELECT
    ROW_NUMBER() OVER() AS fact_id,  -- Surrogate key for each row
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
  inner join `realtimepiplineproject.Stock_DWH.dim_company` AS company
    ON company.Company = stock.Company 
    AND company.industry = stock.Industry 
    AND company.sector = stock.Sector
  inner join `realtimepiplineproject.Stock_DWH.DimDate` AS dim_date
    ON dim_date.date = CAST(stock.Datetime AS DATE)
  inner join `realtimepiplineproject.Stock_DWH.DimTime` AS dim_time
    ON dim_time.time = CAST(stock.Datetime AS TIME)
  inner join  `realtimepiplineproject.Stock_DWH.dim_price` AS price
    ON price.price_category = stock.Price_Category
  WHERE stock.Datetime >= '2020-01-01' 
)

SELECT
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
FROM FactTable
WHERE company_id IS NOT NULL 
AND date_id IS NOT NULL 
AND time_id IS NOT NULL 
AND price_cat_id IS NOT NULL;
