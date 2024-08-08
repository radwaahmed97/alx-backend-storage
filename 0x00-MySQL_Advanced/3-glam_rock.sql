--SQL SCRIPT THAT LISTS ALL BANDS WITH GLAM ROCK AS THEIR MAIN STYLE, RANKED BY THEIR LONGEVITY
SELECT band_name, IFNULL(split, 2022) - formed AS lifespan FROM metal_bands WHERE style LIKE '%glam rock%' ORDER BY lifespan DESC;