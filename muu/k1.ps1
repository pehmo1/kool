# Siim Reimand IT-19E
Clear-Host

Write-Output "Hostname: $(hostname)`n*******************"
Write-Output "Masina nimi: $((Get-WMIObject win32_operatingsystem).name)`n*******************"
Write-Output "IP: $((Get-NetIPAddress | Where-Object {$_.AddressState -eq "Preferred" -and $_.ValidLifetime -lt "24:00:00"}).IPAddress)`n*******************"
Write-Output "Mälu suurus: $(get-wmiobject -class "win32_physicalmemory" -namespace "root\CIMV2").Capacity)`n*******************"
Write-Output "Protsessor: $((Get-WMIObject win32_Processor).Name)`n*******************"
Write-Output "Videokaart: $(foreach($gpu in Get-WmiObject Win32_VideoController){$gpu.Description})`n*******************"
Write-Output "Kasutajad: $(Get-LocalUser)"