$subFolders = Get-ChildItem -Recurse -Path (Join-Path $PSScriptRoot "PS_Demo") -File

Write-Host $subFolders[0]