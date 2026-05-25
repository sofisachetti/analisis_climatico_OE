# Análisis de Datos Climáticos Globales

> Trabajo Práctico - Gestión Colaborativa, Control de Versiones y Organización Empresarial
> Universidad Tecnológica Nacional · Tecnicatura Universitaria en Programación · 2026
> Cátedra: Organización Empresarial
> Alumna: Sofia Sachetti

---

## Equipo

| Rol | Integrante | Responsabilidad |
|-----|-----------|------------------|
| P1 — Líder y Organizador | Hugo | Inicialización del repositorio y estructura |
| P2 — Desarrollador Técnico| Paco | Script de análisis y visualización |
| P3 — Revisor y QA | Luis | Documentación y revisión del PR |

## Escenario

**Escenario A — Análisis de Datos Climáticos**

## Dataset

| Atributo | Detalle |
|----------|---------|
| Nombre | Global Surface Temperature (GISTEMP v4) |
| Fuente | NASA Goddard Institute for Space Studies |
| Acceso | https://datahub.io/core/global-temp |
| Formato | CSV — columnas: Source, Year, Mean |
| Licencia | Dominio público |

## Estructura del repositorio

```
analisis_climatico_OE/
├── datos/
│   └── temperatura_global.csv
├── scripts/
│   └── analisis_climatico.py
├── resultados/
│   ├── grafico_temperatura.png
│   └── indicadores.txt
├── README.md
└── .gitignore
```

## Cómo ejecutar

```bash
git clone https://github.com/sofisachetti/analisis_climatico_OE.git
cd analisis_climatico_OE
pip install pandas matplotlib
python scripts/analisis_climatico.py
```

## Trazabilidad con Jira

| Issue | Descripción | Commit asociado |
|-------|-------------|-----------------|
| PROY-1 | Inicialización del repositorio | `PROY-1: Agregar estructura de carpetas...` |
| PROY-2 | Desarrollo del script de análisis | `PROY-2: Agregar dataset GISTEMP...` |
| PROY-3 | Revisión, documentación y PR | `PROY-3: Actualizar README...` |
