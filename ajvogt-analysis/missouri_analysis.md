# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/06/2020  
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
| St. Louis-Farmington | 1684 | 67473 | 479 | 513 | 531 |
| Kansas City | 640 | 47433 | 390 | 404 | 369 |
| Missouri non-MSA | 336 | 27908 | 358 | 396 | 378 |
| Springfield | 82 | 10383 | 141 | 176 | 168 |
| Columbia-Jefferson City | 38 | 8556 | 68 | 84 | 103 |
| Joplin | 65 | 5719 | 54 | 59 | 64 |
| St. Joseph | 35 | 2825 | 42 | 42 | 37 |
| Cape Girardeau-Sikeston | 37 | 3417 | 40 | 48 | 49 |
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
| Kansas City | Missouri | Kansas City | 143 | 12418 | 163 | 124 | 92 |
| St. Louis-Farmington | Missouri | St. Louis | 819 | 25302 | 156 | 165 | 165 |
| Kansas City | Kansas | Johnson | 158 | 11657 | 91 | 101 | 97 |
| Springfield | Missouri | Greene | 65 | 6978 | 82 | 107 | 105 |
| St. Louis-Farmington | Missouri | Jefferson | 66 | 4762 | 68 | 61 | 58 |
| Joplin | Missouri | Jasper | 52 | 4277 | 63 | 52 | 54 |
| St. Louis-Farmington | Missouri | St. Charles | 115 | 8114 | 51 | 60 | 67 |
| Kansas City | Kansas | Wyandotte | 134 | 7287 | 47 | 42 | 35 |
| St. Louis-Farmington | Illinois | St. Clair | 196 | 6933 | 38 | 44 | 42 |
| St. Louis-Farmington | Illinois | Madison | 147 | 6021 | 37 | 45 | 52 |
| St. Louis-Farmington | Missouri | St. Louis City | 213 | 7321 | 33 | 33 | 31 |
| St. Joseph | Missouri | Buchanan | 30 | 2240 | 30 | 33 | 28 |
| Columbia-Jefferson City | Missouri | Cole | 14 | 1797 | 30 | 29 | 27 |
| Kansas City | Missouri | Jackson | 103 | 7792 | 29 | 52 | 61 |
| Springfield | Missouri | Christian | 6 | 1662 | 27 | 29 | 28 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 18 | 1993 | 26 | 32 | 31 |
| Missouri non-MSA | Missouri | Taney | 36 | 1405 | 26 | 19 | 15 |
| St. Louis-Farmington | Missouri | Franklin | 32 | 1929 | 24 | 26 | 26 |
| Missouri non-MSA | Missouri | Howell | 3 | 781 | 21 | 18 | 15 |
| Missouri non-MSA | Missouri | Laclede | 9 | 794 | 18 | 16 | 15 |
| St. Louis-Farmington | Illinois | Clinton | 21 | 1309 | 17 | 17 | 15 |
| Springfield | Missouri | Webster | 5 | 783 | 16 | 18 | 16 |
| St. Louis-Farmington | Missouri | St. Francois | 14 | 2240 | 15 | 20 | 32 |
| Missouri non-MSA | Missouri | Camden | 16 | 1131 | 15 | 21 | 18 |
| Missouri non-MSA | Missouri | Lawrence | 4 | 738 | 14 | 14 | 11 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 884 | 13 | 11 | 9 |
| Kansas City | Kansas | Leavenworth | 14 | 2268 | 12 | 24 | 18 |
| Missouri non-MSA | Missouri | Dunklin | 8 | 883 | 11 | 9 | 10 |
| Cape Girardeau-Sikeston | Missouri | Scott | 17 | 971 | 11 | 10 | 9 |
| Missouri non-MSA | Missouri | Butler | 6 | 738 | 11 | 11 | 10 |
| Missouri non-MSA | Missouri | Randolph | 2 | 341 | 11 | 8 | 6 |
| Missouri non-MSA | Missouri | Wright | 0 | 436 | 11 | 13 | 11 |
| Missouri non-MSA | Missouri | Saline | 9 | 801 | 10 | 9 | 7 |
| Columbia-Jefferson City | Missouri | Callaway | 3 | 745 | 10 | 11 | 11 |
| Springfield | Missouri | Polk | 5 | 738 | 10 | 17 | 13 |
| Kansas City | Missouri | Lafayette | 5 | 604 | 10 | 10 | 11 |
| Missouri non-MSA | Missouri | Barton | 0 | 259 | 9 | 6 | 4 |
| Missouri non-MSA | Missouri | Morgan | 2 | 439 | 9 | 9 | 9 |
| Kansas City | Missouri | Cass | 26 | 1591 | 9 | 13 | 15 |
| Missouri non-MSA | Missouri | Washington | 11 | 494 | 9 | 11 | 7 |
| Missouri non-MSA | Missouri | Stoddard | 14 | 583 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Benton | 5 | 395 | 8 | 10 | 7 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 823 | 8 | 7 | 6 |
| Columbia-Jefferson City | Missouri | Boone | 11 | 4786 | 8 | 23 | 47 |
| Missouri non-MSA | Missouri | Pettis | 12 | 1215 | 8 | 13 | 12 |
| Missouri non-MSA | Missouri | Miller | 2 | 566 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | New Madrid | 16 | 593 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Texas | 2 | 383 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Pulaski | 7 | 728 | 7 | 10 | 10 |
| St. Louis-Farmington | Illinois | Monroe | 22 | 731 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Livingston | 3 | 456 | 6 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 207 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Marion | 14 | 718 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Stone | 6 | 517 | 6 | 8 | 7 |
| St. Louis-Farmington | Illinois | Macoupin | 8 | 595 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Henry | 5 | 248 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Barry | 6 | 535 | 5 | 7 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 475 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Vernon | 1 | 227 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 10 | 575 | 5 | 6 | 6 |
| St. Joseph | Missouri | Andrew | 3 | 298 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Linn | 1 | 122 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 129 | 5 | 3 | 2 |
| Kansas City | Kansas | Miami | 1 | 407 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Shannon | 1 | 145 | 5 | 4 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 5 | 358 | 4 | 5 | 5 |
| St. Louis-Farmington | Illinois | Bond | 8 | 363 | 4 | 5 | 5 |
| Kansas City | Missouri | Platte | 10 | 744 | 4 | 7 | 7 |
| Missouri non-MSA | Missouri | Cedar | 0 | 151 | 4 | 4 | 3 |
| Kansas City | Missouri | Bates | 3 | 156 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Daviess | 1 | 152 | 4 | 4 | 3 |
| St. Joseph | Missouri | DeKalb | 2 | 164 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Perry | 7 | 662 | 4 | 4 | 7 |
| Springfield | Missouri | Dallas | 1 | 222 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Oregon | 0 | 152 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 325 | 3 | 2 | 2 |
| Kansas City | Missouri | Clinton | 0 | 269 | 3 | 4 | 3 |
| Kansas City | Missouri | Clay | 42 | 1850 | 3 | 8 | 12 |
| Missouri non-MSA | Missouri | Adair | 0 | 373 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Douglas | 3 | 231 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Phelps | 12 | 512 | 3 | 6 | 8 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 223 | 2 | 2 | 3 |
| Kansas City | Missouri | Ray | 0 | 187 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Audrain | 5 | 467 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Crawford | 5 | 426 | 2 | 4 | 6 |
| Kansas City | Missouri | Caldwell | 1 | 119 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 3 | 128 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 227 | 2 | 3 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 133 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Grundy | 4 | 213 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Macon | 0 | 168 | 2 | 1 | 2 |
| St. Louis-Farmington | Missouri | Warren | 1 | 498 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Pike | 4 | 255 | 2 | 1 | 3 |
| St. Joseph | Kansas | Doniphan | 0 | 123 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 9 | 138 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 83 | 1 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 188 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 19 | 405 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 1 | 41 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 1 | 138 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Maries | 0 | 94 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 74 | 1 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 84 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 91 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 0 | 61 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 362 | 1 | 3 | 7 |
| Missouri non-MSA | Missouri | Holt | 1 | 86 | 1 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 66 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 232 | 0 | 3 | 4 |
| Missouri non-MSA | Missouri | Knox | 1 | 55 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 2 | 137 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 61 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 156 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 72 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 1 | 316 | 0 | 2 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 52 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 89 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 79 | 0 | 2 | 1 |
| Missouri non-MSA | Missouri | Carter | 3 | 110 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Monroe | 1 | 92 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 2 | 152 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 22 | 167 | 0 | 0 | 2 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1113 | 0 | 4 | 3 |
| Missouri non-MSA | Missouri | Ripley | 1 | 144 | -3 | 0 | 1 |
| Joplin | Missouri | Newton | 13 | 1442 | -9 | 6 | 10 |
| Missouri non-MSA | Missouri | Johnson | 5 | 1017 | -13 | 1 | 12 |
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
