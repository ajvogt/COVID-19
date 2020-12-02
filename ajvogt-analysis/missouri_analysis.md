# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/01/2020  
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
| St. Louis-Farmington | 2339 | 148420 | 2080 | 2206 | 2062 |
| Kansas City | 1174 | 99336 | 1165 | 1328 | 1251 |
| Missouri non-MSA | 841 | 69966 | 774 | 909 | 930 |
| Columbia-Jefferson City | 107 | 23331 | 245 | 291 | 334 |
| Springfield | 243 | 21768 | 233 | 247 | 235 |
| Cape Girardeau-Sikeston | 113 | 8849 | 106 | 132 | 127 |
| St. Joseph | 78 | 6693 | 96 | 102 | 87 |
| Joplin | 144 | 11251 | 79 | 111 | 119 |
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
| St. Louis-Farmington | Missouri | St. Louis | 980 | 51819 | 695 | 698 | 674 |
| Kansas City | Kansas | Johnson | 285 | 27420 | 342 | 388 | 386 |
| Kansas City | Missouri | Kansas City | 282 | 23525 | 273 | 297 | 276 |
| St. Louis-Farmington | Missouri | St. Charles | 213 | 20229 | 271 | 315 | 290 |
| St. Louis-Farmington | Illinois | Madison | 259 | 14607 | 219 | 238 | 232 |
| St. Louis-Farmington | Illinois | St. Clair | 259 | 13579 | 213 | 206 | 174 |
| Kansas City | Missouri | Jackson | 181 | 17379 | 208 | 243 | 229 |
| St. Louis-Farmington | Missouri | Jefferson | 103 | 11154 | 175 | 193 | 173 |
| Springfield | Missouri | Greene | 175 | 14071 | 153 | 160 | 149 |
| St. Louis-Farmington | Missouri | St. Louis City | 239 | 13032 | 153 | 160 | 142 |
| Columbia-Jefferson City | Missouri | Boone | 23 | 10349 | 89 | 114 | 132 |
| Kansas City | Kansas | Wyandotte | 178 | 11528 | 86 | 111 | 94 |
| Columbia-Jefferson City | Missouri | Cole | 49 | 6257 | 78 | 87 | 98 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 65 | 5098 | 65 | 77 | 75 |
| St. Joseph | Missouri | Buchanan | 57 | 4757 | 64 | 65 | 56 |
| Joplin | Missouri | Jasper | 106 | 8266 | 60 | 84 | 91 |
| St. Louis-Farmington | Missouri | Franklin | 72 | 4886 | 59 | 69 | 66 |
| St. Louis-Farmington | Missouri | St. Francois | 44 | 5109 | 56 | 68 | 69 |
| Kansas City | Missouri | Cass | 39 | 3815 | 52 | 61 | 54 |
| St. Louis-Farmington | Illinois | Macoupin | 18 | 2276 | 51 | 54 | 46 |
| St. Louis-Farmington | Illinois | Clinton | 61 | 3337 | 50 | 54 | 47 |
| Kansas City | Missouri | Clay | 69 | 4670 | 47 | 66 | 65 |
| Springfield | Missouri | Christian | 23 | 3853 | 46 | 48 | 47 |
| Kansas City | Kansas | Leavenworth | 31 | 3817 | 44 | 43 | 37 |
| Columbia-Jefferson City | Missouri | Callaway | 8 | 2857 | 37 | 41 | 46 |
| St. Louis-Farmington | Missouri | Lincoln | 9 | 2476 | 37 | 44 | 39 |
| Missouri non-MSA | Missouri | Taney | 40 | 2905 | 35 | 39 | 34 |
| Cape Girardeau-Sikeston | Missouri | Scott | 38 | 2686 | 33 | 43 | 38 |
| St. Louis-Farmington | Illinois | Monroe | 46 | 2087 | 30 | 35 | 34 |
| Missouri non-MSA | Missouri | Johnson | 15 | 2547 | 30 | 32 | 32 |
| Missouri non-MSA | Missouri | Butler | 9 | 2179 | 30 | 31 | 29 |
| Missouri non-MSA | Missouri | Phelps | 42 | 1797 | 30 | 34 | 29 |
| St. Louis-Farmington | Illinois | Jersey | 24 | 1298 | 25 | 25 | 26 |
| Missouri non-MSA | Missouri | Marion | 16 | 1797 | 24 | 26 | 26 |
| Missouri non-MSA | Missouri | Stoddard | 20 | 1656 | 23 | 29 | 23 |
| Kansas City | Missouri | Lafayette | 29 | 1554 | 23 | 22 | 21 |
| Kansas City | Missouri | Platte | 17 | 1690 | 23 | 25 | 21 |
| Kansas City | Kansas | Miami | 2 | 1073 | 21 | 20 | 16 |
| Missouri non-MSA | Missouri | Nodaway | 13 | 2006 | 21 | 20 | 25 |
| Missouri non-MSA | Missouri | Pulaski | 19 | 1643 | 21 | 23 | 19 |
| Missouri non-MSA | Missouri | Camden | 45 | 2472 | 20 | 26 | 26 |
| St. Louis-Farmington | Illinois | Bond | 10 | 1050 | 19 | 16 | 17 |
| Joplin | Missouri | Newton | 38 | 2985 | 19 | 27 | 27 |
| St. Louis-Farmington | Missouri | Warren | 2 | 1230 | 18 | 22 | 18 |
| Missouri non-MSA | Missouri | Laclede | 30 | 1819 | 18 | 19 | 18 |
| Springfield | Missouri | Webster | 24 | 1852 | 17 | 22 | 20 |
| Missouri non-MSA | Missouri | Audrain | 13 | 1103 | 17 | 17 | 15 |
| Missouri non-MSA | Missouri | Lawrence | 37 | 1932 | 17 | 22 | 25 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1080 | 16 | 17 | 20 |
| Missouri non-MSA | Missouri | Washington | 23 | 1450 | 16 | 20 | 24 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 1371 | 16 | 17 | 18 |
| Missouri non-MSA | Missouri | Pike | 8 | 934 | 16 | 18 | 18 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1708 | 16 | 16 | 17 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 884 | 15 | 18 | 14 |
| Missouri non-MSA | Missouri | Pettis | 32 | 2689 | 15 | 16 | 31 |
| Missouri non-MSA | Missouri | Perry | 12 | 1560 | 15 | 20 | 23 |
| Missouri non-MSA | Missouri | Henry | 10 | 1102 | 14 | 19 | 22 |
| Missouri non-MSA | Missouri | Saline | 12 | 1595 | 14 | 18 | 19 |
| Missouri non-MSA | Missouri | Madison | 7 | 896 | 13 | 13 | 11 |
| Missouri non-MSA | Missouri | Randolph | 5 | 1217 | 13 | 15 | 18 |
| Missouri non-MSA | Missouri | Crawford | 12 | 1205 | 13 | 15 | 17 |
| Missouri non-MSA | Missouri | Miller | 24 | 1509 | 13 | 17 | 18 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1241 | 12 | 14 | 18 |
| St. Joseph | Missouri | Andrew | 9 | 820 | 12 | 14 | 11 |
| Missouri non-MSA | Missouri | Barry | 25 | 1461 | 12 | 17 | 18 |
| St. Joseph | Kansas | Doniphan | 2 | 516 | 11 | 12 | 10 |
| Missouri non-MSA | Missouri | Howell | 28 | 1597 | 11 | 10 | 11 |
| Missouri non-MSA | Missouri | Macon | 3 | 687 | 11 | 16 | 14 |
| Springfield | Missouri | Polk | 12 | 1388 | 11 | 10 | 10 |
| Kansas City | Missouri | Ray | 4 | 709 | 10 | 10 | 13 |
| Missouri non-MSA | Missouri | Pemiscot | 16 | 1095 | 10 | 10 | 11 |
| Missouri non-MSA | Missouri | Stone | 16 | 1198 | 10 | 15 | 15 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 947 | 10 | 12 | 13 |
| Missouri non-MSA | Missouri | Adair | 3 | 1088 | 10 | 15 | 17 |
| Missouri non-MSA | Missouri | Morgan | 12 | 1079 | 9 | 11 | 11 |
| Kansas City | Missouri | Clinton | 45 | 895 | 9 | 10 | 11 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 487 | 9 | 7 | 6 |
| Missouri non-MSA | Missouri | Ralls | 1 | 480 | 8 | 10 | 8 |
| St. Joseph | Missouri | DeKalb | 10 | 600 | 8 | 10 | 9 |
| Columbia-Jefferson City | Missouri | Cooper | 7 | 1170 | 8 | 12 | 16 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 510 | 8 | 8 | 8 |
| Kansas City | Missouri | Bates | 9 | 554 | 8 | 11 | 9 |
| Missouri non-MSA | Missouri | Texas | 8 | 967 | 8 | 9 | 11 |
| Missouri non-MSA | Missouri | Ripley | 8 | 525 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Douglas | 15 | 442 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Monroe | 3 | 395 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Dent | 4 | 522 | 7 | 10 | 8 |
| Missouri non-MSA | Missouri | Vernon | 7 | 681 | 7 | 9 | 10 |
| Kansas City | Kansas | Linn | 1 | 308 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Carroll | 6 | 441 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Benton | 8 | 778 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Wright | 14 | 779 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 349 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1407 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Livingston | 14 | 785 | 6 | 7 | 6 |
| Kansas City | Missouri | Caldwell | 2 | 399 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 502 | 5 | 6 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 8 | 804 | 5 | 7 | 8 |
| Missouri non-MSA | Missouri | Putnam | 1 | 162 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 335 | 5 | 6 | 6 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 251 | 4 | 6 | 5 |
| Springfield | Missouri | Dallas | 9 | 604 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 568 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Oregon | 0 | 384 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Gentry | 11 | 420 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Barton | 4 | 632 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Grundy | 14 | 510 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Linn | 9 | 323 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Maries | 3 | 369 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Harrison | 2 | 397 | 3 | 6 | 6 |
| Missouri non-MSA | Missouri | Holt | 3 | 270 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Shelby | 1 | 208 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 242 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Daviess | 8 | 335 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Carter | 5 | 296 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Ozark | 2 | 297 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 178 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Clark | 4 | 301 | 2 | 5 | 5 |
| Missouri non-MSA | Missouri | Cedar | 6 | 447 | 2 | 5 | 6 |
| Missouri non-MSA | Missouri | Atchison | 3 | 213 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Hickory | 6 | 367 | 2 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 261 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Scotland | 1 | 191 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Iron | 0 | 234 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 340 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 430 | 2 | 4 | 7 |
| Missouri non-MSA | Missouri | Dade | 6 | 290 | 1 | 3 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 132 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 87 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 74 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 133 | 0 | 2 | 2 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
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
