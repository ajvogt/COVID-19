# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 07/31/2020  
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
| St. Louis-Farmington | 1211 | 28926 | 866 | 703 | 485 |
| Kansas City | 345 | 21579 | 564 | 516 | 399 |
| Missouri non-MSA | 86 | 7549 | 232 | 198 | 144 |
| Springfield | 13 | 1714 | 84 | 68 | 43 |
| Columbia-Jefferson City | 8 | 1757 | 66 | 54 | 40 |
| Joplin | 27 | 2389 | 45 | 46 | 51 |
| Cape Girardeau-Sikeston | 16 | 998 | 19 | 21 | 21 |
| St. Joseph | 12 | 1204 | 9 | 10 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 648 | 12548 | 372 | 284 | 198 |
| Kansas City | Missouri | Kansas City | 49 | 5672 | 186 | 164 | 109 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 3288 | 162 | 125 | 74 |
| Kansas City | Missouri | Jackson | 56 | 3189 | 136 | 106 | 65 |
| St. Louis-Farmington | Missouri | St. Louis City | 169 | 4411 | 96 | 86 | 63 |
| Kansas City | Kansas | Johnson | 98 | 4781 | 88 | 97 | 102 |
| St. Louis-Farmington | Illinois | St. Clair | 154 | 3419 | 66 | 66 | 51 |
| Kansas City | Kansas | Wyandotte | 95 | 4325 | 61 | 71 | 69 |
| Springfield | Missouri | Greene | 10 | 1126 | 57 | 41 | 27 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1231 | 57 | 42 | 25 |
| St. Louis-Farmington | Illinois | Madison | 72 | 2047 | 56 | 48 | 37 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1125 | 40 | 32 | 25 |
| Joplin | Missouri | Jasper | 23 | 1608 | 34 | 34 | 38 |
| Kansas City | Missouri | Cass | 9 | 592 | 31 | 25 | 15 |
| Kansas City | Missouri | Clay | 19 | 857 | 24 | 18 | 13 |
| Missouri non-MSA | Missouri | Taney | 3 | 374 | 23 | 16 | 10 |
| Missouri non-MSA | Missouri | Pettis | 3 | 382 | 21 | 14 | 8 |
| Missouri non-MSA | Missouri | Camden | 4 | 277 | 18 | 13 | 7 |
| Springfield | Missouri | Christian | 1 | 249 | 14 | 11 | 6 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 272 | 12 | 10 | 5 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 490 | 11 | 11 | 9 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 137 | 11 | 7 | 3 |
| Joplin | Missouri | Newton | 4 | 781 | 10 | 11 | 12 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 269 | 10 | 9 | 6 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 578 | 9 | 12 | 13 |
| Kansas City | Missouri | Platte | 7 | 295 | 9 | 8 | 5 |
| Kansas City | Kansas | Leavenworth | 8 | 1376 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | McDonald | 7 | 916 | 8 | 10 | 11 |
| Missouri non-MSA | Missouri | Marion | 1 | 127 | 8 | 6 | 3 |
| Missouri non-MSA | Missouri | Butler | 2 | 227 | 8 | 7 | 4 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 330 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 234 | 8 | 6 | 4 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 272 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Howell | 1 | 123 | 7 | 4 | 2 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 172 | 7 | 6 | 4 |
| Springfield | Missouri | Polk | 0 | 186 | 7 | 11 | 5 |
| Missouri non-MSA | Missouri | Johnson | 1 | 445 | 6 | 10 | 10 |
| St. Joseph | Missouri | Buchanan | 10 | 1049 | 6 | 6 | 6 |
| St. Louis-Farmington | Missouri | Warren | 0 | 144 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Saline | 6 | 399 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 161 | 5 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 77 | 5 | 3 | 2 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 248 | 5 | 4 | 4 |
| Kansas City | Missouri | Ray | 0 | 79 | 5 | 3 | 1 |
| Missouri non-MSA | Missouri | Carroll | 0 | 89 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 0 | 213 | 4 | 4 | 5 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 321 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Miller | 0 | 82 | 4 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 106 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Stone | 1 | 79 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Douglas | 2 | 61 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 50 | 3 | 2 | 1 |
| Kansas City | Kansas | Miami | 0 | 117 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Laclede | 1 | 187 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Morgan | 0 | 61 | 3 | 2 | 1 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 123 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 8 | 194 | 3 | 3 | 2 |
| Kansas City | Missouri | Lafayette | 2 | 145 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Benton | 1 | 66 | 2 | 2 | 1 |
| Springfield | Missouri | Webster | 1 | 107 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 205 | 2 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 106 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Henry | 3 | 64 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 58 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 24 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 47 | 2 | 1 | 1 |
| St. Louis-Farmington | Illinois | Bond | 2 | 45 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 130 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 1 | 67 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 42 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Texas | 0 | 31 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 26 | 1 | 1 | 0 |
| Kansas City | Missouri | Clinton | 0 | 59 | 1 | 1 | 1 |
| Springfield | Missouri | Dallas | 1 | 46 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 45 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 176 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 64 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 190 | 1 | 3 | 1 |
| Missouri non-MSA | Missouri | Washington | 1 | 54 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 9 | 82 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 47 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 34 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 16 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Perry | 4 | 194 | 1 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 31 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 24 | 1 | 1 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 80 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 129 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 69 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Crawford | 0 | 40 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 33 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 132 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 43 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 34 | 0 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 44 | 0 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 29 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 55 | 0 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 19 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 32 | 0 | 1 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 61 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 39 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 0 | 7 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 54 | 0 | 0 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 11 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
