# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 03/06/2021  
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
| St. Louis-Farmington | 4681 | 257926 | 297 | 333 | 435 |
| Kansas City | 2536 | 176824 | 149 | 196 | 324 |
| Missouri non-MSA | 2059 | 110363 | 71 | 85 | 119 |
| Springfield | 624 | 36438 | 32 | 36 | 49 |
| Columbia-Jefferson City | 324 | 34542 | 18 | 21 | 33 |
| Joplin | 293 | 16350 | 8 | 14 | 20 |
| Cape Girardeau-Sikeston | 225 | 12880 | 7 | 8 | 15 |
| St. Joseph | 203 | 10124 | 4 | 6 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 2018 | 89030 | 118 | 132 | 159 |
| Kansas City | Kansas | Johnson | 752 | 54533 | 44 | 62 | 138 |
| St. Louis-Farmington | Illinois | St. Clair | 469 | 25649 | 44 | 44 | 56 |
| St. Louis-Farmington | Illinois | Madison | 461 | 28186 | 41 | 44 | 57 |
| St. Louis-Farmington | Missouri | St. Louis City | 425 | 21544 | 27 | 29 | 36 |
| St. Louis-Farmington | Missouri | St. Charles | 428 | 33061 | 26 | 30 | 45 |
| Kansas City | Missouri | Jackson | 388 | 30257 | 25 | 33 | 53 |
| Springfield | Missouri | Greene | 436 | 23527 | 22 | 25 | 33 |
| Kansas City | Kansas | Wyandotte | 270 | 19307 | 20 | 26 | 33 |
| Kansas City | Missouri | Kansas City | 528 | 36770 | 18 | 20 | 32 |
| St. Louis-Farmington | Missouri | Jefferson | 223 | 19049 | 11 | 15 | 22 |
| Kansas City | Kansas | Leavenworth | 83 | 6833 | 9 | 10 | 17 |
| Missouri non-MSA | Missouri | Butler | 35 | 3543 | 9 | 10 | 9 |
| Kansas City | Missouri | Cass | 91 | 7282 | 8 | 8 | 12 |
| Kansas City | Missouri | Clay | 151 | 7943 | 8 | 12 | 13 |
| Joplin | Missouri | Jasper | 224 | 12260 | 6 | 11 | 16 |
| Columbia-Jefferson City | Missouri | Boone | 84 | 15930 | 6 | 10 | 16 |
| St. Louis-Farmington | Missouri | Franklin | 164 | 8449 | 5 | 7 | 12 |
| Springfield | Missouri | Christian | 80 | 6901 | 5 | 6 | 9 |
| Columbia-Jefferson City | Missouri | Cole | 118 | 8602 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Cedar | 19 | 705 | 4 | 2 | 1 |
| Kansas City | Missouri | Lafayette | 56 | 2582 | 4 | 4 | 5 |
| Cape Girardeau-Sikeston | Missouri | Scott | 77 | 3845 | 4 | 3 | 5 |
| St. Louis-Farmington | Missouri | Lincoln | 39 | 4317 | 4 | 4 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 80 | 4372 | 4 | 4 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 86 | 4084 | 3 | 5 | 7 |
| Springfield | Missouri | Polk | 31 | 2182 | 3 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Callaway | 45 | 4502 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Pettis | 75 | 4805 | 3 | 3 | 5 |
| Kansas City | Kansas | Miami | 42 | 2650 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 25 | 2580 | 3 | 1 | 1 |
| Kansas City | Missouri | Platte | 43 | 3132 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Taney | 90 | 4600 | 3 | 4 | 5 |
| St. Louis-Farmington | Missouri | St. Francois | 107 | 7603 | 3 | 4 | 6 |
| St. Joseph | Missouri | Buchanan | 136 | 6969 | 2 | 3 | 5 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 127 | 7528 | 2 | 3 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2323 | 2 | 2 | 2 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5582 | 2 | 3 | 7 |
| Missouri non-MSA | Missouri | Camden | 81 | 3733 | 2 | 2 | 3 |
| Joplin | Missouri | Newton | 69 | 4090 | 2 | 2 | 4 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1916 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Phelps | 121 | 3032 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Howell | 42 | 2830 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Barry | 45 | 2200 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Crawford | 32 | 2060 | 1 | 1 | 2 |
| St. Louis-Farmington | Missouri | Warren | 19 | 2103 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Morgan | 42 | 1632 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Saline | 38 | 2435 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | McDonald | 26 | 1932 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Laclede | 66 | 2929 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Johnson | 45 | 3881 | 1 | 3 | 6 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 590 | 1 | 1 | 0 |
| Kansas City | Missouri | Ray | 25 | 1522 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Barton | 12 | 973 | 1 | 1 | 1 |
| Kansas City | Kansas | Linn | 8 | 756 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Lawrence | 76 | 2764 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Henry | 37 | 1750 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1275 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 7 | 725 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Adair | 18 | 2083 | 1 | 2 | 2 |
| Kansas City | Missouri | Bates | 23 | 1087 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 5 | 277 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Randolph | 30 | 1821 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Marion | 42 | 2652 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Linn | 12 | 548 | 1 | 0 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 47 | 2499 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 41 | 883 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Miller | 49 | 2322 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Audrain | 57 | 2080 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 14 | 1408 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 38 | 1397 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Pulaski | 49 | 2994 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Perry | 27 | 2052 | 0 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 9 | 453 | 0 | 0 | 1 |
| St. Joseph | Kansas | Doniphan | 22 | 945 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 22 | 1490 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Madison | 16 | 1348 | 0 | 0 | 0 |
| Springfield | Missouri | Webster | 53 | 2998 | 0 | 0 | 1 |
| Kansas City | Missouri | Clinton | 65 | 1529 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 15 | 1621 | 0 | 0 | 1 |
| St. Joseph | Missouri | DeKalb | 27 | 924 | 0 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 18 | 1286 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 22 | 1545 | 0 | 0 | 1 |
| Springfield | Missouri | Dallas | 24 | 830 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 482 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Washington | 48 | 2122 | 0 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Cooper | 27 | 1693 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Douglas | 26 | 772 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1682 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 6 | 424 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Stone | 38 | 2031 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Ripley | 14 | 857 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Benton | 27 | 1453 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carroll | 23 | 836 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Macon | 15 | 1213 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 7 | 355 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 12 | 483 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 14 | 748 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 17 | 822 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 16 | 552 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1770 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 10 | 598 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 11 | 821 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 179 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 10 | 631 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 7 | 537 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1054 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 143 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 37 | 1331 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ralls | 12 | 759 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 29 | 1365 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 261 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 14 | 420 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 5 | 465 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 367 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 568 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dunklin | 19 | 2413 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 29 | 1413 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 34 | 829 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 3 | 676 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 179 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 13 | 467 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 263 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 21 | 734 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 6 | 472 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 11 | 587 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 11 | 641 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 3 | 225 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 9 | 424 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 14 | 823 | 0 | 0 | 0 |
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
