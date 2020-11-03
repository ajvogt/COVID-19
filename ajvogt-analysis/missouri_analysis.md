# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/03/2020  
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
| St. Louis-Farmington | 1934 | 88897 | 1035 | 903 | 748 |
| Kansas City | 910 | 61923 | 706 | 576 | 506 |
| Missouri non-MSA | 599 | 43407 | 662 | 591 | 539 |
| Columbia-Jefferson City | 69 | 13719 | 237 | 203 | 178 |
| Springfield | 184 | 15025 | 198 | 169 | 163 |
| Joplin | 99 | 7798 | 87 | 78 | 72 |
| Cape Girardeau-Sikeston | 86 | 5208 | 80 | 68 | 63 |
| St. Joseph | 55 | 4150 | 33 | 42 | 46 |
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
| St. Louis-Farmington | Missouri | St. Louis | 891 | 32500 | 362 | 304 | 250 |
| Kansas City | Kansas | Johnson | 213 | 15218 | 200 | 153 | 122 |
| Kansas City | Missouri | Kansas City | 213 | 15593 | 182 | 132 | 111 |
| St. Louis-Farmington | Missouri | St. Charles | 156 | 11832 | 164 | 149 | 128 |
| Kansas City | Missouri | Jackson | 140 | 10777 | 119 | 112 | 105 |
| Springfield | Missouri | Greene | 140 | 9767 | 117 | 101 | 98 |
| St. Louis-Farmington | Illinois | Madison | 159 | 7891 | 95 | 78 | 64 |
| St. Louis-Farmington | Missouri | Jefferson | 89 | 6133 | 86 | 68 | 54 |
| Columbia-Jefferson City | Missouri | Cole | 26 | 3506 | 81 | 70 | 59 |
| St. Louis-Farmington | Missouri | St. Louis City | 225 | 8901 | 76 | 67 | 54 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 6462 | 71 | 59 | 57 |
| St. Louis-Farmington | Illinois | St. Clair | 224 | 8466 | 67 | 64 | 52 |
| Joplin | Missouri | Jasper | 77 | 5610 | 62 | 57 | 47 |
| Kansas City | Kansas | Wyandotte | 165 | 8580 | 50 | 47 | 46 |
| St. Louis-Farmington | Missouri | Franklin | 48 | 2995 | 48 | 46 | 36 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 1503 | 42 | 34 | 26 |
| Kansas City | Missouri | Clay | 49 | 2801 | 42 | 35 | 32 |
| St. Louis-Farmington | Missouri | St. Francois | 29 | 3126 | 41 | 35 | 30 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 55 | 2909 | 37 | 33 | 33 |
| Springfield | Missouri | Christian | 16 | 2500 | 33 | 29 | 29 |
| Missouri non-MSA | Missouri | Pettis | 24 | 1837 | 32 | 28 | 21 |
| Missouri non-MSA | Missouri | Butler | 8 | 1394 | 31 | 25 | 22 |
| Kansas City | Missouri | Cass | 32 | 2237 | 31 | 25 | 22 |
| Missouri non-MSA | Missouri | Taney | 35 | 1916 | 28 | 24 | 18 |
| Cape Girardeau-Sikeston | Missouri | Scott | 26 | 1585 | 25 | 22 | 21 |
| Joplin | Missouri | Newton | 22 | 2188 | 24 | 21 | 25 |
| St. Joseph | Missouri | Buchanan | 43 | 3129 | 23 | 26 | 31 |
| St. Louis-Farmington | Illinois | Monroe | 34 | 1085 | 22 | 16 | 11 |
| Springfield | Missouri | Polk | 10 | 1091 | 22 | 15 | 12 |
| Missouri non-MSA | Missouri | Howell | 14 | 1293 | 21 | 19 | 18 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1278 | 21 | 18 | 15 |
| St. Louis-Farmington | Illinois | Clinton | 31 | 1936 | 21 | 24 | 21 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1334 | 20 | 19 | 15 |
| Missouri non-MSA | Missouri | Barry | 9 | 942 | 19 | 15 | 13 |
| Missouri non-MSA | Missouri | Lawrence | 24 | 1222 | 18 | 17 | 16 |
| Missouri non-MSA | Missouri | Miller | 15 | 991 | 18 | 15 | 14 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1612 | 17 | 15 | 20 |
| Missouri non-MSA | Missouri | Marion | 14 | 1028 | 17 | 14 | 10 |
| Missouri non-MSA | Missouri | Phelps | 29 | 950 | 17 | 13 | 14 |
| Springfield | Missouri | Webster | 16 | 1256 | 16 | 14 | 16 |
| Missouri non-MSA | Missouri | Camden | 36 | 1696 | 16 | 17 | 20 |
| Kansas City | Kansas | Leavenworth | 20 | 2651 | 15 | 12 | 13 |
| Missouri non-MSA | Missouri | Pulaski | 11 | 1090 | 15 | 14 | 12 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 503 | 15 | 14 | 9 |
| Kansas City | Missouri | Lafayette | 26 | 938 | 15 | 14 | 11 |
| Columbia-Jefferson City | Missouri | Moniteau | 12 | 719 | 14 | 16 | 12 |
| Missouri non-MSA | Missouri | Morgan | 8 | 762 | 13 | 12 | 11 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 965 | 13 | 14 | 13 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1209 | 13 | 15 | 11 |
| Kansas City | Missouri | Platte | 13 | 1067 | 12 | 11 | 11 |
| Missouri non-MSA | Missouri | Crawford | 9 | 718 | 12 | 11 | 9 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 3 | 560 | 12 | 8 | 6 |
| Missouri non-MSA | Missouri | Laclede | 23 | 1276 | 12 | 14 | 17 |
| Missouri non-MSA | Missouri | Henry | 8 | 465 | 12 | 8 | 7 |
| Missouri non-MSA | Missouri | Audrain | 10 | 664 | 12 | 9 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 571 | 12 | 11 | 12 |
| Missouri non-MSA | Missouri | Stone | 11 | 770 | 11 | 9 | 8 |
| Missouri non-MSA | Missouri | Washington | 20 | 741 | 11 | 10 | 8 |
| Missouri non-MSA | Missouri | Sullivan | 3 | 384 | 11 | 7 | 5 |
| Missouri non-MSA | Missouri | Perry | 8 | 886 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | Randolph | 3 | 683 | 11 | 12 | 12 |
| Columbia-Jefferson City | Missouri | Cooper | 4 | 685 | 10 | 8 | 7 |
| Kansas City | Missouri | Clinton | 25 | 570 | 10 | 10 | 10 |
| Missouri non-MSA | Missouri | Saline | 11 | 1026 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Adair | 0 | 581 | 10 | 8 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 835 | 9 | 9 | 8 |
| St. Louis-Farmington | Illinois | Macoupin | 11 | 879 | 9 | 10 | 9 |
| Missouri non-MSA | Missouri | Texas | 3 | 649 | 8 | 8 | 9 |
| Springfield | Missouri | Dallas | 2 | 411 | 8 | 9 | 6 |
| Missouri non-MSA | Missouri | Madison | 3 | 554 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Hickory | 4 | 258 | 8 | 5 | 4 |
| Kansas City | Missouri | Ray | 2 | 333 | 8 | 6 | 5 |
| St. Louis-Farmington | Missouri | Warren | 2 | 681 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 200 | 8 | 6 | 3 |
| Kansas City | Kansas | Miami | 2 | 564 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 14 | 771 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Pike | 8 | 402 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Macon | 1 | 256 | 7 | 4 | 3 |
| Missouri non-MSA | Missouri | McDonald | 12 | 1264 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Vernon | 3 | 377 | 6 | 6 | 5 |
| St. Joseph | Missouri | Andrew | 8 | 482 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Maries | 0 | 226 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Wright | 8 | 626 | 5 | 4 | 6 |
| St. Louis-Farmington | Illinois | Bond | 9 | 546 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Shannon | 5 | 275 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 295 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Lewis | 2 | 235 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Monroe | 2 | 196 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Carroll | 4 | 223 | 4 | 3 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 507 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Livingston | 9 | 588 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Cedar | 4 | 259 | 4 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 154 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Barton | 4 | 456 | 4 | 4 | 7 |
| Missouri non-MSA | Missouri | Benton | 7 | 511 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Ripley | 4 | 296 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Wayne | 3 | 336 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 4 | 280 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 467 | 4 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 273 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Grundy | 11 | 286 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Gentry | 10 | 209 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 253 | 3 | 2 | 3 |
| St. Joseph | Missouri | DeKalb | 3 | 324 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 95 | 3 | 2 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 195 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 12 | 308 | 3 | 2 | 2 |
| Kansas City | Missouri | Bates | 8 | 272 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Clark | 1 | 135 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ralls | 0 | 222 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 3 | 194 | 2 | 2 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 85 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Ozark | 1 | 228 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Iron | 0 | 118 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 7 | 177 | 2 | 1 | 1 |
| Kansas City | Kansas | Linn | 1 | 127 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 1 | 131 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 75 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 154 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Harrison | 1 | 203 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 1 | 90 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Daviess | 4 | 234 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 130 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 82 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 50 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 37 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 69 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 61 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 112 | 0 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 1 | 215 | 0 | 4 | 3 |
| Missouri non-MSA | Missouri | Worth | 0 | 37 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
