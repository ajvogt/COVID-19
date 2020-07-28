# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 07/28/2020  
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
| St. Louis-Farmington | 1190 | 26240 | 777 | 616 | 418 |
| Kansas City | 332 | 19475 | 491 | 435 | 349 |
| Missouri non-MSA | 78 | 6611 | 186 | 168 | 122 |
| Springfield | 12 | 1396 | 60 | 54 | 34 |
| Joplin | 26 | 2284 | 52 | 50 | 49 |
| Columbia-Jefferson City | 8 | 1502 | 52 | 44 | 33 |
| Cape Girardeau-Sikeston | 16 | 919 | 22 | 23 | 19 |
| St. Joseph | 12 | 1164 | 9 | 8 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 636 | 11507 | 341 | 257 | 173 |
| Kansas City | Missouri | Kansas City | 46 | 4949 | 162 | 128 | 90 |
| St. Louis-Farmington | Missouri | St. Charles | 84 | 2764 | 141 | 99 | 58 |
| Kansas City | Kansas | Johnson | 94 | 4538 | 101 | 104 | 99 |
| Kansas City | Missouri | Jackson | 56 | 2591 | 91 | 70 | 48 |
| St. Louis-Farmington | Missouri | St. Louis City | 165 | 4042 | 85 | 76 | 56 |
| St. Louis-Farmington | Illinois | St. Clair | 153 | 3202 | 62 | 61 | 48 |
| Kansas City | Kansas | Wyandotte | 92 | 4128 | 61 | 72 | 67 |
| St. Louis-Farmington | Illinois | Madison | 71 | 1915 | 54 | 46 | 33 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1021 | 41 | 30 | 19 |
| Joplin | Missouri | Jasper | 23 | 1531 | 39 | 36 | 36 |
| Springfield | Missouri | Greene | 9 | 914 | 37 | 31 | 21 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 956 | 29 | 25 | 21 |
| Kansas City | Missouri | Cass | 8 | 472 | 26 | 18 | 11 |
| Kansas City | Missouri | Clay | 19 | 744 | 16 | 12 | 11 |
| Missouri non-MSA | Missouri | Camden | 3 | 216 | 15 | 9 | 5 |
| Missouri non-MSA | Missouri | Pettis | 3 | 296 | 13 | 10 | 6 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 540 | 13 | 15 | 13 |
| Joplin | Missouri | Newton | 3 | 753 | 13 | 13 | 13 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 451 | 13 | 12 | 8 |
| Missouri non-MSA | Missouri | Taney | 3 | 267 | 12 | 10 | 7 |
| Kansas City | Kansas | Leavenworth | 7 | 1361 | 10 | 9 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 228 | 10 | 7 | 4 |
| Missouri non-MSA | Missouri | McDonald | 7 | 888 | 9 | 12 | 13 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 229 | 9 | 8 | 5 |
| Springfield | Missouri | Christian | 1 | 188 | 9 | 7 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 96 | 9 | 5 | 2 |
| Missouri non-MSA | Missouri | Johnson | 1 | 417 | 8 | 12 | 10 |
| Springfield | Missouri | Polk | 0 | 153 | 8 | 9 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 3 | 205 | 8 | 5 | 3 |
| Missouri non-MSA | Missouri | Butler | 2 | 201 | 7 | 5 | 4 |
| Kansas City | Missouri | Platte | 6 | 260 | 7 | 7 | 4 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 294 | 7 | 6 | 4 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 238 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Howell | 0 | 108 | 6 | 4 | 2 |
| St. Joseph | Missouri | Buchanan | 10 | 1018 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Marion | 1 | 92 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 142 | 5 | 5 | 3 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 306 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Barry | 0 | 194 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 134 | 4 | 5 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 122 | 4 | 4 | 2 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 227 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Laclede | 1 | 173 | 4 | 6 | 4 |
| Missouri non-MSA | Missouri | Carroll | 0 | 74 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Miller | 0 | 67 | 3 | 3 | 1 |
| Missouri non-MSA | Missouri | Benton | 1 | 57 | 3 | 2 | 1 |
| Kansas City | Kansas | Miami | 0 | 103 | 3 | 3 | 2 |
| Springfield | Missouri | Webster | 1 | 101 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Saline | 6 | 371 | 3 | 4 | 2 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 112 | 3 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 94 | 3 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 57 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 180 | 3 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 39 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 122 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Stone | 1 | 59 | 3 | 2 | 1 |
| Kansas City | Missouri | Ray | 0 | 58 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 191 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 6 | 181 | 2 | 4 | 2 |
| Missouri non-MSA | Missouri | Douglas | 1 | 47 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 172 | 2 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 53 | 2 | 1 | 1 |
| St. Louis-Farmington | Illinois | Bond | 2 | 40 | 2 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 95 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 54 | 1 | 2 | 1 |
| Kansas City | Missouri | Bates | 1 | 32 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 25 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Morgan | 0 | 46 | 1 | 1 | 1 |
| Springfield | Missouri | Dallas | 1 | 40 | 1 | 1 | 0 |
| Kansas City | Missouri | Lafayette | 2 | 131 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 121 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 32 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 32 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 40 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 44 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 0 | 39 | 1 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 75 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Pike | 1 | 56 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Shannon | 0 | 41 | 1 | 0 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 28 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 37 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 50 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Crawford | 0 | 35 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 13 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 12 | 1 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 43 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Perry | 3 | 188 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Washington | 1 | 46 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 31 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 76 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 59 | 0 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 27 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 41 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Madison | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 55 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 46 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 54 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 124 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Phelps | 0 | 59 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 5 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 0 | 4 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 13 | 0 | 0 | 0 |
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
