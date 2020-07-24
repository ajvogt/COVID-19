# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 07/24/2020  
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
| St. Louis-Farmington | 1171 | 22864 | 540 | 464 | 331 |
| Kansas City | 322 | 17625 | 468 | 388 | 314 |
| Missouri non-MSA | 75 | 5923 | 164 | 139 | 110 |
| Springfield | 12 | 1126 | 53 | 40 | 27 |
| Joplin | 24 | 2073 | 47 | 42 | 48 |
| Columbia-Jefferson City | 8 | 1293 | 42 | 37 | 27 |
| Cape Girardeau-Sikeston | 16 | 864 | 24 | 24 | 18 |
| St. Joseph | 12 | 1137 | 11 | 7 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 626 | 9944 | 197 | 176 | 133 |
| Kansas City | Missouri | Kansas City | 43 | 4366 | 142 | 100 | 78 |
| Kansas City | Kansas | Johnson | 96 | 4161 | 105 | 109 | 94 |
| St. Louis-Farmington | Missouri | St. Charles | 79 | 2151 | 88 | 65 | 39 |
| Kansas City | Kansas | Wyandotte | 90 | 3894 | 82 | 78 | 66 |
| St. Louis-Farmington | Missouri | St. Louis City | 164 | 3733 | 77 | 65 | 47 |
| Kansas City | Missouri | Jackson | 50 | 2233 | 75 | 53 | 39 |
| St. Louis-Farmington | Illinois | St. Clair | 152 | 2951 | 66 | 58 | 44 |
| St. Louis-Farmington | Illinois | Madison | 71 | 1651 | 40 | 39 | 27 |
| Joplin | Missouri | Jasper | 21 | 1366 | 35 | 30 | 34 |
| St. Louis-Farmington | Missouri | Jefferson | 23 | 832 | 27 | 20 | 14 |
| Springfield | Missouri | Greene | 9 | 724 | 25 | 22 | 16 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 839 | 24 | 23 | 18 |
| Kansas City | Missouri | Cass | 8 | 372 | 19 | 13 | 8 |
| Springfield | Missouri | Polk | 0 | 137 | 16 | 8 | 4 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 509 | 15 | 15 | 12 |
| Missouri non-MSA | Missouri | Johnson | 1 | 397 | 14 | 13 | 10 |
| Kansas City | Missouri | Clay | 18 | 685 | 12 | 10 | 10 |
| Missouri non-MSA | Missouri | McDonald | 6 | 854 | 12 | 12 | 15 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 408 | 12 | 11 | 7 |
| Joplin | Missouri | Newton | 3 | 707 | 11 | 11 | 14 |
| Kansas City | Kansas | Leavenworth | 7 | 1310 | 10 | 8 | 5 |
| Missouri non-MSA | Missouri | Taney | 3 | 212 | 9 | 6 | 5 |
| Missouri non-MSA | Missouri | Camden | 3 | 151 | 9 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 196 | 9 | 6 | 4 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 185 | 8 | 5 | 3 |
| Kansas City | Missouri | Platte | 6 | 228 | 7 | 6 | 4 |
| Springfield | Missouri | Christian | 1 | 145 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Pettis | 3 | 232 | 6 | 6 | 4 |
| St. Joseph | Missouri | Buchanan | 10 | 1003 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Butler | 1 | 169 | 6 | 3 | 3 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 122 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Laclede | 1 | 162 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 3 | 176 | 5 | 4 | 3 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 216 | 5 | 3 | 4 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 272 | 5 | 5 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 103 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Saline | 6 | 359 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 122 | 4 | 5 | 2 |
| Missouri non-MSA | Missouri | Audrain | 1 | 178 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Barry | 0 | 179 | 4 | 6 | 4 |
| Missouri non-MSA | Missouri | Marion | 1 | 68 | 4 | 2 | 1 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 210 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 55 | 4 | 2 | 1 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 288 | 4 | 3 | 2 |
| Springfield | Missouri | Webster | 1 | 87 | 3 | 2 | 2 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 101 | 3 | 2 | 1 |
| Kansas City | Kansas | Miami | 0 | 92 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 121 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 6 | 173 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 185 | 3 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 29 | 3 | 1 | 0 |
| Kansas City | Missouri | Lafayette | 2 | 124 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Miller | 0 | 50 | 2 | 2 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 50 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 164 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Stone | 1 | 50 | 2 | 2 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 72 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Benton | 0 | 46 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Howell | 0 | 72 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 46 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Douglas | 1 | 36 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 87 | 2 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 39 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 28 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 29 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 36 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 54 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 116 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 52 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 38 | 1 | 0 | 0 |
| Kansas City | Missouri | Clinton | 0 | 46 | 1 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 33 | 1 | 1 | 0 |
| Kansas City | Missouri | Ray | 0 | 42 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Perry | 3 | 185 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Pike | 1 | 54 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Phelps | 0 | 61 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 44 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 0 | 37 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 10 | 1 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 24 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 33 | 1 | 0 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 57 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 41 | 1 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 24 | 1 | 0 | 0 |
| St. Louis-Farmington | Illinois | Bond | 1 | 30 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Crawford | 0 | 32 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 38 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 12 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 33 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 24 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 76 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 7 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 37 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 52 | 0 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Washington | 1 | 42 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 7 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 125 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 71 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 10 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 2 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 10 | 0 | 0 | 0 |
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
