# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/29/2021  
Source: [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)  
Source Code: `/ajvogt-analysis/mo_analysis_script.py`  
[Release Notes found below](#release-notes)

This analysis shows the Johns Hopkins University COVID-19 data broken down by 
[Metropolitan Statistcal Area](https://en.wikipedia.org/wiki/Metropolitan_statistical_area) (MSA)
 combinations within the state of Missouri. The list of counties in each MSA comibination can be found in the 
[table](#msa-counties) 
below. The [detailed map of MSAs](https://www2.census.gov/geo/maps/metroarea/us_wall/Sep2018/CBSA_WallMap_Sep2018.pdf) 
can be found here.  The clusters used in the charts and tables below 
are a custom combination of MSAs and 
[Combined Statistical Areas](https://en.wikipedia.org/wiki/Combined_statistical_area) (CSA). 
County populations are pulled from this 
[JHU CSSE repository file](https://github.com/ajvogt/COVID-19/blob/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv).

## Missouri New Daily Confirmed Cases by Metropolitan Statistcal Areas
![](images/mo_daily_cases.png)

## Missouri New Daily Deaths by Metropolitan Statistcal Areas
![](images/mo_daily_deaths.png)

## Missouri Cumulative Deaths by Metropolitan Statistcal Areas
![](images/mo_cumulative_deaths.png)

## Missouri Metropolitan Statistical Area Totals
<!-- msa_table start -->
| MSA | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|
| St. Louis-Farmington | 4103 | 240398 | 1017 | 1105 | 1395 |
| Kansas City | 2082 | 163542 | 804 | 848 | 1035 |
| Missouri non-MSA | 1702 | 105470 | 293 | 320 | 497 |
| Springfield | 533 | 34471 | 128 | 124 | 195 |
| Columbia-Jefferson City | 261 | 33051 | 86 | 88 | 133 |
| Joplin | 253 | 15418 | 54 | 53 | 74 |
| St. Joseph | 173 | 9736 | 29 | 30 | 41 |
| Cape Girardeau-Sikeston | 201 | 12279 | 28 | 30 | 45 |
<!-- msa_table end -->

## STL-Farmington MSA New Daily Confirmed Cases by County
![](images/stl_daily_cases.png)

## STL-Farmington MSA New Daily Deaths by County
![](images/stl_daily_deaths.png)

## STL-Farmington MSA Cumulative Deaths by County
![](images/stl_cumulative_deaths.png)

<a name="msa-counties"></a>
## Metropolitan Statistical Area (MSA) Counties
<!-- county_table start -->
| MSA | State | County | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|---|---|
| St. Louis-Farmington | Missouri | St. Louis | 1675 | 82831 | 422 | 412 | 486 |
| Kansas City | Kansas | Johnson | 646 | 49248 | 313 | 350 | 379 |
| St. Louis-Farmington | Illinois | Madison | 497 | 25824 | 143 | 154 | 175 |
| Kansas City | Missouri | Jackson | 307 | 28001 | 136 | 130 | 166 |
| Kansas City | Missouri | Kansas City | 439 | 35059 | 130 | 130 | 180 |
| St. Louis-Farmington | Illinois | St. Clair | 466 | 23408 | 112 | 129 | 159 |
| St. Louis-Farmington | Missouri | St. Charles | 344 | 31269 | 84 | 104 | 150 |
| Springfield | Missouri | Greene | 379 | 22175 | 81 | 79 | 125 |
| St. Louis-Farmington | Missouri | Jefferson | 169 | 18043 | 68 | 76 | 108 |
| Kansas City | Kansas | Wyandotte | 228 | 18044 | 68 | 71 | 94 |
| Columbia-Jefferson City | Missouri | Boone | 61 | 15200 | 51 | 51 | 68 |
| Joplin | Missouri | Jasper | 193 | 11518 | 44 | 43 | 57 |
| Kansas City | Kansas | Leavenworth | 55 | 6121 | 36 | 39 | 39 |
| St. Louis-Farmington | Missouri | St. Louis City | 348 | 20009 | 35 | 61 | 92 |
| Kansas City | Missouri | Cass | 69 | 6779 | 34 | 34 | 44 |
| St. Louis-Farmington | Missouri | Franklin | 131 | 7967 | 30 | 36 | 51 |
| Kansas City | Missouri | Clay | 124 | 7390 | 28 | 29 | 41 |
| Springfield | Missouri | Christian | 63 | 6541 | 26 | 25 | 39 |
| St. Louis-Farmington | Illinois | Macoupin | 99 | 4090 | 25 | 25 | 29 |
| St. Louis-Farmington | Illinois | Clinton | 90 | 5265 | 22 | 25 | 29 |
| St. Joseph | Missouri | Buchanan | 121 | 6725 | 18 | 19 | 25 |
| St. Louis-Farmington | Illinois | Monroe | 72 | 3755 | 18 | 18 | 23 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 110 | 7187 | 17 | 18 | 27 |
| Missouri non-MSA | Missouri | Taney | 68 | 4379 | 16 | 15 | 22 |
| Kansas City | Kansas | Miami | 27 | 2452 | 15 | 19 | 24 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8302 | 14 | 14 | 27 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 4052 | 14 | 14 | 19 |
| St. Louis-Farmington | Missouri | St. Francois | 83 | 7319 | 13 | 16 | 30 |
| Missouri non-MSA | Missouri | Pettis | 69 | 4596 | 13 | 12 | 20 |
| St. Louis-Farmington | Illinois | Jersey | 62 | 2341 | 11 | 13 | 13 |
| Springfield | Missouri | Webster | 46 | 2903 | 10 | 11 | 18 |
| Columbia-Jefferson City | Missouri | Callaway | 34 | 4237 | 10 | 9 | 18 |
| Missouri non-MSA | Missouri | Butler | 24 | 3203 | 10 | 12 | 14 |
| Joplin | Missouri | Newton | 60 | 3900 | 10 | 9 | 17 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1970 | 9 | 9 | 11 |
| Missouri non-MSA | Missouri | Johnson | 35 | 3640 | 8 | 10 | 14 |
| Kansas City | Missouri | Platte | 36 | 2877 | 8 | 10 | 18 |
| Kansas City | Missouri | Ray | 17 | 1397 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Macon | 10 | 1151 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Camden | 74 | 3592 | 8 | 9 | 16 |
| Missouri non-MSA | Missouri | Howell | 41 | 2724 | 8 | 8 | 15 |
| Missouri non-MSA | Missouri | Audrain | 50 | 2013 | 7 | 6 | 12 |
| Missouri non-MSA | Missouri | Adair | 7 | 1967 | 7 | 9 | 13 |
| Kansas City | Missouri | Lafayette | 46 | 2376 | 7 | 8 | 11 |
| Missouri non-MSA | Missouri | Saline | 30 | 2319 | 7 | 7 | 11 |
| Missouri non-MSA | Missouri | Stone | 31 | 1908 | 7 | 7 | 11 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3656 | 6 | 7 | 12 |
| Missouri non-MSA | Missouri | Washington | 41 | 2060 | 6 | 7 | 10 |
| Missouri non-MSA | Missouri | Henry | 28 | 1641 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Laclede | 57 | 2807 | 6 | 7 | 11 |
| Missouri non-MSA | Missouri | Lawrence | 61 | 2624 | 6 | 5 | 11 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1254 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2214 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2335 | 6 | 6 | 9 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2872 | 6 | 9 | 14 |
| Missouri non-MSA | Missouri | Crawford | 24 | 1972 | 6 | 6 | 10 |
| Missouri non-MSA | Missouri | Barry | 41 | 2094 | 6 | 8 | 10 |
| Springfield | Missouri | Polk | 25 | 2065 | 5 | 4 | 9 |
| St. Louis-Farmington | Illinois | Bond | 26 | 1803 | 5 | 6 | 9 |
| Missouri non-MSA | Missouri | Harrison | 11 | 784 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Miller | 45 | 2272 | 5 | 5 | 9 |
| Kansas City | Kansas | Linn | 4 | 703 | 5 | 4 | 7 |
| Missouri non-MSA | Missouri | Carroll | 18 | 781 | 5 | 3 | 4 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1560 | 5 | 3 | 5 |
| Kansas City | Missouri | Bates | 16 | 1020 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Marion | 36 | 2564 | 4 | 5 | 8 |
| St. Joseph | Kansas | Doniphan | 12 | 880 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 549 | 4 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 10 | 1346 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Pike | 17 | 1439 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Wright | 24 | 1310 | 4 | 5 | 9 |
| Kansas City | Missouri | Clinton | 60 | 1460 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Linn | 10 | 519 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 33 | 834 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Vernon | 32 | 1322 | 3 | 4 | 12 |
| Missouri non-MSA | Missouri | Pulaski | 34 | 2896 | 3 | 4 | 12 |
| Springfield | Missouri | Dallas | 20 | 787 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Benton | 20 | 1379 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Gentry | 19 | 711 | 3 | 3 | 3 |
| St. Joseph | Missouri | Andrew | 16 | 1242 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Ripley | 10 | 777 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | McDonald | 24 | 1861 | 3 | 5 | 7 |
| St. Joseph | Missouri | DeKalb | 24 | 889 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Perry | 22 | 1990 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Ozark | 10 | 515 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Barton | 9 | 907 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 21 | 1210 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Cedar | 9 | 636 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Dent | 11 | 793 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Madison | 13 | 1323 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Daviess | 10 | 556 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1378 | 2 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 412 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Oregon | 3 | 659 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Wayne | 9 | 783 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Douglas | 23 | 740 | 2 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1646 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Texas | 21 | 1492 | 2 | 2 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1631 | 2 | 3 | 5 |
| Kansas City | Missouri | Caldwell | 8 | 615 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Morgan | 34 | 1584 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Monroe | 7 | 577 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 6 | 437 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Dade | 12 | 410 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 10 | 732 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 41 | 1732 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Shelby | 5 | 342 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2501 | 1 | 3 | 7 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1024 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Chariton | 3 | 402 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 689 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 258 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Grundy | 30 | 792 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 738 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Lewis | 3 | 616 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Shannon | 10 | 456 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Holt | 10 | 355 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 5 | 452 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Maries | 7 | 515 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 2 | 171 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 1 | 458 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Mercer | 2 | 161 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Randolph | 24 | 1782 | 0 | 3 | 6 |
| Missouri non-MSA | Missouri | Worth | 1 | 136 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 8 | 409 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 216 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 288 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 549 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Hickory | 10 | 456 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 236 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 256 | 0 | 0 | 1 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
* 1/17/2021: including cumulative deaths plots
* 1/4/2021: small fix for including 2021 data
* 7/20/2020:
  * update table insertion code
  * fix cases vs. deaths total header bug
  * include MSA totals table
  * added STL-Farmington County-level Deaths & Cases plots
  * including release notes in missouri_analysis.md
* 7/19/2020: 
  * code refactor
  * updating color scheme for plots
  * updating county numbers to table to include
  latest new daily case average numbers and
  sorting by last 7-day average
* 6/19/2020: Added description of MSAs & CSAs
* 6/16/2020: Including individual county totals (only) in analysis md table
* 6/11/2020:
  * Updated MSA definitions
  * Including table of individual county case counts
* 6/7/2020: Creating markdown & script
  * Including list of county-MSA/CSA associations to markdown
  * Including cumulative totals in MSA/CSA plots
* 5/30/2020: including plots of cumulative cases/deaths in jupyter notebook
* 5/17/2020: Initial analysis jupyter notebook created
* 4/4/2020: Cloned JHU CSSE Repository and set up development environment

### To-Do (updated 1/17/2021)
- [ ] Verify county population data

#### Analysis Page
- [x] Update description to accurately reflect CSA vs. MSA
- [x] Make table for CSA info
- [x] Include 7, 14, & 30 day changes for each county
- [ ] Plot top CSAs (for latest daily case change) with testing data
- [x] Analysis breakdown of St. Louis-Farmington counties
- [x] Include release notes and to-do list
- [ ] ~~Update color scheme~~, plot markers, and line thickness
- [ ] Include table of contents

#### Analysis Script
- [x] Simplify data ingestion and summarization functionality
- [x] Simplify plotting functionality
- [x] Include ability to update markdown with table between markdown sections
