$path = "C:\git\Messenger"

# Deleting folders __pycache__
Get-ChildItem -Path $path -Directory -Recurse -Filter "__pycache__" | ForEach-Object {
    Remove-Item -Path $_.FullName -Recurse -Force
    Write-Host "The folder was deleted: $($_.FullName)"
}

# Deleting *.pyc files
Get-ChildItem -Path $path -Recurse -Include *.pyc | ForEach-Object {
    Remove-Item -Path $_.FullName -Force
    Write-Host "The file was deleted: $($_.FullName)"
}