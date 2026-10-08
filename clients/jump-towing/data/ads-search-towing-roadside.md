---
cliente: Jump Towing LLC
slug: jump-towing
campaña: Search | Towing & Roadside | 10mi | v1
idioma: EN
actualizado: 2026-10-08
---

# RSA — Search | Towing & Roadside

Longitudes validadas (headlines ≤30, descripciones ≤90).

**Las afirmaciones marcadas [C] dependen de que el cliente las confirme.** No se publican hasta que estén en el brief: precio base, flatbed, licencia/seguro, sin daños, servicio de roadside concreto. Si no se confirman, se reemplazan por headlines del pool común sin [C].

**Prohibido en copy**: "24/7", "24 Hour", "Open Now" (no lo es), número de reseñas o años en el negocio (PENDIENTE), tiempos de llegada concretos ("in 30 min") hasta que el cliente los confirme.

## Pool común de headlines (para completar 15 por ad group)
| # | Headline | Nota |
|---|---|---|
| C1 | Based in Brooklyn Park, MN | operador local frente a los sitios lead-gen |
| C2 | Cars, SUVs & Light Trucks | filtra heavy-duty |
| C3 | Call Now for a Quick Quote | |
| C4 | Open Mon-Sat From 6 AM | dice el horario real sin prometer 24/7 |
| C5 | Serving the NW Metro | |
| C6 | Stuck? We Can Help Today | |
| C7 | Quick Response in Your Area | |
| C8 | Talk to a Local Dispatcher | [C] confirmar quién contesta |
| C9 | Clear Price Before We Roll | [C] precio por teléfono antes de salir |
| C10 | Local Tows From $XX | [C] precio base PENDIENTE: gap de competencia (nadie publica precio) |
| C11 | Damage-Free Car Towing | [C] |
| C12 | Flatbed Towing Available | [C] confirmar flatbed |
| C13 | Licensed & Insured Towing | [C] |

## Descripciones
| # | Descripción | Uso |
|---|---|---|
| D1 | Local towing for cars, SUVs and light trucks in Brooklyn Park and the NW metro. Call now. | Towing |
| D2 | Open Mon-Fri 6 AM-6 PM and Sat 6 AM-3:30 PM. Call and get a clear quote before we roll. | Todos ([C] por "clear quote") |
| D3 | Stuck on the side of the road? Call Jump Towing and talk to a local dispatcher right away. | Todos |
| D4 | Towing, jump starts, lockouts and tire help from a Brooklyn Park-based team. Call today. | Towing |
| D5 | Dead battery, locked keys or a flat? A local roadside tech can head your way. Call now. | Roadside |
| D6 | Fast roadside help in Brooklyn Park and nearby cities. One call gets a truck on the way. | Roadside |

Towing (G1–G3): D1, D2, D3, D4. Roadside (G4): D5, D6, D2, D3.

## Ad groups: headlines propios (pin H1) — v2, 4 grupos
Cada ad group lleva sus headlines propios (el primero pinneado en H1) más el pool común hasta completar 15.

| Ad group | H1 pinneado | Otros propios (sin pin) |
|---|---|---|
| G1 Towing Near Me | Tow Truck Near You | Towing Service Near You · Local Towing Company |
| G2 Towing Brooklyn Park & NW | {KeyWord:Towing in Brooklyn Park} (por defecto 23 caracteres) | Brooklyn Park Tow Truck · Maple Grove & Plymouth Towing · Coon Rapids & Fridley Towing · Crystal & New Hope Towing · Brooklyn Center Towing |
| G3 Towing Minneapolis | Towing in Minneapolis, MN | Minneapolis Tow Truck · North Minneapolis Towing |
| G4 Roadside | {KeyWord:Roadside Help Near You} (por defecto 22) | Car Jump Start Service · Dead Battery? Get a Jump · Car Lockout Service [C] · Flat Tire Help Near You [C] · Out of Gas? We Bring Fuel [C] |

La inserción de keyword usa keywords de ≤30 caracteres; las más largas del grupo ("towing brooklyn center", 22) caben.

## 1 RSA por ad group (máx. 2)
Estándar 4 de CLAUDE.md y playbook §9: con <$1,500/mes y ~4.7 clics/día, un A/B da ~60 clics por variante en 90 días, lo que es ruido.
- **RSA único**: H1 pinneado, H2 pinneado a C1 "Based in Brooklyn Park, MN" (el ángulo que nadie más puede usar). El resto rota.
- **Segundo RSA (opcional, solo cuando el cliente confirme el precio)**: H2 pinneado a C10 "Local Tows From $XX". Se evalúa por llamadas calificadas en CallFire, no por CTR, y no antes de ~100 clics por variante.

## Extensiones (nivel campaña)
- **Llamada**: el número del negocio detrás del tracking es el (612) 616-0723, y CallFire (612) 665-6274 reenvía a él. Con el reenvío de Google activado, la conversión "Llamada desde anuncio" ≥60 s la mide Google y CallFire sigue viendo todas las llamadas. Hay que confirmar qué número muestra hoy la extensión. Programada en el horario de la campaña.
- **Sitelinks** (landings PENDIENTES de audit):
  - Towing Service: "Cars, SUVs & light trucks" / "Call for a quick quote"
  - Jump Start: "Dead battery help" / "Local roadside tech"
  - Car Lockout [C]: "Locked keys in the car?" / "Fast local unlock"
  - Flat Tire & Fuel [C]: "Tire change on the spot" / "Fuel brought to you"
  - Service Area: "Brooklyn Park & NW metro" / "Maple Grove, Plymouth & more"
- **Callouts**: Based in Brooklyn Park · Cars & SUVs · Open Mon–Sat · Quick Phone Quotes · Local Dispatch [C] · Flatbed Available [C] · Licensed & Insured [C] · Upfront Pricing [C]
- **Snippet "Services"**: Towing, Jump Starts, Lockouts [C], Tire Changes [C], Fuel Delivery [C], Flatbed Towing [C]
- **Ubicación**: vinculada al GBP. Bloqueada hasta tener acceso al GBP.
- **Imágenes**: solo fotos propias de grúas o del equipo. Nada de stock.
