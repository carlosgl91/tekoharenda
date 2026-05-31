# 1. Get the list of all TIF files from your Google Cloud bucket
$files = gsutil ls "gs://tekoharenda/mapbiomas/fire/col1/monthly/*.tif"

# 2. Loop through every file found
foreach ($file in $files) {
    # Extract just the filename without the .tif extension (e.g., "fire_1985")
    $name = [System.IO.Path]::GetFileNameWithoutExtension($file)
    
    # Build the Earth Engine target path
    $assetId = "projects/arapy-487423/assets/mapbiomas_fire_col1_monthly/$name"
    
    Write-Host "Queueing upload for $name..."
    
    # Run the Earth Engine upload command
    earthengine upload image --asset_id=$assetId $file
}