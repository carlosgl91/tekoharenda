import csv
import os
import re

# Configuración
csv_file = 'base_datos_espacial_PINV_530_FMB.csv'
output_dir = 'docs/datasets'

# Crear el directorio si no existe
os.makedirs(output_dir, exist_ok=True)

def clean_filename(name):
    """Limpia el nombre de la variable para usarlo como nombre de archivo."""
    name = str(name).lower().replace(' ', '_')
    name = re.sub(r'[^a-z0-9_]', '', name)
    return name[:50]

print("Generando catálogo Tekoharenda agrupado...")

# Diccionario para agrupar los datos por Tipo
catalogo_agrupado = {}

with open(csv_file, mode='r', encoding='latin-1') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        titulo = row.get('Variable', '').strip()
        if not titulo:
            continue
            
        tipo = row.get('Tipo', '').strip()
        if not tipo:
            tipo = "Otros" # Por si alguna fila no tiene tipo definido
            
        descripcion = row.get('Descripción', '').strip()
        resolucion = row.get('Resolución nativa en metros', 'No especificada')
        fuente = row.get('Fuente de datos original', 'No especificada')
        fecha = row.get('Fecha de publicación', 'No especificada')
        cita = row.get('Cita de fuente de datos originales', '').strip()
        ee_asset = row.get('EE asset', '').strip()
        
        filename = clean_filename(titulo) + '.md'
        filepath = os.path.join(output_dir, filename)
        
        # Generar el contenido Markdown
        md_content = f"# {titulo}\n\n"
        md_content += f"**Tipo de Dato:** {tipo}\n"
        md_content += f"**Descripción:** {descripcion}\n\n"
        md_content += f"**Resolución Espacial:** {resolucion} metros\n"
        md_content += f"**Fuente Original:** {fuente}\n"
        md_content += f"**Fecha de Publicación:** {fecha}\n\n"
        
        if ee_asset:
            md_content += f"## Acceso en Google Earth Engine\n\n"
            md_content += "Puedes acceder a este conjunto de datos en el Code Editor de GEE usando el siguiente snippet:\n\n"
            md_content += "```javascript\n"
            md_content += f"var dataset = ee.Image(\"{ee_asset}\"); \n"
            md_content += f"Map.addLayer(dataset, {{}}, '{titulo[:20]}...');\n"
            md_content += "```\n\n"
            
        if cita:
            md_content += "## Cita\n"
            md_content += "Si utilizas estos datos, por favor cita la fuente original:\n"
            md_content += f"> *{cita}*\n"
            
        # Guardar el archivo Markdown
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
        # Agregarlo al diccionario según su Tipo
        if tipo not in catalogo_agrupado:
            catalogo_agrupado[tipo] = []
        catalogo_agrupado[tipo].append(f"      - '{titulo}': datasets/{filename}")

print("\n¡Archivos generados con éxito!")
print("-" * 50)
print("Copia y pega este nuevo menú en tu archivo mkdocs.yml:\n")

print("nav:")
print("  - Inicio: index.md")
print("  - Catálogo de Datos:")

# Imprimir el menú agrupado por categorías
for tipo, items in catalogo_agrupado.items():
    print(f"    - {tipo}:")
    for item in items:
        print(item)