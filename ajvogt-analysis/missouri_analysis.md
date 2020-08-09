# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/09/2020  
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
| St. Louis-Farmington | 1244 | 34328 | 561 | 691 | 599 |
| Kansas City | 380 | 25028 | 376 | 452 | 427 |
| Missouri non-MSA | 98 | 9080 | 160 | 197 | 170 |
| Springfield | 13 | 2172 | 49 | 63 | 53 |
| Columbia-Jefferson City | 10 | 2195 | 38 | 57 | 47 |
| Joplin | 36 | 2606 | 23 | 27 | 37 |
| Cape Girardeau-Sikeston | 19 | 1118 | 12 | 16 | 19 |
| St. Joseph | 12 | 1247 | 4 | 6 | 7 |
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
| St. Louis-Farmington | Missouri | St. Louis | 663 | 14666 | 214 | 284 | 239 |
| Kansas City | Kansas | Johnson | 103 | 5643 | 89 | 89 | 100 |
| Kansas City | Missouri | Kansas City | 61 | 6476 | 87 | 125 | 117 |
| St. Louis-Farmington | Missouri | St. Louis City | 174 | 5139 | 80 | 88 | 77 |
| Kansas City | Missouri | Jackson | 64 | 3909 | 73 | 105 | 80 |
| Kansas City | Kansas | Wyandotte | 99 | 4864 | 70 | 57 | 69 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 3954 | 63 | 100 | 90 |
| St. Louis-Farmington | Illinois | Madison | 76 | 2530 | 56 | 54 | 47 |
| St. Louis-Farmington | Illinois | St. Clair | 161 | 3953 | 54 | 60 | 60 |
| Springfield | Missouri | Greene | 10 | 1440 | 33 | 43 | 34 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1544 | 30 | 43 | 33 |
| Missouri non-MSA | Missouri | Taney | 3 | 548 | 20 | 22 | 14 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1328 | 17 | 31 | 27 |
| Kansas City | Missouri | Clay | 20 | 1011 | 16 | 21 | 15 |
| Joplin | Missouri | Jasper | 30 | 1738 | 13 | 17 | 26 |
| Missouri non-MSA | Missouri | Pettis | 4 | 487 | 11 | 16 | 11 |
| Kansas City | Missouri | Cass | 9 | 705 | 10 | 19 | 17 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 590 | 10 | 10 | 11 |
| Joplin | Missouri | Newton | 6 | 868 | 9 | 9 | 10 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 376 | 9 | 11 | 9 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 360 | 9 | 10 | 8 |
| Kansas City | Kansas | Leavenworth | 8 | 1459 | 9 | 8 | 8 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 396 | 9 | 7 | 5 |
| Springfield | Missouri | Christian | 1 | 335 | 8 | 11 | 8 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 300 | 8 | 7 | 6 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 350 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 230 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Camden | 5 | 339 | 6 | 10 | 8 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 312 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Stone | 1 | 123 | 5 | 4 | 3 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 5 | 636 | 5 | 8 | 11 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 381 | 5 | 6 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 170 | 5 | 4 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 104 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Butler | 2 | 275 | 5 | 6 | 5 |
| Kansas City | Missouri | Platte | 10 | 343 | 5 | 7 | 6 |
| St. Louis-Farmington | Missouri | Warren | 0 | 191 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Marion | 1 | 181 | 4 | 7 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 234 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 211 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Pike | 1 | 95 | 3 | 2 | 1 |
| Kansas City | Missouri | Ray | 2 | 116 | 3 | 4 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 116 | 3 | 5 | 3 |
| Missouri non-MSA | Missouri | McDonald | 7 | 950 | 3 | 4 | 9 |
| Kansas City | Missouri | Lafayette | 2 | 175 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Johnson | 2 | 486 | 3 | 5 | 9 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 175 | 3 | 7 | 5 |
| Missouri non-MSA | Missouri | Miller | 1 | 114 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Perry | 4 | 223 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 55 | 3 | 3 | 1 |
| Missouri non-MSA | Missouri | Barry | 4 | 248 | 3 | 4 | 5 |
| St. Joseph | Missouri | Buchanan | 10 | 1076 | 2 | 4 | 4 |
| Springfield | Missouri | Polk | 0 | 209 | 2 | 4 | 6 |
| Missouri non-MSA | Missouri | Howell | 2 | 152 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Crawford | 0 | 71 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 142 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 90 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 152 | 2 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 79 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 139 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 197 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 224 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 78 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 27 | 2 | 1 | 0 |
| Kansas City | Kansas | Miami | 0 | 133 | 2 | 2 | 2 |
| Springfield | Missouri | Webster | 1 | 128 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Saline | 7 | 424 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Washington | 1 | 69 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 0 | 50 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 28 | 1 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 60 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 67 | 1 | 2 | 1 |
| St. Louis-Farmington | Illinois | Bond | 3 | 60 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 51 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 27 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 53 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 2 | 83 | 1 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 64 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 45 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 29 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 40 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 41 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Audrain | 1 | 199 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 141 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 20 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 21 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 76 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Madison | 0 | 24 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 60 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 20 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Phelps | 0 | 81 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 12 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 49 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 44 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 134 | 0 | 0 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 88 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 38 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 83 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 49 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 69 | 0 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 48 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 57 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 61 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Atchison | 0 | 14 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 100 | 0 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 0 | 30 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 14 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 9 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Laclede | 1 | 195 | 0 | 1 | 3 |
| Missouri non-MSA | Missouri | Grundy | 1 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 43 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 29 | 0 | 0 | 0 |
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
