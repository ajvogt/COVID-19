# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/25/2021  
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
| St. Louis-Farmington | 3946 | 234656 | 1133 | 1180 | 1375 |
| Kansas City | 2016 | 160637 | 972 | 966 | 1047 |
| Missouri non-MSA | 1652 | 104456 | 325 | 384 | 513 |
| Springfield | 509 | 33985 | 130 | 145 | 199 |
| Columbia-Jefferson City | 256 | 32765 | 89 | 101 | 137 |
| Joplin | 252 | 15195 | 52 | 57 | 72 |
| St. Joseph | 168 | 9646 | 28 | 34 | 43 |
| Cape Girardeau-Sikeston | 197 | 12173 | 24 | 33 | 46 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1628 | 81147 | 387 | 424 | 495 |
| St. Louis-Farmington | Illinois | Madison | 477 | 25299 | 165 | 167 | 170 |
| Kansas City | Missouri | Kansas City | 425 | 34742 | 152 | 143 | 191 |
| Kansas City | Missouri | Jackson | 297 | 27585 | 139 | 157 | 168 |
| St. Louis-Farmington | Illinois | St. Clair | 450 | 22976 | 130 | 143 | 159 |
| St. Louis-Farmington | Missouri | St. Charles | 333 | 31019 | 117 | 129 | 159 |
| Springfield | Missouri | Greene | 358 | 21871 | 85 | 94 | 128 |
| St. Louis-Farmington | Missouri | Jefferson | 165 | 17800 | 81 | 89 | 110 |
| Kansas City | Kansas | Wyandotte | 223 | 17751 | 76 | 83 | 96 |
| St. Louis-Farmington | Missouri | St. Louis City | 306 | 17987 | 74 | 38 | 53 |
| Columbia-Jefferson City | Missouri | Boone | 58 | 15026 | 53 | 55 | 68 |
| Kansas City | Kansas | Leavenworth | 53 | 5968 | 43 | 40 | 38 |
| Joplin | Missouri | Jasper | 192 | 11336 | 42 | 45 | 55 |
| St. Louis-Farmington | Missouri | Franklin | 128 | 7854 | 38 | 41 | 52 |
| Kansas City | Missouri | Cass | 68 | 6697 | 38 | 43 | 46 |
| Kansas City | Missouri | Clay | 120 | 7311 | 34 | 38 | 43 |
| St. Louis-Farmington | Illinois | Macoupin | 96 | 4009 | 28 | 31 | 29 |
| Springfield | Missouri | Christian | 61 | 6439 | 27 | 28 | 39 |
| St. Louis-Farmington | Illinois | Clinton | 86 | 5174 | 26 | 27 | 28 |
| Kansas City | Kansas | Miami | 22 | 2384 | 25 | 21 | 24 |
| St. Louis-Farmington | Illinois | Monroe | 71 | 3673 | 18 | 19 | 23 |
| St. Joseph | Missouri | Buchanan | 117 | 6673 | 17 | 21 | 26 |
| St. Louis-Farmington | Missouri | St. Francois | 81 | 7267 | 17 | 19 | 33 |
| St. Louis-Farmington | Illinois | Jersey | 61 | 2301 | 15 | 14 | 14 |
| Missouri non-MSA | Missouri | Taney | 68 | 4314 | 14 | 18 | 22 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 108 | 7117 | 14 | 19 | 29 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 3984 | 13 | 13 | 19 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8253 | 13 | 17 | 28 |
| Missouri non-MSA | Missouri | Butler | 22 | 3163 | 12 | 11 | 14 |
| Missouri non-MSA | Missouri | Pettis | 68 | 4545 | 12 | 15 | 22 |
| Springfield | Missouri | Webster | 45 | 2869 | 12 | 14 | 18 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3611 | 12 | 12 | 15 |
| Kansas City | Missouri | Lafayette | 45 | 2358 | 11 | 10 | 12 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1934 | 10 | 10 | 12 |
| Missouri non-MSA | Missouri | Macon | 10 | 1136 | 10 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Callaway | 33 | 4205 | 10 | 12 | 19 |
| Missouri non-MSA | Missouri | Camden | 69 | 3564 | 9 | 11 | 17 |
| Joplin | Missouri | Newton | 60 | 3859 | 9 | 12 | 16 |
| Kansas City | Missouri | Platte | 34 | 2845 | 9 | 14 | 19 |
| Missouri non-MSA | Missouri | Adair | 7 | 1938 | 9 | 11 | 13 |
| Kansas City | Missouri | Ray | 17 | 1367 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2852 | 8 | 13 | 15 |
| Missouri non-MSA | Missouri | Lawrence | 61 | 2602 | 8 | 6 | 11 |
| Missouri non-MSA | Missouri | Howell | 41 | 2694 | 8 | 11 | 15 |
| Missouri non-MSA | Missouri | Saline | 28 | 2292 | 8 | 9 | 11 |
| Missouri non-MSA | Missouri | Marion | 34 | 2569 | 7 | 7 | 10 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1782 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Laclede | 55 | 2780 | 7 | 8 | 12 |
| Cape Girardeau-Sikeston | Missouri | Scott | 70 | 3633 | 7 | 9 | 12 |
| Missouri non-MSA | Missouri | Livingston | 25 | 1235 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Barry | 40 | 2073 | 6 | 10 | 10 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2199 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Washington | 41 | 2032 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Crawford | 23 | 1954 | 6 | 7 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2311 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Miller | 45 | 2257 | 6 | 6 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 33 | 2890 | 5 | 7 | 13 |
| Missouri non-MSA | Missouri | McDonald | 24 | 1852 | 5 | 7 | 8 |
| Missouri non-MSA | Missouri | Stone | 29 | 1875 | 5 | 8 | 10 |
| Kansas City | Missouri | Bates | 15 | 1001 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Vernon | 31 | 1312 | 5 | 6 | 12 |
| Missouri non-MSA | Missouri | Henry | 27 | 1614 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2492 | 5 | 5 | 6 |
| Columbia-Jefferson City | Missouri | Osage | 9 | 1334 | 5 | 5 | 6 |
| Kansas City | Kansas | Linn | 4 | 676 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Wright | 24 | 1295 | 4 | 7 | 9 |
| Missouri non-MSA | Missouri | Carroll | 18 | 765 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Harrison | 10 | 756 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Pike | 17 | 1425 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Benton | 19 | 1367 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 32 | 820 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Audrain | 47 | 1979 | 4 | 5 | 13 |
| St. Joseph | Missouri | Andrew | 16 | 1235 | 4 | 4 | 6 |
| Kansas City | Missouri | Clinton | 60 | 1445 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1545 | 3 | 3 | 5 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1640 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Gentry | 18 | 703 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Ozark | 7 | 508 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Madison | 13 | 1314 | 3 | 2 | 5 |
| Missouri non-MSA | Missouri | Linn | 10 | 506 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Wayne | 9 | 771 | 3 | 3 | 4 |
| St. Joseph | Missouri | DeKalb | 23 | 881 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 536 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Ripley | 10 | 767 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1371 | 3 | 2 | 3 |
| Springfield | Missouri | Dallas | 20 | 771 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Perry | 22 | 1974 | 3 | 3 | 5 |
| Springfield | Missouri | Polk | 25 | 2035 | 3 | 5 | 9 |
| St. Joseph | Kansas | Doniphan | 12 | 857 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Mississippi | 21 | 1199 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Douglas | 21 | 735 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 40 | 1724 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Grundy | 30 | 790 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Cedar | 9 | 627 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Barton | 9 | 899 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Daviess | 10 | 547 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 398 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 12 | 737 | 2 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 404 | 2 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1621 | 2 | 5 | 5 |
| Missouri non-MSA | Missouri | Dent | 10 | 781 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 648 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Clark | 5 | 432 | 2 | 3 | 2 |
| Kansas City | Missouri | Caldwell | 8 | 610 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Ralls | 9 | 730 | 1 | 1 | 3 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 450 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Texas | 20 | 1485 | 1 | 3 | 6 |
| Missouri non-MSA | Missouri | Morgan | 34 | 1577 | 1 | 3 | 5 |
| Missouri non-MSA | Missouri | Lewis | 3 | 615 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Maries | 7 | 513 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dade | 12 | 406 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 250 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 686 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Randolph | 21 | 1771 | 1 | 5 | 7 |
| Missouri non-MSA | Missouri | Shelby | 5 | 338 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 216 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 355 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Monroe | 7 | 570 | 1 | 1 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1019 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 2 | 169 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 8 | 408 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Mercer | 2 | 158 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 548 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Shannon | 10 | 452 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 135 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 254 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Iron | 1 | 454 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 10 | 455 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Atchison | 6 | 287 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 235 | 0 | 0 | 0 |
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
