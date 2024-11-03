CREATE OR REPLACE TABLE `realtimepiplineproject.Stock_DWH.fact_stock_data` AS
WITH FactTable AS (
  SELECT
    ROW_NUMBER() OVER() AS fact_id,  -- Surrogate key for each row
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

SELECT
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
FROM FactTable
WHERE company_id IS NOT NULL 
AND date_id IS NOT NULL 
AND price_cat_id IS NOT NULL;
