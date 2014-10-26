#this file needs to be in the same folder as InternetHistoryExport.bat
#This file needs to be modified to 
$shell = New-Object -ComObject Shell.Application
$hist = $shell.NameSpace(34)
$folder = $hist.Self
$folder.Path
$hist.Items() | foreach {
    ""; ""; $_.Name
     if ($_.IsFolder) {
         $siteFolder = $_.GetFolder
         $siteFolder.Items() | foreach {
            $site = $_
            ""; $site.Name
            if ($site.IsFolder) {
                $pageFolder  = $site.GetFolder
                $pageFolder.Items() | foreach {
                    $url = $pageFolder.GetDetailsOf($_,0)
                    $date =  $pageFolder.GetDetailsOf($_,2)
                    "$date visited $url" 
                }
            }
         }
     }
}
