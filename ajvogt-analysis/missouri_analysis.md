# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/20/2020  
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
| St. Louis-Farmington | 1326 | 41391 | 671 | 620 | 686 |
| Kansas City | 412 | 29754 | 419 | 412 | 457 |
| Missouri non-MSA | 109 | 11709 | 229 | 218 | 213 |
| Springfield | 13 | 3075 | 81 | 74 | 70 |
| Columbia-Jefferson City | 12 | 3029 | 78 | 65 | 63 |
| Joplin | 46 | 2984 | 32 | 32 | 35 |
| Cape Girardeau-Sikeston | 20 | 1442 | 31 | 26 | 22 |
| St. Joseph | 12 | 1360 | 11 | 8 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 705 | 17094 | 229 | 215 | 266 |
| Kansas City | Missouri | Kansas City | 66 | 7967 | 127 | 121 | 138 |
| Kansas City | Kansas | Johnson | 108 | 6736 | 103 | 101 | 96 |
| St. Louis-Farmington | Missouri | St. Charles | 96 | 4945 | 89 | 78 | 105 |
| St. Louis-Farmington | Illinois | Madison | 87 | 3289 | 73 | 69 | 58 |
| Kansas City | Missouri | Jackson | 67 | 4758 | 69 | 74 | 93 |
| St. Louis-Farmington | Illinois | St. Clair | 165 | 4626 | 67 | 62 | 61 |
| Kansas City | Kansas | Wyandotte | 109 | 5501 | 67 | 59 | 60 |
| Springfield | Missouri | Greene | 10 | 2090 | 57 | 52 | 48 |
| St. Louis-Farmington | Missouri | St. Louis City | 181 | 5728 | 52 | 62 | 76 |
| St. Louis-Farmington | Missouri | Jefferson | 30 | 2088 | 51 | 43 | 45 |
| Columbia-Jefferson City | Missouri | Boone | 5 | 1704 | 35 | 30 | 31 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 661 | 34 | 23 | 15 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 634 | 24 | 20 | 15 |
| Joplin | Missouri | Jasper | 35 | 2010 | 24 | 22 | 25 |
| Missouri non-MSA | Missouri | Taney | 3 | 800 | 20 | 20 | 20 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 791 | 17 | 16 | 14 |
| Kansas City | Missouri | Cass | 9 | 901 | 16 | 15 | 20 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 6 | 800 | 15 | 13 | 11 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 524 | 15 | 11 | 8 |
| Missouri non-MSA | Missouri | Pettis | 5 | 684 | 14 | 16 | 16 |
| Springfield | Missouri | Christian | 1 | 489 | 13 | 12 | 12 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 515 | 13 | 11 | 9 |
| Kansas City | Missouri | Clay | 30 | 1180 | 13 | 14 | 18 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 420 | 12 | 10 | 9 |
| Missouri non-MSA | Missouri | Marion | 1 | 293 | 10 | 9 | 8 |
| Missouri non-MSA | Missouri | Washington | 1 | 156 | 8 | 6 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 274 | 8 | 6 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 260 | 8 | 8 | 5 |
| Missouri non-MSA | Missouri | Stone | 1 | 209 | 8 | 7 | 5 |
| Joplin | Missouri | Newton | 11 | 974 | 8 | 10 | 10 |
| Missouri non-MSA | Missouri | Camden | 8 | 428 | 8 | 7 | 10 |
| Kansas City | Kansas | Leavenworth | 9 | 1560 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 245 | 7 | 5 | 7 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 174 | 7 | 7 | 4 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 213 | 7 | 5 | 4 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 461 | 7 | 8 | 10 |
| St. Joseph | Missouri | Buchanan | 10 | 1155 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 288 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 316 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 291 | 6 | 7 | 4 |
| Missouri non-MSA | Missouri | Barry | 4 | 306 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Crawford | 0 | 121 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Butler | 2 | 326 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Saline | 7 | 496 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Laclede | 1 | 246 | 5 | 3 | 3 |
| Kansas City | Missouri | Platte | 10 | 421 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 184 | 5 | 3 | 2 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 367 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 276 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Perry | 4 | 275 | 4 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 170 | 4 | 4 | 4 |
| Springfield | Missouri | Polk | 0 | 249 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Phelps | 0 | 129 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Miller | 1 | 166 | 4 | 4 | 4 |
| St. Louis-Farmington | Illinois | Bond | 3 | 92 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Audrain | 1 | 233 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Howell | 2 | 184 | 3 | 2 | 4 |
| Springfield | Missouri | Webster | 1 | 164 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Johnson | 3 | 523 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Ralls | 0 | 65 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Holt | 0 | 49 | 3 | 3 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 75 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 77 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 92 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Madison | 0 | 46 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 192 | 2 | 3 | 2 |
| Kansas City | Missouri | Lafayette | 2 | 201 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Pike | 1 | 137 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 79 | 2 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 105 | 2 | 2 | 2 |
| Kansas City | Kansas | Miami | 0 | 165 | 2 | 3 | 2 |
| Springfield | Missouri | Dallas | 1 | 83 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 250 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 101 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | McDonald | 8 | 967 | 2 | 1 | 4 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 66 | 1 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 102 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 48 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 167 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Benton | 1 | 125 | 1 | 3 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 87 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 76 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 66 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 32 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 25 | 1 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 58 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 25 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 98 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 38 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 33 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 155 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 1 | 68 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 70 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 0 | 30 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 69 | 1 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 45 | 1 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 50 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 41 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 95 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Scotland | 1 | 20 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 56 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 38 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 74 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 36 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Livingston | 1 | 67 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 0 | 105 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 0 | 43 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 22 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 53 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 87 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 62 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 19 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 19 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 44 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 116 | 0 | 0 | 2 |
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
