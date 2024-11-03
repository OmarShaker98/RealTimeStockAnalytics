-- Insert new company, industry, sector combinations into dim_company table
INSERT INTO `realtimepiplineproject.Stock_DWH.dim_company` (company_id, business_id, Company, industry, sector)
WITH NewCompanies AS (
  SELECT
    ROW_NUMBER() OVER (ORDER BY Company, industry, sector) + (SELECT MAX(company_id) FROM `realtimepiplineproject.Stock_DWH.dim_company`) AS company_id,  -- Generate new surrogate keys
    CONCAT(Company, "-", industry, "-", sector) AS business_id,
    Company,
    industry,
    sector
  FROM `realtimepiplineproject.Stock_Pipline.Years` AS stock
  GROUP BY Company, industry, sector
)
-- Insert only new companies not already present in dim_company
SELECT 
  company_id,
  business_id,
  Company,
  industry,
  sector
FROM NewCompanies
WHERE business_id NOT IN (SELECT business_id FROM `realtimepiplineproject.Stock_DWH.dim_company`);
