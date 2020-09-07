# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/07/2020  
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
| St. Louis-Farmington | 1459 | 52108 | 604 | 594 | 603 |
| Kansas City | 493 | 36673 | 358 | 371 | 394 |
| Missouri non-MSA | 178 | 16849 | 346 | 302 | 258 |
| Columbia-Jefferson City | 24 | 5633 | 194 | 159 | 114 |
| Springfield | 22 | 5466 | 166 | 146 | 109 |
| Joplin | 50 | 3810 | 57 | 48 | 40 |
| Cape Girardeau-Sikeston | 24 | 1954 | 29 | 30 | 27 |
| St. Joseph | 14 | 1721 | 23 | 23 | 15 |
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
| St. Louis-Farmington | Missouri | St. Louis | 760 | 20574 | 185 | 193 | 200 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 3473 | 137 | 111 | 71 |
| Springfield | Missouri | Greene | 18 | 3904 | 123 | 109 | 82 |
| Kansas City | Kansas | Johnson | 121 | 8850 | 103 | 110 | 110 |
| Kansas City | Missouri | Jackson | 83 | 6002 | 77 | 68 | 69 |
| Kansas City | Missouri | Kansas City | 94 | 9720 | 76 | 92 | 108 |
| St. Louis-Farmington | Illinois | Madison | 108 | 4498 | 73 | 66 | 67 |
| St. Louis-Farmington | Missouri | St. Charles | 105 | 6140 | 63 | 65 | 72 |
| St. Louis-Farmington | Illinois | St. Clair | 175 | 5674 | 61 | 56 | 59 |
| St. Louis-Farmington | Missouri | Jefferson | 46 | 3064 | 57 | 56 | 50 |
| Joplin | Missouri | Jasper | 37 | 2676 | 49 | 40 | 31 |
| Missouri non-MSA | Missouri | Livingston | 1 | 338 | 37 | 19 | 9 |
| St. Louis-Farmington | Missouri | St. Louis City | 189 | 6405 | 36 | 35 | 44 |
| St. Louis-Farmington | Missouri | St. Francois | 5 | 1298 | 36 | 35 | 31 |
| Missouri non-MSA | Missouri | Nodaway | 6 | 638 | 35 | 26 | 15 |
| Kansas City | Kansas | Wyandotte | 117 | 6251 | 34 | 39 | 48 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1010 | 25 | 20 | 21 |
| Springfield | Missouri | Christian | 2 | 816 | 23 | 20 | 16 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 842 | 21 | 18 | 15 |
| St. Louis-Farmington | Missouri | Franklin | 22 | 1157 | 19 | 21 | 18 |
| Kansas City | Missouri | Clay | 39 | 1493 | 18 | 16 | 16 |
| St. Joseph | Missouri | Buchanan | 12 | 1414 | 16 | 16 | 11 |
| Missouri non-MSA | Missouri | Johnson | 4 | 699 | 15 | 11 | 7 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 8 | 1064 | 14 | 15 | 14 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 428 | 14 | 12 | 9 |
| Missouri non-MSA | Missouri | Marion | 7 | 545 | 11 | 15 | 12 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 568 | 11 | 8 | 8 |
| Missouri non-MSA | Missouri | Camden | 9 | 596 | 11 | 10 | 8 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 524 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Howell | 3 | 329 | 10 | 9 | 5 |
| Kansas City | Missouri | Cass | 16 | 1138 | 10 | 12 | 14 |
| Springfield | Missouri | Webster | 1 | 285 | 9 | 8 | 5 |
| Missouri non-MSA | Missouri | Madison | 0 | 199 | 9 | 9 | 5 |
| Kansas City | Kansas | Leavenworth | 9 | 1704 | 9 | 9 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 14 | 684 | 9 | 10 | 10 |
| St. Louis-Farmington | Illinois | Bond | 4 | 206 | 9 | 7 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 286 | 9 | 7 | 5 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 621 | 8 | 8 | 8 |
| Springfield | Missouri | Polk | 0 | 339 | 8 | 5 | 4 |
| Missouri non-MSA | Missouri | Pettis | 8 | 847 | 8 | 7 | 12 |
| Joplin | Missouri | Newton | 13 | 1134 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Phelps | 1 | 265 | 8 | 8 | 6 |
| Missouri non-MSA | Missouri | Texas | 1 | 154 | 8 | 5 | 3 |
| Missouri non-MSA | Missouri | Taney | 22 | 960 | 7 | 7 | 13 |
| Kansas City | Kansas | Miami | 0 | 242 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Perry | 4 | 441 | 7 | 10 | 7 |
| Missouri non-MSA | Missouri | Miller | 1 | 295 | 7 | 6 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 6 | 394 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Audrain | 2 | 313 | 7 | 5 | 3 |
| Kansas City | Missouri | Platte | 10 | 526 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 375 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Grundy | 1 | 90 | 6 | 4 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 6 | 320 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Butler | 4 | 417 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | Saline | 9 | 585 | 6 | 4 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 393 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Adair | 0 | 267 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Crawford | 2 | 217 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Pulaski | 2 | 423 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 9 | 445 | 5 | 7 | 7 |
| St. Louis-Farmington | Missouri | Warren | 0 | 358 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Ozark | 0 | 62 | 5 | 3 | 1 |
| Missouri non-MSA | Missouri | Stone | 2 | 311 | 5 | 5 | 6 |
| Kansas City | Missouri | Lafayette | 2 | 271 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Laclede | 1 | 326 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Morgan | 1 | 152 | 4 | 3 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 156 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Washington | 1 | 268 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Randolph | 1 | 148 | 4 | 2 | 2 |
| Kansas City | Missouri | Clinton | 0 | 158 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 319 | 3 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 139 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Barry | 5 | 378 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Vernon | 0 | 106 | 3 | 2 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 149 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 131 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 0 | 44 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 108 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 102 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 104 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 205 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Dent | 0 | 55 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 4 | 129 | 2 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 80 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 85 | 2 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 122 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 64 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 92 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 115 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Pike | 2 | 155 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | McDonald | 10 | 998 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 120 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 37 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 245 | 1 | 2 | 3 |
| Kansas City | Missouri | Ray | 0 | 135 | 1 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 78 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 60 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 85 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 37 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 181 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 1 | 118 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 76 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 0 | 70 | 1 | 1 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 49 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 3 | 118 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 9 | 101 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 50 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 0 | 24 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 34 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 59 | 1 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 33 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Benton | 1 | 162 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Carter | 1 | 42 | 0 | 1 | 0 |
| Kansas City | Missouri | Bates | 1 | 78 | 0 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 50 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 65 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 4 | 100 | 0 | 3 | 2 |
| Missouri non-MSA | Missouri | Shelby | 0 | 52 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 51 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 1 | 67 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 51 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 42 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 56 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 20 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 43 | 0 | 0 | 0 |
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
