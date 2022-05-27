# Siim Reimand IT-19E
Clear-Host

Write-Output "Arvuti nimi $(hostname)`n*******************"
Write-Output "Ketaste arv $((Get-Volume).Number.Count)`n*******************"

$maht = get-psdrive c | % { $_.free/($_.used + $_.free) } | % tostring p
Write-Output "Ketta protsent $maht`n*******************"
if($maht -ge 50) { Write-Output 'Ketas hakkab täis saama' }