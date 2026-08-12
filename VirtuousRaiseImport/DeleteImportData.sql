SELECT c.ContributionId, c.ContributionDate, c.ContributionAmount, c.MetaInfo,  
       h.BundleHeaderId, h.ReferenceId, h.BundleHeaderTypeId  
FROM dbo.BundleHeader h  
JOIN lookup.BundleHeaderTypes t ON t.Id = h.BundleHeaderTypeId  
JOIN dbo.BundleDetail d ON d.BundleHeaderId = h.BundleHeaderId  
JOIN dbo.Contribution c ON c.ContributionId = d.ContributionId  
WHERE t.Code = 'VRDI'  
ORDER BY h.BundleHeaderId, c.ContributionId;



BEGIN TRAN;  
  
-- collect the target contribution ids from all VRDI bundles  
SELECT DISTINCT d.ContributionId  
INTO #cids  
FROM dbo.BundleHeader h  
JOIN lookup.BundleHeaderTypes t ON t.Id = h.BundleHeaderTypeId  
JOIN dbo.BundleDetail d ON d.BundleHeaderId = h.BundleHeaderId  
WHERE t.Code = 'VRDI';  
  
-- 1) child: contribution tags (import doesn't create these, but safe)  
DELETE ct FROM dbo.ContributionTag ct  
JOIN #cids x ON x.ContributionId = ct.ContributionId;  
  
-- 2) clear any self-referencing parent links among the targets  
UPDATE c SET c.ParentContributionId = NULL  
FROM dbo.Contribution c  
JOIN #cids x ON x.ContributionId = c.ContributionId  
WHERE c.ParentContributionId IS NOT NULL;  
  
-- 3) bundle details linking bundles <-> contributions  
DELETE d FROM dbo.BundleDetail d  
JOIN #cids x ON x.ContributionId = d.ContributionId;  
  
-- 4) the contributions  
DELETE c FROM dbo.Contribution c  
JOIN #cids x ON x.ContributionId = c.ContributionId;  
  
-- 5) the now-empty VRDI bundle headers  
DELETE h FROM dbo.BundleHeader h  
JOIN lookup.BundleHeaderTypes t ON t.Id = h.BundleHeaderTypeId  
WHERE t.Code = 'VRDI'  
  AND NOT EXISTS (SELECT 1 FROM dbo.BundleDetail d WHERE d.BundleHeaderId = h.BundleHeaderId);  
  
DROP TABLE #cids;  
  
-- inspect the affected row counts, then decide:  
-- COMMIT;   -- if correct  
-- ROLLBACK; -- if anything looks wrong  
