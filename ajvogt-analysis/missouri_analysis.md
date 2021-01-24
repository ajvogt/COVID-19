# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/24/2021  
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
| St. Louis-Farmington | 3943 | 233737 | 1136 | 1210 | 1365 |
| Kansas City | 2016 | 159829 | 896 | 955 | 1039 |
| Missouri non-MSA | 1649 | 104123 | 319 | 406 | 516 |
| Springfield | 509 | 33872 | 124 | 150 | 199 |
| Columbia-Jefferson City | 256 | 32664 | 86 | 107 | 140 |
| Joplin | 248 | 15155 | 53 | 60 | 72 |
| St. Joseph | 168 | 9612 | 27 | 34 | 43 |
| Cape Girardeau-Sikeston | 197 | 12149 | 24 | 35 | 48 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1628 | 80771 | 392 | 430 | 482 |
| St. Louis-Farmington | Illinois | Madison | 475 | 25198 | 171 | 172 | 171 |
| St. Louis-Farmington | Illinois | St. Clair | 449 | 22904 | 137 | 149 | 161 |
| Kansas City | Missouri | Kansas City | 425 | 34406 | 121 | 140 | 186 |
| St. Louis-Farmington | Missouri | St. Charles | 333 | 30916 | 117 | 136 | 160 |
| Kansas City | Missouri | Jackson | 297 | 27320 | 116 | 152 | 165 |
| St. Louis-Farmington | Missouri | Jefferson | 165 | 17750 | 82 | 94 | 111 |
| Springfield | Missouri | Greene | 358 | 21801 | 81 | 97 | 127 |
| Kansas City | Kansas | Wyandotte | 223 | 17751 | 76 | 83 | 96 |
| St. Louis-Farmington | Missouri | St. Louis City | 306 | 17852 | 55 | 29 | 49 |
| Columbia-Jefferson City | Missouri | Boone | 58 | 14968 | 51 | 57 | 69 |
| Joplin | Missouri | Jasper | 188 | 11302 | 43 | 47 | 55 |
| Kansas City | Kansas | Leavenworth | 53 | 5968 | 43 | 40 | 38 |
| St. Louis-Farmington | Missouri | Franklin | 128 | 7828 | 38 | 45 | 53 |
| St. Louis-Farmington | Illinois | Macoupin | 96 | 4002 | 29 | 32 | 30 |
| Kansas City | Missouri | Clay | 120 | 7264 | 28 | 37 | 43 |
| Kansas City | Missouri | Cass | 68 | 6598 | 28 | 40 | 44 |
| St. Louis-Farmington | Illinois | Clinton | 86 | 5162 | 26 | 27 | 28 |
| Springfield | Missouri | Christian | 61 | 6416 | 25 | 29 | 40 |
| Kansas City | Kansas | Miami | 22 | 2384 | 25 | 21 | 24 |
| St. Louis-Farmington | Illinois | Monroe | 71 | 3667 | 19 | 20 | 24 |
| St. Louis-Farmington | Missouri | St. Francois | 81 | 7257 | 17 | 21 | 33 |
| St. Joseph | Missouri | Buchanan | 117 | 6645 | 17 | 22 | 26 |
| Missouri non-MSA | Missouri | Taney | 68 | 4305 | 16 | 20 | 22 |
| St. Louis-Farmington | Illinois | Jersey | 61 | 2294 | 15 | 13 | 14 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 108 | 7099 | 14 | 20 | 29 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 3976 | 13 | 15 | 19 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8239 | 13 | 18 | 29 |
| Missouri non-MSA | Missouri | Butler | 22 | 3160 | 12 | 13 | 14 |
| Missouri non-MSA | Missouri | Pettis | 68 | 4541 | 12 | 16 | 22 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3598 | 11 | 13 | 16 |
| Springfield | Missouri | Webster | 45 | 2855 | 11 | 14 | 18 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1931 | 10 | 10 | 12 |
| Kansas City | Missouri | Lafayette | 45 | 2343 | 10 | 9 | 12 |
| Missouri non-MSA | Missouri | Macon | 10 | 1123 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2843 | 9 | 14 | 16 |
| Joplin | Missouri | Newton | 60 | 3853 | 9 | 12 | 16 |
| Missouri non-MSA | Missouri | Adair | 7 | 1933 | 9 | 12 | 14 |
| Missouri non-MSA | Missouri | Camden | 69 | 3549 | 8 | 12 | 18 |
| Columbia-Jefferson City | Missouri | Callaway | 33 | 4189 | 8 | 12 | 19 |
| Kansas City | Missouri | Platte | 34 | 2828 | 8 | 14 | 19 |
| Missouri non-MSA | Missouri | Saline | 28 | 2287 | 8 | 9 | 11 |
| Kansas City | Missouri | Ray | 17 | 1356 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Lawrence | 61 | 2590 | 8 | 7 | 11 |
| Missouri non-MSA | Missouri | Howell | 41 | 2687 | 7 | 12 | 15 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1779 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Marion | 34 | 2562 | 7 | 7 | 10 |
| Cape Girardeau-Sikeston | Missouri | Scott | 70 | 3628 | 7 | 9 | 13 |
| Missouri non-MSA | Missouri | Livingston | 25 | 1229 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2306 | 6 | 8 | 9 |
| Missouri non-MSA | Missouri | Laclede | 55 | 2768 | 6 | 8 | 11 |
| Missouri non-MSA | Missouri | Washington | 41 | 2023 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Barry | 40 | 2063 | 6 | 10 | 10 |
| Missouri non-MSA | Missouri | Stone | 29 | 1869 | 5 | 8 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 33 | 2882 | 5 | 7 | 13 |
| Missouri non-MSA | Missouri | Crawford | 23 | 1945 | 5 | 7 | 11 |
| Missouri non-MSA | Missouri | Miller | 45 | 2250 | 5 | 7 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2186 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Wright | 24 | 1292 | 5 | 7 | 9 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2492 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Vernon | 31 | 1307 | 5 | 6 | 12 |
| Kansas City | Kansas | Linn | 4 | 676 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Pike | 17 | 1423 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 32 | 819 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | McDonald | 24 | 1844 | 4 | 7 | 7 |
| Missouri non-MSA | Missouri | Harrison | 10 | 752 | 4 | 5 | 5 |
| Kansas City | Missouri | Bates | 15 | 993 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Benton | 19 | 1364 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Audrain | 47 | 1972 | 4 | 5 | 13 |
| Columbia-Jefferson City | Missouri | Osage | 9 | 1327 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Henry | 26 | 1603 | 4 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1638 | 3 | 5 | 6 |
| St. Joseph | Missouri | Andrew | 16 | 1231 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1540 | 3 | 3 | 5 |
| Kansas City | Missouri | Clinton | 60 | 1437 | 3 | 5 | 8 |
| Missouri non-MSA | Missouri | Madison | 13 | 1312 | 3 | 3 | 6 |
| St. Joseph | Missouri | DeKalb | 23 | 879 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Douglas | 21 | 733 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Wayne | 9 | 769 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Gentry | 18 | 697 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Carroll | 18 | 753 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Ozark | 6 | 502 | 3 | 6 | 4 |
| Springfield | Missouri | Dallas | 20 | 768 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 533 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 40 | 1723 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Perry | 22 | 1974 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Linn | 10 | 503 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 10 | 780 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Texas | 20 | 1485 | 3 | 4 | 6 |
| St. Joseph | Kansas | Doniphan | 12 | 857 | 3 | 4 | 6 |
| Springfield | Missouri | Polk | 25 | 2032 | 2 | 5 | 9 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 404 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1367 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 20 | 1195 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Ripley | 10 | 763 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Clark | 5 | 428 | 2 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1619 | 2 | 5 | 5 |
| Missouri non-MSA | Missouri | Chariton | 3 | 397 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Randolph | 21 | 1771 | 2 | 6 | 7 |
| Missouri non-MSA | Missouri | Barton | 9 | 895 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Sullivan | 12 | 733 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Grundy | 30 | 786 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Cedar | 9 | 623 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Oregon | 3 | 645 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Lewis | 3 | 615 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 251 | 2 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 684 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 10 | 542 | 1 | 2 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 450 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ralls | 9 | 729 | 1 | 1 | 3 |
| Kansas City | Missouri | Caldwell | 8 | 608 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Maries | 7 | 512 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 5 | 336 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 34 | 1574 | 1 | 3 | 5 |
| Missouri non-MSA | Missouri | Holt | 10 | 354 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 169 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 214 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 12 | 401 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1018 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Monroe | 7 | 568 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Carter | 8 | 407 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 548 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 1 | 135 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 255 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 2 | 157 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 451 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 1 | 454 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Atchison | 6 | 287 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 235 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 10 | 455 | 0 | 0 | 1 |
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
