# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/04/2020  
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
| St. Louis-Farmington | 1681 | 66454 | 474 | 511 | 546 |
| Kansas City | 634 | 46743 | 404 | 402 | 371 |
| Missouri non-MSA | 332 | 27209 | 364 | 402 | 388 |
| Springfield | 80 | 10113 | 169 | 178 | 173 |
| Columbia-Jefferson City | 38 | 8364 | 65 | 81 | 114 |
| Joplin | 65 | 5618 | 50 | 57 | 66 |
| St. Joseph | 35 | 2758 | 42 | 44 | 37 |
| Cape Girardeau-Sikeston | 37 | 3315 | 41 | 48 | 49 |
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
| Kansas City | Missouri | Kansas City | 143 | 12253 | 166 | 127 | 91 |
| St. Louis-Farmington | Missouri | St. Louis | 819 | 24994 | 154 | 161 | 165 |
| Springfield | Missouri | Greene | 65 | 6814 | 101 | 109 | 111 |
| Kansas City | Kansas | Johnson | 158 | 11546 | 96 | 104 | 101 |
| Joplin | Missouri | Jasper | 52 | 4198 | 57 | 50 | 56 |
| St. Louis-Farmington | Missouri | St. Charles | 115 | 7984 | 54 | 65 | 68 |
| St. Louis-Farmington | Illinois | Madison | 147 | 5971 | 43 | 48 | 58 |
| St. Louis-Farmington | Illinois | St. Clair | 196 | 6878 | 43 | 45 | 47 |
| St. Louis-Farmington | Missouri | Jefferson | 66 | 4491 | 42 | 50 | 54 |
| Kansas City | Kansas | Wyandotte | 134 | 7181 | 42 | 37 | 34 |
| St. Louis-Farmington | Missouri | St. Louis City | 213 | 7254 | 31 | 32 | 31 |
| St. Joseph | Missouri | Buchanan | 30 | 2189 | 31 | 34 | 28 |
| Springfield | Missouri | Christian | 6 | 1619 | 28 | 29 | 29 |
| Kansas City | Kansas | Leavenworth | 13 | 2235 | 28 | 25 | 18 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 18 | 1915 | 27 | 32 | 30 |
| St. Louis-Farmington | Missouri | Franklin | 32 | 1899 | 26 | 28 | 26 |
| Columbia-Jefferson City | Missouri | Cole | 14 | 1721 | 26 | 26 | 26 |
| Missouri non-MSA | Missouri | Taney | 36 | 1376 | 26 | 18 | 14 |
| Springfield | Missouri | Polk | 3 | 719 | 20 | 18 | 13 |
| Missouri non-MSA | Missouri | Howell | 3 | 751 | 19 | 18 | 15 |
| Missouri non-MSA | Missouri | Laclede | 9 | 760 | 19 | 18 | 14 |
| Kansas City | Missouri | Jackson | 100 | 7601 | 18 | 43 | 60 |
| St. Louis-Farmington | Missouri | St. Francois | 14 | 2202 | 18 | 21 | 35 |
| St. Louis-Farmington | Illinois | Clinton | 21 | 1279 | 18 | 16 | 16 |
| Springfield | Missouri | Webster | 5 | 754 | 16 | 18 | 16 |
| Missouri non-MSA | Missouri | Camden | 16 | 1096 | 15 | 22 | 17 |
| Missouri non-MSA | Missouri | Lawrence | 4 | 716 | 13 | 14 | 11 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 858 | 13 | 11 | 8 |
| Columbia-Jefferson City | Missouri | Boone | 11 | 4742 | 12 | 26 | 58 |
| Kansas City | Missouri | Lafayette | 5 | 594 | 12 | 13 | 11 |
| Missouri non-MSA | Missouri | Wright | 0 | 417 | 12 | 13 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 8 | 867 | 11 | 9 | 10 |
| Cape Girardeau-Sikeston | Missouri | Scott | 17 | 954 | 11 | 10 | 9 |
| Missouri non-MSA | Missouri | Pettis | 12 | 1202 | 11 | 15 | 12 |
| Missouri non-MSA | Missouri | Butler | 6 | 722 | 10 | 12 | 11 |
| Missouri non-MSA | Missouri | Stoddard | 14 | 566 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Saline | 9 | 789 | 10 | 9 | 7 |
| Kansas City | Missouri | Cass | 26 | 1572 | 10 | 13 | 15 |
| Missouri non-MSA | Missouri | Morgan | 1 | 413 | 9 | 9 | 9 |
| Columbia-Jefferson City | Missouri | Callaway | 3 | 718 | 9 | 10 | 11 |
| St. Louis-Farmington | Illinois | Monroe | 19 | 734 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 16 | 590 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 6 | 720 | 8 | 13 | 10 |
| Missouri non-MSA | Missouri | Washington | 11 | 472 | 8 | 10 | 7 |
| Missouri non-MSA | Missouri | Benton | 5 | 374 | 8 | 9 | 7 |
| Missouri non-MSA | Missouri | Texas | 2 | 376 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 810 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Barton | 0 | 237 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Stone | 6 | 509 | 7 | 8 | 7 |
| St. Louis-Farmington | Illinois | Macoupin | 8 | 593 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Marion | 14 | 708 | 7 | 5 | 7 |
| Missouri non-MSA | Missouri | Miller | 2 | 554 | 7 | 8 | 9 |
| Kansas City | Kansas | Miami | 1 | 407 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Barry | 6 | 527 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Henry | 5 | 241 | 6 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 471 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 10 | 566 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Randolph | 2 | 298 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Vernon | 1 | 219 | 5 | 4 | 4 |
| St. Joseph | Missouri | Andrew | 3 | 287 | 5 | 5 | 5 |
| St. Louis-Farmington | Illinois | Bond | 8 | 358 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Douglas | 3 | 229 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Cedar | 0 | 143 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Linn | 1 | 121 | 5 | 4 | 2 |
| Kansas City | Missouri | Bates | 2 | 152 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Perry | 7 | 656 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Adair | 0 | 372 | 4 | 3 | 4 |
| Kansas City | Missouri | Platte | 10 | 730 | 4 | 7 | 7 |
| Missouri non-MSA | Missouri | Shannon | 1 | 136 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Phelps | 12 | 507 | 4 | 7 | 8 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 184 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Lewis | 2 | 120 | 4 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 5 | 343 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Daviess | 1 | 144 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 221 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Audrain | 5 | 453 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Livingston | 2 | 430 | 4 | 3 | 11 |
| Kansas City | Missouri | Clinton | 0 | 262 | 3 | 4 | 4 |
| St. Joseph | Missouri | DeKalb | 2 | 159 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Crawford | 5 | 421 | 3 | 5 | 7 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 321 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Harrison | 1 | 129 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 141 | 3 | 3 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 112 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 217 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Dade | 0 | 80 | 2 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 207 | 2 | 2 | 3 |
| St. Louis-Farmington | Missouri | Warren | 1 | 491 | 2 | 3 | 5 |
| Kansas City | Missouri | Ray | 0 | 183 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Grundy | 4 | 207 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Hickory | 3 | 117 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 165 | 2 | 1 | 2 |
| Kansas City | Missouri | Clay | 41 | 1832 | 2 | 8 | 12 |
| Missouri non-MSA | Missouri | Gentry | 9 | 132 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 231 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1109 | 2 | 4 | 3 |
| St. Joseph | Kansas | Doniphan | 0 | 123 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 185 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 19 | 402 | 1 | 1 | 3 |
| Kansas City | Kansas | Linn | 0 | 83 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ozark | 1 | 136 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Pike | 4 | 251 | 1 | 1 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 358 | 1 | 3 | 7 |
| Missouri non-MSA | Missouri | Atchison | 0 | 61 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 88 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 73 | 1 | 1 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 66 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 38 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 89 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 1 | 84 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 52 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 72 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 55 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 74 | 0 | 2 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 154 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 1 | 91 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 87 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 2 | 107 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 59 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 2 | 135 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 1 | 305 | 0 | 2 | 4 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 22 | 165 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Putnam | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 2 | 144 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Ripley | 1 | 139 | -3 | 0 | 1 |
| Joplin | Missouri | Newton | 13 | 1420 | -7 | 6 | 10 |
| Missouri non-MSA | Missouri | Johnson | 5 | 1008 | -13 | 2 | 13 |
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
