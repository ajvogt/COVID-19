# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/28/2020  
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
| St. Louis-Farmington | 1610 | 63644 | 555 | 545 | 567 |
| Missouri non-MSA | 297 | 25069 | 445 | 431 | 372 |
| Kansas City | 596 | 44189 | 392 | 383 | 359 |
| Springfield | 73 | 9256 | 212 | 189 | 175 |
| Columbia-Jefferson City | 37 | 7990 | 98 | 99 | 134 |
| Joplin | 68 | 5292 | 60 | 69 | 65 |
| Cape Girardeau-Sikeston | 34 | 3089 | 56 | 54 | 47 |
| St. Joseph | 20 | 2508 | 45 | 42 | 33 |
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
| St. Louis-Farmington | Missouri | St. Louis | 801 | 24104 | 181 | 162 | 177 |
| Springfield | Missouri | Greene | 58 | 6312 | 132 | 118 | 116 |
| Kansas City | Kansas | Johnson | 146 | 10952 | 110 | 108 | 102 |
| Kansas City | Missouri | Kansas City | 125 | 11147 | 86 | 71 | 71 |
| St. Louis-Farmington | Missouri | St. Charles | 120 | 7678 | 75 | 72 | 70 |
| Kansas City | Missouri | Jackson | 99 | 7512 | 64 | 74 | 72 |
| St. Louis-Farmington | Missouri | Jefferson | 59 | 4240 | 57 | 58 | 56 |
| St. Louis-Farmington | Illinois | Madison | 136 | 5698 | 51 | 56 | 61 |
| St. Louis-Farmington | Illinois | St. Clair | 190 | 6607 | 47 | 44 | 48 |
| Joplin | Missouri | Jasper | 53 | 3811 | 41 | 50 | 52 |
| Columbia-Jefferson City | Missouri | Boone | 10 | 4686 | 40 | 43 | 80 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 15 | 1779 | 39 | 35 | 28 |
| St. Joseph | Missouri | Buchanan | 16 | 2006 | 36 | 32 | 25 |
| Kansas City | Kansas | Wyandotte | 134 | 6929 | 35 | 34 | 33 |
| St. Louis-Farmington | Missouri | St. Louis City | 197 | 7067 | 33 | 32 | 33 |
| Springfield | Missouri | Christian | 6 | 1453 | 31 | 30 | 28 |
| St. Louis-Farmington | Missouri | Franklin | 29 | 1736 | 29 | 29 | 25 |
| Missouri non-MSA | Missouri | Camden | 11 | 1008 | 28 | 23 | 16 |
| Columbia-Jefferson City | Missouri | Cole | 14 | 1559 | 26 | 25 | 25 |
| Springfield | Missouri | Polk | 3 | 644 | 25 | 18 | 12 |
| St. Louis-Farmington | Missouri | St. Francois | 11 | 2092 | 25 | 34 | 37 |
| Kansas City | Kansas | Leavenworth | 11 | 2039 | 23 | 19 | 13 |
| Missouri non-MSA | Missouri | Pettis | 12 | 1149 | 20 | 18 | 12 |
| Springfield | Missouri | Webster | 5 | 657 | 19 | 19 | 15 |
| Joplin | Missouri | Newton | 15 | 1481 | 19 | 19 | 13 |
| Missouri non-MSA | Missouri | Johnson | 4 | 1117 | 19 | 18 | 17 |
| Missouri non-MSA | Missouri | Laclede | 4 | 641 | 18 | 17 | 12 |
| Kansas City | Missouri | Cass | 24 | 1515 | 18 | 18 | 16 |
| Missouri non-MSA | Missouri | Howell | 3 | 622 | 16 | 16 | 12 |
| St. Louis-Farmington | Illinois | Clinton | 20 | 1169 | 15 | 15 | 16 |
| Missouri non-MSA | Missouri | Wright | 0 | 352 | 14 | 14 | 8 |
| Missouri non-MSA | Missouri | Pulaski | 5 | 659 | 14 | 14 | 9 |
| Missouri non-MSA | Missouri | Lawrence | 4 | 624 | 14 | 13 | 9 |
| Missouri non-MSA | Missouri | Butler | 7 | 650 | 13 | 11 | 9 |
| Kansas City | Missouri | Lafayette | 2 | 529 | 12 | 14 | 10 |
| Missouri non-MSA | Missouri | Benton | 3 | 333 | 12 | 10 | 5 |
| Missouri non-MSA | Missouri | Taney | 31 | 1213 | 12 | 11 | 10 |
| Kansas City | Missouri | Clay | 41 | 1809 | 12 | 14 | 15 |
| Missouri non-MSA | Missouri | Washington | 10 | 423 | 12 | 8 | 6 |
| Columbia-Jefferson City | Missouri | Callaway | 3 | 662 | 11 | 11 | 11 |
| Missouri non-MSA | Missouri | Phelps | 8 | 488 | 11 | 10 | 9 |
| Kansas City | Missouri | Platte | 10 | 704 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Stone | 4 | 466 | 10 | 8 | 6 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1113 | 10 | 6 | 4 |
| Missouri non-MSA | Missouri | Miller | 1 | 508 | 9 | 10 | 9 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 776 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 10 | 531 | 9 | 7 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 17 | 878 | 9 | 9 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 13 | 508 | 9 | 10 | 7 |
| Missouri non-MSA | Missouri | Saline | 9 | 726 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Morgan | 1 | 359 | 8 | 11 | 8 |
| Missouri non-MSA | Missouri | Barry | 6 | 490 | 8 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 431 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Crawford | 4 | 402 | 7 | 10 | 7 |
| Missouri non-MSA | Missouri | Perry | 7 | 625 | 7 | 7 | 8 |
| St. Louis-Farmington | Illinois | Macoupin | 7 | 544 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Texas | 2 | 326 | 6 | 9 | 7 |
| St. Louis-Farmington | Illinois | Monroe | 16 | 674 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Dunklin | 8 | 789 | 6 | 10 | 10 |
| Kansas City | Missouri | Clinton | 0 | 241 | 6 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 321 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Wayne | 0 | 223 | 6 | 5 | 4 |
| Kansas City | Kansas | Miami | 1 | 357 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 760 | 6 | 5 | 12 |
| Missouri non-MSA | Missouri | Henry | 5 | 203 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Douglas | 3 | 205 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Randolph | 2 | 258 | 5 | 5 | 5 |
| St. Louis-Farmington | Illinois | Bond | 5 | 328 | 5 | 6 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 351 | 5 | 7 | 7 |
| St. Louis-Farmington | Missouri | Warren | 1 | 479 | 5 | 5 | 5 |
| St. Joseph | Missouri | Andrew | 2 | 258 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Madison | 1 | 306 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Marion | 14 | 663 | 5 | 4 | 7 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 76 | 4 | 3 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 109 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Daviess | 1 | 117 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Vernon | 1 | 185 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Dent | 2 | 149 | 4 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 2 | 156 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 16 | 534 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Livingston | 1 | 406 | 3 | 3 | 11 |
| Missouri non-MSA | Missouri | Audrain | 4 | 431 | 3 | 6 | 5 |
| Missouri non-MSA | Missouri | Cedar | 0 | 113 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 205 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Oregon | 0 | 123 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ripley | 0 | 165 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Shannon | 1 | 109 | 3 | 3 | 1 |
| Kansas City | Missouri | Bates | 2 | 123 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 343 | 3 | 3 | 4 |
| Springfield | Missouri | Dallas | 1 | 190 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Grundy | 4 | 193 | 3 | 4 | 5 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 60 | 3 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 2 | 134 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 3 | 108 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 83 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 68 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 185 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Lewis | 2 | 91 | 2 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 95 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 300 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Pike | 4 | 239 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Ozark | 0 | 125 | 1 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 175 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Maries | 0 | 82 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 20 | 166 | 1 | 2 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 15 | 392 | 1 | 2 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 81 | 1 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 166 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 150 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 109 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 56 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 53 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 67 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 193 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 39 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 150 | 0 | 3 | 2 |
| Missouri non-MSA | Missouri | Clark | 0 | 65 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 71 | 0 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 110 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 84 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Monroe | 1 | 90 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 1 | 79 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 31 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 47 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 50 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 122 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 33 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 2 | 132 | 0 | 0 | 0 |
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
