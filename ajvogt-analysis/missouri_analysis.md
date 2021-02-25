# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/24/2021  
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
| Kansas City | 2464 | 174723 | 419 | 379 | 469 |
| St. Louis-Farmington | 4514 | 254622 | 373 | 448 | 600 |
| Missouri non-MSA | 1998 | 109476 | 93 | 108 | 167 |
| Springfield | 607 | 36066 | 37 | 43 | 69 |
| Columbia-Jefferson City | 309 | 34329 | 32 | 32 | 52 |
| Joplin | 281 | 16218 | 18 | 19 | 34 |
| Cape Girardeau-Sikeston | 220 | 12787 | 11 | 13 | 20 |
| St. Joseph | 199 | 10064 | 7 | 7 | 13 |
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
| Kansas City | Kansas | Johnson | 738 | 53708 | 215 | 182 | 193 |
| St. Louis-Farmington | Missouri | St. Louis | 1932 | 87744 | 150 | 171 | 219 |
| Kansas City | Missouri | Jackson | 377 | 29952 | 62 | 56 | 78 |
| St. Louis-Farmington | Illinois | St. Clair | 463 | 25173 | 49 | 51 | 73 |
| Kansas City | Kansas | Wyandotte | 265 | 19039 | 45 | 40 | 42 |
| St. Louis-Farmington | Illinois | Madison | 451 | 27715 | 41 | 53 | 80 |
| Kansas City | Missouri | Kansas City | 513 | 36592 | 33 | 33 | 61 |
| St. Louis-Farmington | Missouri | St. Louis City | 416 | 21283 | 33 | 37 | 45 |
| St. Louis-Farmington | Missouri | St. Charles | 413 | 32759 | 31 | 53 | 58 |
| Springfield | Missouri | Greene | 425 | 23271 | 26 | 30 | 46 |
| St. Louis-Farmington | Missouri | Jefferson | 210 | 18904 | 18 | 21 | 36 |
| Columbia-Jefferson City | Missouri | Boone | 79 | 15842 | 17 | 17 | 27 |
| Kansas City | Kansas | Leavenworth | 76 | 6708 | 15 | 18 | 24 |
| Joplin | Missouri | Jasper | 215 | 12153 | 14 | 15 | 27 |
| Kansas City | Missouri | Clay | 143 | 7841 | 14 | 11 | 17 |
| St. Louis-Farmington | Missouri | Franklin | 154 | 8380 | 11 | 13 | 17 |
| Kansas City | Missouri | Cass | 89 | 7185 | 8 | 11 | 16 |
| Missouri non-MSA | Missouri | Butler | 33 | 3437 | 8 | 9 | 9 |
| Columbia-Jefferson City | Missouri | Callaway | 43 | 4461 | 7 | 5 | 8 |
| Springfield | Missouri | Christian | 77 | 6838 | 7 | 7 | 13 |
| Kansas City | Missouri | Ray | 24 | 1505 | 6 | 4 | 4 |
| St. Louis-Farmington | Missouri | St. Francois | 104 | 7559 | 6 | 6 | 9 |
| St. Louis-Farmington | Illinois | Monroe | 80 | 4032 | 6 | 6 | 11 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 125 | 7495 | 6 | 7 | 12 |
| Kansas City | Missouri | Platte | 42 | 3082 | 5 | 5 | 7 |
| St. Joseph | Missouri | Buchanan | 135 | 6935 | 5 | 4 | 8 |
| St. Louis-Farmington | Missouri | Lincoln | 35 | 4273 | 5 | 8 | 9 |
| Missouri non-MSA | Missouri | Phelps | 121 | 2992 | 5 | 4 | 4 |
| St. Louis-Farmington | Illinois | Macoupin | 78 | 4321 | 5 | 6 | 10 |
| Cape Girardeau-Sikeston | Missouri | Scott | 75 | 3799 | 5 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Cole | 114 | 8556 | 4 | 6 | 10 |
| Missouri non-MSA | Missouri | Johnson | 45 | 3846 | 4 | 6 | 7 |
| Kansas City | Kansas | Miami | 39 | 2600 | 4 | 5 | 7 |
| Joplin | Missouri | Newton | 66 | 4065 | 4 | 4 | 6 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1891 | 3 | 4 | 3 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5551 | 3 | 5 | 12 |
| St. Louis-Farmington | Illinois | Jersey | 45 | 2479 | 3 | 4 | 5 |
| Kansas City | Missouri | Lafayette | 53 | 2534 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Taney | 83 | 4557 | 3 | 4 | 8 |
| Missouri non-MSA | Missouri | Pettis | 76 | 4761 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Stone | 36 | 2018 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Henry | 36 | 1734 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Pulaski | 44 | 2979 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Camden | 81 | 3710 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Vernon | 39 | 1386 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Barry | 44 | 2178 | 2 | 1 | 3 |
| St. Louis-Farmington | Missouri | Warren | 18 | 2083 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Howell | 42 | 2800 | 2 | 2 | 3 |
| Springfield | Missouri | Polk | 30 | 2147 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Benton | 26 | 1447 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Crawford | 30 | 2044 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Saline | 35 | 2419 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Barton | 12 | 960 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Laclede | 65 | 2917 | 2 | 1 | 4 |
| Missouri non-MSA | Missouri | Adair | 16 | 2059 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2296 | 1 | 1 | 3 |
| Kansas City | Missouri | Clinton | 64 | 1522 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Marion | 41 | 2642 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Lawrence | 72 | 2745 | 1 | 3 | 4 |
| Missouri non-MSA | Missouri | Perry | 26 | 2039 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1256 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 37 | 1325 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 15 | 1613 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | McDonald | 26 | 1914 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Chariton | 6 | 421 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 26 | 1685 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dunklin | 19 | 2404 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Washington | 46 | 2119 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ripley | 14 | 853 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 6 | 471 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 13 | 1394 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Texas | 22 | 1536 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Miller | 49 | 2313 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 22 | 1483 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Nodaway | 24 | 2555 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Monroe | 10 | 593 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 27 | 919 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Macon | 14 | 1201 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Dent | 16 | 818 | 0 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 10 | 640 | 0 | 0 | 1 |
| Kansas City | Missouri | Bates | 23 | 1071 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Audrain | 58 | 2067 | 0 | 1 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 475 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 258 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Shannon | 10 | 481 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 34 | 826 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 38 | 874 | 0 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 17 | 1280 | 0 | 1 | 1 |
| Springfield | Missouri | Webster | 52 | 2989 | 0 | 1 | 4 |
| St. Joseph | Kansas | Doniphan | 20 | 930 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Ozark | 13 | 549 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Wayne | 10 | 817 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 28 | 1409 | 0 | 0 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 442 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Wright | 29 | 1366 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Lewis | 5 | 628 | 0 | 0 | 0 |
| Springfield | Missouri | Dallas | 23 | 821 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 11 | 587 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carroll | 23 | 833 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1769 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 567 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1678 | 0 | 0 | 1 |
| Kansas City | Kansas | Linn | 8 | 744 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Cedar | 17 | 666 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Harrison | 14 | 826 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 577 | 0 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 5 | 713 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Randolph | 29 | 1807 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 534 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 14 | 747 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1051 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 8 | 421 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 5 | 465 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 178 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 3 | 672 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 366 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 12 | 755 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 20 | 734 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Douglas | 25 | 766 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Morgan | 40 | 1621 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dade | 13 | 418 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 13 | 466 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 176 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 141 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 16 | 1343 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 3 | 263 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 12 | 540 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 260 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 3 | 223 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 7 | 349 | 0 | 0 | 0 |
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
