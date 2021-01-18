# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/18/2021  
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
| St. Louis-Farmington | 3789 | 226724 | 1227 | 1446 | 1449 |
| Kansas City | 1905 | 153827 | 960 | 1085 | 1041 |
| Missouri non-MSA | 1584 | 102179 | 444 | 559 | 580 |
| Springfield | 482 | 33074 | 161 | 222 | 217 |
| Columbia-Jefferson City | 244 | 32141 | 113 | 147 | 160 |
| Joplin | 242 | 14830 | 63 | 78 | 75 |
| Cape Girardeau-Sikeston | 193 | 12001 | 41 | 54 | 54 |
| St. Joseph | 160 | 9449 | 40 | 46 | 47 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1563 | 78438 | 462 | 531 | 509 |
| Kansas City | Kansas | Johnson | 600 | 44973 | 359 | 376 | 329 |
| Kansas City | Missouri | Jackson | 283 | 26610 | 175 | 187 | 178 |
| St. Louis-Farmington | Illinois | Madison | 462 | 24144 | 170 | 184 | 173 |
| St. Louis-Farmington | Illinois | St. Clair | 424 | 22065 | 156 | 176 | 161 |
| St. Louis-Farmington | Missouri | St. Charles | 315 | 30200 | 141 | 176 | 178 |
| Kansas City | Missouri | Kansas City | 382 | 33674 | 133 | 199 | 200 |
| Springfield | Missouri | Greene | 333 | 21276 | 104 | 143 | 139 |
| St. Louis-Farmington | Missouri | Jefferson | 154 | 17227 | 96 | 123 | 115 |
| Kansas City | Kansas | Wyandotte | 220 | 17217 | 91 | 94 | 103 |
| Columbia-Jefferson City | Missouri | Boone | 54 | 14652 | 57 | 75 | 78 |
| Joplin | Missouri | Jasper | 182 | 11038 | 48 | 59 | 56 |
| Kansas City | Missouri | Cass | 62 | 6426 | 47 | 51 | 49 |
| St. Louis-Farmington | Missouri | Franklin | 122 | 7582 | 45 | 55 | 55 |
| Kansas City | Missouri | Clay | 118 | 7071 | 41 | 45 | 46 |
| Kansas City | Kansas | Leavenworth | 51 | 5666 | 38 | 39 | 32 |
| St. Louis-Farmington | Illinois | Macoupin | 94 | 3810 | 33 | 33 | 28 |
| Springfield | Missouri | Christian | 60 | 6249 | 29 | 43 | 45 |
| St. Louis-Farmington | Illinois | Clinton | 85 | 4989 | 28 | 31 | 29 |
| St. Joseph | Missouri | Buchanan | 113 | 6549 | 25 | 29 | 28 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 106 | 7018 | 25 | 32 | 34 |
| Missouri non-MSA | Missouri | Taney | 60 | 4211 | 22 | 26 | 22 |
| St. Louis-Farmington | Missouri | St. Francois | 79 | 7147 | 21 | 34 | 38 |
| Columbia-Jefferson City | Missouri | Cole | 101 | 8162 | 21 | 30 | 33 |
| St. Louis-Farmington | Illinois | Monroe | 70 | 3545 | 19 | 24 | 27 |
| Kansas City | Missouri | Platte | 27 | 2778 | 18 | 20 | 22 |
| Missouri non-MSA | Missouri | Pettis | 68 | 4459 | 18 | 25 | 22 |
| Missouri non-MSA | Missouri | Phelps | 103 | 2792 | 18 | 15 | 19 |
| Kansas City | Kansas | Miami | 19 | 2209 | 18 | 23 | 23 |
| Springfield | Missouri | Webster | 45 | 2785 | 16 | 21 | 19 |
| Joplin | Missouri | Newton | 60 | 3792 | 15 | 18 | 18 |
| Missouri non-MSA | Missouri | Howell | 41 | 2635 | 15 | 17 | 17 |
| Columbia-Jefferson City | Missouri | Callaway | 29 | 4135 | 15 | 19 | 23 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 3891 | 14 | 21 | 22 |
| Missouri non-MSA | Missouri | Barry | 38 | 2026 | 14 | 14 | 11 |
| Missouri non-MSA | Missouri | Adair | 6 | 1874 | 13 | 15 | 15 |
| St. Louis-Farmington | Illinois | Jersey | 56 | 2194 | 13 | 12 | 15 |
| Missouri non-MSA | Missouri | Camden | 66 | 3497 | 12 | 20 | 20 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3527 | 12 | 17 | 17 |
| Missouri non-MSA | Missouri | Butler | 18 | 3076 | 11 | 14 | 14 |
| Missouri non-MSA | Missouri | Stone | 28 | 1837 | 11 | 12 | 12 |
| Cape Girardeau-Sikeston | Missouri | Scott | 68 | 3583 | 11 | 15 | 14 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1731 | 10 | 11 | 10 |
| Missouri non-MSA | Missouri | Laclede | 54 | 2730 | 10 | 13 | 14 |
| Missouri non-MSA | Missouri | Saline | 26 | 2236 | 10 | 12 | 13 |
| Missouri non-MSA | Missouri | Washington | 41 | 1985 | 9 | 11 | 11 |
| St. Louis-Farmington | Missouri | Warren | 11 | 1860 | 9 | 12 | 12 |
| Missouri non-MSA | Missouri | Wright | 24 | 1263 | 9 | 10 | 10 |
| Missouri non-MSA | Missouri | Randolph | 20 | 1760 | 9 | 9 | 9 |
| Kansas City | Missouri | Lafayette | 44 | 2278 | 9 | 11 | 14 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2266 | 9 | 11 | 9 |
| Missouri non-MSA | Missouri | McDonald | 23 | 1814 | 8 | 8 | 8 |
| Springfield | Missouri | Polk | 25 | 2014 | 8 | 11 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 33 | 2850 | 8 | 18 | 21 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1605 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Ozark | 5 | 482 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Crawford | 21 | 1908 | 7 | 10 | 14 |
| Missouri non-MSA | Missouri | Vernon | 30 | 1276 | 7 | 9 | 13 |
| Kansas City | Missouri | Ray | 13 | 1305 | 7 | 10 | 11 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2152 | 7 | 7 | 7 |
| Kansas City | Missouri | Clinton | 60 | 1417 | 7 | 9 | 9 |
| Missouri non-MSA | Missouri | Marion | 32 | 2514 | 7 | 9 | 11 |
| Missouri non-MSA | Missouri | Macon | 10 | 1064 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Livingston | 25 | 1186 | 7 | 9 | 8 |
| Missouri non-MSA | Missouri | Pike | 17 | 1394 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Henry | 25 | 1579 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Audrain | 44 | 1950 | 7 | 8 | 16 |
| Missouri non-MSA | Missouri | Miller | 44 | 2215 | 6 | 10 | 11 |
| Missouri non-MSA | Missouri | Barton | 9 | 880 | 6 | 7 | 5 |
| St. Joseph | Kansas | Doniphan | 10 | 836 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Harrison | 10 | 724 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 31 | 791 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Texas | 20 | 1472 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2457 | 5 | 12 | 7 |
| Kansas City | Missouri | Bates | 14 | 964 | 5 | 6 | 8 |
| Columbia-Jefferson City | Missouri | Osage | 9 | 1299 | 5 | 6 | 6 |
| Kansas City | Kansas | Linn | 5 | 642 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Douglas | 20 | 714 | 5 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Moniteau | 26 | 1613 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Benton | 19 | 1337 | 4 | 8 | 7 |
| Missouri non-MSA | Missouri | Morgan | 31 | 1565 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Wayne | 9 | 747 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Clark | 5 | 418 | 4 | 2 | 2 |
| St. Joseph | Missouri | Andrew | 16 | 1207 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Grundy | 28 | 770 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Cedar | 9 | 608 | 4 | 4 | 4 |
| St. Joseph | Missouri | DeKalb | 21 | 857 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Dent | 9 | 765 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Ripley | 9 | 745 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Lawrence | 60 | 2542 | 3 | 12 | 12 |
| Missouri non-MSA | Missouri | Perry | 22 | 1953 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Oregon | 3 | 633 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Gentry | 16 | 677 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Carroll | 18 | 733 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Linn | 11 | 482 | 3 | 4 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 388 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Lewis | 3 | 603 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 381 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 11 | 1518 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Sullivan | 12 | 721 | 3 | 3 | 3 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 437 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 39 | 1704 | 2 | 5 | 6 |
| Springfield | Missouri | Dallas | 19 | 750 | 2 | 2 | 2 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17464 | 2 | 12 | 66 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 675 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1349 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Daviess | 10 | 530 | 2 | 3 | 3 |
| Kansas City | Missouri | Caldwell | 7 | 597 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 514 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Iron | 1 | 452 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 449 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Madison | 11 | 1290 | 2 | 4 | 6 |
| Missouri non-MSA | Missouri | Maries | 7 | 501 | 2 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1012 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 545 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 20 | 1178 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Dade | 10 | 394 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 9 | 717 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Shelby | 4 | 328 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 252 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 9 | 454 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 7 | 562 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 239 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 7 | 404 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 2 | 155 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 163 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 132 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 9 | 346 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 6 | 286 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 207 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 234 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
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
