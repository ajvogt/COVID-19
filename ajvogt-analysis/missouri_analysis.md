# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/23/2020  
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
| St. Louis-Farmington | 1837 | 78149 | 715 | 673 | 582 |
| Missouri non-MSA | 476 | 36443 | 502 | 531 | 459 |
| Kansas City | 792 | 55156 | 447 | 476 | 439 |
| Columbia-Jefferson City | 53 | 11291 | 161 | 174 | 129 |
| Springfield | 141 | 13059 | 141 | 158 | 164 |
| Joplin | 85 | 6901 | 64 | 70 | 64 |
| Cape Girardeau-Sikeston | 68 | 4438 | 56 | 64 | 55 |
| St. Joseph | 43 | 3687 | 50 | 51 | 47 |
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
| St. Louis-Farmington | Missouri | St. Louis | 865 | 28842 | 256 | 223 | 190 |
| St. Louis-Farmington | Missouri | St. Charles | 144 | 10055 | 122 | 121 | 91 |
| Kansas City | Missouri | Kansas City | 177 | 13904 | 114 | 91 | 106 |
| Kansas City | Kansas | Johnson | 185 | 13377 | 98 | 102 | 101 |
| Springfield | Missouri | Greene | 111 | 8592 | 80 | 95 | 99 |
| Kansas City | Missouri | Jackson | 118 | 9541 | 80 | 112 | 82 |
| St. Louis-Farmington | Illinois | Madison | 153 | 6957 | 56 | 54 | 51 |
| Columbia-Jefferson City | Missouri | Cole | 18 | 2649 | 55 | 52 | 41 |
| St. Louis-Farmington | Illinois | St. Clair | 216 | 7759 | 53 | 47 | 47 |
| St. Louis-Farmington | Missouri | St. Louis City | 218 | 8103 | 50 | 49 | 40 |
| Joplin | Missouri | Jasper | 68 | 4955 | 48 | 37 | 45 |
| Kansas City | Kansas | Wyandotte | 161 | 8059 | 46 | 43 | 44 |
| Columbia-Jefferson City | Missouri | Boone | 14 | 5777 | 45 | 63 | 43 |
| St. Louis-Farmington | Missouri | Jefferson | 78 | 5282 | 42 | 45 | 44 |
| St. Louis-Farmington | Missouri | Franklin | 42 | 2433 | 33 | 31 | 28 |
| St. Joseph | Missouri | Buchanan | 37 | 2821 | 29 | 34 | 33 |
| St. Louis-Farmington | Illinois | Clinton | 25 | 1687 | 29 | 23 | 20 |
| Kansas City | Missouri | Clay | 45 | 2412 | 28 | 36 | 22 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 46 | 2540 | 26 | 34 | 33 |
| Springfield | Missouri | Christian | 10 | 2154 | 26 | 28 | 29 |
| Missouri non-MSA | Missouri | Pettis | 14 | 1500 | 25 | 18 | 15 |
| Cape Girardeau-Sikeston | Missouri | Scott | 19 | 1337 | 24 | 23 | 17 |
| St. Louis-Farmington | Missouri | St. Francois | 22 | 2699 | 22 | 27 | 25 |
| Missouri non-MSA | Missouri | Butler | 8 | 1067 | 21 | 21 | 16 |
| Columbia-Jefferson City | Missouri | Callaway | 5 | 1083 | 19 | 22 | 16 |
| Kansas City | Missouri | Cass | 28 | 1940 | 18 | 22 | 17 |
| Missouri non-MSA | Missouri | Taney | 33 | 1626 | 17 | 13 | 16 |
| Missouri non-MSA | Missouri | Camden | 28 | 1510 | 17 | 22 | 21 |
| Missouri non-MSA | Missouri | Miller | 7 | 804 | 17 | 15 | 11 |
| Missouri non-MSA | Missouri | Barry | 8 | 748 | 16 | 14 | 9 |
| Joplin | Missouri | Newton | 17 | 1946 | 16 | 33 | 18 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 438 | 16 | 15 | 10 |
| Missouri non-MSA | Missouri | Lawrence | 14 | 1018 | 15 | 17 | 15 |
| Missouri non-MSA | Missouri | Randolph | 3 | 562 | 15 | 12 | 11 |
| Missouri non-MSA | Missouri | Howell | 6 | 1066 | 15 | 17 | 17 |
| Kansas City | Kansas | Leavenworth | 18 | 2493 | 15 | 14 | 19 |
| Springfield | Missouri | Webster | 11 | 1080 | 15 | 16 | 16 |
| Missouri non-MSA | Missouri | Laclede | 21 | 1118 | 15 | 19 | 18 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 1067 | 15 | 13 | 11 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 813 | 15 | 13 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 12 | 1043 | 15 | 9 | 9 |
| Missouri non-MSA | Missouri | Morgan | 6 | 622 | 12 | 11 | 10 |
| Kansas City | Missouri | Platte | 12 | 945 | 11 | 13 | 10 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1084 | 11 | 12 | 12 |
| Columbia-Jefferson City | Missouri | Moniteau | 9 | 523 | 11 | 10 | 8 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1411 | 10 | 26 | 13 |
| St. Louis-Farmington | Illinois | Macoupin | 10 | 760 | 10 | 10 | 8 |
| Springfield | Missouri | Polk | 8 | 908 | 10 | 11 | 13 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 586 | 10 | 6 | 6 |
| Missouri non-MSA | Missouri | Crawford | 7 | 583 | 10 | 10 | 7 |
| Missouri non-MSA | Missouri | Phelps | 20 | 785 | 10 | 18 | 12 |
| Missouri non-MSA | Missouri | Marion | 14 | 858 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 331 | 9 | 7 | 4 |
| St. Louis-Farmington | Illinois | Bond | 9 | 483 | 9 | 8 | 6 |
| St. Louis-Farmington | Illinois | Monroe | 28 | 884 | 9 | 8 | 8 |
| Kansas City | Missouri | Clinton | 13 | 447 | 8 | 11 | 8 |
| Springfield | Missouri | Dallas | 1 | 325 | 8 | 6 | 4 |
| Kansas City | Missouri | Lafayette | 24 | 767 | 8 | 10 | 9 |
| Missouri non-MSA | Missouri | New Madrid | 20 | 725 | 8 | 8 | 7 |
| Missouri non-MSA | Missouri | Washington | 16 | 617 | 8 | 7 | 9 |
| Missouri non-MSA | Missouri | Saline | 10 | 916 | 7 | 6 | 8 |
| Missouri non-MSA | Missouri | Mississippi | 5 | 406 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 12 | 691 | 7 | 7 | 6 |
| St. Joseph | Missouri | DeKalb | 2 | 262 | 7 | 6 | 4 |
| St. Joseph | Kansas | Doniphan | 0 | 190 | 7 | 3 | 2 |
| St. Joseph | Missouri | Andrew | 4 | 414 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Stone | 8 | 655 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Pulaski | 9 | 906 | 7 | 11 | 10 |
| Missouri non-MSA | Missouri | Madison | 3 | 454 | 6 | 9 | 5 |
| Missouri non-MSA | Missouri | Adair | 0 | 482 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Perry | 8 | 771 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Texas | 3 | 550 | 6 | 10 | 9 |
| Missouri non-MSA | Missouri | Ripley | 4 | 241 | 6 | 6 | 3 |
| Missouri non-MSA | Missouri | Barton | 2 | 409 | 6 | 9 | 7 |
| Missouri non-MSA | Missouri | Wright | 3 | 572 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Audrain | 7 | 553 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Benton | 5 | 468 | 5 | 4 | 7 |
| Kansas City | Missouri | Ray | 2 | 257 | 5 | 4 | 3 |
| Kansas City | Kansas | Miami | 2 | 509 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 235 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Henry | 5 | 352 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Maries | 0 | 155 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Shannon | 3 | 214 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Pike | 8 | 321 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Vernon | 3 | 305 | 4 | 4 | 4 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 2 | 448 | 4 | 5 | 4 |
| St. Louis-Farmington | Missouri | Warren | 1 | 587 | 4 | 6 | 4 |
| Missouri non-MSA | Missouri | Monroe | 1 | 142 | 4 | 3 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 467 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1195 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Ozark | 1 | 192 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 179 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Oregon | 0 | 219 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Harrison | 1 | 182 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Grundy | 9 | 254 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 3 | 190 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 3 | 239 | 3 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 235 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Wayne | 1 | 295 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Carter | 3 | 164 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Douglas | 9 | 276 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Scotland | 1 | 68 | 2 | 1 | 1 |
| Kansas City | Missouri | Bates | 5 | 233 | 2 | 4 | 4 |
| Kansas City | Missouri | Caldwell | 1 | 163 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 195 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Cedar | 2 | 216 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 281 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 116 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 6 | 551 | 2 | 5 | 5 |
| Missouri non-MSA | Missouri | Holt | 1 | 112 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 115 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 95 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 62 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Daviess | 4 | 206 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Carroll | 2 | 174 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Macon | 1 | 199 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 10 | 176 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 98 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 104 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 2 | 153 | 1 | 1 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 113 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 130 | 1 | 3 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 74 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 1 | 57 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 49 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 67 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 1 | 109 | 0 | 1 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
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
