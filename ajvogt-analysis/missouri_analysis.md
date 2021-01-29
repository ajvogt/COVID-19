# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/28/2021  
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
| St. Louis-Farmington | 4078 | 239121 | 1023 | 1123 | 1408 |
| Kansas City | 2075 | 163212 | 815 | 866 | 1041 |
| Missouri non-MSA | 1701 | 105123 | 317 | 345 | 505 |
| Springfield | 532 | 34327 | 127 | 132 | 197 |
| Columbia-Jefferson City | 261 | 32939 | 87 | 91 | 135 |
| Joplin | 253 | 15345 | 53 | 52 | 73 |
| St. Joseph | 171 | 9713 | 30 | 31 | 42 |
| Cape Girardeau-Sikeston | 201 | 12238 | 27 | 31 | 44 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1664 | 82071 | 365 | 390 | 487 |
| Kansas City | Kansas | Johnson | 646 | 49248 | 313 | 350 | 379 |
| St. Louis-Farmington | Illinois | Madison | 492 | 25705 | 157 | 161 | 175 |
| Kansas City | Missouri | Jackson | 307 | 27886 | 136 | 136 | 168 |
| Kansas City | Missouri | Kansas City | 434 | 34951 | 134 | 137 | 183 |
| St. Louis-Farmington | Illinois | St. Clair | 462 | 23296 | 116 | 134 | 158 |
| St. Louis-Farmington | Missouri | St. Charles | 344 | 31215 | 100 | 111 | 154 |
| Springfield | Missouri | Greene | 378 | 22076 | 80 | 84 | 126 |
| St. Louis-Farmington | Missouri | Jefferson | 168 | 17977 | 71 | 80 | 109 |
| Kansas City | Kansas | Wyandotte | 228 | 18044 | 68 | 71 | 94 |
| Columbia-Jefferson City | Missouri | Boone | 61 | 15136 | 51 | 52 | 68 |
| St. Louis-Farmington | Missouri | St. Louis City | 348 | 20009 | 47 | 70 | 97 |
| Joplin | Missouri | Jasper | 193 | 11453 | 42 | 42 | 56 |
| Kansas City | Missouri | Cass | 69 | 6751 | 36 | 37 | 45 |
| Kansas City | Kansas | Leavenworth | 55 | 6121 | 36 | 39 | 39 |
| St. Louis-Farmington | Missouri | Franklin | 131 | 7928 | 33 | 39 | 52 |
| Kansas City | Missouri | Clay | 123 | 7362 | 30 | 30 | 41 |
| St. Louis-Farmington | Illinois | Macoupin | 99 | 4073 | 27 | 26 | 30 |
| Springfield | Missouri | Christian | 63 | 6515 | 26 | 27 | 39 |
| St. Louis-Farmington | Illinois | Clinton | 87 | 5247 | 23 | 25 | 29 |
| St. Joseph | Missouri | Buchanan | 120 | 6707 | 18 | 20 | 26 |
| St. Louis-Farmington | Illinois | Monroe | 71 | 3733 | 17 | 18 | 24 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 110 | 7160 | 16 | 19 | 27 |
| Kansas City | Kansas | Miami | 27 | 2452 | 15 | 19 | 24 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 4030 | 15 | 13 | 19 |
| Missouri non-MSA | Missouri | Taney | 68 | 4352 | 15 | 15 | 22 |
| St. Louis-Farmington | Missouri | St. Francois | 83 | 7300 | 15 | 17 | 31 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8280 | 14 | 15 | 27 |
| Missouri non-MSA | Missouri | Pettis | 69 | 4576 | 14 | 12 | 23 |
| St. Louis-Farmington | Illinois | Jersey | 62 | 2329 | 12 | 13 | 13 |
| Springfield | Missouri | Webster | 46 | 2897 | 12 | 12 | 18 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1961 | 11 | 10 | 12 |
| Joplin | Missouri | Newton | 60 | 3892 | 11 | 10 | 17 |
| Columbia-Jefferson City | Missouri | Callaway | 34 | 4222 | 9 | 9 | 18 |
| Missouri non-MSA | Missouri | Johnson | 35 | 3627 | 9 | 11 | 14 |
| Missouri non-MSA | Missouri | Butler | 24 | 3185 | 9 | 11 | 14 |
| Kansas City | Missouri | Platte | 35 | 2865 | 9 | 10 | 18 |
| Missouri non-MSA | Missouri | Macon | 10 | 1149 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Camden | 73 | 3585 | 9 | 9 | 17 |
| Missouri non-MSA | Missouri | Adair | 7 | 1961 | 9 | 10 | 13 |
| Missouri non-MSA | Missouri | Howell | 41 | 2713 | 9 | 10 | 15 |
| Kansas City | Missouri | Ray | 17 | 1384 | 9 | 7 | 10 |
| Missouri non-MSA | Missouri | Saline | 30 | 2304 | 8 | 7 | 11 |
| Missouri non-MSA | Missouri | Lawrence | 61 | 2619 | 8 | 5 | 11 |
| Missouri non-MSA | Missouri | Audrain | 50 | 2010 | 7 | 6 | 13 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3646 | 7 | 8 | 11 |
| Kansas City | Missouri | Lafayette | 46 | 2366 | 7 | 8 | 11 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2865 | 7 | 11 | 15 |
| St. Louis-Farmington | Illinois | Bond | 26 | 1795 | 7 | 6 | 10 |
| Missouri non-MSA | Missouri | Laclede | 57 | 2798 | 7 | 7 | 11 |
| Missouri non-MSA | Missouri | Stone | 31 | 1898 | 6 | 7 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2323 | 6 | 6 | 9 |
| Missouri non-MSA | Missouri | Crawford | 24 | 1967 | 6 | 7 | 10 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2209 | 6 | 6 | 7 |
| Kansas City | Missouri | Bates | 16 | 1016 | 6 | 4 | 7 |
| Missouri non-MSA | Missouri | Washington | 41 | 2049 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Livingston | 32 | 1243 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Harrison | 11 | 780 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Marion | 36 | 2570 | 6 | 5 | 9 |
| Missouri non-MSA | Missouri | Barry | 41 | 2087 | 5 | 8 | 10 |
| Missouri non-MSA | Missouri | Miller | 45 | 2265 | 5 | 5 | 9 |
| Missouri non-MSA | Missouri | Henry | 28 | 1626 | 5 | 5 | 7 |
| Kansas City | Kansas | Linn | 4 | 703 | 5 | 4 | 7 |
| Springfield | Missouri | Polk | 25 | 2058 | 5 | 4 | 9 |
| Missouri non-MSA | Missouri | Linn | 10 | 519 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Carroll | 18 | 773 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1553 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | McDonald | 24 | 1858 | 4 | 5 | 7 |
| St. Joseph | Kansas | Doniphan | 12 | 880 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Pike | 17 | 1431 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Vernon | 32 | 1317 | 4 | 5 | 12 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 543 | 4 | 2 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 21 | 1209 | 4 | 2 | 3 |
| Missouri non-MSA | Missouri | Wright | 24 | 1304 | 4 | 5 | 9 |
| Missouri non-MSA | Missouri | Ozark | 10 | 514 | 3 | 4 | 4 |
| St. Joseph | Missouri | Andrew | 16 | 1240 | 3 | 3 | 5 |
| Columbia-Jefferson City | Missouri | Osage | 10 | 1341 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 33 | 829 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 34 | 2892 | 3 | 6 | 12 |
| St. Joseph | Missouri | DeKalb | 23 | 886 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Perry | 22 | 1983 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Madison | 13 | 1320 | 3 | 2 | 5 |
| Kansas City | Missouri | Clinton | 60 | 1450 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Gentry | 19 | 707 | 3 | 3 | 3 |
| Springfield | Missouri | Dallas | 20 | 781 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Benton | 20 | 1372 | 3 | 3 | 7 |
| Missouri non-MSA | Missouri | Barton | 9 | 905 | 3 | 3 | 5 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1644 | 3 | 3 | 6 |
| Missouri non-MSA | Missouri | Ripley | 10 | 770 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Daviess | 10 | 553 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Wayne | 9 | 783 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Douglas | 23 | 739 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 41 | 1728 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1375 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dent | 11 | 789 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 654 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Cedar | 9 | 633 | 2 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1628 | 2 | 4 | 5 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 409 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 34 | 1584 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Chariton | 3 | 400 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Grundy | 30 | 793 | 2 | 3 | 4 |
| Kansas City | Missouri | Caldwell | 8 | 613 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Dade | 12 | 410 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 6 | 438 | 1 | 3 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 256 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Texas | 21 | 1490 | 1 | 3 | 6 |
| Missouri non-MSA | Missouri | Ralls | 10 | 734 | 1 | 1 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 688 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shelby | 5 | 341 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 5 | 452 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2501 | 1 | 4 | 7 |
| Missouri non-MSA | Missouri | Maries | 7 | 514 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Holt | 10 | 355 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 737 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Monroe | 7 | 572 | 1 | 1 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1023 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Lewis | 3 | 617 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Iron | 1 | 459 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Randolph | 24 | 1780 | 0 | 4 | 6 |
| Missouri non-MSA | Missouri | Knox | 2 | 170 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 160 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 216 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 10 | 454 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 136 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 256 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 8 | 408 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 549 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Hickory | 10 | 456 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Atchison | 6 | 287 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 236 | 0 | 0 | 0 |
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
