# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/19/2020  
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
| St. Louis-Farmington | 1322 | 40811 | 683 | 631 | 678 |
| Kansas City | 411 | 29407 | 458 | 417 | 457 |
| Missouri non-MSA | 107 | 11427 | 238 | 211 | 206 |
| Springfield | 13 | 2962 | 78 | 70 | 67 |
| Columbia-Jefferson City | 12 | 2920 | 71 | 61 | 60 |
| Joplin | 40 | 2944 | 39 | 31 | 35 |
| Cape Girardeau-Sikeston | 20 | 1392 | 30 | 23 | 21 |
| St. Joseph | 12 | 1336 | 10 | 7 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 705 | 16968 | 240 | 227 | 265 |
| Kansas City | Missouri | Kansas City | 66 | 7857 | 138 | 122 | 138 |
| Kansas City | Kansas | Johnson | 108 | 6655 | 112 | 101 | 97 |
| St. Louis-Farmington | Missouri | St. Charles | 95 | 4810 | 83 | 75 | 102 |
| Kansas City | Missouri | Jackson | 67 | 4712 | 79 | 76 | 93 |
| St. Louis-Farmington | Illinois | Madison | 86 | 3241 | 77 | 69 | 58 |
| Kansas City | Kansas | Wyandotte | 108 | 5450 | 70 | 59 | 59 |
| St. Louis-Farmington | Illinois | St. Clair | 163 | 4551 | 63 | 61 | 60 |
| St. Louis-Farmington | Missouri | St. Louis City | 181 | 5693 | 56 | 68 | 76 |
| Springfield | Missouri | Greene | 10 | 2004 | 54 | 50 | 45 |
| St. Louis-Farmington | Missouri | Jefferson | 30 | 2028 | 52 | 42 | 43 |
| St. Louis-Farmington | Missouri | St. Francois | 4 | 612 | 31 | 20 | 14 |
| Columbia-Jefferson City | Missouri | Boone | 5 | 1635 | 29 | 26 | 29 |
| Joplin | Missouri | Jasper | 34 | 1981 | 28 | 21 | 24 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 613 | 25 | 19 | 15 |
| Missouri non-MSA | Missouri | Taney | 3 | 778 | 20 | 21 | 20 |
| St. Louis-Farmington | Missouri | Franklin | 19 | 778 | 19 | 16 | 14 |
| Kansas City | Missouri | Cass | 9 | 887 | 16 | 15 | 20 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 6 | 776 | 15 | 11 | 11 |
| Missouri non-MSA | Missouri | Pettis | 5 | 666 | 15 | 15 | 15 |
| Kansas City | Missouri | Clay | 30 | 1167 | 14 | 15 | 18 |
| Springfield | Missouri | Christian | 1 | 472 | 14 | 12 | 11 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 512 | 13 | 11 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 492 | 12 | 9 | 8 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 402 | 11 | 9 | 8 |
| Joplin | Missouri | Newton | 6 | 963 | 11 | 9 | 10 |
| Missouri non-MSA | Missouri | Marion | 1 | 278 | 10 | 8 | 7 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 252 | 10 | 7 | 5 |
| Missouri non-MSA | Missouri | Stone | 1 | 204 | 9 | 7 | 5 |
| Kansas City | Kansas | Leavenworth | 9 | 1548 | 9 | 8 | 9 |
| Missouri non-MSA | Missouri | Washington | 1 | 149 | 8 | 6 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 267 | 8 | 6 | 6 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 454 | 8 | 8 | 10 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 173 | 8 | 7 | 4 |
| Missouri non-MSA | Missouri | Camden | 7 | 415 | 7 | 7 | 10 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 238 | 7 | 5 | 6 |
| St. Joseph | Missouri | Buchanan | 10 | 1140 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 3 | 306 | 6 | 7 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 369 | 6 | 6 | 5 |
| Kansas City | Missouri | Platte | 10 | 418 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 275 | 6 | 6 | 4 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 205 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Saline | 7 | 483 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 275 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Laclede | 1 | 243 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Phelps | 0 | 129 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 180 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Holt | 0 | 46 | 5 | 2 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 274 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Butler | 2 | 322 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Crawford | 0 | 115 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Pike | 1 | 145 | 5 | 4 | 3 |
| Springfield | Missouri | Polk | 0 | 244 | 4 | 3 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 166 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Barry | 4 | 293 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Perry | 4 | 264 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Adair | 0 | 189 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 61 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Miller | 1 | 161 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Johnson | 3 | 520 | 3 | 3 | 5 |
| St. Louis-Farmington | Illinois | Bond | 3 | 88 | 3 | 2 | 2 |
| Springfield | Missouri | Webster | 1 | 161 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ripley | 0 | 76 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 227 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Howell | 2 | 178 | 3 | 2 | 3 |
| Kansas City | Missouri | Lafayette | 2 | 200 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 75 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 71 | 2 | 1 | 1 |
| Kansas City | Missouri | Clinton | 0 | 103 | 2 | 2 | 2 |
| Kansas City | Kansas | Miami | 0 | 150 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Madison | 0 | 41 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 41 | 2 | 1 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 84 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 166 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Randolph | 1 | 87 | 2 | 2 | 2 |
| St. Joseph | Missouri | Andrew | 1 | 102 | 2 | 1 | 1 |
| Springfield | Missouri | Dallas | 1 | 81 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Benton | 1 | 119 | 1 | 3 | 2 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 244 | 1 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 64 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 98 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Wright | 0 | 73 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 45 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 95 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | McDonald | 8 | 964 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | Dent | 0 | 22 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 155 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 1 | 67 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Vernon | 0 | 64 | 1 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 50 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Wayne | 0 | 69 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 31 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 36 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 25 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 69 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 41 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 29 | 1 | 1 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 44 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 31 | 1 | 1 | 0 |
| Kansas City | Missouri | Bates | 1 | 55 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 37 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 1 | 53 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 2 | 94 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Shelby | 0 | 43 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 74 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 104 | 0 | 0 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 40 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 87 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 1 | 65 | 0 | 0 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 50 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 62 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 19 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 23 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 44 | 0 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 119 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 24 | 0 | 0 | 0 |
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
