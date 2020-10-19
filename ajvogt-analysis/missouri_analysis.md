# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/19/2020  
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
| St. Louis-Farmington | 1815 | 75455 | 679 | 600 | 557 |
| Missouri non-MSA | 455 | 34726 | 524 | 507 | 452 |
| Kansas City | 744 | 53544 | 486 | 449 | 428 |
| Columbia-Jefferson City | 51 | 10776 | 173 | 183 | 121 |
| Springfield | 131 | 12562 | 147 | 164 | 169 |
| Joplin | 84 | 6693 | 75 | 71 | 65 |
| St. Joseph | 40 | 3518 | 55 | 51 | 47 |
| Cape Girardeau-Sikeston | 66 | 4220 | 53 | 60 | 54 |
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
| St. Louis-Farmington | Missouri | St. Louis | 857 | 27900 | 222 | 199 | 178 |
| St. Louis-Farmington | Missouri | St. Charles | 140 | 9608 | 133 | 112 | 86 |
| Kansas City | Missouri | Jackson | 117 | 9174 | 122 | 100 | 75 |
| Kansas City | Kansas | Johnson | 173 | 13009 | 105 | 98 | 101 |
| Springfield | Missouri | Greene | 104 | 8299 | 81 | 99 | 103 |
| Kansas City | Missouri | Kansas City | 163 | 13614 | 76 | 87 | 108 |
| St. Louis-Farmington | Illinois | Madison | 152 | 6748 | 59 | 54 | 50 |
| Columbia-Jefferson City | Missouri | Cole | 18 | 2477 | 54 | 51 | 38 |
| Columbia-Jefferson City | Missouri | Boone | 14 | 5612 | 52 | 77 | 42 |
| Joplin | Missouri | Newton | 17 | 1887 | 52 | 32 | 19 |
| Kansas City | Kansas | Wyandotte | 145 | 7897 | 47 | 45 | 42 |
| St. Louis-Farmington | Missouri | St. Louis City | 218 | 7891 | 46 | 43 | 38 |
| Kansas City | Missouri | Clay | 46 | 2300 | 45 | 32 | 20 |
| St. Louis-Farmington | Illinois | St. Clair | 213 | 7512 | 43 | 43 | 44 |
| St. Louis-Farmington | Missouri | Jefferson | 77 | 5132 | 40 | 26 | 46 |
| St. Joseph | Missouri | Buchanan | 34 | 2736 | 39 | 36 | 35 |
| St. Louis-Farmington | Missouri | Franklin | 40 | 2321 | 35 | 28 | 28 |
| Springfield | Missouri | Christian | 10 | 2080 | 33 | 31 | 30 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 45 | 2437 | 28 | 33 | 33 |
| Missouri non-MSA | Missouri | Butler | 8 | 1017 | 26 | 20 | 16 |
| Missouri non-MSA | Missouri | Phelps | 19 | 759 | 24 | 17 | 12 |
| Joplin | Missouri | Jasper | 67 | 4806 | 22 | 39 | 45 |
| St. Louis-Farmington | Missouri | St. Francois | 22 | 2618 | 21 | 29 | 25 |
| Columbia-Jefferson City | Missouri | Callaway | 5 | 1008 | 21 | 20 | 14 |
| St. Louis-Farmington | Illinois | Clinton | 24 | 1560 | 21 | 18 | 17 |
| Missouri non-MSA | Missouri | Laclede | 18 | 1067 | 21 | 20 | 19 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 397 | 21 | 14 | 9 |
| Missouri non-MSA | Missouri | Camden | 26 | 1448 | 20 | 23 | 22 |
| Kansas City | Missouri | Cass | 28 | 1872 | 19 | 20 | 17 |
| Missouri non-MSA | Missouri | Lawrence | 14 | 957 | 19 | 16 | 15 |
| Cape Girardeau-Sikeston | Missouri | Scott | 18 | 1244 | 18 | 20 | 14 |
| Missouri non-MSA | Missouri | Johnson | 11 | 1399 | 18 | 27 | 14 |
| Missouri non-MSA | Missouri | Barry | 7 | 707 | 17 | 12 | 9 |
| Springfield | Missouri | Webster | 8 | 1039 | 17 | 19 | 18 |
| Missouri non-MSA | Missouri | Miller | 5 | 749 | 16 | 13 | 10 |
| Missouri non-MSA | Missouri | Howell | 6 | 995 | 16 | 16 | 17 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 1017 | 15 | 14 | 10 |
| Missouri non-MSA | Missouri | Pettis | 14 | 1411 | 15 | 14 | 14 |
| Kansas City | Missouri | Platte | 12 | 903 | 14 | 11 | 9 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1049 | 14 | 12 | 11 |
| Kansas City | Kansas | Leavenworth | 17 | 2424 | 12 | 13 | 18 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 754 | 12 | 12 | 10 |
| Kansas City | Missouri | Clinton | 8 | 420 | 12 | 11 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 7 | 486 | 12 | 10 | 7 |
| Missouri non-MSA | Missouri | Randolph | 3 | 493 | 11 | 13 | 9 |
| Missouri non-MSA | Missouri | Barton | 2 | 395 | 11 | 10 | 7 |
| St. Louis-Farmington | Illinois | Macoupin | 9 | 722 | 10 | 8 | 8 |
| Missouri non-MSA | Missouri | Taney | 33 | 1556 | 10 | 12 | 15 |
| St. Louis-Farmington | Illinois | Bond | 9 | 460 | 10 | 7 | 6 |
| Springfield | Missouri | Polk | 8 | 866 | 10 | 9 | 14 |
| Missouri non-MSA | Missouri | Morgan | 6 | 571 | 10 | 10 | 10 |
| Missouri non-MSA | Missouri | Pulaski | 8 | 891 | 10 | 11 | 12 |
| Missouri non-MSA | Missouri | Wright | 1 | 556 | 10 | 9 | 11 |
| Kansas City | Missouri | Lafayette | 24 | 738 | 9 | 9 | 12 |
| Missouri non-MSA | Missouri | Crawford | 7 | 545 | 9 | 8 | 6 |
| Missouri non-MSA | Missouri | Stone | 7 | 633 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Madison | 2 | 428 | 8 | 8 | 5 |
| Missouri non-MSA | Missouri | Texas | 3 | 517 | 8 | 9 | 8 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 570 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Adair | 0 | 460 | 7 | 6 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 27 | 842 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Ripley | 4 | 215 | 7 | 5 | 2 |
| Missouri non-MSA | Missouri | Henry | 5 | 343 | 7 | 7 | 6 |
| St. Joseph | Missouri | DeKalb | 2 | 241 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Washington | 14 | 596 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Pemiscot | 12 | 667 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Marion | 14 | 813 | 6 | 7 | 6 |
| St. Louis-Farmington | Missouri | Warren | 1 | 570 | 6 | 5 | 4 |
| St. Joseph | Missouri | Andrew | 4 | 388 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1183 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Audrain | 7 | 527 | 6 | 4 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 20 | 695 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 290 | 5 | 4 | 4 |
| Kansas City | Kansas | Miami | 2 | 474 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Perry | 7 | 748 | 5 | 6 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 2 | 432 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Saline | 9 | 891 | 5 | 6 | 8 |
| Kansas City | Missouri | Bates | 5 | 224 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 5 | 381 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Oregon | 0 | 209 | 5 | 4 | 3 |
| Springfield | Missouri | Dallas | 1 | 278 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Dunklin | 12 | 982 | 4 | 7 | 9 |
| Missouri non-MSA | Missouri | Dent | 3 | 230 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Vernon | 3 | 288 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 217 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Benton | 5 | 452 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Wayne | 1 | 290 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Maries | 0 | 139 | 4 | 3 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 453 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 275 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 2 | 208 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Daviess | 3 | 199 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Pike | 8 | 302 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Hickory | 3 | 177 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Harrison | 1 | 171 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 226 | 3 | 2 | 2 |
| Kansas City | Missouri | Ray | 2 | 233 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Monroe | 1 | 125 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Livingston | 6 | 542 | 3 | 7 | 5 |
| Missouri non-MSA | Missouri | Gentry | 10 | 171 | 3 | 2 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 153 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Shannon | 3 | 196 | 3 | 4 | 4 |
| Kansas City | Kansas | Linn | 1 | 109 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Douglas | 6 | 268 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Lewis | 2 | 169 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 109 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 125 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 91 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Ozark | 1 | 175 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 3 | 153 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 184 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Carroll | 2 | 171 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 61 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 99 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 105 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 57 | 1 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 153 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Macon | 1 | 194 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Holt | 1 | 106 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 96 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Grundy | 9 | 239 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Linn | 2 | 152 | 1 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 107 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 48 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 59 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 1 | 71 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 69 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Chariton | 1 | 55 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
