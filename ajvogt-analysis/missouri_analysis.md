# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/18/2020  
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
| St. Louis-Farmington | 1812 | 74682 | 620 | 587 | 551 |
| Kansas City | 742 | 53178 | 452 | 459 | 434 |
| Missouri non-MSA | 446 | 34158 | 444 | 496 | 451 |
| Columbia-Jefferson City | 51 | 10636 | 153 | 162 | 120 |
| Springfield | 131 | 12442 | 130 | 166 | 172 |
| Joplin | 84 | 6646 | 68 | 73 | 67 |
| Cape Girardeau-Sikeston | 66 | 4176 | 47 | 61 | 54 |
| St. Joseph | 40 | 3454 | 46 | 49 | 47 |
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
| St. Louis-Farmington | Missouri | St. Louis | 857 | 27603 | 209 | 186 | 173 |
| St. Louis-Farmington | Missouri | St. Charles | 140 | 9483 | 115 | 107 | 84 |
| Kansas City | Missouri | Jackson | 117 | 9088 | 109 | 106 | 76 |
| Kansas City | Kansas | Johnson | 173 | 12932 | 106 | 99 | 103 |
| Springfield | Missouri | Greene | 104 | 8229 | 71 | 101 | 105 |
| Kansas City | Missouri | Kansas City | 162 | 13499 | 60 | 89 | 107 |
| St. Louis-Farmington | Illinois | Madison | 152 | 6685 | 57 | 51 | 51 |
| Kansas City | Kansas | Wyandotte | 145 | 7879 | 51 | 49 | 43 |
| Joplin | Missouri | Newton | 17 | 1876 | 50 | 32 | 20 |
| Columbia-Jefferson City | Missouri | Boone | 14 | 5582 | 48 | 60 | 43 |
| Columbia-Jefferson City | Missouri | Cole | 18 | 2422 | 46 | 50 | 37 |
| St. Louis-Farmington | Missouri | St. Louis City | 218 | 7854 | 46 | 42 | 37 |
| Kansas City | Missouri | Clay | 46 | 2283 | 42 | 32 | 20 |
| St. Louis-Farmington | Illinois | St. Clair | 211 | 7460 | 41 | 41 | 43 |
| St. Louis-Farmington | Missouri | Jefferson | 77 | 5081 | 33 | 42 | 47 |
| St. Joseph | Missouri | Buchanan | 34 | 2677 | 31 | 34 | 35 |
| Springfield | Missouri | Christian | 10 | 2059 | 30 | 31 | 30 |
| St. Louis-Farmington | Missouri | Franklin | 40 | 2284 | 30 | 27 | 28 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 45 | 2418 | 25 | 35 | 33 |
| Missouri non-MSA | Missouri | Butler | 8 | 992 | 22 | 19 | 15 |
| Missouri non-MSA | Missouri | Phelps | 19 | 741 | 21 | 16 | 12 |
| St. Louis-Farmington | Illinois | Clinton | 24 | 1541 | 20 | 18 | 17 |
| Columbia-Jefferson City | Missouri | Callaway | 5 | 995 | 19 | 19 | 14 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 386 | 19 | 14 | 8 |
| Missouri non-MSA | Missouri | Camden | 26 | 1434 | 18 | 24 | 22 |
| Missouri non-MSA | Missouri | Laclede | 18 | 1045 | 17 | 20 | 19 |
| Joplin | Missouri | Jasper | 67 | 4770 | 17 | 40 | 47 |
| Kansas City | Missouri | Cass | 28 | 1855 | 17 | 20 | 17 |
| Missouri non-MSA | Missouri | Lawrence | 14 | 944 | 17 | 16 | 15 |
| St. Louis-Farmington | Missouri | St. Francois | 22 | 2587 | 17 | 27 | 24 |
| Missouri non-MSA | Missouri | Johnson | 11 | 1387 | 16 | 27 | 14 |
| Cape Girardeau-Sikeston | Missouri | Scott | 18 | 1224 | 15 | 19 | 14 |
| Missouri non-MSA | Missouri | Barry | 7 | 691 | 15 | 11 | 9 |
| Missouri non-MSA | Missouri | Howell | 6 | 986 | 15 | 16 | 17 |
| Springfield | Missouri | Webster | 8 | 1021 | 14 | 19 | 18 |
| Missouri non-MSA | Missouri | Miller | 5 | 734 | 14 | 12 | 10 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 987 | 13 | 12 | 9 |
| Kansas City | Kansas | Leavenworth | 17 | 2424 | 12 | 13 | 19 |
| Kansas City | Missouri | Platte | 12 | 888 | 12 | 11 | 9 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1034 | 12 | 12 | 11 |
| Missouri non-MSA | Missouri | Pettis | 14 | 1383 | 11 | 12 | 15 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 746 | 11 | 12 | 10 |
| Kansas City | Missouri | Clinton | 7 | 408 | 10 | 10 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 7 | 473 | 10 | 9 | 7 |
| St. Louis-Farmington | Illinois | Macoupin | 8 | 709 | 10 | 8 | 8 |
| Missouri non-MSA | Missouri | Barton | 2 | 388 | 10 | 10 | 7 |
| Missouri non-MSA | Missouri | Randolph | 3 | 481 | 9 | 13 | 9 |
| Springfield | Missouri | Polk | 8 | 858 | 9 | 9 | 14 |
| Missouri non-MSA | Missouri | Morgan | 6 | 559 | 8 | 10 | 10 |
| Kansas City | Missouri | Lafayette | 24 | 733 | 8 | 9 | 12 |
| Missouri non-MSA | Missouri | Wright | 1 | 546 | 8 | 9 | 11 |
| Missouri non-MSA | Missouri | Madison | 2 | 425 | 8 | 8 | 5 |
| St. Louis-Farmington | Illinois | Bond | 9 | 440 | 8 | 5 | 5 |
| Missouri non-MSA | Missouri | Pulaski | 8 | 875 | 8 | 11 | 12 |
| Missouri non-MSA | Missouri | Texas | 3 | 513 | 7 | 9 | 9 |
| Missouri non-MSA | Missouri | Stone | 7 | 624 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Taney | 33 | 1533 | 7 | 11 | 14 |
| Missouri non-MSA | Missouri | Crawford | 7 | 531 | 7 | 7 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 27 | 835 | 7 | 7 | 7 |
| St. Joseph | Missouri | DeKalb | 2 | 238 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Ripley | 4 | 209 | 6 | 5 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 12 | 662 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Adair | 0 | 452 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Henry | 5 | 334 | 6 | 6 | 6 |
| St. Louis-Farmington | Missouri | Warren | 1 | 568 | 6 | 5 | 4 |
| St. Joseph | Missouri | Andrew | 4 | 386 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Audrain | 7 | 524 | 5 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 556 | 5 | 6 | 6 |
| Kansas City | Kansas | Miami | 2 | 474 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Marion | 14 | 804 | 5 | 6 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 2 | 429 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Perry | 7 | 744 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Washington | 14 | 581 | 5 | 7 | 8 |
| Kansas City | Missouri | Bates | 5 | 222 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1174 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 20 | 688 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 283 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Oregon | 0 | 207 | 4 | 4 | 3 |
| Springfield | Missouri | Dallas | 1 | 275 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 5 | 376 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Wayne | 1 | 289 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Dent | 3 | 225 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Vernon | 3 | 283 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Saline | 9 | 880 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Cedar | 2 | 207 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Hickory | 3 | 176 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Daviess | 3 | 198 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 273 | 3 | 3 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 448 | 3 | 3 | 2 |
| Kansas City | Missouri | Ray | 2 | 233 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 211 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Benton | 5 | 445 | 3 | 5 | 8 |
| Missouri non-MSA | Missouri | Monroe | 1 | 124 | 3 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 222 | 3 | 2 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 151 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Maries | 0 | 130 | 3 | 2 | 2 |
| Kansas City | Kansas | Linn | 1 | 109 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Dunklin | 12 | 968 | 2 | 7 | 9 |
| Missouri non-MSA | Missouri | Dade | 0 | 126 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Gentry | 10 | 167 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 164 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 91 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Livingston | 6 | 536 | 2 | 7 | 5 |
| Missouri non-MSA | Missouri | Pike | 4 | 291 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 166 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 183 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 105 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 99 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 2 | 168 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 58 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 153 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 103 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 3 | 149 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Ozark | 1 | 170 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Shannon | 3 | 185 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Douglas | 3 | 259 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Macon | 1 | 191 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 54 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 1 | 103 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 48 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 92 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 150 | 0 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 105 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 59 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 70 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 8 | 233 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 70 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 1 | 54 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
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
