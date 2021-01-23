# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/23/2021  
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
| St. Louis-Farmington | 3917 | 232507 | 1129 | 1271 | 1381 |
| Kansas City | 2010 | 159392 | 899 | 988 | 1050 |
| Missouri non-MSA | 1647 | 103785 | 333 | 441 | 534 |
| Springfield | 508 | 33745 | 126 | 161 | 203 |
| Columbia-Jefferson City | 256 | 32560 | 88 | 112 | 145 |
| Joplin | 248 | 15104 | 52 | 63 | 73 |
| St. Joseph | 168 | 9587 | 30 | 37 | 44 |
| Cape Girardeau-Sikeston | 196 | 12114 | 24 | 37 | 49 |
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
| Kansas City | Kansas | Johnson | 625 | 47897 | 417 | 388 | 372 |
| St. Louis-Farmington | Missouri | St. Louis | 1620 | 80285 | 399 | 459 | 483 |
| St. Louis-Farmington | Illinois | Madison | 472 | 25015 | 166 | 175 | 174 |
| St. Louis-Farmington | Illinois | St. Clair | 439 | 22782 | 135 | 154 | 163 |
| St. Louis-Farmington | Missouri | St. Charles | 333 | 30812 | 121 | 148 | 162 |
| Kansas City | Missouri | Kansas City | 423 | 34236 | 119 | 156 | 189 |
| Kansas City | Missouri | Jackson | 293 | 27169 | 117 | 159 | 168 |
| St. Louis-Farmington | Missouri | Jefferson | 165 | 17666 | 82 | 100 | 112 |
| Springfield | Missouri | Greene | 357 | 21711 | 82 | 103 | 130 |
| Kansas City | Kansas | Wyandotte | 223 | 17751 | 76 | 83 | 96 |
| Columbia-Jefferson City | Missouri | Boone | 58 | 14909 | 52 | 61 | 72 |
| St. Louis-Farmington | Missouri | St. Louis City | 303 | 17770 | 44 | 24 | 51 |
| Kansas City | Kansas | Leavenworth | 53 | 5968 | 43 | 40 | 38 |
| Joplin | Missouri | Jasper | 188 | 11265 | 42 | 50 | 56 |
| St. Louis-Farmington | Missouri | Franklin | 128 | 7790 | 40 | 49 | 53 |
| Kansas City | Missouri | Cass | 68 | 6559 | 30 | 45 | 45 |
| St. Louis-Farmington | Illinois | Macoupin | 96 | 3975 | 29 | 34 | 30 |
| Kansas City | Missouri | Clay | 120 | 7220 | 28 | 39 | 45 |
| St. Louis-Farmington | Illinois | Clinton | 86 | 5145 | 27 | 27 | 29 |
| Springfield | Missouri | Christian | 61 | 6397 | 27 | 32 | 41 |
| Kansas City | Kansas | Miami | 22 | 2384 | 25 | 21 | 24 |
| St. Joseph | Missouri | Buchanan | 117 | 6628 | 20 | 24 | 27 |
| St. Louis-Farmington | Illinois | Monroe | 71 | 3651 | 19 | 21 | 25 |
| St. Louis-Farmington | Missouri | St. Francois | 81 | 7236 | 16 | 24 | 34 |
| Missouri non-MSA | Missouri | Taney | 68 | 4288 | 16 | 22 | 22 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 108 | 7081 | 14 | 22 | 30 |
| St. Louis-Farmington | Illinois | Jersey | 59 | 2274 | 14 | 13 | 14 |
| Missouri non-MSA | Missouri | Butler | 22 | 3148 | 13 | 14 | 14 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 3964 | 13 | 15 | 20 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8210 | 12 | 19 | 30 |
| Missouri non-MSA | Missouri | Pettis | 68 | 4526 | 11 | 17 | 23 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3589 | 11 | 14 | 16 |
| Springfield | Missouri | Webster | 45 | 2842 | 11 | 16 | 18 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1919 | 10 | 11 | 12 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2831 | 10 | 13 | 16 |
| Missouri non-MSA | Missouri | Lawrence | 61 | 2585 | 10 | 8 | 12 |
| Missouri non-MSA | Missouri | Adair | 7 | 1920 | 9 | 13 | 14 |
| Kansas City | Missouri | Lafayette | 45 | 2334 | 9 | 10 | 12 |
| Missouri non-MSA | Missouri | Howell | 41 | 2679 | 9 | 12 | 16 |
| Joplin | Missouri | Newton | 60 | 3839 | 9 | 13 | 16 |
| Missouri non-MSA | Missouri | Saline | 28 | 2284 | 9 | 10 | 12 |
| Missouri non-MSA | Missouri | Camden | 69 | 3543 | 8 | 15 | 18 |
| Kansas City | Missouri | Platte | 34 | 2819 | 8 | 14 | 20 |
| Missouri non-MSA | Missouri | Macon | 10 | 1104 | 8 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Callaway | 33 | 4179 | 8 | 13 | 20 |
| Kansas City | Missouri | Ray | 17 | 1347 | 8 | 8 | 10 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1774 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Washington | 41 | 2017 | 7 | 8 | 10 |
| Missouri non-MSA | Missouri | Livingston | 25 | 1221 | 6 | 8 | 8 |
| Missouri non-MSA | Missouri | Stone | 29 | 1863 | 6 | 9 | 11 |
| Missouri non-MSA | Missouri | Laclede | 54 | 2763 | 6 | 9 | 12 |
| Missouri non-MSA | Missouri | Marion | 34 | 2547 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Wright | 24 | 1289 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Vernon | 31 | 1302 | 6 | 7 | 13 |
| Missouri non-MSA | Missouri | McDonald | 24 | 1841 | 5 | 7 | 8 |
| Missouri non-MSA | Missouri | Barry | 40 | 2056 | 5 | 10 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2296 | 5 | 9 | 9 |
| Cape Girardeau-Sikeston | Missouri | Scott | 69 | 3613 | 5 | 10 | 13 |
| Missouri non-MSA | Missouri | Pike | 17 | 1417 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2179 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Crawford | 23 | 1936 | 5 | 8 | 12 |
| Missouri non-MSA | Missouri | Randolph | 21 | 1782 | 5 | 8 | 8 |
| Missouri non-MSA | Missouri | Pulaski | 33 | 2874 | 5 | 8 | 13 |
| Missouri non-MSA | Missouri | Miller | 45 | 2241 | 5 | 7 | 9 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2492 | 5 | 5 | 7 |
| Kansas City | Missouri | Bates | 15 | 992 | 4 | 5 | 8 |
| Kansas City | Kansas | Linn | 4 | 676 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Harrison | 10 | 750 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 32 | 813 | 4 | 5 | 6 |
| Columbia-Jefferson City | Missouri | Osage | 9 | 1324 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Wayne | 9 | 768 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Benton | 19 | 1363 | 4 | 5 | 7 |
| Kansas City | Missouri | Clinton | 60 | 1433 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Ozark | 5 | 498 | 4 | 6 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1621 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Audrain | 47 | 1965 | 4 | 6 | 14 |
| Missouri non-MSA | Missouri | Perry | 22 | 1971 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Douglas | 21 | 729 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Texas | 20 | 1482 | 3 | 4 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1634 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Barton | 9 | 893 | 3 | 5 | 5 |
| St. Joseph | Missouri | Andrew | 16 | 1225 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 40 | 1723 | 3 | 3 | 5 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 404 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Linn | 10 | 499 | 3 | 4 | 3 |
| St. Joseph | Missouri | DeKalb | 23 | 877 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1532 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Clark | 5 | 426 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Henry | 26 | 1595 | 3 | 6 | 7 |
| Missouri non-MSA | Missouri | Carroll | 18 | 751 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Dent | 10 | 779 | 3 | 3 | 4 |
| Springfield | Missouri | Dallas | 20 | 766 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Gentry | 18 | 693 | 3 | 3 | 4 |
| Springfield | Missouri | Polk | 25 | 2029 | 3 | 6 | 9 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1364 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Madison | 13 | 1308 | 3 | 3 | 6 |
| St. Joseph | Kansas | Doniphan | 12 | 857 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Grundy | 30 | 786 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 12 | 732 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 397 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Cedar | 9 | 621 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Lewis | 3 | 613 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 20 | 1193 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 644 | 2 | 3 | 4 |
| Kansas City | Missouri | Caldwell | 8 | 607 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 683 | 2 | 2 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 449 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 251 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 34 | 1572 | 1 | 4 | 5 |
| Missouri non-MSA | Missouri | Daviess | 10 | 540 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 522 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ripley | 10 | 755 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Maries | 7 | 509 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 5 | 335 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 9 | 724 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Putnam | 2 | 214 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 167 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 351 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 7 | 567 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dade | 12 | 400 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 8 | 407 | 0 | 0 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1016 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Mercer | 2 | 157 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 450 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 548 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 10 | 455 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 254 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 1 | 453 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Worth | 1 | 132 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 235 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 286 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
