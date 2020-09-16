# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/16/2020  
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
| St. Louis-Farmington | 1513 | 57003 | 579 | 574 | 577 |
| Missouri non-MSA | 197 | 19715 | 359 | 343 | 285 |
| Kansas City | 532 | 39504 | 335 | 336 | 364 |
| Springfield | 26 | 6938 | 179 | 169 | 137 |
| Columbia-Jefferson City | 24 | 6814 | 148 | 161 | 132 |
| Joplin | 56 | 4423 | 84 | 68 | 51 |
| Cape Girardeau-Sikeston | 26 | 2419 | 59 | 45 | 36 |
| St. Joseph | 16 | 1977 | 33 | 29 | 22 |
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
| St. Louis-Farmington | Missouri | St. Louis | 774 | 22090 | 178 | 173 | 182 |
| Springfield | Missouri | Greene | 19 | 4872 | 115 | 116 | 99 |
| Kansas City | Kansas | Johnson | 138 | 9619 | 90 | 94 | 108 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 4182 | 87 | 104 | 86 |
| Kansas City | Missouri | Jackson | 88 | 6609 | 75 | 71 | 68 |
| St. Louis-Farmington | Missouri | St. Charles | 109 | 6793 | 73 | 70 | 71 |
| Joplin | Missouri | Jasper | 42 | 3194 | 70 | 58 | 41 |
| St. Louis-Farmington | Illinois | Madison | 122 | 5020 | 62 | 65 | 63 |
| Kansas City | Missouri | Kansas City | 99 | 10250 | 58 | 66 | 86 |
| St. Louis-Farmington | Missouri | St. Francois | 7 | 1748 | 55 | 46 | 39 |
| St. Louis-Farmington | Missouri | Jefferson | 49 | 3536 | 55 | 54 | 53 |
| St. Louis-Farmington | Illinois | St. Clair | 178 | 6043 | 41 | 49 | 53 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 9 | 1339 | 34 | 26 | 19 |
| Springfield | Missouri | Christian | 3 | 1068 | 31 | 26 | 20 |
| Kansas City | Kansas | Wyandotte | 128 | 6504 | 31 | 31 | 39 |
| St. Louis-Farmington | Missouri | St. Louis City | 192 | 6667 | 30 | 32 | 35 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1233 | 28 | 26 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 23 | 1376 | 28 | 24 | 21 |
| Missouri non-MSA | Missouri | Johnson | 4 | 905 | 24 | 22 | 13 |
| St. Joseph | Missouri | Buchanan | 13 | 1598 | 23 | 21 | 15 |
| Kansas City | Missouri | Clay | 39 | 1642 | 18 | 17 | 16 |
| Kansas City | Missouri | Cass | 16 | 1288 | 18 | 14 | 14 |
| Springfield | Missouri | Webster | 2 | 427 | 18 | 14 | 9 |
| Missouri non-MSA | Missouri | Camden | 10 | 722 | 15 | 13 | 10 |
| St. Louis-Farmington | Illinois | Clinton | 19 | 971 | 14 | 16 | 16 |
| Missouri non-MSA | Missouri | Laclede | 2 | 437 | 14 | 9 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 263 | 14 | 9 | 6 |
| Joplin | Missouri | Newton | 14 | 1229 | 13 | 9 | 9 |
| Missouri non-MSA | Missouri | Howell | 3 | 431 | 13 | 11 | 8 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 532 | 13 | 13 | 11 |
| Kansas City | Kansas | Leavenworth | 9 | 1823 | 13 | 11 | 9 |
| Missouri non-MSA | Missouri | Taney | 22 | 1061 | 12 | 10 | 10 |
| Missouri non-MSA | Missouri | Perry | 4 | 533 | 12 | 9 | 9 |
| Missouri non-MSA | Missouri | Phelps | 1 | 353 | 11 | 10 | 7 |
| Missouri non-MSA | Missouri | Crawford | 2 | 294 | 10 | 7 | 6 |
| Kansas City | Missouri | Lafayette | 2 | 350 | 10 | 7 | 5 |
| Missouri non-MSA | Missouri | Miller | 1 | 375 | 10 | 8 | 7 |
| Springfield | Missouri | Polk | 1 | 417 | 9 | 8 | 5 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 647 | 9 | 9 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 15 | 756 | 9 | 8 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 4 | 489 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Butler | 4 | 492 | 8 | 8 | 5 |
| Missouri non-MSA | Missouri | Pettis | 8 | 919 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Morgan | 1 | 220 | 8 | 7 | 4 |
| Missouri non-MSA | Missouri | Wright | 0 | 165 | 8 | 5 | 3 |
| St. Louis-Farmington | Missouri | Lincoln | 2 | 682 | 8 | 7 | 8 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 454 | 7 | 7 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 585 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 374 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Pike | 2 | 209 | 7 | 4 | 2 |
| Kansas City | Missouri | Platte | 10 | 583 | 6 | 6 | 5 |
| St. Louis-Farmington | Missouri | Warren | 0 | 412 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Grundy | 2 | 141 | 6 | 6 | 3 |
| Missouri non-MSA | Missouri | Marion | 7 | 610 | 6 | 9 | 11 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 434 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Wayne | 0 | 152 | 6 | 4 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 350 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Texas | 2 | 204 | 6 | 7 | 4 |
| Missouri non-MSA | Missouri | Stone | 2 | 359 | 6 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 251 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Audrain | 2 | 372 | 6 | 7 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 7 | 682 | 5 | 9 | 15 |
| St. Joseph | Missouri | Andrew | 1 | 189 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Madison | 0 | 247 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 6 | 140 | 5 | 3 | 3 |
| St. Louis-Farmington | Illinois | Macoupin | 6 | 440 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Dent | 0 | 94 | 5 | 3 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 13 | 361 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Randolph | 2 | 187 | 5 | 4 | 3 |
| St. Louis-Farmington | Illinois | Bond | 4 | 245 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Barton | 0 | 153 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Washington | 1 | 304 | 5 | 4 | 5 |
| Kansas City | Kansas | Miami | 1 | 298 | 4 | 7 | 4 |
| Missouri non-MSA | Missouri | Saline | 9 | 624 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Barry | 5 | 411 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 12 | 489 | 4 | 5 | 6 |
| Springfield | Missouri | Dallas | 1 | 154 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Benton | 2 | 188 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 0 | 92 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Ripley | 0 | 137 | 3 | 3 | 2 |
| Kansas City | Missouri | Clinton | 0 | 185 | 3 | 4 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 151 | 3 | 1 | 2 |
| Missouri non-MSA | Missouri | Macon | 0 | 109 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 270 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Livingston | 1 | 360 | 3 | 20 | 9 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 115 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 158 | 2 | 3 | 2 |
| St. Joseph | Missouri | DeKalb | 2 | 101 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 0 | 69 | 2 | 3 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 294 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Douglas | 3 | 139 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 132 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | McDonald | 10 | 1017 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 4 | 149 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 82 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 137 | 2 | 1 | 2 |
| Kansas City | Missouri | Ray | 0 | 146 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 53 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 89 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 62 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 97 | 1 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 60 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 61 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 69 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Carroll | 1 | 128 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 44 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 70 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 68 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 109 | 1 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 63 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 42 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 82 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Hickory | 2 | 74 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 56 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 55 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 84 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Atchison | 0 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 69 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 185 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 52 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 72 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 43 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 34 | 0 | 0 | 0 |
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
