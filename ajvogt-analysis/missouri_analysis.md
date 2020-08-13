# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/12/2020  
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
| St. Louis-Farmington | 1258 | 36025 | 579 | 662 | 622 |
| Kansas City | 388 | 26199 | 376 | 426 | 436 |
| Missouri non-MSA | 99 | 9761 | 184 | 201 | 185 |
| Springfield | 13 | 2413 | 63 | 65 | 60 |
| Columbia-Jefferson City | 10 | 2419 | 52 | 58 | 52 |
| Joplin | 37 | 2666 | 23 | 23 | 36 |
| Cape Girardeau-Sikeston | 19 | 1180 | 16 | 15 | 19 |
| St. Joseph | 12 | 1264 | 5 | 6 | 7 |
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
| St. Louis-Farmington | Missouri | St. Louis | 672 | 15284 | 213 | 263 | 249 |
| Kansas City | Missouri | Kansas City | 64 | 6885 | 106 | 115 | 125 |
| Kansas City | Kansas | Johnson | 105 | 5869 | 89 | 91 | 96 |
| St. Louis-Farmington | Missouri | St. Louis City | 177 | 5295 | 79 | 83 | 78 |
| Kansas City | Missouri | Jackson | 66 | 4155 | 73 | 97 | 85 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 4226 | 68 | 93 | 96 |
| St. Louis-Farmington | Illinois | Madison | 76 | 2702 | 62 | 54 | 50 |
| St. Louis-Farmington | Illinois | St. Clair | 161 | 4107 | 58 | 60 | 60 |
| Kansas City | Kansas | Wyandotte | 101 | 4959 | 48 | 54 | 63 |
| Springfield | Missouri | Greene | 10 | 1621 | 45 | 46 | 39 |
| St. Louis-Farmington | Missouri | Jefferson | 26 | 1663 | 33 | 42 | 36 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1429 | 24 | 29 | 28 |
| Missouri non-MSA | Missouri | Taney | 3 | 632 | 21 | 24 | 16 |
| Kansas City | Missouri | Clay | 20 | 1064 | 17 | 20 | 16 |
| Missouri non-MSA | Missouri | Pettis | 4 | 560 | 15 | 17 | 13 |
| Joplin | Missouri | Jasper | 31 | 1780 | 15 | 14 | 25 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 438 | 14 | 13 | 11 |
| Kansas City | Missouri | Cass | 9 | 770 | 13 | 18 | 18 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 642 | 12 | 12 | 12 |
| Springfield | Missouri | Christian | 1 | 373 | 10 | 11 | 9 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 392 | 10 | 10 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 398 | 9 | 11 | 9 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 415 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 2 | 259 | 8 | 8 | 6 |
| Joplin | Missouri | Newton | 6 | 886 | 8 | 8 | 11 |
| Kansas City | Kansas | Leavenworth | 9 | 1483 | 8 | 8 | 9 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 5 | 668 | 7 | 7 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 319 | 7 | 7 | 6 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 406 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Camden | 5 | 363 | 6 | 8 | 9 |
| Kansas City | Missouri | Platte | 10 | 373 | 6 | 7 | 7 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 117 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Marion | 1 | 204 | 6 | 7 | 5 |
| Missouri non-MSA | Missouri | Stone | 1 | 138 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 230 | 6 | 4 | 2 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 182 | 5 | 4 | 3 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 323 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 233 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Butler | 2 | 286 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Benton | 1 | 107 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Pike | 1 | 110 | 4 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 135 | 4 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 161 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Barry | 4 | 263 | 4 | 4 | 5 |
| St. Joseph | Missouri | Buchanan | 10 | 1092 | 4 | 4 | 5 |
| St. Louis-Farmington | Missouri | Warren | 0 | 208 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Miller | 1 | 135 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Washington | 1 | 87 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Saline | 7 | 441 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Adair | 0 | 161 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Perry | 4 | 235 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 186 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Johnson | 2 | 494 | 3 | 4 | 8 |
| Missouri non-MSA | Missouri | Crawford | 0 | 79 | 3 | 3 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 151 | 3 | 3 | 2 |
| Kansas City | Missouri | Clinton | 0 | 85 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 232 | 2 | 2 | 2 |
| Springfield | Missouri | Polk | 0 | 213 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | Hickory | 0 | 34 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 237 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Randolph | 1 | 73 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 60 | 2 | 3 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 87 | 2 | 2 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 180 | 2 | 3 | 2 |
| Springfield | Missouri | Dallas | 1 | 68 | 2 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 119 | 2 | 3 | 2 |
| Springfield | Missouri | Webster | 1 | 138 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Howell | 2 | 157 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Texas | 0 | 57 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 90 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 1 | 48 | 2 | 1 | 1 |
| Kansas City | Kansas | Miami | 0 | 134 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | McDonald | 7 | 953 | 1 | 4 | 8 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 69 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 84 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 205 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 141 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 0 | 63 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 31 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 34 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 57 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 145 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 54 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 27 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 38 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 48 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Madison | 0 | 25 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 15 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 21 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 24 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 19 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 54 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 52 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 2 | 89 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Macon | 0 | 60 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 41 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 53 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Bond | 3 | 62 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 26 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Laclede | 1 | 203 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Grundy | 1 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 70 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 62 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 15 | 0 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 88 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dent | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 85 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 101 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 16 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 48 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 8 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 11 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 22 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 35 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 43 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 9 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 15 | 0 | 0 | 0 |
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
