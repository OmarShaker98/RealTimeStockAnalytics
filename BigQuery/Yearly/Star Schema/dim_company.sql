-- Create dim_company table 
CREATE OR REPLACE TABLE `realtimepiplineproject.Stock_DWH.dim_company` AS
WITH RowNumTable AS (
  SELECT
    ROW_NUMBER() OVER () AS company_id,  -- Surrogate key, auto-incremented
    CONCAT(Company, "-", industry, "-", sector) AS business_id,  -- Composite business key
    Company,
    industry,
    sector
  FROM `realtimepiplineproject.Stock_Pipline.Years` 
  GROUP BY Company, industry, sector  -- Ensure unique combinations
)
SELECT
    company_id,
    business_id,
    Company,
    industry,
    sector
FROM RowNumTable;
