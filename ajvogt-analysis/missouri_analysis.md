# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/24/2020  
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
| St. Louis-Farmington | 1342 | 43792 | 587 | 637 | 667 |
| Kansas City | 420 | 31467 | 414 | 427 | 442 |
| Missouri non-MSA | 112 | 12614 | 210 | 229 | 215 |
| Springfield | 13 | 3416 | 86 | 81 | 73 |
| Columbia-Jefferson City | 13 | 3404 | 81 | 77 | 68 |
| Joplin | 46 | 3131 | 34 | 35 | 32 |
| Cape Girardeau-Sikeston | 20 | 1527 | 26 | 26 | 21 |
| St. Joseph | 12 | 1398 | 12 | 10 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 713 | 17872 | 179 | 220 | 251 |
| Kansas City | Kansas | Johnson | 110 | 7310 | 136 | 114 | 101 |
| Kansas City | Missouri | Kansas City | 66 | 8422 | 110 | 126 | 128 |
| St. Louis-Farmington | Missouri | St. Charles | 96 | 5219 | 81 | 83 | 94 |
| Kansas City | Missouri | Jackson | 71 | 5038 | 68 | 73 | 90 |
| Springfield | Missouri | Greene | 10 | 2365 | 66 | 60 | 52 |
| St. Louis-Farmington | Illinois | St. Clair | 166 | 4882 | 65 | 62 | 61 |
| St. Louis-Farmington | Illinois | Madison | 91 | 3562 | 64 | 69 | 62 |
| Kansas City | Kansas | Wyandotte | 111 | 5701 | 53 | 57 | 57 |
| St. Louis-Farmington | Missouri | Jefferson | 30 | 2269 | 46 | 48 | 46 |
| Columbia-Jefferson City | Missouri | Boone | 5 | 1917 | 46 | 38 | 35 |
| St. Louis-Farmington | Missouri | St. Louis City | 184 | 5907 | 41 | 50 | 70 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 806 | 33 | 31 | 19 |
| Joplin | Missouri | Jasper | 35 | 2113 | 23 | 25 | 22 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 719 | 18 | 22 | 17 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 863 | 17 | 17 | 14 |
| Kansas City | Missouri | Clay | 30 | 1261 | 16 | 16 | 19 |
| Missouri non-MSA | Missouri | Taney | 3 | 855 | 16 | 19 | 20 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 6 | 848 | 15 | 14 | 11 |
| Kansas City | Missouri | Cass | 9 | 961 | 14 | 15 | 18 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 582 | 13 | 12 | 9 |
| Springfield | Missouri | Christian | 1 | 529 | 12 | 12 | 12 |
| Missouri non-MSA | Missouri | Pettis | 5 | 736 | 12 | 16 | 16 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 223 | 10 | 8 | 5 |
| Joplin | Missouri | Newton | 11 | 1018 | 10 | 10 | 9 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 544 | 9 | 10 | 8 |
| Missouri non-MSA | Missouri | Marion | 1 | 335 | 9 | 10 | 8 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 497 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 331 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Washington | 1 | 191 | 8 | 8 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 445 | 8 | 9 | 8 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 253 | 7 | 6 | 5 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 296 | 7 | 8 | 6 |
| St. Joseph | Missouri | Buchanan | 10 | 1182 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Stone | 1 | 240 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Nodaway | 1 | 272 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Miller | 1 | 203 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 310 | 6 | 5 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 398 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Camden | 8 | 452 | 6 | 7 | 9 |
| St. Louis-Farmington | Missouri | Warren | 0 | 291 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 214 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 338 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Saline | 7 | 522 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 301 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Perry | 4 | 292 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Madison | 0 | 71 | 5 | 3 | 1 |
| Kansas City | Missouri | Platte | 10 | 441 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Butler | 2 | 351 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Crawford | 1 | 141 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Johnson | 3 | 543 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Barry | 4 | 322 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Ralls | 0 | 85 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Laclede | 1 | 263 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Phelps | 0 | 151 | 4 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 186 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Benton | 1 | 144 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Randolph | 1 | 108 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 207 | 3 | 3 | 3 |
| St. Louis-Farmington | Illinois | Bond | 3 | 104 | 3 | 3 | 2 |
| Springfield | Missouri | Polk | 0 | 261 | 3 | 3 | 3 |
| Kansas City | Kansas | Leavenworth | 9 | 1572 | 3 | 8 | 7 |
| Missouri non-MSA | Missouri | Howell | 2 | 198 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 90 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 262 | 2 | 2 | 2 |
| Springfield | Missouri | Webster | 1 | 173 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | McDonald | 9 | 976 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Monroe | 0 | 53 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 85 | 2 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 113 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 40 | 2 | 1 | 1 |
| Kansas City | Kansas | Miami | 0 | 167 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Audrain | 1 | 241 | 2 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 95 | 2 | 1 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 211 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 108 | 1 | 1 | 2 |
| Springfield | Missouri | Dallas | 1 | 88 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 58 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 106 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 0 | 51 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 1 | 78 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 174 | 1 | 2 | 3 |
| St. Joseph | Missouri | DeKalb | 1 | 51 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 47 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 0 | 55 | 1 | 3 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 30 | 1 | 1 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 107 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dent | 0 | 31 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 70 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 79 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 35 | 1 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 21 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 70 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 72 | 0 | 1 | 2 |
| Kansas City | Missouri | Bates | 1 | 60 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 160 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 79 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 78 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 33 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 48 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 1 | 68 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carroll | 0 | 107 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 1 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 97 | 0 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 39 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 38 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 0 | 44 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 43 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 18 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 121 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Macon | 0 | 71 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Grundy | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 88 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 10 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 50 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 62 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 53 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pike | 1 | 131 | -1 | 2 | 2 |
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
