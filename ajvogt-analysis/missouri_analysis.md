# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/28/2020  
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
| St. Louis-Farmington | 1370 | 45984 | 573 | 604 | 640 |
| Kansas City | 434 | 32960 | 402 | 401 | 424 |
| Missouri non-MSA | 119 | 13524 | 228 | 226 | 219 |
| Columbia-Jefferson City | 15 | 3860 | 104 | 92 | 75 |
| Springfield | 13 | 3887 | 101 | 93 | 79 |
| Joplin | 47 | 3263 | 36 | 33 | 30 |
| Cape Girardeau-Sikeston | 21 | 1648 | 27 | 28 | 22 |
| St. Joseph | 12 | 1480 | 15 | 13 | 10 |
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
| St. Louis-Farmington | Missouri | St. Louis | 726 | 18507 | 173 | 188 | 230 |
| Kansas City | Kansas | Johnson | 116 | 7754 | 127 | 116 | 105 |
| Kansas City | Missouri | Kansas City | 66 | 8837 | 109 | 110 | 119 |
| Springfield | Missouri | Greene | 10 | 2718 | 77 | 70 | 58 |
| St. Louis-Farmington | Missouri | St. Charles | 96 | 5473 | 67 | 76 | 85 |
| St. Louis-Farmington | Illinois | Madison | 95 | 3818 | 64 | 68 | 62 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 2209 | 63 | 50 | 39 |
| St. Louis-Farmington | Illinois | St. Clair | 170 | 5107 | 63 | 63 | 61 |
| Kansas City | Missouri | Jackson | 77 | 5254 | 60 | 63 | 81 |
| St. Louis-Farmington | Missouri | Jefferson | 31 | 2486 | 49 | 51 | 47 |
| Kansas City | Kansas | Wyandotte | 113 | 5882 | 47 | 56 | 56 |
| St. Louis-Farmington | Missouri | St. Louis City | 188 | 6032 | 37 | 43 | 63 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 932 | 36 | 33 | 22 |
| Joplin | Missouri | Jasper | 34 | 2207 | 26 | 23 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 943 | 19 | 18 | 15 |
| Kansas City | Missouri | Clay | 30 | 1323 | 18 | 16 | 17 |
| Columbia-Jefferson City | Missouri | Cole | 4 | 775 | 17 | 21 | 17 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 667 | 17 | 16 | 11 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 7 | 914 | 14 | 14 | 11 |
| Kansas City | Missouri | Cass | 9 | 1009 | 13 | 14 | 16 |
| Missouri non-MSA | Missouri | Nodaway | 1 | 341 | 13 | 10 | 7 |
| Springfield | Missouri | Christian | 1 | 589 | 13 | 13 | 12 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 299 | 10 | 9 | 6 |
| Missouri non-MSA | Missouri | Perry | 4 | 347 | 10 | 7 | 5 |
| St. Joseph | Missouri | Buchanan | 10 | 1234 | 10 | 8 | 6 |
| Missouri non-MSA | Missouri | Marion | 1 | 378 | 10 | 10 | 9 |
| Joplin | Missouri | Newton | 13 | 1056 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | Taney | 3 | 886 | 10 | 14 | 20 |
| St. Louis-Farmington | Illinois | Monroe | 14 | 442 | 9 | 7 | 7 |
| St. Louis-Farmington | Illinois | Jersey | 3 | 264 | 9 | 8 | 6 |
| Kansas City | Kansas | Leavenworth | 9 | 1624 | 9 | 8 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 581 | 8 | 10 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 366 | 8 | 8 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 333 | 8 | 8 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 525 | 8 | 7 | 9 |
| Missouri non-MSA | Missouri | Pettis | 8 | 758 | 8 | 12 | 14 |
| Missouri non-MSA | Missouri | Washington | 1 | 224 | 7 | 8 | 5 |
| Missouri non-MSA | Missouri | Camden | 8 | 488 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Madison | 0 | 98 | 7 | 4 | 2 |
| Missouri non-MSA | Missouri | Phelps | 0 | 180 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Miller | 1 | 222 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 335 | 6 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 215 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 471 | 5 | 9 | 8 |
| Missouri non-MSA | Missouri | Johnson | 3 | 568 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 4 | 362 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Crawford | 1 | 164 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Stone | 2 | 261 | 5 | 7 | 6 |
| Kansas City | Missouri | Platte | 10 | 460 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Butler | 2 | 363 | 5 | 4 | 5 |
| Springfield | Missouri | Webster | 1 | 201 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 284 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 314 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Howell | 3 | 218 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 221 | 4 | 4 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 306 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Saline | 7 | 531 | 4 | 4 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 106 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 96 | 4 | 3 | 2 |
| St. Louis-Farmington | Illinois | Bond | 3 | 123 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 4 | 340 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Laclede | 1 | 275 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Monroe | 0 | 65 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 63 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Benton | 1 | 154 | 3 | 3 | 3 |
| Springfield | Missouri | Polk | 0 | 275 | 3 | 3 | 3 |
| Kansas City | Kansas | Miami | 0 | 188 | 3 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 109 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 219 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 99 | 2 | 2 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 223 | 2 | 2 | 2 |
| Springfield | Missouri | Dallas | 1 | 104 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Barton | 0 | 92 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 42 | 2 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 120 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 1 | 89 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 171 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 249 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | McDonald | 9 | 985 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Henry | 3 | 112 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 80 | 1 | 1 | 1 |
| Kansas City | Missouri | Clinton | 0 | 123 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Randolph | 1 | 105 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 114 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 88 | 1 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 59 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 44 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 59 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 181 | 1 | 1 | 2 |
| St. Joseph | Kansas | Doniphan | 0 | 67 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 75 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 65 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Holt | 0 | 58 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 32 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 85 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 38 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dent | 0 | 33 | 1 | 1 | 0 |
| Kansas City | Missouri | Ray | 0 | 124 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 78 | 1 | 1 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 26 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 39 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 53 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 102 | 0 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 49 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 90 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 34 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 73 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 65 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 1 | 71 | 0 | 0 | 1 |
| Kansas City | Kansas | Linn | 0 | 53 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 55 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 107 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 38 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Pike | 1 | 135 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Shelby | 0 | 45 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 20 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 18 | 0 | 0 | 0 |
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
