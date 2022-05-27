#Get-Service | Select-Object -Property Name,Status | Where-Object {$_.Status -eq "Stopped"}

#Get-Service | Select-Object -Property Name | Where-Object {$_.Name.StartsWith("A")}

#Get-Service | Select-Object -Property Name,StartType | Where-Object {$_.StartType -eq "Automatic"}

#Restart-Service -Name winmgmt

#Get-Service | Select-Object Name, Status | Out-File -FilePath "$PSScriptRootj\Services.txt"

#Get-Service | Select-Object Name, StartType, Status | ConvertTo-Html | Out-File -FilePath "$PSScriptRootj\Services.html"


$From = 'siim.reimand@tptlive.ee'
$To = 'siim.reimand@tptlive.ee'
$service = "ssh-agent"
$pass = Read-Host -AsSecureString -Prompt "Password: "
$encryptpassword = ConvertTo-SecureString $pass -AsPlainText -Force
$secureCreds = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $From,$encryptpassword
if (Get-Service $service | Where-Object {$_.Status -EQ "Stopped"}) {
    $Subject = "$service report"
    $Body = "$service has stopped at $(Get-Date)"
    $SMTPServer = "smtp.gmail.com"
    $SMTPPort = "587"
    Send-MailMessage -From $From -to $To -Subject $Subject `
    -Body $Body -SmtpServer $SMTPServer -port $SMTPPort -UseSsl `
    -Credential (Get-Credential)
}