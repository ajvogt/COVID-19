# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/02/2021  
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
| St. Louis-Farmington | 3956 | 243228 | 858 | 970 | 1259 |
| Kansas City | 2112 | 166162 | 680 | 765 | 934 |
| Missouri non-MSA | 1708 | 106404 | 245 | 284 | 419 |
| Springfield | 534 | 34793 | 104 | 114 | 166 |
| Columbia-Jefferson City | 261 | 33369 | 82 | 84 | 113 |
| Joplin | 255 | 15583 | 52 | 51 | 62 |
| Cape Girardeau-Sikeston | 201 | 12366 | 25 | 25 | 39 |
| St. Joseph | 175 | 9839 | 23 | 26 | 36 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1689 | 83642 | 337 | 347 | 441 |
| Kansas City | Kansas | Johnson | 662 | 50030 | 245 | 287 | 344 |
| Kansas City | Missouri | Kansas City | 440 | 35700 | 127 | 139 | 167 |
| Kansas City | Missouri | Jackson | 308 | 28474 | 120 | 125 | 154 |
| St. Louis-Farmington | Illinois | Madison | 429 | 26251 | 117 | 142 | 161 |
| St. Louis-Farmington | Illinois | St. Clair | 428 | 23770 | 94 | 112 | 143 |
| St. Louis-Farmington | Missouri | St. Charles | 344 | 31588 | 72 | 93 | 134 |
| Springfield | Missouri | Greene | 380 | 22403 | 68 | 74 | 108 |
| St. Louis-Farmington | Missouri | Jefferson | 170 | 18274 | 60 | 68 | 96 |
| Kansas City | Kansas | Wyandotte | 232 | 18216 | 50 | 56 | 77 |
| St. Louis-Farmington | Missouri | St. Louis City | 351 | 20260 | 45 | 54 | 87 |
| Columbia-Jefferson City | Missouri | Boone | 61 | 15349 | 44 | 47 | 58 |
| Joplin | Missouri | Jasper | 195 | 11651 | 42 | 41 | 49 |
| Kansas City | Kansas | Leavenworth | 60 | 6247 | 33 | 33 | 37 |
| St. Louis-Farmington | Missouri | Franklin | 131 | 8052 | 25 | 30 | 44 |
| Kansas City | Missouri | Clay | 124 | 7502 | 25 | 29 | 37 |
| Kansas City | Missouri | Cass | 69 | 6887 | 25 | 32 | 40 |
| St. Louis-Farmington | Illinois | Clinton | 83 | 5325 | 19 | 22 | 26 |
| St. Louis-Farmington | Illinois | Monroe | 73 | 3829 | 19 | 19 | 21 |
| Springfield | Missouri | Christian | 63 | 6595 | 19 | 23 | 32 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 110 | 7246 | 17 | 15 | 23 |
| St. Louis-Farmington | Illinois | Macoupin | 72 | 4146 | 16 | 22 | 27 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8368 | 15 | 14 | 22 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 4094 | 14 | 13 | 17 |
| St. Louis-Farmington | Missouri | St. Francois | 83 | 7376 | 14 | 15 | 24 |
| Missouri non-MSA | Missouri | Taney | 68 | 4420 | 14 | 14 | 19 |
| St. Joseph | Missouri | Buchanan | 122 | 6781 | 13 | 15 | 22 |
| Kansas City | Missouri | Platte | 36 | 2932 | 12 | 10 | 15 |
| Missouri non-MSA | Missouri | Pettis | 69 | 4635 | 12 | 12 | 17 |
| Columbia-Jefferson City | Missouri | Callaway | 34 | 4292 | 11 | 10 | 15 |
| Kansas City | Kansas | Miami | 28 | 2502 | 11 | 20 | 20 |
| Joplin | Missouri | Newton | 60 | 3932 | 9 | 9 | 13 |
| Missouri non-MSA | Missouri | Johnson | 35 | 3680 | 9 | 10 | 13 |
| Missouri non-MSA | Missouri | Stone | 32 | 1943 | 9 | 7 | 9 |
| Missouri non-MSA | Missouri | Butler | 24 | 3231 | 8 | 10 | 12 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1993 | 8 | 9 | 10 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2366 | 8 | 11 | 12 |
| Springfield | Missouri | Webster | 46 | 2930 | 8 | 9 | 15 |
| Kansas City | Missouri | Lafayette | 46 | 2412 | 7 | 9 | 9 |
| Missouri non-MSA | Missouri | Camden | 74 | 3619 | 7 | 8 | 14 |
| Missouri non-MSA | Missouri | Adair | 7 | 1992 | 7 | 8 | 11 |
| Missouri non-MSA | Missouri | Saline | 30 | 2344 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Howell | 41 | 2739 | 6 | 7 | 12 |
| Missouri non-MSA | Missouri | Laclede | 58 | 2830 | 6 | 6 | 10 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3672 | 5 | 6 | 10 |
| Missouri non-MSA | Missouri | Crawford | 24 | 1994 | 5 | 5 | 8 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1275 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Harrison | 12 | 801 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Henry | 28 | 1657 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Lawrence | 61 | 2646 | 5 | 7 | 9 |
| Kansas City | Missouri | Ray | 19 | 1409 | 5 | 6 | 8 |
| Springfield | Missouri | Polk | 25 | 2072 | 5 | 4 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2347 | 5 | 5 | 8 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2889 | 4 | 6 | 11 |
| Missouri non-MSA | Missouri | Wright | 24 | 1331 | 4 | 4 | 7 |
| Kansas City | Missouri | Bates | 16 | 1037 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Washington | 41 | 2073 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | Pulaski | 34 | 2920 | 4 | 4 | 11 |
| Missouri non-MSA | Missouri | Barry | 41 | 2112 | 4 | 5 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2230 | 4 | 5 | 6 |
| Kansas City | Missouri | Clinton | 60 | 1479 | 4 | 4 | 6 |
| Kansas City | Kansas | Linn | 4 | 716 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Pike | 17 | 1453 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Macon | 10 | 1167 | 4 | 7 | 7 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1649 | 3 | 3 | 4 |
| St. Joseph | Kansas | Doniphan | 12 | 901 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Ripley | 10 | 792 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1572 | 3 | 3 | 4 |
| St. Louis-Farmington | Illinois | Bond | 21 | 1809 | 3 | 5 | 8 |
| Missouri non-MSA | Missouri | Miller | 45 | 2283 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Carroll | 18 | 796 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 562 | 3 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 10 | 1361 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Benton | 20 | 1392 | 3 | 3 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 33 | 843 | 3 | 3 | 5 |
| Springfield | Missouri | Dallas | 20 | 793 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 21 | 1222 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2521 | 2 | 3 | 7 |
| St. Joseph | Missouri | Andrew | 17 | 1255 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 41 | 1745 | 2 | 2 | 4 |
| St. Joseph | Missouri | DeKalb | 24 | 902 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | McDonald | 24 | 1872 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | Barton | 9 | 920 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 24 | 1389 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Daviess | 10 | 567 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Marion | 36 | 2586 | 2 | 4 | 7 |
| Missouri non-MSA | Missouri | Vernon | 32 | 1330 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | Dent | 11 | 803 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Randolph | 24 | 1790 | 2 | 1 | 5 |
| Missouri non-MSA | Missouri | Texas | 21 | 1502 | 2 | 1 | 4 |
| Missouri non-MSA | Missouri | Cedar | 9 | 646 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1656 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Madison | 13 | 1331 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Perry | 22 | 1994 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Morgan | 36 | 1594 | 2 | 1 | 4 |
| Missouri non-MSA | Missouri | Wayne | 9 | 790 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Audrain | 50 | 2017 | 2 | 4 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1032 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gentry | 19 | 717 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Douglas | 23 | 747 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Clark | 6 | 443 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shannon | 10 | 463 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 262 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Grundy | 30 | 802 | 1 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 416 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Monroe | 7 | 580 | 1 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 8 | 619 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 10 | 526 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 660 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Maries | 7 | 522 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 5 | 346 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 10 | 519 | 1 | 2 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 694 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Iron | 1 | 461 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ralls | 10 | 739 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Holt | 10 | 360 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 2 | 163 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 3 | 404 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 2 | 173 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 240 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 12 | 410 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 219 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 453 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Lewis | 3 | 620 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 740 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 10 | 459 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 550 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Atchison | 6 | 289 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 257 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 8 | 409 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 137 | 0 | 0 | 0 |
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
