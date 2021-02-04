# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/04/2021  
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
| St. Louis-Farmington | 4118 | 244860 | 819 | 921 | 1222 |
| Kansas City | 2169 | 167098 | 555 | 685 | 909 |
| Missouri non-MSA | 1807 | 106789 | 238 | 277 | 409 |
| Springfield | 551 | 34958 | 90 | 108 | 162 |
| Columbia-Jefferson City | 277 | 33547 | 86 | 87 | 113 |
| Joplin | 265 | 15722 | 53 | 53 | 64 |
| Cape Girardeau-Sikeston | 207 | 12410 | 24 | 26 | 38 |
| St. Joseph | 180 | 9871 | 22 | 26 | 34 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1764 | 84254 | 311 | 338 | 426 |
| Kansas City | Kansas | Johnson | 668 | 50392 | 163 | 238 | 333 |
| Kansas City | Missouri | Kansas City | 453 | 35799 | 121 | 127 | 159 |
| Kansas City | Missouri | Jackson | 321 | 28660 | 110 | 123 | 153 |
| St. Louis-Farmington | Illinois | Madison | 437 | 26467 | 108 | 133 | 159 |
| St. Louis-Farmington | Illinois | St. Clair | 431 | 23940 | 92 | 104 | 139 |
| St. Louis-Farmington | Missouri | St. Charles | 376 | 31696 | 68 | 84 | 129 |
| St. Louis-Farmington | Missouri | St. Louis City | 360 | 20453 | 63 | 55 | 83 |
| Springfield | Missouri | Greene | 388 | 22517 | 63 | 71 | 106 |
| St. Louis-Farmington | Missouri | Jefferson | 181 | 18380 | 57 | 64 | 93 |
| Joplin | Missouri | Jasper | 203 | 11772 | 45 | 44 | 51 |
| Columbia-Jefferson City | Missouri | Boone | 69 | 15430 | 42 | 46 | 59 |
| Kansas City | Kansas | Wyandotte | 236 | 18309 | 37 | 52 | 76 |
| Kansas City | Kansas | Leavenworth | 64 | 6304 | 26 | 31 | 37 |
| Kansas City | Missouri | Clay | 128 | 7543 | 25 | 28 | 37 |
| Kansas City | Missouri | Cass | 72 | 6917 | 23 | 30 | 40 |
| St. Louis-Farmington | Missouri | Franklin | 138 | 8086 | 22 | 28 | 42 |
| St. Louis-Farmington | Illinois | Clinton | 85 | 5372 | 17 | 20 | 26 |
| St. Louis-Farmington | Illinois | Monroe | 75 | 3855 | 17 | 17 | 20 |
| Columbia-Jefferson City | Missouri | Cole | 107 | 8399 | 17 | 15 | 21 |
| Columbia-Jefferson City | Missouri | Callaway | 37 | 4337 | 16 | 13 | 15 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 116 | 7274 | 16 | 16 | 23 |
| Springfield | Missouri | Christian | 69 | 6627 | 16 | 21 | 31 |
| St. Louis-Farmington | Illinois | Macoupin | 72 | 4180 | 15 | 21 | 27 |
| St. Louis-Farmington | Missouri | St. Francois | 92 | 7404 | 14 | 14 | 24 |
| St. Joseph | Missouri | Buchanan | 126 | 6798 | 13 | 15 | 21 |
| Kansas City | Missouri | Platte | 37 | 2956 | 13 | 11 | 15 |
| Missouri non-MSA | Missouri | Taney | 73 | 4438 | 12 | 13 | 19 |
| St. Louis-Farmington | Missouri | Lincoln | 27 | 4115 | 12 | 13 | 16 |
| Missouri non-MSA | Missouri | Pettis | 72 | 4654 | 11 | 12 | 17 |
| Missouri non-MSA | Missouri | Butler | 27 | 3259 | 10 | 10 | 12 |
| Missouri non-MSA | Missouri | Johnson | 38 | 3693 | 9 | 9 | 13 |
| Kansas City | Missouri | Lafayette | 48 | 2428 | 8 | 8 | 10 |
| Joplin | Missouri | Newton | 62 | 3950 | 8 | 9 | 13 |
| Kansas City | Kansas | Miami | 28 | 2510 | 8 | 11 | 18 |
| Missouri non-MSA | Missouri | Camden | 75 | 3642 | 8 | 8 | 14 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2382 | 7 | 10 | 11 |
| Missouri non-MSA | Missouri | Stone | 33 | 1950 | 7 | 7 | 9 |
| Missouri non-MSA | Missouri | Laclede | 60 | 2845 | 6 | 6 | 9 |
| Missouri non-MSA | Missouri | Saline | 33 | 2351 | 6 | 7 | 9 |
| Springfield | Missouri | Webster | 46 | 2942 | 6 | 9 | 14 |
| St. Louis-Farmington | Missouri | Warren | 13 | 2006 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Henry | 30 | 1669 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Phelps | 114 | 2906 | 5 | 6 | 11 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1282 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Adair | 11 | 2000 | 5 | 7 | 11 |
| Missouri non-MSA | Missouri | Lawrence | 64 | 2657 | 5 | 6 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 37 | 2928 | 5 | 4 | 11 |
| Kansas City | Missouri | Ray | 20 | 1420 | 5 | 7 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3680 | 4 | 6 | 10 |
| Missouri non-MSA | Missouri | Barry | 43 | 2119 | 4 | 5 | 9 |
| Missouri non-MSA | Missouri | Crawford | 28 | 1998 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Howell | 41 | 2743 | 4 | 6 | 11 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1370 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Wright | 26 | 1333 | 4 | 4 | 7 |
| St. Joseph | Kansas | Doniphan | 13 | 909 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2352 | 4 | 5 | 8 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1657 | 4 | 3 | 5 |
| Kansas City | Missouri | Bates | 19 | 1044 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Benton | 23 | 1400 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Washington | 42 | 2077 | 4 | 5 | 8 |
| Kansas City | Missouri | Clinton | 60 | 1478 | 4 | 3 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2237 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Pike | 20 | 1458 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Ripley | 11 | 797 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Carroll | 21 | 798 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Macon | 12 | 1173 | 3 | 6 | 7 |
| Missouri non-MSA | Missouri | Nodaway | 23 | 2525 | 3 | 2 | 7 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 13 | 1577 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Texas | 21 | 1514 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Harrison | 14 | 802 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 43 | 1750 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Miller | 48 | 2286 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 564 | 3 | 3 | 2 |
| St. Louis-Farmington | Illinois | Bond | 21 | 1816 | 3 | 5 | 8 |
| Missouri non-MSA | Missouri | Barton | 10 | 925 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Perry | 22 | 2003 | 2 | 3 | 4 |
| St. Joseph | Missouri | Andrew | 17 | 1260 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Marion | 39 | 2590 | 2 | 4 | 6 |
| Springfield | Missouri | Polk | 26 | 2078 | 2 | 4 | 7 |
| Missouri non-MSA | Missouri | Mississippi | 22 | 1228 | 2 | 3 | 2 |
| St. Joseph | Missouri | DeKalb | 24 | 904 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 14 | 807 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1876 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Daviess | 11 | 570 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Vernon | 33 | 1334 | 2 | 3 | 6 |
| Kansas City | Kansas | Linn | 5 | 719 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Cedar | 10 | 649 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Randolph | 27 | 1795 | 2 | 1 | 5 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1038 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 25 | 1390 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 33 | 844 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Madison | 15 | 1335 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1659 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Grundy | 31 | 806 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Morgan | 36 | 1597 | 1 | 2 | 4 |
| Springfield | Missouri | Dallas | 22 | 794 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Shannon | 10 | 466 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 19 | 719 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Douglas | 23 | 751 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Linn | 10 | 531 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Maries | 7 | 524 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 6 | 448 | 1 | 1 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 418 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Audrain | 50 | 2019 | 1 | 4 | 6 |
| Missouri non-MSA | Missouri | Wayne | 9 | 792 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Monroe | 8 | 581 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 695 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Oregon | 3 | 661 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Ralls | 12 | 741 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 263 | 1 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 10 | 619 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 6 | 347 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 11 | 461 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 360 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 10 | 519 | 0 | 2 | 4 |
| Missouri non-MSA | Missouri | Scotland | 3 | 240 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 741 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Lewis | 3 | 621 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Mercer | 2 | 164 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 3 | 404 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Putnam | 2 | 219 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 8 | 411 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 173 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 3 | 461 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 551 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dade | 13 | 412 | 0 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 454 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Atchison | 6 | 289 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 257 | 0 | 0 | 0 |
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
