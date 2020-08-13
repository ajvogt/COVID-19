# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/13/2020  
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
| St. Louis-Farmington | 1262 | 36689 | 569 | 639 | 635 |
| Kansas City | 393 | 26821 | 405 | 423 | 448 |
| Missouri non-MSA | 103 | 10102 | 207 | 206 | 194 |
| Springfield | 13 | 2505 | 67 | 65 | 62 |
| Columbia-Jefferson City | 10 | 2483 | 53 | 58 | 53 |
| Joplin | 37 | 2754 | 32 | 27 | 39 |
| Cape Girardeau-Sikeston | 19 | 1222 | 22 | 18 | 21 |
| St. Joseph | 12 | 1281 | 6 | 6 | 7 |
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
| St. Louis-Farmington | Missouri | St. Louis | 672 | 15485 | 201 | 247 | 252 |
| Kansas City | Missouri | Kansas City | 65 | 7077 | 115 | 117 | 130 |
| Kansas City | Kansas | Johnson | 106 | 6009 | 98 | 92 | 97 |
| Kansas City | Missouri | Jackson | 66 | 4272 | 79 | 93 | 88 |
| St. Louis-Farmington | Missouri | St. Louis City | 178 | 5364 | 72 | 80 | 79 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 4316 | 67 | 86 | 98 |
| St. Louis-Farmington | Illinois | Madison | 78 | 2777 | 65 | 57 | 50 |
| St. Louis-Farmington | Illinois | St. Clair | 162 | 4155 | 57 | 58 | 60 |
| Kansas City | Kansas | Wyandotte | 102 | 5031 | 51 | 54 | 64 |
| Springfield | Missouri | Greene | 10 | 1686 | 48 | 46 | 40 |
| St. Louis-Farmington | Missouri | Jefferson | 26 | 1730 | 34 | 42 | 37 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1457 | 24 | 27 | 28 |
| Missouri non-MSA | Missouri | Taney | 3 | 658 | 21 | 25 | 17 |
| Joplin | Missouri | Jasper | 31 | 1838 | 20 | 17 | 27 |
| Missouri non-MSA | Missouri | Pettis | 4 | 580 | 18 | 16 | 14 |
| Kansas City | Missouri | Clay | 22 | 1087 | 16 | 18 | 17 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 460 | 15 | 15 | 11 |
| Kansas City | Missouri | Cass | 9 | 785 | 15 | 16 | 19 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 669 | 14 | 13 | 12 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 421 | 12 | 11 | 8 |
| Joplin | Missouri | Newton | 6 | 916 | 11 | 9 | 11 |
| Springfield | Missouri | Christian | 1 | 392 | 11 | 11 | 10 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 5 | 689 | 10 | 8 | 11 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 412 | 9 | 11 | 9 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 269 | 9 | 8 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 421 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 336 | 8 | 7 | 6 |
| Kansas City | Kansas | Leavenworth | 9 | 1503 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Marion | 1 | 223 | 8 | 8 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 200 | 8 | 5 | 4 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 249 | 8 | 5 | 3 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 419 | 7 | 7 | 5 |
| Kansas City | Missouri | Platte | 10 | 385 | 7 | 7 | 7 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 122 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Camden | 6 | 370 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Stone | 1 | 150 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Pike | 1 | 120 | 5 | 3 | 2 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 332 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 240 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Saline | 7 | 459 | 5 | 5 | 4 |
| St. Joseph | Missouri | Buchanan | 10 | 1106 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Butler | 2 | 289 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Benton | 1 | 113 | 5 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 140 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 174 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Perry | 4 | 244 | 4 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 163 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Miller | 1 | 137 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Washington | 1 | 94 | 4 | 3 | 2 |
| Kansas City | Kansas | Miami | 0 | 150 | 3 | 2 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 212 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Johnson | 3 | 499 | 3 | 4 | 8 |
| Missouri non-MSA | Missouri | Barry | 4 | 266 | 3 | 3 | 5 |
| Springfield | Missouri | Polk | 0 | 219 | 3 | 2 | 6 |
| Kansas City | Missouri | Clinton | 0 | 90 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 190 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Holt | 0 | 27 | 3 | 1 | 0 |
| Missouri non-MSA | Missouri | Phelps | 0 | 100 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Crawford | 0 | 83 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 236 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 155 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 42 | 2 | 1 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 183 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 62 | 2 | 3 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 243 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Henry | 3 | 89 | 2 | 1 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 75 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Howell | 2 | 159 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Texas | 0 | 60 | 2 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 68 | 2 | 1 | 1 |
| Springfield | Missouri | Webster | 1 | 140 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Lewis | 1 | 50 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 148 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 74 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 35 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 87 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Laclede | 1 | 209 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | McDonald | 8 | 953 | 1 | 3 | 8 |
| Missouri non-MSA | Missouri | Ripley | 0 | 58 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 62 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 0 | 40 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Livingston | 0 | 63 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Madison | 0 | 28 | 1 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 51 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 33 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 29 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 56 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Audrain | 1 | 207 | 1 | 1 | 2 |
| Kansas City | Missouri | Ray | 0 | 119 | 1 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 55 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 32 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 147 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 23 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 65 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 15 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 53 | 1 | 1 | 1 |
| Kansas City | Kansas | Linn | 0 | 43 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 62 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 24 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 89 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 0 | 41 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Bond | 3 | 64 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 70 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carroll | 0 | 102 | 0 | 1 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 11 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 38 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 85 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 16 | 0 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 89 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 21 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 48 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 42 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 10 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 13 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 44 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 9 | 0 | 0 | 0 |
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
