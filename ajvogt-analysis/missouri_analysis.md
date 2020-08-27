# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/27/2020  
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
| St. Louis-Farmington | 1360 | 45370 | 568 | 620 | 637 |
| Kansas City | 432 | 32515 | 394 | 406 | 434 |
| Missouri non-MSA | 119 | 13236 | 218 | 223 | 220 |
| Springfield | 13 | 3721 | 92 | 86 | 77 |
| Columbia-Jefferson City | 15 | 3672 | 91 | 84 | 72 |
| Joplin | 47 | 3202 | 31 | 32 | 30 |
| Cape Girardeau-Sikeston | 21 | 1605 | 23 | 27 | 22 |
| St. Joseph | 12 | 1441 | 11 | 11 | 9 |
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
| St. Louis-Farmington | Missouri | St. Louis | 721 | 18334 | 177 | 203 | 227 |
| Kansas City | Kansas | Johnson | 116 | 7604 | 124 | 113 | 102 |
| Kansas City | Missouri | Kansas City | 66 | 8686 | 102 | 114 | 124 |
| Springfield | Missouri | Greene | 10 | 2585 | 70 | 64 | 55 |
| St. Louis-Farmington | Illinois | Madison | 92 | 3752 | 66 | 69 | 61 |
| St. Louis-Farmington | Missouri | St. Charles | 96 | 5392 | 63 | 76 | 87 |
| St. Louis-Farmington | Illinois | St. Clair | 168 | 5058 | 61 | 64 | 61 |
| Kansas City | Missouri | Jackson | 75 | 5184 | 60 | 65 | 86 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 2097 | 56 | 45 | 38 |
| Kansas City | Kansas | Wyandotte | 113 | 5850 | 49 | 58 | 57 |
| St. Louis-Farmington | Missouri | Jefferson | 31 | 2417 | 47 | 49 | 46 |
| St. Louis-Farmington | Missouri | St. Louis City | 188 | 6015 | 41 | 46 | 65 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 873 | 30 | 32 | 21 |
| Joplin | Missouri | Jasper | 34 | 2162 | 21 | 23 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 922 | 18 | 18 | 15 |
| Kansas City | Missouri | Clay | 30 | 1309 | 18 | 15 | 18 |
| Columbia-Jefferson City | Missouri | Cole | 4 | 758 | 17 | 21 | 17 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 647 | 17 | 16 | 11 |
| Kansas City | Missouri | Cass | 9 | 998 | 13 | 15 | 17 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 7 | 893 | 13 | 14 | 11 |
| Springfield | Missouri | Christian | 1 | 576 | 12 | 13 | 12 |
| Missouri non-MSA | Missouri | Taney | 3 | 879 | 11 | 15 | 20 |
| Missouri non-MSA | Missouri | Nodaway | 1 | 319 | 10 | 9 | 7 |
| St. Louis-Farmington | Illinois | Jersey | 3 | 246 | 10 | 8 | 6 |
| Missouri non-MSA | Missouri | Marion | 1 | 365 | 10 | 10 | 9 |
| Missouri non-MSA | Missouri | Pettis | 8 | 754 | 10 | 12 | 15 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 360 | 9 | 7 | 6 |
| Joplin | Missouri | Newton | 13 | 1040 | 9 | 8 | 9 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 324 | 9 | 8 | 7 |
| Kansas City | Kansas | Leavenworth | 9 | 1624 | 9 | 8 | 8 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 276 | 9 | 8 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 14 | 429 | 8 | 6 | 6 |
| St. Joseph | Missouri | Buchanan | 10 | 1215 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Washington | 1 | 212 | 8 | 8 | 5 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 514 | 7 | 7 | 9 |
| Missouri non-MSA | Missouri | Camden | 8 | 481 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Miller | 1 | 218 | 7 | 5 | 5 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 565 | 7 | 10 | 9 |
| Missouri non-MSA | Missouri | Perry | 4 | 324 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Phelps | 0 | 175 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 464 | 6 | 9 | 8 |
| Missouri non-MSA | Missouri | Stone | 2 | 252 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 4 | 358 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Crawford | 1 | 159 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Madison | 0 | 84 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Johnson | 3 | 560 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 323 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 311 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Saline | 7 | 530 | 4 | 5 | 5 |
| Kansas City | Missouri | Platte | 10 | 454 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Butler | 2 | 358 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 216 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Howell | 3 | 214 | 4 | 3 | 3 |
| Springfield | Missouri | Webster | 1 | 194 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Barry | 4 | 335 | 4 | 4 | 4 |
| St. Louis-Farmington | Missouri | Warren | 0 | 303 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 277 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 152 | 3 | 2 | 3 |
| St. Louis-Farmington | Illinois | Bond | 3 | 119 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 92 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Laclede | 1 | 271 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Monroe | 0 | 62 | 3 | 2 | 1 |
| Kansas City | Kansas | Miami | 0 | 188 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 193 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Randolph | 1 | 114 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 96 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 99 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 212 | 2 | 2 | 3 |
| Kansas City | Missouri | Lafayette | 2 | 220 | 2 | 2 | 2 |
| Springfield | Missouri | Polk | 0 | 267 | 2 | 3 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 105 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Texas | 1 | 85 | 2 | 1 | 2 |
| Kansas City | Missouri | Clinton | 0 | 121 | 2 | 2 | 2 |
| Springfield | Missouri | Dallas | 1 | 99 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | McDonald | 9 | 981 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Barton | 0 | 88 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 52 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 169 | 2 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 114 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 245 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Henry | 3 | 110 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 179 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 113 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Vernon | 0 | 77 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 43 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 34 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 85 | 1 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 54 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 33 | 1 | 1 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 25 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 73 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 84 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 76 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Douglas | 2 | 101 | 0 | 0 | 1 |
| Kansas City | Missouri | Bates | 1 | 62 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Holt | 0 | 55 | 0 | 2 | 1 |
| Kansas City | Missouri | Ray | 0 | 122 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Linn | 1 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 53 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 51 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 34 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Livingston | 1 | 71 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 34 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 22 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 53 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 72 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 1 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 46 | 0 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 107 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 24 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 42 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 89 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 38 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 2 | 54 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 62 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 58 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pike | 1 | 133 | 0 | 0 | 2 |
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
