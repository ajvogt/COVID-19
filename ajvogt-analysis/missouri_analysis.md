# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/30/2020  
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


## Missouri New Daily Deaths by Metropolitan Statistcal Areas
![](images/mo_daily_deaths.png)

## Missouri New Daily Confirmed Cases by Metropolitan Statistcal Areas
![](images/mo_daily_cases.png)

## Missouri Metropolitan Statistical Area Totals
<!-- msa_table start -->
| MSA | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|
| St. Louis-Farmington | 1626 | 64506 | 547 | 535 | 554 |
| Kansas City | 606 | 44837 | 410 | 380 | 355 |
| Missouri non-MSA | 298 | 25410 | 392 | 406 | 366 |
| Springfield | 73 | 9395 | 181 | 175 | 169 |
| Columbia-Jefferson City | 37 | 8076 | 94 | 90 | 126 |
| Cape Girardeau-Sikeston | 34 | 3137 | 53 | 51 | 46 |
| Joplin | 68 | 5337 | 52 | 65 | 64 |
| St. Joseph | 20 | 2531 | 38 | 39 | 32 |
<!-- msa_table end -->

## STL-Farmington MSA New Daily Deaths by County
![](images/stl_daily_deaths.png)

## STL-Farmington MSA New Daily Confirmed Cases by County
![](images/stl_daily_cases.png)

<a name="msa-counties"></a>
## Metropolitan Statistical Area (MSA) Counties
<!-- county_table start -->
| MSA | State | County | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|---|---|
| St. Louis-Farmington | Missouri | St. Louis | 809 | 24425 | 184 | 166 | 171 |
| Kansas City | Kansas | Johnson | 153 | 11123 | 114 | 107 | 99 |
| Springfield | Missouri | Greene | 58 | 6398 | 114 | 109 | 111 |
| Kansas City | Missouri | Kansas City | 125 | 11276 | 80 | 73 | 69 |
| Kansas City | Missouri | Jackson | 102 | 7588 | 74 | 69 | 70 |
| St. Louis-Farmington | Missouri | St. Charles | 120 | 7751 | 61 | 68 | 68 |
| St. Louis-Farmington | Illinois | St. Clair | 190 | 6729 | 55 | 49 | 49 |
| St. Louis-Farmington | Illinois | Madison | 141 | 5802 | 55 | 55 | 60 |
| St. Louis-Farmington | Missouri | Jefferson | 59 | 4282 | 47 | 53 | 53 |
| Kansas City | Kansas | Wyandotte | 134 | 6991 | 38 | 34 | 32 |
| Columbia-Jefferson City | Missouri | Boone | 10 | 4727 | 37 | 38 | 73 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 15 | 1807 | 37 | 33 | 28 |
| Kansas City | Kansas | Leavenworth | 11 | 2178 | 36 | 25 | 18 |
| Joplin | Missouri | Jasper | 53 | 3830 | 34 | 45 | 50 |
| St. Louis-Farmington | Missouri | St. Louis City | 198 | 7125 | 34 | 32 | 32 |
| St. Joseph | Missouri | Buchanan | 16 | 2026 | 31 | 30 | 24 |
| Springfield | Missouri | Christian | 6 | 1472 | 27 | 28 | 27 |
| Columbia-Jefferson City | Missouri | Cole | 14 | 1584 | 26 | 25 | 25 |
| St. Louis-Farmington | Missouri | Franklin | 29 | 1757 | 26 | 27 | 24 |
| St. Louis-Farmington | Missouri | St. Francois | 11 | 2131 | 26 | 27 | 36 |
| Springfield | Missouri | Polk | 3 | 666 | 24 | 17 | 12 |
| Missouri non-MSA | Missouri | Camden | 11 | 1023 | 22 | 21 | 16 |
| Joplin | Missouri | Newton | 15 | 1507 | 18 | 19 | 14 |
| St. Louis-Farmington | Illinois | Clinton | 21 | 1203 | 17 | 16 | 17 |
| Missouri non-MSA | Missouri | Pettis | 12 | 1159 | 16 | 17 | 12 |
| Kansas City | Missouri | Cass | 24 | 1527 | 15 | 17 | 15 |
| Missouri non-MSA | Missouri | Wright | 0 | 359 | 14 | 13 | 9 |
| Missouri non-MSA | Missouri | Laclede | 4 | 668 | 13 | 16 | 12 |
| Missouri non-MSA | Missouri | Howell | 3 | 634 | 13 | 14 | 12 |
| Missouri non-MSA | Missouri | Johnson | 4 | 1111 | 13 | 14 | 17 |
| Springfield | Missouri | Webster | 5 | 665 | 12 | 17 | 14 |
| Missouri non-MSA | Missouri | Washington | 10 | 430 | 12 | 9 | 6 |
| Missouri non-MSA | Missouri | Pulaski | 5 | 676 | 12 | 13 | 9 |
| Missouri non-MSA | Missouri | Benton | 3 | 335 | 12 | 10 | 5 |
| Kansas City | Missouri | Clay | 41 | 1827 | 12 | 13 | 15 |
| Columbia-Jefferson City | Missouri | Callaway | 3 | 672 | 11 | 10 | 11 |
| Missouri non-MSA | Missouri | Lawrence | 4 | 635 | 11 | 12 | 9 |
| Missouri non-MSA | Missouri | Taney | 31 | 1219 | 11 | 11 | 10 |
| Missouri non-MSA | Missouri | Butler | 7 | 659 | 10 | 11 | 9 |
| Missouri non-MSA | Missouri | Phelps | 8 | 490 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1118 | 9 | 7 | 4 |
| Kansas City | Missouri | Platte | 10 | 711 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | Morgan | 2 | 373 | 9 | 10 | 8 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 787 | 9 | 7 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 17 | 891 | 9 | 9 | 9 |
| Missouri non-MSA | Missouri | Stone | 4 | 470 | 9 | 7 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 16 | 686 | 8 | 7 | 7 |
| St. Louis-Farmington | Illinois | Macoupin | 7 | 556 | 8 | 8 | 7 |
| Kansas City | Missouri | Lafayette | 2 | 533 | 8 | 13 | 9 |
| Missouri non-MSA | Missouri | Miller | 1 | 510 | 8 | 9 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 13 | 520 | 7 | 10 | 7 |
| Missouri non-MSA | Missouri | Saline | 9 | 728 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 10 | 536 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 776 | 7 | 6 | 12 |
| Missouri non-MSA | Missouri | Texas | 2 | 329 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 8 | 800 | 7 | 10 | 10 |
| Missouri non-MSA | Missouri | Crawford | 4 | 407 | 6 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 434 | 6 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 324 | 6 | 5 | 4 |
| Kansas City | Kansas | Miami | 1 | 370 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Barry | 6 | 494 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Randolph | 2 | 264 | 5 | 5 | 4 |
| St. Louis-Farmington | Illinois | Bond | 6 | 334 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Douglas | 3 | 208 | 5 | 4 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 355 | 5 | 6 | 7 |
| Kansas City | Missouri | Clinton | 0 | 244 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Henry | 5 | 205 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Marion | 14 | 671 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Audrain | 4 | 447 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Wayne | 0 | 226 | 4 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Osage | 2 | 159 | 4 | 3 | 2 |
| St. Louis-Farmington | Missouri | Warren | 1 | 482 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Cedar | 0 | 121 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Daviess | 1 | 123 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Perry | 7 | 634 | 4 | 7 | 8 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 76 | 4 | 3 | 1 |
| St. Joseph | Missouri | Andrew | 2 | 259 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 16 | 537 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Adair | 0 | 350 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Madison | 1 | 312 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Oregon | 0 | 126 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ripley | 0 | 170 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Vernon | 1 | 187 | 3 | 3 | 3 |
| Kansas City | Missouri | Bates | 2 | 126 | 3 | 3 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 209 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 107 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Shannon | 1 | 110 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Grundy | 4 | 195 | 3 | 3 | 5 |
| Kansas City | Missouri | Caldwell | 1 | 100 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 85 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Hickory | 3 | 109 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Dent | 2 | 150 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Livingston | 1 | 408 | 2 | 3 | 11 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 203 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Dade | 0 | 70 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 192 | 2 | 2 | 3 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 61 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 2 | 92 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 115 | 2 | 1 | 1 |
| Springfield | Missouri | Dallas | 1 | 194 | 2 | 2 | 2 |
| St. Joseph | Missouri | DeKalb | 2 | 136 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Maries | 0 | 84 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 4 | 241 | 1 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 84 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 300 | 1 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 176 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ozark | 0 | 128 | 1 | 2 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 15 | 395 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Atchison | 0 | 54 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 20 | 166 | 1 | 1 | 2 |
| Kansas City | Missouri | Ray | 0 | 167 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 9 | 125 | 1 | 1 | 1 |
| Kansas City | Kansas | Linn | 0 | 76 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 68 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 151 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 110 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 151 | 0 | 3 | 2 |
| Missouri non-MSA | Missouri | Holt | 1 | 79 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 48 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 65 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 1 | 90 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 39 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 85 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 56 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 50 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 2 | 132 | 0 | 0 | 0 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
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

### To-Do (updated 7/20/2020)

#### Analysis Page
- [ ] Update description to accurately reflect CSA vs. MSA
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
