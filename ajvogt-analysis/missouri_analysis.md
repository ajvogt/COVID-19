# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/06/2020  
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
| St. Louis-Farmington | 1223 | 32701 | 708 | 757 | 580 |
| Kansas City | 366 | 23985 | 442 | 499 | 425 |
| Missouri non-MSA | 94 | 8649 | 204 | 213 | 167 |
| Springfield | 13 | 2035 | 63 | 70 | 52 |
| Columbia-Jefferson City | 10 | 2106 | 62 | 62 | 48 |
| Joplin | 33 | 2527 | 22 | 36 | 42 |
| Cape Girardeau-Sikeston | 18 | 1067 | 14 | 16 | 20 |
| St. Joseph | 12 | 1238 | 6 | 7 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 652 | 14074 | 293 | 317 | 238 |
| Kansas City | Missouri | Kansas City | 57 | 6268 | 120 | 154 | 117 |
| Kansas City | Missouri | Jackson | 61 | 3713 | 108 | 114 | 78 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 3842 | 104 | 130 | 90 |
| St. Louis-Farmington | Missouri | St. Louis City | 171 | 4857 | 88 | 87 | 74 |
| Kansas City | Kansas | Johnson | 98 | 5320 | 86 | 90 | 101 |
| St. Louis-Farmington | Illinois | St. Clair | 159 | 3753 | 59 | 62 | 57 |
| Kansas City | Kansas | Wyandotte | 98 | 4674 | 58 | 60 | 69 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1486 | 50 | 49 | 32 |
| St. Louis-Farmington | Illinois | Madison | 73 | 2320 | 49 | 51 | 42 |
| Springfield | Missouri | Greene | 10 | 1350 | 45 | 47 | 33 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1283 | 30 | 34 | 28 |
| Missouri non-MSA | Missouri | Taney | 3 | 507 | 29 | 21 | 13 |
| Kansas City | Missouri | Clay | 20 | 974 | 21 | 22 | 15 |
| Kansas City | Missouri | Cass | 9 | 679 | 17 | 23 | 17 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 354 | 14 | 12 | 8 |
| Missouri non-MSA | Missouri | Pettis | 3 | 454 | 14 | 17 | 10 |
| Joplin | Missouri | Jasper | 27 | 1694 | 14 | 26 | 30 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 343 | 12 | 12 | 8 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 566 | 11 | 12 | 11 |
| Springfield | Missouri | Christian | 1 | 311 | 11 | 13 | 8 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 334 | 10 | 8 | 6 |
| Kansas City | Kansas | Leavenworth | 8 | 1444 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | Camden | 5 | 326 | 9 | 13 | 8 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 205 | 8 | 6 | 5 |
| Joplin | Missouri | Newton | 6 | 833 | 7 | 9 | 11 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 292 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Marion | 1 | 164 | 7 | 7 | 4 |
| St. Louis-Farmington | Missouri | Warren | 0 | 185 | 7 | 6 | 4 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 5 | 614 | 7 | 8 | 13 |
| Kansas City | Missouri | Platte | 11 | 332 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 276 | 6 | 7 | 5 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 366 | 6 | 6 | 4 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 358 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 202 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 168 | 6 | 8 | 4 |
| Kansas City | Missouri | Ray | 0 | 110 | 5 | 5 | 2 |
| Missouri non-MSA | Missouri | Butler | 2 | 253 | 5 | 7 | 4 |
| Missouri non-MSA | Missouri | Johnson | 2 | 474 | 5 | 6 | 10 |
| Missouri non-MSA | Missouri | Stone | 1 | 106 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 226 | 4 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 136 | 4 | 4 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 107 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | McDonald | 7 | 942 | 4 | 8 | 10 |
| Missouri non-MSA | Missouri | Saline | 7 | 421 | 4 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 133 | 4 | 3 | 2 |
| St. Joseph | Missouri | Buchanan | 10 | 1069 | 4 | 5 | 5 |
| Kansas City | Missouri | Lafayette | 2 | 166 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 2 | 242 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Wayne | 0 | 45 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Miller | 0 | 109 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Douglas | 2 | 83 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Crawford | 0 | 62 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Perry | 4 | 214 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Howell | 2 | 143 | 3 | 5 | 3 |
| Springfield | Missouri | Webster | 1 | 125 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Texas | 0 | 45 | 2 | 2 | 1 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 142 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 74 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 24 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 29 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 192 | 2 | 2 | 2 |
| St. Louis-Farmington | Illinois | Bond | 2 | 59 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Washington | 1 | 66 | 2 | 1 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 74 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 143 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 0 | 99 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 78 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 46 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 1 | 79 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 79 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Laclede | 1 | 197 | 1 | 3 | 4 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 215 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Randolph | 1 | 60 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 24 | 1 | 1 | 0 |
| Springfield | Missouri | Polk | 0 | 196 | 1 | 5 | 6 |
| Missouri non-MSA | Missouri | Iron | 0 | 22 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 15 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 73 | 1 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 68 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 198 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 20 | 1 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 42 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 41 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 47 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 139 | 1 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 53 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 51 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 55 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 18 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 13 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 35 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 47 | 1 | 1 | 1 |
| Kansas City | Kansas | Linn | 0 | 36 | 1 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 36 | 1 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 87 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 0 | 53 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 21 | 0 | 1 | 0 |
| Kansas City | Kansas | Miami | 0 | 123 | 0 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 59 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 20 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 133 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 66 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 11 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 58 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 1 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 14 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 47 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 82 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
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
