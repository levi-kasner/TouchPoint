import re  
  
reportName = "My Widget Report"  
searchUrl  = "/Query/0cb9ffb7-7043-4779-ad13-ee6005ee45a8"  
  
def Get():  
    m = re.search(r'[0-9a-fA-F-]{36}', searchUrl)  
    guid = m.group(0) if m else ""  
  
    savedSearchName = q.QuerySqlScalar(  
        "SELECT TOP 1 Name FROM dbo.Query WHERE QueryId = '{0}'".format(guid))  
  
    Data.searchUrl  = searchUrl  
    Data.reportUrl  = "/Reports/Custom/{0}/{1}".format(reportName, guid)  
    Data.excelUrl   = "/Reports/CustomExcel/{0}/{1}".format(reportName, guid)  
    Data.editUrl    = "/Reports/EditCustomReport/{0}/{1}".format(reportName, guid)  
    Data.count      = q.QueryCount(savedSearchName) if savedSearchName else 0  
    Data.isAdmin    = (model.UserIsInRole("Admin")  
                       or model.UserIsInRole("SpecialContentFull")  
                       or model.UserIsInRole("SpecialContentBasic"))  
    print model.RenderTemplate(Data.HTMLContent)  
Get()