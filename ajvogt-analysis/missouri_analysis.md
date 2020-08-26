# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/26/2020  
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
| St. Louis-Farmington | 1355 | 44817 | 572 | 628 | 644 |
| Kansas City | 424 | 31980 | 367 | 412 | 434 |
| Missouri non-MSA | 115 | 12917 | 212 | 225 | 216 |
| Springfield | 13 | 3602 | 91 | 84 | 76 |
| Columbia-Jefferson City | 15 | 3498 | 82 | 77 | 67 |
| Joplin | 46 | 3165 | 31 | 35 | 30 |
| Cape Girardeau-Sikeston | 20 | 1557 | 23 | 26 | 22 |
| St. Joseph | 12 | 1415 | 11 | 10 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 720 | 18210 | 177 | 209 | 233 |
| Kansas City | Kansas | Johnson | 112 | 7485 | 118 | 115 | 101 |
| Kansas City | Missouri | Kansas City | 66 | 8538 | 97 | 118 | 125 |
| St. Louis-Farmington | Missouri | St. Charles | 96 | 5338 | 75 | 79 | 89 |
| Springfield | Missouri | Greene | 10 | 2514 | 72 | 63 | 55 |
| St. Louis-Farmington | Illinois | St. Clair | 166 | 5010 | 65 | 64 | 61 |
| St. Louis-Farmington | Illinois | Madison | 92 | 3666 | 60 | 68 | 60 |
| Kansas City | Missouri | Jackson | 73 | 5116 | 57 | 68 | 86 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 1984 | 49 | 39 | 35 |
| St. Louis-Farmington | Missouri | Jefferson | 30 | 2351 | 46 | 49 | 46 |
| Kansas City | Kansas | Wyandotte | 111 | 5741 | 41 | 55 | 55 |
| St. Louis-Farmington | Missouri | St. Louis City | 187 | 5978 | 40 | 48 | 69 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 839 | 32 | 31 | 20 |
| Joplin | Missouri | Jasper | 35 | 2137 | 22 | 25 | 20 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 632 | 17 | 15 | 11 |
| Kansas City | Missouri | Clay | 30 | 1285 | 16 | 15 | 18 |
| Columbia-Jefferson City | Missouri | Cole | 4 | 729 | 16 | 20 | 16 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 889 | 15 | 17 | 14 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 6 | 868 | 13 | 14 | 11 |
| Missouri non-MSA | Missouri | Taney | 3 | 868 | 12 | 16 | 20 |
| Kansas City | Missouri | Cass | 9 | 975 | 12 | 14 | 17 |
| Missouri non-MSA | Missouri | Marion | 1 | 360 | 11 | 11 | 9 |
| Missouri non-MSA | Missouri | Pettis | 7 | 746 | 11 | 13 | 15 |
| Springfield | Missouri | Christian | 1 | 546 | 10 | 12 | 12 |
| St. Louis-Farmington | Illinois | Jersey | 3 | 239 | 9 | 8 | 6 |
| Joplin | Missouri | Newton | 11 | 1028 | 9 | 10 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 336 | 8 | 7 | 5 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 551 | 8 | 10 | 8 |
| Missouri non-MSA | Missouri | Nodaway | 1 | 297 | 8 | 7 | 6 |
| Kansas City | Kansas | Leavenworth | 9 | 1606 | 8 | 8 | 8 |
| St. Joseph | Missouri | Buchanan | 10 | 1197 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Camden | 8 | 471 | 8 | 7 | 8 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 510 | 8 | 8 | 9 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 260 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Washington | 1 | 200 | 7 | 8 | 5 |
| Missouri non-MSA | Missouri | Miller | 1 | 212 | 7 | 5 | 5 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 302 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 452 | 7 | 9 | 8 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 319 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Perry | 4 | 308 | 6 | 5 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 14 | 413 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Stone | 1 | 247 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Saline | 7 | 525 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 342 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Madison | 0 | 77 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Phelps | 0 | 164 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 214 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 308 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Crawford | 1 | 148 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Barry | 4 | 326 | 4 | 4 | 4 |
| St. Louis-Farmington | Missouri | Warren | 0 | 299 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Butler | 2 | 354 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Johnson | 3 | 551 | 4 | 4 | 4 |
| Kansas City | Missouri | Platte | 10 | 448 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Ralls | 0 | 91 | 4 | 4 | 2 |
| St. Louis-Farmington | Illinois | Bond | 3 | 117 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 273 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 147 | 4 | 2 | 3 |
| Missouri non-MSA | Missouri | Howell | 3 | 206 | 4 | 3 | 3 |
| Kansas City | Kansas | Miami | 0 | 177 | 3 | 3 | 2 |
| Springfield | Missouri | Webster | 1 | 185 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Laclede | 1 | 267 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Randolph | 1 | 110 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 188 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 97 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 209 | 2 | 3 | 3 |
| Springfield | Missouri | Polk | 0 | 264 | 2 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 90 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 56 | 2 | 1 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 217 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Audrain | 1 | 243 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | McDonald | 9 | 980 | 2 | 1 | 3 |
| Kansas City | Missouri | Clinton | 0 | 118 | 2 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 97 | 1 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 93 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 107 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 1 | 79 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 42 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 109 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 166 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 176 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Barton | 0 | 84 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 24 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 31 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 55 | 1 | 3 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 49 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 53 | 1 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 52 | 1 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 58 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 71 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 32 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 71 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 62 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 83 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 79 | 0 | 1 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 108 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 2 | 98 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 27 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 33 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Livingston | 1 | 69 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Grundy | 1 | 34 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 73 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Macon | 0 | 72 | 0 | 0 | 1 |
| Kansas City | Missouri | Ray | 0 | 122 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 107 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 49 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 89 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 45 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 38 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 54 | 0 | 0 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 41 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 19 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 62 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 50 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Pike | 1 | 132 | -1 | 1 | 2 |
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
