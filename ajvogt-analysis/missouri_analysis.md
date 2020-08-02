# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/01/2020  
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
| St. Louis-Farmington | 1214 | 29773 | 856 | 729 | 510 |
| Kansas City | 348 | 22081 | 556 | 520 | 405 |
| Missouri non-MSA | 89 | 7792 | 235 | 204 | 151 |
| Springfield | 13 | 1792 | 82 | 71 | 46 |
| Columbia-Jefferson City | 8 | 1834 | 70 | 55 | 42 |
| Joplin | 29 | 2420 | 37 | 43 | 50 |
| Cape Girardeau-Sikeston | 16 | 1027 | 21 | 22 | 21 |
| St. Joseph | 12 | 1211 | 8 | 9 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 650 | 12880 | 365 | 295 | 208 |
| Kansas City | Missouri | Kansas City | 51 | 5798 | 177 | 167 | 111 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 3432 | 148 | 132 | 78 |
| Kansas City | Missouri | Jackson | 57 | 3320 | 141 | 112 | 69 |
| St. Louis-Farmington | Missouri | St. Louis City | 169 | 4491 | 97 | 88 | 66 |
| Kansas City | Kansas | Johnson | 98 | 4883 | 86 | 94 | 102 |
| St. Louis-Farmington | Illinois | St. Clair | 155 | 3507 | 68 | 67 | 53 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1295 | 59 | 44 | 27 |
| St. Louis-Farmington | Illinois | Madison | 72 | 2099 | 57 | 49 | 38 |
| Kansas City | Kansas | Wyandotte | 95 | 4373 | 57 | 67 | 67 |
| Springfield | Missouri | Greene | 10 | 1182 | 56 | 43 | 29 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1152 | 41 | 32 | 26 |
| Kansas City | Missouri | Cass | 9 | 621 | 32 | 27 | 16 |
| Kansas City | Missouri | Clay | 19 | 882 | 27 | 19 | 14 |
| Joplin | Missouri | Jasper | 24 | 1626 | 27 | 32 | 38 |
| Missouri non-MSA | Missouri | Taney | 3 | 391 | 23 | 16 | 10 |
| Missouri non-MSA | Missouri | Pettis | 3 | 405 | 22 | 15 | 9 |
| Missouri non-MSA | Missouri | Camden | 4 | 285 | 17 | 13 | 7 |
| Springfield | Missouri | Christian | 1 | 265 | 15 | 11 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 288 | 12 | 11 | 6 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 509 | 12 | 12 | 10 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 288 | 11 | 10 | 7 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 594 | 11 | 13 | 14 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 147 | 11 | 8 | 4 |
| Kansas City | Missouri | Platte | 7 | 301 | 10 | 7 | 6 |
| Joplin | Missouri | Newton | 5 | 794 | 10 | 11 | 12 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 285 | 9 | 7 | 4 |
| Missouri non-MSA | Missouri | Marion | 1 | 139 | 9 | 7 | 4 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 342 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Butler | 2 | 236 | 8 | 7 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 182 | 8 | 6 | 4 |
| Kansas City | Kansas | Leavenworth | 8 | 1392 | 7 | 10 | 7 |
| Missouri non-MSA | Missouri | Howell | 1 | 127 | 7 | 4 | 2 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 261 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 239 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | McDonald | 7 | 925 | 6 | 10 | 11 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 171 | 6 | 5 | 4 |
| St. Joseph | Missouri | Buchanan | 10 | 1054 | 6 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 86 | 6 | 3 | 2 |
| Missouri non-MSA | Missouri | Johnson | 2 | 454 | 6 | 9 | 11 |
| Springfield | Missouri | Polk | 0 | 187 | 6 | 11 | 5 |
| Missouri non-MSA | Missouri | Saline | 7 | 407 | 6 | 5 | 4 |
| Kansas City | Missouri | Ray | 0 | 87 | 6 | 3 | 2 |
| St. Louis-Farmington | Missouri | Warren | 0 | 153 | 5 | 5 | 3 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 330 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Barry | 0 | 218 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Carroll | 0 | 95 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Miller | 0 | 89 | 4 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 111 | 4 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 118 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 2 | 68 | 4 | 3 | 2 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 127 | 3 | 3 | 2 |
| Kansas City | Missouri | Lafayette | 2 | 150 | 3 | 3 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 52 | 3 | 2 | 1 |
| Kansas City | Kansas | Miami | 0 | 117 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Henry | 3 | 69 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 8 | 199 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Stone | 1 | 80 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 31 | 3 | 1 | 0 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 208 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 62 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Laclede | 1 | 188 | 2 | 4 | 5 |
| Springfield | Missouri | Webster | 1 | 111 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 71 | 2 | 3 | 1 |
| Missouri non-MSA | Missouri | Livingston | 0 | 51 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Crawford | 0 | 47 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 132 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 52 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Perry | 4 | 201 | 2 | 1 | 1 |
| St. Louis-Farmington | Illinois | Bond | 2 | 48 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 59 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 1 | 27 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Audrain | 1 | 192 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Pike | 1 | 68 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Washington | 1 | 55 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 72 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 0 | 32 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 65 | 1 | 1 | 1 |
| Springfield | Missouri | Dallas | 1 | 47 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 178 | 1 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 61 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 46 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 134 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 43 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 11 | 1 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 81 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 18 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 129 | 1 | 2 | 1 |
| Kansas City | Missouri | Bates | 1 | 36 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 16 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 33 | 1 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 32 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 17 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 56 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 9 | 79 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 34 | 0 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 41 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 14 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 36 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 56 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 62 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 8 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 43 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 11 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 14 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 44 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 11 | 0 | 0 | 0 |
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
