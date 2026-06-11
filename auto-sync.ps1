Write-Host "Iniciando sincronização automática com o GitHub..."
Write-Host "O sistema vai checar por mudanças a cada 60 segundos."

while ($true) {
    $status = git status --porcelain
    if ($status) {
        Write-Host "Mudanças detectadas! Salvando no GitHub..."
        git add .
        git commit -m "Auto-sync: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
        git push origin main
        Write-Host "Sincronização concluída com sucesso!"
    }
    Start-Sleep -Seconds 60
}
