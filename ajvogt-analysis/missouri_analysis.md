# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/08/2020  
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
| St. Louis-Farmington | 1699 | 68147 | 482 | 493 | 518 |
| Missouri non-MSA | 341 | 28519 | 442 | 379 | 384 |
| Kansas City | 653 | 48070 | 440 | 409 | 369 |
| Springfield | 107 | 10629 | 176 | 166 | 168 |
| Columbia-Jefferson City | 38 | 8733 | 93 | 85 | 101 |
| Joplin | 68 | 5828 | 70 | 56 | 67 |
| St. Joseph | 35 | 2894 | 50 | 42 | 38 |
| Cape Girardeau-Sikeston | 37 | 3470 | 47 | 46 | 49 |
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
| Kansas City | Missouri | Kansas City | 146 | 12536 | 180 | 122 | 90 |
| St. Louis-Farmington | Missouri | St. Louis | 826 | 25572 | 142 | 162 | 161 |
| Springfield | Missouri | Greene | 90 | 7139 | 105 | 102 | 104 |
| Kansas City | Kansas | Johnson | 160 | 11817 | 86 | 100 | 96 |
| St. Louis-Farmington | Missouri | St. Charles | 115 | 8296 | 77 | 64 | 68 |
| Joplin | Missouri | Jasper | 55 | 4369 | 77 | 52 | 56 |
| Kansas City | Kansas | Wyandotte | 134 | 7394 | 58 | 45 | 37 |
| St. Louis-Farmington | Missouri | Jefferson | 66 | 4612 | 47 | 42 | 50 |
| Kansas City | Missouri | Jackson | 107 | 7899 | 44 | 59 | 62 |
| Columbia-Jefferson City | Missouri | Cole | 14 | 1880 | 42 | 31 | 28 |
| St. Joseph | Missouri | Buchanan | 30 | 2292 | 38 | 32 | 29 |
| St. Louis-Farmington | Illinois | Madison | 148 | 6085 | 36 | 44 | 51 |
| St. Louis-Farmington | Illinois | St. Clair | 199 | 6994 | 35 | 43 | 42 |
| St. Louis-Farmington | Missouri | St. Louis City | 213 | 7386 | 34 | 32 | 31 |
| Springfield | Missouri | Christian | 6 | 1706 | 33 | 28 | 29 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 18 | 2025 | 31 | 31 | 31 |
| St. Louis-Farmington | Missouri | Franklin | 32 | 1972 | 30 | 25 | 26 |
| Missouri non-MSA | Missouri | Taney | 37 | 1422 | 29 | 18 | 15 |
| Missouri non-MSA | Missouri | Howell | 3 | 808 | 24 | 18 | 15 |
| Missouri non-MSA | Missouri | Laclede | 10 | 827 | 22 | 17 | 16 |
| Springfield | Missouri | Webster | 5 | 818 | 21 | 16 | 17 |
| St. Louis-Farmington | Missouri | St. Francois | 14 | 2282 | 21 | 23 | 32 |
| Missouri non-MSA | Missouri | Camden | 17 | 1171 | 21 | 20 | 18 |
| Missouri non-MSA | Missouri | Lawrence | 3 | 755 | 17 | 13 | 12 |
| St. Louis-Farmington | Illinois | Clinton | 23 | 1338 | 16 | 17 | 16 |
| Missouri non-MSA | Missouri | Randolph | 2 | 379 | 16 | 10 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 901 | 16 | 12 | 9 |
| Columbia-Jefferson City | Missouri | Boone | 11 | 4836 | 15 | 23 | 43 |
| Missouri non-MSA | Missouri | Butler | 7 | 756 | 13 | 10 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 8 | 897 | 13 | 9 | 11 |
| Kansas City | Kansas | Leavenworth | 15 | 2296 | 13 | 23 | 18 |
| Kansas City | Missouri | Cass | 26 | 1620 | 13 | 13 | 15 |
| Columbia-Jefferson City | Missouri | Callaway | 3 | 764 | 13 | 11 | 11 |
| Cape Girardeau-Sikeston | Missouri | Scott | 17 | 982 | 13 | 10 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 14 | 607 | 12 | 9 | 9 |
| Missouri non-MSA | Missouri | Saline | 9 | 814 | 12 | 8 | 7 |
| Missouri non-MSA | Missouri | Wright | 0 | 444 | 12 | 11 | 11 |
| Missouri non-MSA | Missouri | Miller | 2 | 590 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Morgan | 2 | 451 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Washington | 11 | 504 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Barton | 1 | 265 | 10 | 6 | 4 |
| Kansas City | Missouri | Lafayette | 6 | 606 | 10 | 8 | 11 |
| Springfield | Missouri | Polk | 5 | 739 | 10 | 16 | 13 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 862 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Pettis | 12 | 1226 | 9 | 11 | 12 |
| Missouri non-MSA | Missouri | Stone | 6 | 534 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Texas | 2 | 393 | 9 | 6 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 16 | 600 | 9 | 6 | 5 |
| Missouri non-MSA | Missouri | Livingston | 3 | 469 | 8 | 5 | 4 |
| Missouri non-MSA | Missouri | Benton | 5 | 395 | 8 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 218 | 8 | 5 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 24 | 749 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Marion | 14 | 730 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 7 | 734 | 8 | 8 | 10 |
| Kansas City | Missouri | Clay | 42 | 1882 | 7 | 8 | 12 |
| Missouri non-MSA | Missouri | Barry | 6 | 546 | 7 | 6 | 5 |
| St. Joseph | Missouri | Andrew | 3 | 308 | 7 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 480 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Henry | 5 | 251 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 10 | 582 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Vernon | 1 | 233 | 6 | 4 | 4 |
| St. Louis-Farmington | Illinois | Macoupin | 8 | 610 | 6 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 5 | 366 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Linn | 1 | 127 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Shannon | 1 | 151 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Lewis | 2 | 133 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Perry | 7 | 674 | 5 | 4 | 7 |
| Kansas City | Missouri | Platte | 10 | 749 | 5 | 6 | 7 |
| Kansas City | Missouri | Bates | 3 | 163 | 5 | 4 | 2 |
| Kansas City | Missouri | Clinton | 0 | 280 | 5 | 5 | 3 |
| St. Joseph | Missouri | DeKalb | 2 | 171 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 1 | 156 | 4 | 4 | 3 |
| Springfield | Missouri | Dallas | 1 | 227 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 0 | 154 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 380 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Phelps | 12 | 520 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | Oregon | 0 | 154 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 231 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 327 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 3 | 235 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Crawford | 5 | 434 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Grundy | 4 | 221 | 3 | 2 | 4 |
| St. Louis-Farmington | Illinois | Bond | 8 | 368 | 3 | 5 | 5 |
| Kansas City | Kansas | Miami | 1 | 433 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Hickory | 3 | 133 | 3 | 3 | 2 |
| Kansas City | Missouri | Ray | 2 | 190 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 137 | 3 | 2 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 120 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Audrain | 5 | 467 | 2 | 3 | 5 |
| St. Louis-Farmington | Missouri | Warren | 1 | 501 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Macon | 0 | 170 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 228 | 2 | 3 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 19 | 415 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Pike | 4 | 258 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Gentry | 9 | 141 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 1 | 143 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 241 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Dade | 0 | 84 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 189 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 97 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 366 | 1 | 3 | 6 |
| Missouri non-MSA | Missouri | Maries | 0 | 95 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 41 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 74 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 2 | 141 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 65 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 62 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 1 | 320 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Holt | 1 | 86 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 158 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 74 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 81 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 53 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 3 | 112 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 55 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 90 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1122 | 0 | 5 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 28 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 66 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 1 | 94 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 23 | 170 | 0 | 0 | 2 |
| Kansas City | Kansas | Linn | 0 | 85 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 2 | 152 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 41 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 123 | 0 | 1 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 1 | 150 | -2 | 0 | 1 |
| Joplin | Missouri | Newton | 13 | 1459 | -6 | 3 | 10 |
| Missouri non-MSA | Missouri | Johnson | 5 | 1027 | -12 | -1 | 10 |
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
