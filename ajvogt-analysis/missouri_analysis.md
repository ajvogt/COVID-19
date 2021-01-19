# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/19/2021  
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
| St. Louis-Farmington | 3791 | 227635 | 1210 | 1432 | 1412 |
| Kansas City | 1914 | 155445 | 942 | 1115 | 1076 |
| Missouri non-MSA | 1583 | 102421 | 423 | 564 | 568 |
| Springfield | 482 | 33196 | 158 | 223 | 214 |
| Columbia-Jefferson City | 244 | 32190 | 108 | 146 | 154 |
| Joplin | 242 | 14869 | 65 | 77 | 74 |
| Cape Girardeau-Sikeston | 193 | 12009 | 38 | 54 | 52 |
| St. Joseph | 160 | 9474 | 35 | 46 | 46 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1563 | 78781 | 451 | 523 | 496 |
| Kansas City | Kansas | Johnson | 603 | 46009 | 365 | 402 | 364 |
| St. Louis-Farmington | Illinois | Madison | 463 | 24262 | 171 | 183 | 171 |
| Kansas City | Missouri | Jackson | 283 | 26712 | 166 | 188 | 176 |
| St. Louis-Farmington | Illinois | St. Clair | 426 | 22191 | 153 | 174 | 160 |
| St. Louis-Farmington | Missouri | St. Charles | 315 | 30273 | 136 | 175 | 172 |
| Kansas City | Missouri | Kansas City | 382 | 33754 | 136 | 196 | 196 |
| Springfield | Missouri | Greene | 333 | 21363 | 103 | 144 | 138 |
| St. Louis-Farmington | Missouri | Jefferson | 153 | 17310 | 96 | 124 | 114 |
| Kansas City | Kansas | Wyandotte | 221 | 17419 | 89 | 99 | 110 |
| Columbia-Jefferson City | Missouri | Boone | 54 | 14678 | 56 | 74 | 75 |
| Joplin | Missouri | Jasper | 182 | 11074 | 50 | 59 | 56 |
| St. Louis-Farmington | Missouri | Franklin | 122 | 7623 | 45 | 57 | 55 |
| Kansas City | Missouri | Cass | 62 | 6432 | 44 | 51 | 47 |
| Kansas City | Missouri | Clay | 119 | 7093 | 38 | 47 | 45 |
| Kansas City | Kansas | Leavenworth | 52 | 5780 | 38 | 42 | 36 |
| St. Louis-Farmington | Illinois | Macoupin | 94 | 3826 | 31 | 33 | 28 |
| Springfield | Missouri | Christian | 60 | 6271 | 27 | 42 | 43 |
| St. Louis-Farmington | Illinois | Clinton | 85 | 5006 | 27 | 30 | 29 |
| St. Joseph | Missouri | Buchanan | 113 | 6561 | 23 | 29 | 28 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 106 | 7024 | 23 | 32 | 32 |
| St. Louis-Farmington | Missouri | St. Francois | 79 | 7165 | 20 | 34 | 37 |
| Missouri non-MSA | Missouri | Taney | 60 | 4222 | 19 | 26 | 22 |
| St. Louis-Farmington | Illinois | Monroe | 70 | 3561 | 18 | 23 | 26 |
| Missouri non-MSA | Missouri | Pettis | 68 | 4463 | 18 | 24 | 22 |
| Columbia-Jefferson City | Missouri | Cole | 101 | 8166 | 18 | 30 | 33 |
| Springfield | Missouri | Webster | 45 | 2793 | 16 | 21 | 19 |
| Missouri non-MSA | Missouri | Phelps | 103 | 2803 | 16 | 16 | 19 |
| Kansas City | Missouri | Platte | 27 | 2788 | 15 | 20 | 22 |
| Joplin | Missouri | Newton | 60 | 3795 | 15 | 18 | 18 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 3907 | 14 | 21 | 22 |
| Missouri non-MSA | Missouri | Howell | 41 | 2638 | 14 | 17 | 17 |
| Missouri non-MSA | Missouri | Barry | 38 | 2035 | 14 | 14 | 11 |
| Columbia-Jefferson City | Missouri | Callaway | 29 | 4141 | 14 | 19 | 22 |
| St. Louis-Farmington | Illinois | Jersey | 56 | 2206 | 13 | 12 | 15 |
| Missouri non-MSA | Missouri | Adair | 6 | 1877 | 13 | 14 | 15 |
| Missouri non-MSA | Missouri | Camden | 66 | 3505 | 13 | 20 | 20 |
| Kansas City | Kansas | Miami | 19 | 2221 | 12 | 20 | 23 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3530 | 12 | 17 | 16 |
| Missouri non-MSA | Missouri | Butler | 18 | 3088 | 12 | 14 | 15 |
| Missouri non-MSA | Missouri | Stone | 28 | 1842 | 10 | 12 | 11 |
| Missouri non-MSA | Missouri | Laclede | 54 | 2736 | 10 | 12 | 13 |
| Cape Girardeau-Sikeston | Missouri | Scott | 68 | 3584 | 10 | 15 | 14 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1735 | 9 | 12 | 10 |
| Missouri non-MSA | Missouri | Randolph | 20 | 1763 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | Saline | 26 | 2241 | 9 | 12 | 12 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2271 | 9 | 11 | 9 |
| Missouri non-MSA | Missouri | Washington | 41 | 1993 | 9 | 12 | 11 |
| Missouri non-MSA | Missouri | Vernon | 30 | 1284 | 8 | 10 | 13 |
| St. Louis-Farmington | Missouri | Warren | 11 | 1864 | 8 | 12 | 12 |
| Missouri non-MSA | Missouri | Pulaski | 33 | 2861 | 8 | 19 | 21 |
| Kansas City | Missouri | Lafayette | 44 | 2283 | 8 | 11 | 13 |
| Missouri non-MSA | Missouri | Wright | 24 | 1269 | 8 | 10 | 10 |
| Springfield | Missouri | Polk | 25 | 2016 | 8 | 11 | 10 |
| Missouri non-MSA | Missouri | McDonald | 23 | 1817 | 7 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1607 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Crawford | 21 | 1914 | 7 | 10 | 14 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17487 | 7 | 10 | 56 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2155 | 7 | 7 | 7 |
| Kansas City | Missouri | Ray | 15 | 1312 | 7 | 10 | 11 |
| Missouri non-MSA | Missouri | Henry | 25 | 1585 | 7 | 8 | 7 |
| Kansas City | Missouri | Clinton | 60 | 1419 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Livingston | 25 | 1189 | 7 | 9 | 8 |
| Missouri non-MSA | Missouri | Macon | 10 | 1067 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | Miller | 44 | 2216 | 6 | 10 | 10 |
| Missouri non-MSA | Missouri | Pike | 17 | 1396 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Marion | 32 | 2517 | 6 | 8 | 11 |
| Missouri non-MSA | Missouri | Gasconade | 31 | 798 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Harrison | 10 | 727 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Ozark | 5 | 484 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Audrain | 44 | 1953 | 6 | 8 | 15 |
| Kansas City | Kansas | Linn | 5 | 659 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2477 | 5 | 13 | 8 |
| Missouri non-MSA | Missouri | Barton | 9 | 882 | 5 | 7 | 5 |
| Missouri non-MSA | Missouri | Texas | 20 | 1475 | 5 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 26 | 1619 | 5 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Osage | 9 | 1304 | 4 | 6 | 6 |
| Kansas City | Missouri | Bates | 14 | 967 | 4 | 6 | 8 |
| St. Joseph | Kansas | Doniphan | 10 | 843 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Douglas | 20 | 714 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Morgan | 31 | 1567 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Dent | 9 | 771 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Clark | 5 | 418 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Grundy | 28 | 773 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Benton | 19 | 1341 | 4 | 8 | 6 |
| St. Joseph | Missouri | DeKalb | 21 | 859 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Wayne | 9 | 754 | 4 | 4 | 4 |
| St. Joseph | Missouri | Andrew | 16 | 1211 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Oregon | 3 | 636 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Cedar | 9 | 609 | 3 | 4 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 389 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Gentry | 17 | 680 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Lewis | 3 | 604 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Carroll | 18 | 737 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 12 | 723 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Ripley | 9 | 745 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Perry | 22 | 1954 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 11 | 1518 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Lawrence | 60 | 2542 | 3 | 12 | 11 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 438 | 2 | 3 | 2 |
| Springfield | Missouri | Dallas | 19 | 753 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Linn | 9 | 482 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 39 | 1705 | 2 | 5 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1350 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Chariton | 3 | 381 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 10 | 532 | 2 | 3 | 3 |
| Kansas City | Missouri | Caldwell | 8 | 597 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 675 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Iron | 1 | 453 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Maries | 7 | 503 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shannon | 9 | 449 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 515 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Madison | 11 | 1291 | 1 | 4 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1012 | 1 | 3 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 20 | 1178 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ralls | 9 | 718 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Dade | 10 | 394 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 4 | 329 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 545 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Hickory | 9 | 454 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 239 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Monroe | 7 | 562 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 252 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 7 | 404 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 2 | 156 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 163 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 209 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 132 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 9 | 346 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 6 | 286 | 0 | 1 | 1 |
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
