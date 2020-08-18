# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/18/2020  
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
| St. Louis-Farmington | 1316 | 40232 | 707 | 639 | 672 |
| Kansas City | 409 | 29110 | 461 | 428 | 463 |
| Missouri non-MSA | 106 | 11303 | 239 | 214 | 205 |
| Springfield | 13 | 2871 | 74 | 69 | 66 |
| Columbia-Jefferson City | 10 | 2868 | 72 | 62 | 58 |
| Joplin | 38 | 2930 | 40 | 33 | 35 |
| Cape Girardeau-Sikeston | 20 | 1384 | 30 | 23 | 21 |
| St. Joseph | 12 | 1336 | 10 | 8 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 701 | 16764 | 260 | 235 | 263 |
| Kansas City | Missouri | Kansas City | 66 | 7773 | 141 | 124 | 140 |
| Kansas City | Kansas | Johnson | 108 | 6582 | 111 | 102 | 97 |
| St. Louis-Farmington | Missouri | St. Charles | 95 | 4760 | 91 | 80 | 102 |
| Kansas City | Missouri | Jackson | 66 | 4640 | 79 | 78 | 94 |
| St. Louis-Farmington | Illinois | Madison | 85 | 3152 | 74 | 66 | 56 |
| Kansas City | Kansas | Wyandotte | 107 | 5405 | 69 | 62 | 62 |
| St. Louis-Farmington | Illinois | St. Clair | 162 | 4484 | 65 | 59 | 61 |
| St. Louis-Farmington | Missouri | St. Louis City | 181 | 5652 | 59 | 70 | 77 |
| St. Louis-Farmington | Missouri | Jefferson | 30 | 1998 | 52 | 43 | 43 |
| Springfield | Missouri | Greene | 10 | 1940 | 52 | 48 | 44 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 599 | 31 | 20 | 13 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1610 | 30 | 26 | 29 |
| Joplin | Missouri | Jasper | 32 | 1968 | 28 | 22 | 24 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 597 | 24 | 19 | 14 |
| Missouri non-MSA | Missouri | Taney | 3 | 763 | 21 | 21 | 19 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 762 | 18 | 15 | 13 |
| Kansas City | Missouri | Cass | 9 | 883 | 18 | 16 | 21 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 6 | 770 | 15 | 11 | 11 |
| Missouri non-MSA | Missouri | Pettis | 5 | 656 | 15 | 15 | 15 |
| Kansas City | Missouri | Clay | 30 | 1158 | 15 | 17 | 18 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 492 | 13 | 10 | 8 |
| Springfield | Missouri | Christian | 1 | 453 | 12 | 11 | 11 |
| Joplin | Missouri | Newton | 6 | 962 | 12 | 11 | 10 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 492 | 11 | 10 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 398 | 11 | 10 | 8 |
| Missouri non-MSA | Missouri | Marion | 1 | 272 | 10 | 8 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 449 | 9 | 9 | 10 |
| Kansas City | Kansas | Leavenworth | 9 | 1548 | 9 | 8 | 9 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 245 | 9 | 7 | 5 |
| Missouri non-MSA | Missouri | Washington | 1 | 143 | 8 | 6 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 264 | 8 | 6 | 6 |
| Missouri non-MSA | Missouri | Stone | 1 | 196 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Camden | 7 | 412 | 8 | 7 | 10 |
| St. Joseph | Missouri | Buchanan | 10 | 1141 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 275 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 304 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Saline | 7 | 483 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 232 | 6 | 5 | 6 |
| Kansas City | Missouri | Platte | 10 | 412 | 6 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 202 | 6 | 5 | 4 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 157 | 6 | 6 | 3 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 271 | 5 | 5 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 358 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Pike | 1 | 145 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Phelps | 0 | 128 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Butler | 2 | 321 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Holt | 0 | 46 | 5 | 2 | 1 |
| Missouri non-MSA | Missouri | Barry | 4 | 296 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Crawford | 0 | 115 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Laclede | 1 | 238 | 5 | 2 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 268 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 174 | 4 | 3 | 2 |
| Springfield | Missouri | Polk | 0 | 243 | 4 | 3 | 6 |
| Missouri non-MSA | Missouri | Perry | 4 | 263 | 4 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 162 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Johnson | 3 | 517 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Miller | 1 | 159 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Adair | 0 | 184 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 58 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Howell | 2 | 177 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Audrain | 1 | 226 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ripley | 0 | 74 | 3 | 2 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 199 | 3 | 2 | 2 |
| Springfield | Missouri | Webster | 1 | 157 | 2 | 2 | 2 |
| St. Louis-Farmington | Illinois | Bond | 3 | 82 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 71 | 2 | 1 | 1 |
| Kansas City | Missouri | Clinton | 0 | 101 | 2 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 164 | 2 | 2 | 3 |
| Kansas City | Kansas | Miami | 0 | 150 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 98 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 72 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Benton | 1 | 118 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 38 | 2 | 1 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 82 | 2 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 101 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 1 | 68 | 1 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 62 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Madison | 0 | 38 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 244 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Henry | 3 | 95 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 84 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 68 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 155 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 73 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | McDonald | 8 | 962 | 1 | 1 | 5 |
| Missouri non-MSA | Missouri | Dent | 0 | 23 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 63 | 1 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 50 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 43 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 69 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 29 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 36 | 1 | 1 | 1 |
| Springfield | Missouri | Dallas | 1 | 78 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 25 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 41 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 54 | 1 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 44 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 31 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 94 | 1 | 0 | 2 |
| Missouri non-MSA | Missouri | Monroe | 0 | 37 | 0 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 54 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 43 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 73 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 104 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 21 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 62 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 50 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 87 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 65 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 14 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 36 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 119 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 23 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
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
