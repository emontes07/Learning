param([string[]]$files)
$xl = New-Object -ComObject Excel.Application
$xl.Visible = $false; $xl.DisplayAlerts = $false
foreach ($f in $files) {
  $wb = $xl.Workbooks.Open($f)
  $xl.CalculateFull()
  $wb.Save(); $wb.Close($true)
  "recalc $f"
}
$xl.Quit()
[System.Runtime.InteropServices.Marshal]::ReleaseComObject($xl) | Out-Null
