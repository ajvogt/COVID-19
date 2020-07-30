# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 07/30/2020  
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
| St. Louis-Farmington | 1203 | 27739 | 806 | 655 | 453 |
| Kansas City | 339 | 20887 | 555 | 497 | 381 |
| Missouri non-MSA | 79 | 7217 | 223 | 185 | 137 |
| Springfield | 13 | 1591 | 76 | 62 | 40 |
| Columbia-Jefferson City | 8 | 1668 | 62 | 51 | 37 |
| Joplin | 27 | 2370 | 49 | 48 | 51 |
| Cape Girardeau-Sikeston | 16 | 966 | 17 | 21 | 20 |
| St. Joseph | 12 | 1192 | 9 | 9 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 646 | 12018 | 342 | 265 | 185 |
| Kansas City | Missouri | Kansas City | 49 | 5428 | 189 | 152 | 102 |
| St. Louis-Farmington | Missouri | St. Charles | 84 | 3111 | 157 | 115 | 69 |
| Kansas City | Missouri | Jackson | 55 | 2957 | 120 | 91 | 59 |
| Kansas City | Kansas | Johnson | 96 | 4717 | 94 | 102 | 102 |
| St. Louis-Farmington | Missouri | St. Louis City | 167 | 4236 | 85 | 78 | 59 |
| St. Louis-Farmington | Illinois | St. Clair | 154 | 3340 | 65 | 64 | 49 |
| Kansas City | Kansas | Wyandotte | 93 | 4268 | 63 | 79 | 67 |
| St. Louis-Farmington | Illinois | Madison | 71 | 1975 | 53 | 47 | 34 |
| Springfield | Missouri | Greene | 10 | 1030 | 49 | 36 | 24 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1133 | 49 | 35 | 22 |
| Joplin | Missouri | Jasper | 23 | 1592 | 38 | 35 | 38 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1069 | 38 | 30 | 24 |
| Kansas City | Missouri | Cass | 8 | 559 | 30 | 23 | 14 |
| Kansas City | Missouri | Clay | 19 | 826 | 24 | 16 | 12 |
| Missouri non-MSA | Missouri | Pettis | 3 | 351 | 20 | 13 | 7 |
| Missouri non-MSA | Missouri | Camden | 3 | 262 | 17 | 12 | 6 |
| Springfield | Missouri | Christian | 1 | 230 | 14 | 10 | 6 |
| Missouri non-MSA | Missouri | Taney | 3 | 304 | 14 | 11 | 8 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 484 | 12 | 11 | 9 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 258 | 12 | 9 | 5 |
| Missouri non-MSA | Missouri | McDonald | 7 | 910 | 12 | 10 | 12 |
| Joplin | Missouri | Newton | 4 | 778 | 11 | 12 | 13 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 125 | 10 | 7 | 3 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 565 | 9 | 13 | 13 |
| Kansas City | Kansas | Leavenworth | 8 | 1376 | 9 | 9 | 7 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 250 | 9 | 8 | 5 |
| Missouri non-MSA | Missouri | Butler | 2 | 215 | 8 | 6 | 3 |
| Kansas City | Missouri | Platte | 7 | 283 | 8 | 7 | 5 |
| Missouri non-MSA | Missouri | Dunklin | 3 | 228 | 8 | 6 | 4 |
| Springfield | Missouri | Polk | 0 | 184 | 8 | 11 | 5 |
| Missouri non-MSA | Missouri | Marion | 1 | 111 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Howell | 0 | 121 | 7 | 4 | 2 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 159 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Johnson | 1 | 437 | 6 | 11 | 10 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 261 | 6 | 6 | 4 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 313 | 6 | 5 | 4 |
| St. Joseph | Missouri | Buchanan | 10 | 1039 | 6 | 6 | 5 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 319 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Barry | 0 | 213 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Miller | 0 | 81 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Saline | 6 | 389 | 5 | 4 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 136 | 5 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 73 | 5 | 2 | 1 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 149 | 5 | 5 | 3 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 239 | 4 | 4 | 3 |
| Kansas City | Missouri | Ray | 0 | 72 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Laclede | 1 | 184 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Carroll | 0 | 84 | 4 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 102 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Benton | 1 | 63 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 202 | 3 | 2 | 2 |
| Kansas City | Kansas | Miami | 0 | 117 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Randolph | 1 | 48 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 2 | 56 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Stone | 1 | 71 | 3 | 2 | 1 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 122 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 6 | 192 | 2 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 102 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 62 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 187 | 2 | 3 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 55 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 0 | 47 | 2 | 1 | 1 |
| Springfield | Missouri | Webster | 1 | 103 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Pike | 1 | 65 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 53 | 2 | 1 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 137 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Lewis | 1 | 28 | 2 | 1 | 0 |
| Kansas City | Missouri | Clinton | 0 | 57 | 2 | 1 | 1 |
| St. Louis-Farmington | Illinois | Bond | 2 | 42 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 17 | 1 | 0 | 0 |
| Springfield | Missouri | Dallas | 1 | 44 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 174 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 43 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 15 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 40 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 47 | 1 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 80 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 62 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 128 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 9 | 81 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Washington | 1 | 50 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Texas | 0 | 25 | 1 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 32 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 23 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 128 | 1 | 2 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 29 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 31 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Perry | 3 | 191 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 53 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 0 | 41 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 66 | 0 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 44 | 0 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 15 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 32 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 46 | 0 | 0 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 29 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 130 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Crawford | 0 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 38 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 11 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 55 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 32 | 0 | 1 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 59 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 7 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 3 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 14 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
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
