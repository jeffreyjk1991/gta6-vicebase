# Community map data and map artwork attribution

The `/map/` experience offers two cartographic layers:

1. The default detailed view loads the YANIS v17/GTADB community reconstruction as processed and made available by GTAMI at https://gtami.com/en/official-map/ (4096px overview, 8192px high-resolution image). GTA VI Map Tiles are copyright GTADB.ORG and community contributors, licensed **CC BY 4.0**: https://creativecommons.org/licenses/by/4.0/. Original project: https://map.gtadb.org and https://github.com/rolux/gtadb.org.
2. The fallback neon atlas (`leonida-concept.svg`) is original artwork created for ViceBase. It is deliberately conceptual.

`site/assets/gtadb-landmarks.json` derives from the open GTADB GTA VI Landmarks Data, `map/data/6/landmarks.json`, excluding unnamed, unconfirmed and demolished entries, grouping tags into visitor-friendly categories, and projecting the community source coordinates onto the rendered overview. Titles and positions are community estimates; a marker does not establish any in-game interior, service or mission. All source entries retain their `GTADB` IDs. Cite GTADB.ORG and contributors under CC BY 4.0 when displaying or adapting this data. Snapshot: 2026-11-18.

Rockstar Games promotional poster used on the homepage is served from Rockstar's officially published wallpaper, with link to https://www.rockstargames.com/VI/media/artwork-wallpapers. The artwork remains copyright Rockstar Games, and ViceBase is not endorsed by Rockstar or Take-Two.

**Before release**: neither this data nor the reference site is the final, official in-game street map. Do not market it as exact until independent gameplay verification or authorized official map assets exist. Revisit at release and correct markers with dated verified gameplay evidence.

**External image dependencies:** The website references a high-resolution image served by GTAMI and Rockstar promotional art served by Rockstar. These are not bundled with this repository. If their hosts become unavailable, the site falls back to the original illustrated neon map and skyline rather than a broken full-page design. To bundle official art locally, review artwork reuse rights and copy only assets that are licensed/authorized for the intended website.
