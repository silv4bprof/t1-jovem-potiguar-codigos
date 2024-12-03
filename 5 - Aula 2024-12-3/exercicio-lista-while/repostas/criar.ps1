param([int]$n)
1..$n | ForEach-Object { New-Item -Name "q$_.py" -ItemType File }
