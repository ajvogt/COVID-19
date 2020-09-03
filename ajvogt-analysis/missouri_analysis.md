# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/03/2020  
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
| St. Louis-Farmington | 1430 | 49561 | 598 | 583 | 609 |
| Kansas City | 447 | 35242 | 389 | 392 | 404 |
| Missouri non-MSA | 146 | 15264 | 289 | 253 | 232 |
| Springfield | 13 | 4761 | 148 | 120 | 95 |
| Columbia-Jefferson City | 17 | 4694 | 146 | 118 | 89 |
| Joplin | 48 | 3544 | 48 | 40 | 35 |
| Cape Girardeau-Sikeston | 23 | 1819 | 30 | 26 | 25 |
| St. Joseph | 12 | 1597 | 22 | 16 | 12 |
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
| St. Louis-Farmington | Missouri | St. Louis | 752 | 19852 | 216 | 197 | 212 |
| Kansas City | Kansas | Johnson | 118 | 8436 | 118 | 121 | 109 |
| Springfield | Missouri | Greene | 10 | 3372 | 112 | 91 | 70 |
| Kansas City | Missouri | Kansas City | 72 | 9424 | 105 | 104 | 113 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 2817 | 102 | 79 | 52 |
| Kansas City | Missouri | Jackson | 78 | 5707 | 74 | 67 | 72 |
| St. Louis-Farmington | Missouri | St. Charles | 105 | 5861 | 67 | 65 | 74 |
| St. Louis-Farmington | Illinois | Madison | 100 | 4182 | 61 | 63 | 65 |
| St. Louis-Farmington | Missouri | Jefferson | 40 | 2819 | 57 | 52 | 47 |
| St. Louis-Farmington | Illinois | St. Clair | 172 | 5413 | 50 | 56 | 58 |
| Joplin | Missouri | Jasper | 35 | 2440 | 39 | 30 | 26 |
| St. Louis-Farmington | Missouri | St. Louis City | 188 | 6271 | 36 | 38 | 53 |
| Missouri non-MSA | Missouri | Nodaway | 6 | 567 | 35 | 23 | 13 |
| Kansas City | Kansas | Wyandotte | 114 | 6091 | 34 | 42 | 51 |
| St. Louis-Farmington | Missouri | St. Francois | 5 | 1113 | 34 | 32 | 26 |
| Springfield | Missouri | Christian | 1 | 719 | 20 | 16 | 14 |
| St. Louis-Farmington | Missouri | Franklin | 22 | 1055 | 19 | 18 | 17 |
| Missouri non-MSA | Missouri | Marion | 3 | 489 | 17 | 14 | 11 |
| Columbia-Jefferson City | Missouri | Cole | 4 | 881 | 17 | 17 | 18 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 765 | 16 | 17 | 13 |
| St. Joseph | Missouri | Buchanan | 10 | 1322 | 15 | 11 | 8 |
| Kansas City | Missouri | Clay | 31 | 1412 | 14 | 16 | 16 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 8 | 989 | 13 | 13 | 12 |
| Kansas City | Missouri | Cass | 11 | 1092 | 13 | 13 | 14 |
| Missouri non-MSA | Missouri | Perry | 4 | 412 | 12 | 9 | 6 |
| Cape Girardeau-Sikeston | Missouri | Scott | 14 | 652 | 12 | 9 | 10 |
| Missouri non-MSA | Missouri | Madison | 0 | 170 | 12 | 8 | 5 |
| Missouri non-MSA | Missouri | Camden | 8 | 556 | 10 | 9 | 8 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 586 | 10 | 8 | 9 |
| Missouri non-MSA | Missouri | Howell | 3 | 285 | 10 | 7 | 4 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 344 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 532 | 9 | 8 | 9 |
| Joplin | Missouri | Newton | 13 | 1104 | 9 | 9 | 9 |
| Missouri non-MSA | Missouri | New Madrid | 5 | 421 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | Pettis | 8 | 816 | 8 | 9 | 12 |
| Springfield | Missouri | Webster | 1 | 253 | 8 | 6 | 4 |
| Kansas City | Kansas | Leavenworth | 9 | 1680 | 8 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Cooper | 1 | 244 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Taney | 14 | 929 | 7 | 9 | 15 |
| Missouri non-MSA | Missouri | Phelps | 0 | 224 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 3 | 99 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Miller | 1 | 265 | 6 | 7 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 14 | 472 | 6 | 7 | 6 |
| Springfield | Missouri | Polk | 0 | 309 | 6 | 4 | 3 |
| St. Louis-Farmington | Illinois | Bond | 3 | 161 | 6 | 4 | 3 |
| Kansas City | Missouri | Platte | 10 | 495 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 2 | 400 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 363 | 5 | 5 | 5 |
| St. Louis-Farmington | Illinois | Jersey | 6 | 285 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Johnson | 3 | 599 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Crawford | 1 | 198 | 5 | 5 | 4 |
| St. Louis-Farmington | Illinois | Macoupin | 5 | 362 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Laclede | 1 | 307 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 346 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Stone | 2 | 286 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Washington | 1 | 246 | 4 | 6 | 6 |
| St. Louis-Farmington | Missouri | Warren | 0 | 337 | 4 | 4 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 128 | 4 | 3 | 2 |
| Kansas City | Kansas | Miami | 0 | 218 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 242 | 4 | 3 | 3 |
| Kansas City | Missouri | Lafayette | 2 | 250 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Audrain | 1 | 273 | 4 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 133 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 5 | 360 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Butler | 3 | 383 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 301 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Grundy | 1 | 58 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 115 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Texas | 1 | 107 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 237 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Saline | 7 | 551 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Barton | 0 | 108 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 52 | 2 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 131 | 2 | 2 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 71 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 3 | 195 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Randolph | 1 | 130 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Harrison | 1 | 78 | 2 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 73 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Pike | 2 | 148 | 2 | 0 | 2 |
| Kansas City | Missouri | Bates | 1 | 77 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 128 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 48 | 2 | 1 | 1 |
| Kansas City | Missouri | Clinton | 0 | 135 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 113 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 89 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | McDonald | 10 | 994 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 2 | 114 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 85 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 0 | 67 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 0 | 64 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 9 | 100 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 33 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 88 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 82 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 43 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 72 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 37 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 30 | 1 | 0 | 0 |
| Springfield | Missouri | Dallas | 1 | 108 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 46 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 27 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 92 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 118 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 54 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 51 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 30 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 54 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 114 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 91 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 1 | 76 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 174 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Benton | 1 | 156 | 0 | 2 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 55 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 49 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 13 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 56 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 45 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 125 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 39 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 27 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 46 | 0 | 0 | 0 |
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
