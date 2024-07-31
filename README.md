# Demo site and data prep for algolia
- Data in [dataset/](dataset/)
- Scripts for data prep and upload + final json in [scripts/](scripts/)
- Website files in [site/](site/)

Website deployed via github actions to [https://alexander-frank.github.io/Algolia/](https://alexander-frank.github.io/Algolia/)

### Considerartions
- Dataset was old, image urls did not work. Added a script to scrape new image urls. This worked for some restaurants. SOme restaurants are closed permanently. Needs refinement for a live deployment.
- Website will use geolocation via lat long if allowed, otherwise will default to location via IP.
- Website will switch to mobile opentable links to reserve a table if rendered on a mobile device.