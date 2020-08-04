# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/04/2020  
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
| St. Louis-Farmington | 1218 | 31281 | 720 | 748 | 541 |
| Kansas City | 358 | 23109 | 519 | 505 | 410 |
| Missouri non-MSA | 90 | 8303 | 241 | 213 | 160 |
| Springfield | 13 | 1902 | 72 | 66 | 49 |
| Columbia-Jefferson City | 8 | 2000 | 71 | 61 | 45 |
| Joplin | 31 | 2466 | 26 | 39 | 42 |
| Cape Girardeau-Sikeston | 16 | 1051 | 18 | 20 | 21 |
| St. Joseph | 12 | 1224 | 8 | 9 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 650 | 13474 | 281 | 311 | 221 |
| Kansas City | Missouri | Kansas City | 54 | 6027 | 154 | 158 | 112 |
| Kansas City | Missouri | Jackson | 59 | 3537 | 135 | 113 | 73 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 3636 | 124 | 133 | 83 |
| St. Louis-Farmington | Missouri | St. Louis City | 171 | 4667 | 89 | 87 | 69 |
| Kansas City | Kansas | Johnson | 98 | 5150 | 87 | 94 | 101 |
| St. Louis-Farmington | Illinois | St. Clair | 156 | 3655 | 64 | 63 | 55 |
| Kansas City | Kansas | Wyandotte | 96 | 4535 | 58 | 59 | 66 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1395 | 53 | 47 | 29 |
| Springfield | Missouri | Greene | 10 | 1256 | 48 | 43 | 31 |
| St. Louis-Farmington | Illinois | Madison | 73 | 2222 | 43 | 49 | 40 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1236 | 40 | 34 | 27 |
| Missouri non-MSA | Missouri | Taney | 3 | 456 | 27 | 19 | 12 |
| Kansas City | Missouri | Cass | 9 | 654 | 26 | 26 | 16 |
| Kansas City | Missouri | Clay | 20 | 914 | 24 | 20 | 14 |
| Missouri non-MSA | Missouri | Pettis | 3 | 435 | 19 | 16 | 10 |
| Joplin | Missouri | Jasper | 25 | 1659 | 18 | 28 | 30 |
| Springfield | Missouri | Christian | 1 | 286 | 14 | 11 | 7 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 325 | 13 | 11 | 8 |
| Missouri non-MSA | Missouri | Camden | 4 | 309 | 13 | 14 | 8 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 542 | 13 | 13 | 10 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 314 | 12 | 11 | 7 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 307 | 9 | 8 | 5 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 607 | 9 | 11 | 13 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 162 | 9 | 9 | 4 |
| Missouri non-MSA | Missouri | Marion | 1 | 157 | 9 | 7 | 4 |
| Kansas City | Kansas | Leavenworth | 8 | 1425 | 9 | 10 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 194 | 8 | 6 | 5 |
| Kansas City | Missouri | Platte | 10 | 318 | 8 | 7 | 6 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 352 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Johnson | 2 | 473 | 8 | 8 | 10 |
| Joplin | Missouri | Newton | 6 | 807 | 7 | 10 | 11 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 278 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 255 | 7 | 7 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 192 | 7 | 6 | 5 |
| St. Louis-Farmington | Missouri | Warren | 0 | 171 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | McDonald | 7 | 936 | 6 | 8 | 11 |
| Missouri non-MSA | Missouri | Butler | 2 | 247 | 6 | 7 | 4 |
| Missouri non-MSA | Missouri | Saline | 7 | 415 | 6 | 4 | 4 |
| St. Joseph | Missouri | Buchanan | 10 | 1062 | 6 | 6 | 5 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 349 | 6 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 98 | 5 | 4 | 2 |
| Springfield | Missouri | Polk | 0 | 192 | 5 | 7 | 5 |
| Kansas City | Missouri | Ray | 0 | 96 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Miller | 0 | 104 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Barry | 0 | 230 | 5 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 130 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Douglas | 2 | 81 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 8 | 214 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Howell | 2 | 140 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Stone | 1 | 88 | 4 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 123 | 4 | 3 | 2 |
| Kansas City | Missouri | Lafayette | 2 | 158 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Laclede | 1 | 200 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Morgan | 0 | 71 | 3 | 2 | 1 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 137 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Randolph | 1 | 57 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Carroll | 0 | 99 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 37 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Crawford | 0 | 57 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Perry | 4 | 208 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 72 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Shelby | 0 | 29 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 209 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 75 | 2 | 3 | 1 |
| Missouri non-MSA | Missouri | Pike | 1 | 74 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 0 | 38 | 2 | 1 | 1 |
| Kansas City | Kansas | Miami | 0 | 120 | 2 | 2 | 2 |
| Springfield | Missouri | Webster | 1 | 118 | 2 | 2 | 2 |
| St. Louis-Farmington | Illinois | Bond | 2 | 57 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 74 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 53 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 19 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Audrain | 1 | 194 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 134 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 14 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 21 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 53 | 1 | 1 | 1 |
| Kansas City | Missouri | Clinton | 0 | 65 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 136 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 183 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 21 | 1 | 1 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 70 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 42 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Washington | 1 | 56 | 1 | 1 | 1 |
| Springfield | Missouri | Dallas | 1 | 50 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 65 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 131 | 1 | 2 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 84 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 19 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 34 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 17 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 38 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 45 | 1 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 35 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 17 | 1 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 40 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 20 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 46 | 1 | 2 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 35 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 56 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 46 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 82 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 58 | 0 | 0 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 34 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 7 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 43 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 17 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 7 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 12 | 0 | 0 | 0 |
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
