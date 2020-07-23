# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 07/23/2020  
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
| St. Louis-Farmington | 1160 | 22097 | 504 | 441 | 310 |
| Kansas City | 314 | 16997 | 438 | 372 | 298 |
| Missouri non-MSA | 67 | 5654 | 148 | 128 | 104 |
| Springfield | 12 | 1055 | 49 | 37 | 25 |
| Joplin | 23 | 2022 | 46 | 44 | 49 |
| Columbia-Jefferson City | 7 | 1234 | 40 | 35 | 26 |
| Cape Girardeau-Sikeston | 16 | 841 | 25 | 24 | 17 |
| St. Joseph | 11 | 1127 | 10 | 7 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 615 | 9624 | 189 | 167 | 124 |
| Kansas City | Missouri | Kansas City | 42 | 4102 | 115 | 88 | 71 |
| Kansas City | Kansas | Johnson | 96 | 4053 | 109 | 111 | 92 |
| Kansas City | Kansas | Wyandotte | 90 | 3822 | 95 | 80 | 64 |
| St. Louis-Farmington | Missouri | St. Charles | 79 | 2012 | 73 | 58 | 35 |
| St. Louis-Farmington | Missouri | St. Louis City | 164 | 3635 | 71 | 67 | 43 |
| St. Louis-Farmington | Illinois | St. Clair | 152 | 2883 | 63 | 56 | 42 |
| Kansas City | Missouri | Jackson | 48 | 2115 | 62 | 48 | 36 |
| St. Louis-Farmington | Illinois | Madison | 71 | 1604 | 42 | 37 | 26 |
| Joplin | Missouri | Jasper | 20 | 1323 | 33 | 31 | 35 |
| Springfield | Missouri | Greene | 9 | 684 | 23 | 21 | 15 |
| Columbia-Jefferson City | Missouri | Boone | 2 | 800 | 23 | 23 | 17 |
| St. Louis-Farmington | Missouri | Jefferson | 23 | 789 | 22 | 18 | 12 |
| Kansas City | Missouri | Cass | 8 | 349 | 17 | 12 | 7 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 496 | 17 | 16 | 12 |
| Missouri non-MSA | Missouri | Johnson | 1 | 389 | 15 | 13 | 10 |
| Springfield | Missouri | Polk | 0 | 125 | 14 | 7 | 3 |
| Joplin | Missouri | Newton | 3 | 699 | 13 | 12 | 14 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 394 | 11 | 11 | 6 |
| Kansas City | Kansas | Leavenworth | 7 | 1310 | 10 | 8 | 5 |
| Missouri non-MSA | Missouri | McDonald | 1 | 824 | 9 | 11 | 15 |
| Kansas City | Missouri | Clay | 13 | 655 | 9 | 9 | 10 |
| Missouri non-MSA | Missouri | Taney | 3 | 205 | 9 | 6 | 5 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 186 | 8 | 6 | 4 |
| Kansas City | Missouri | Platte | 6 | 223 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Barry | 0 | 173 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Camden | 2 | 139 | 6 | 4 | 2 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 172 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 110 | 6 | 4 | 3 |
| St. Joseph | Missouri | Buchanan | 9 | 997 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Pettis | 2 | 206 | 5 | 4 | 3 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 214 | 5 | 4 | 4 |
| Springfield | Missouri | Christian | 1 | 128 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Laclede | 1 | 151 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 114 | 5 | 4 | 2 |
| St. Louis-Farmington | Missouri | Warren | 0 | 99 | 4 | 3 | 2 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 205 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Butler | 0 | 154 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 6 | 172 | 4 | 4 | 2 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 266 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Dunklin | 3 | 168 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Saline | 6 | 351 | 3 | 4 | 2 |
| Springfield | Missouri | Webster | 1 | 86 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Audrain | 1 | 168 | 3 | 1 | 1 |
| Kansas City | Kansas | Miami | 0 | 92 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 51 | 3 | 1 | 1 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 100 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 121 | 3 | 1 | 1 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 278 | 3 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 29 | 3 | 1 | 0 |
| Missouri non-MSA | Missouri | Marion | 1 | 58 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 83 | 2 | 1 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 122 | 2 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 47 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 43 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 162 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Douglas | 1 | 32 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Stone | 1 | 47 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 177 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 29 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Miller | 0 | 43 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Howell | 0 | 68 | 2 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 69 | 2 | 0 | 0 |
| Missouri non-MSA | Missouri | Adair | 0 | 117 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Washington | 1 | 41 | 1 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 39 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 34 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 27 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 53 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Benton | 0 | 38 | 1 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 32 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 51 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 37 | 1 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 24 | 1 | 0 | 0 |
| St. Louis-Farmington | Illinois | Bond | 1 | 29 | 1 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 39 | 1 | 0 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 56 | 1 | 1 | 0 |
| Kansas City | Missouri | Bates | 1 | 24 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Phelps | 0 | 60 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Perry | 3 | 184 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Wright | 0 | 52 | 1 | 1 | 1 |
| Kansas City | Missouri | Clinton | 0 | 43 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Crawford | 0 | 31 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 9 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 38 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Shannon | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 13 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 24 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pike | 1 | 49 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 125 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 36 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 37 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 71 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 41 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Texas | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 3 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Randolph | 1 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 8 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 71 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 5 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 3 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 3 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 7 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 9 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 11 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 14 | 0 | 0 | 0 |
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
