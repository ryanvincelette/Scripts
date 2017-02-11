param (
    [string]$infile = "infile",
)


$shell_app=new-object -com shell.application
$zip_file = $shell_app.namespace((Get-Location).Path + "\$infile")
$destination = $shell_app.namespace((Get-Location).Path)
$destination.Copyhere($zip_file.items())
