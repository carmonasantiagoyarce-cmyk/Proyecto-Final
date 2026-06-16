from bing_image_downloader import downloader
from pathlib import Path

CATEGORIAS = {
    "Papel": [
        "crumpled paper isolated",
        "used notebook paper isolated",
        "newspaper isolated",
        "paper sheet isolated"
    ],

    "Carton": [
        "cardboard box isolated",
        "cardboard packaging isolated",
        "used cardboard box isolated"
    ],

    "Plastico": [
        "plastic bottle isolated",
        "plastic container isolated",
        "plastic cup isolated",
        "empty plastic bottle isolated"
    ],

    "Vidrio": [
        "glass bottle isolated",
        "glass jar isolated",
        "empty glass bottle isolated"
    ],

    "Metal": [
        "aluminum can isolated",
        "soda can isolated",
        "tin can isolated",
        "metal can isolated"
    ],

    "Organico": [
        "banana peel isolated",
        "apple core isolated",
        "food scraps isolated",
        "vegetable scraps isolated"
    ],

    "No_aprovechable": [
        "used tissue isolated",
        "dirty napkin isolated",
        "cigarette butt isolated",
        "snack wrapper isolated"
    ]
}

Path("dataset").mkdir(exist_ok=True)

for categoria, busquedas in CATEGORIAS.items():

    print(f"\n=== {categoria} ===")

    carpeta = Path("dataset") / categoria
    carpeta.mkdir(exist_ok=True)

    for busqueda in busquedas:

        print(f"Descargando: {busqueda}")

        downloader.download(
            busqueda,
            limit=25,
            output_dir=str(carpeta),
            adult_filter_off=True,
            force_replace=False,
            timeout=60
        )

print("\n✅ Dataset descargado")

