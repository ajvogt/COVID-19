# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/22/2020  
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
| St. Louis-Farmington | 1336 | 42596 | 615 | 614 | 683 |
| Kansas City | 420 | 30525 | 385 | 405 | 450 |
| Missouri non-MSA | 109 | 12187 | 217 | 221 | 217 |
| Springfield | 13 | 3264 | 90 | 78 | 73 |
| Columbia-Jefferson City | 13 | 3244 | 88 | 74 | 67 |
| Joplin | 46 | 3066 | 36 | 32 | 34 |
| Cape Girardeau-Sikeston | 20 | 1504 | 29 | 27 | 22 |
| St. Joseph | 12 | 1382 | 11 | 9 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 710 | 17517 | 197 | 211 | 263 |
| Kansas City | Kansas | Johnson | 110 | 7004 | 110 | 105 | 98 |
| Kansas City | Missouri | Kansas City | 66 | 8213 | 110 | 124 | 137 |
| St. Louis-Farmington | Missouri | St. Charles | 96 | 5086 | 80 | 80 | 102 |
| Springfield | Missouri | Greene | 10 | 2249 | 67 | 57 | 52 |
| St. Louis-Farmington | Illinois | Madison | 90 | 3441 | 67 | 69 | 61 |
| St. Louis-Farmington | Illinois | St. Clair | 166 | 4723 | 62 | 59 | 61 |
| Kansas City | Missouri | Jackson | 71 | 4869 | 59 | 68 | 91 |
| Kansas City | Kansas | Wyandotte | 111 | 5551 | 59 | 52 | 57 |
| St. Louis-Farmington | Missouri | Jefferson | 30 | 2176 | 49 | 45 | 46 |
| St. Louis-Farmington | Missouri | St. Louis City | 182 | 5816 | 48 | 54 | 72 |
| Columbia-Jefferson City | Missouri | Boone | 5 | 1816 | 41 | 34 | 33 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 726 | 35 | 26 | 17 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 690 | 27 | 22 | 16 |
| Joplin | Missouri | Jasper | 35 | 2067 | 25 | 23 | 24 |
| Missouri non-MSA | Missouri | Taney | 3 | 832 | 21 | 20 | 20 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 818 | 16 | 16 | 14 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 6 | 836 | 14 | 14 | 11 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 553 | 14 | 11 | 9 |
| Missouri non-MSA | Missouri | Pettis | 5 | 721 | 13 | 16 | 17 |
| Kansas City | Missouri | Cass | 9 | 925 | 13 | 15 | 19 |
| Springfield | Missouri | Christian | 1 | 503 | 13 | 12 | 12 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 535 | 12 | 11 | 8 |
| Kansas City | Missouri | Clay | 30 | 1210 | 12 | 14 | 18 |
| Joplin | Missouri | Newton | 11 | 999 | 10 | 9 | 10 |
| Missouri non-MSA | Missouri | Stone | 1 | 230 | 9 | 7 | 6 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 440 | 9 | 10 | 9 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 235 | 9 | 6 | 5 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 206 | 9 | 7 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 324 | 8 | 9 | 5 |
| Missouri non-MSA | Missouri | Marion | 1 | 315 | 8 | 9 | 8 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 281 | 8 | 8 | 6 |
| Missouri non-MSA | Missouri | Washington | 1 | 181 | 8 | 8 | 4 |
| St. Louis-Farmington | Missouri | Warren | 0 | 280 | 7 | 6 | 6 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 474 | 7 | 8 | 10 |
| Kansas City | Kansas | Leavenworth | 9 | 1572 | 7 | 8 | 8 |
| St. Joseph | Missouri | Buchanan | 10 | 1170 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Camden | 8 | 440 | 7 | 7 | 10 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 334 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 296 | 7 | 6 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 383 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Miller | 1 | 186 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Barry | 4 | 318 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Laclede | 1 | 256 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Crawford | 0 | 132 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Butler | 2 | 337 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 201 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Johnson | 3 | 537 | 4 | 3 | 4 |
| Kansas City | Missouri | Platte | 10 | 434 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 283 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 249 | 4 | 5 | 6 |
| Springfield | Missouri | Polk | 0 | 255 | 4 | 3 | 4 |
| St. Louis-Farmington | Illinois | Bond | 3 | 97 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Howell | 2 | 196 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Perry | 4 | 280 | 3 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 183 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Saline | 7 | 503 | 3 | 5 | 5 |
| Springfield | Missouri | Webster | 1 | 171 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Madison | 0 | 54 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 137 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Randolph | 1 | 97 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 199 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 136 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 69 | 2 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 112 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Audrain | 1 | 235 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | McDonald | 8 | 973 | 2 | 1 | 4 |
| Missouri non-MSA | Missouri | Ripley | 0 | 78 | 2 | 1 | 1 |
| Kansas City | Kansas | Miami | 0 | 167 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 82 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 254 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 37 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 79 | 2 | 2 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 93 | 1 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 173 | 1 | 2 | 3 |
| Springfield | Missouri | Dallas | 1 | 86 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 68 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 1 | 75 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dent | 0 | 30 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Morgan | 0 | 104 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 0 | 49 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 45 | 1 | 1 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 205 | 1 | 2 | 2 |
| St. Joseph | Kansas | Doniphan | 0 | 58 | 1 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 50 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 69 | 1 | 1 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 104 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 101 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 0 | 50 | 1 | 3 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 71 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Douglas | 2 | 97 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 42 | 1 | 1 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 19 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 76 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 76 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 71 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 107 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 48 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 50 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 156 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 24 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 40 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 57 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 1 | 67 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 26 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 38 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 62 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 87 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 36 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 43 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 53 | 0 | 0 | 1 |
| Kansas City | Missouri | Ray | 0 | 118 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Pike | 1 | 131 | -1 | 2 | 2 |
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
