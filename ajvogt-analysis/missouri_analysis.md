# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/15/2020  
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
| St. Louis-Farmington | 1274 | 38291 | 614 | 608 | 657 |
| Kansas City | 398 | 27824 | 424 | 410 | 463 |
| Missouri non-MSA | 108 | 10667 | 226 | 205 | 201 |
| Springfield | 13 | 2633 | 65 | 60 | 64 |
| Columbia-Jefferson City | 10 | 2628 | 61 | 56 | 55 |
| Joplin | 38 | 2814 | 29 | 28 | 37 |
| Cape Girardeau-Sikeston | 19 | 1298 | 25 | 19 | 21 |
| St. Joseph | 12 | 1300 | 7 | 6 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 676 | 16133 | 224 | 232 | 261 |
| Kansas City | Missouri | Kansas City | 65 | 7440 | 137 | 117 | 138 |
| Kansas City | Kansas | Johnson | 106 | 6228 | 100 | 96 | 98 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 4520 | 80 | 77 | 100 |
| Kansas City | Missouri | Jackson | 66 | 4451 | 77 | 80 | 92 |
| St. Louis-Farmington | Illinois | Madison | 85 | 2969 | 71 | 62 | 55 |
| St. Louis-Farmington | Missouri | St. Louis City | 178 | 5479 | 60 | 70 | 78 |
| St. Louis-Farmington | Illinois | St. Clair | 162 | 4289 | 56 | 55 | 61 |
| Springfield | Missouri | Greene | 10 | 1775 | 47 | 42 | 41 |
| Kansas City | Kansas | Wyandotte | 107 | 5137 | 46 | 54 | 66 |
| St. Louis-Farmington | Missouri | Jefferson | 27 | 1833 | 41 | 38 | 39 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1525 | 28 | 26 | 29 |
| Joplin | Missouri | Jasper | 32 | 1891 | 21 | 18 | 26 |
| Missouri non-MSA | Missouri | Taney | 3 | 685 | 19 | 21 | 18 |
| Missouri non-MSA | Missouri | Pettis | 6 | 624 | 19 | 15 | 15 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 478 | 18 | 13 | 10 |
| Kansas City | Missouri | Cass | 9 | 830 | 17 | 14 | 20 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 496 | 17 | 14 | 12 |
| Kansas City | Missouri | Clay | 22 | 1126 | 16 | 17 | 17 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 704 | 16 | 13 | 12 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 5 | 732 | 13 | 9 | 11 |
| Springfield | Missouri | Christian | 1 | 411 | 10 | 10 | 10 |
| Missouri non-MSA | Missouri | Marion | 1 | 256 | 10 | 8 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 372 | 10 | 9 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 449 | 9 | 7 | 7 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 454 | 9 | 8 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 222 | 9 | 6 | 4 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 262 | 9 | 6 | 3 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 421 | 8 | 9 | 9 |
| Kansas City | Kansas | Leavenworth | 9 | 1519 | 8 | 9 | 9 |
| Kansas City | Missouri | Platte | 10 | 401 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Washington | 1 | 124 | 7 | 4 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 285 | 7 | 8 | 6 |
| Joplin | Missouri | Newton | 6 | 923 | 7 | 9 | 10 |
| Missouri non-MSA | Missouri | Saline | 7 | 478 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Camden | 7 | 388 | 7 | 7 | 9 |
| Missouri non-MSA | Missouri | Pike | 1 | 142 | 6 | 5 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 143 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 220 | 6 | 5 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 157 | 5 | 5 | 4 |
| St. Joseph | Missouri | Buchanan | 10 | 1117 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Stone | 1 | 161 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 247 | 5 | 4 | 6 |
| St. Louis-Farmington | Missouri | Warren | 0 | 226 | 5 | 5 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 339 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Holt | 0 | 41 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 167 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Phelps | 0 | 114 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 4 | 280 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Perry | 4 | 254 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Miller | 1 | 144 | 4 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 170 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Butler | 2 | 302 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Crawford | 0 | 97 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Laclede | 1 | 221 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Benton | 2 | 116 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 178 | 3 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 160 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 49 | 2 | 2 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 194 | 2 | 3 | 3 |
| Springfield | Missouri | Webster | 1 | 147 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Audrain | 1 | 217 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Johnson | 3 | 504 | 2 | 3 | 7 |
| Springfield | Missouri | Polk | 0 | 227 | 2 | 2 | 6 |
| Missouri non-MSA | Missouri | Howell | 2 | 169 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 251 | 2 | 3 | 3 |
| Kansas City | Kansas | Miami | 0 | 150 | 2 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 65 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 92 | 2 | 1 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 80 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 239 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 92 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Lewis | 1 | 54 | 2 | 1 | 1 |
| Kansas City | Missouri | Clinton | 0 | 93 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 34 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 66 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 1 | 63 | 1 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 73 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 0 | 42 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 152 | 1 | 1 | 1 |
| Kansas City | Kansas | Linn | 0 | 46 | 1 | 1 | 0 |
| St. Louis-Farmington | Illinois | Bond | 3 | 69 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 55 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 54 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 59 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Randolph | 1 | 76 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 60 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 70 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 66 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 37 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 38 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 18 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 63 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 35 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 27 | 1 | 1 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 95 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 27 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 21 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 34 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 89 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Grundy | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | McDonald | 8 | 955 | 0 | 2 | 6 |
| St. Joseph | Missouri | DeKalb | 1 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 64 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ozark | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 86 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 119 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 0 | 41 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 102 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Barton | 0 | 71 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 21 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 10 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 13 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 48 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 9 | 0 | 0 | 0 |
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
