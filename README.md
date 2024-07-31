# Demo site and data prep for Algolia
- Data in [dataset/](dataset/)
- Scripts for data prep and upload, final json, pickle of new urls in [scripts/](scripts/)
- Website files in [site/](site/)

Website deployed via github actions to [https://alexander-frank.github.io/Algolia/](https://alexander-frank.github.io/Algolia/)

### Considerations
- Dataset was old, image urls did not work. Added a script to scrape new image urls. This worked for some restaurants. Some restaurants are closed permanently. Needs refinement for a live deployment.
- Website will use geolocation via lat long if allowed, otherwise will default to location via IP.
- Website will switch to mobile opentable links to reserve a table if rendered on a mobile device.
- Dataprep and ingest scripts were run in local python3 env, requirements listed in [requirements.txt](requirements.txt).