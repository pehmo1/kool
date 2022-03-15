if ((Test-Path -Path "PS_Demo") -eq $true) {
    Write-Host "Kaust olemas"
} else {
    New-Item -Path "." -Name "PS_Demo" -ItemType Directory
}

for ($i = 1; $i -le 3; $i++) {
    $kaustaNimi = "Kaust" + $i
    $loodavKaust = ".\PS_Demo\" + $kaustaNimi
    if (Test-Path -Path $loodavKaust) {
        Write-Host "Kataloog $loodavKaust olemas"
    } else {
        New-Item -Path ".\PS_Demo" -Name $kaustaNimi -ItemType Directory

        for ($j = 1; $j -le 50; $j++) {
            $failiNumber = $j.PadLeft(3,"0")
            New-Item -Path ($loodavKaust + "\Fail$failinumber")
        }
    }
}