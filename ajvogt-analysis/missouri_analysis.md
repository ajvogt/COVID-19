# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/01/2020  
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
| St. Louis-Farmington | 1930 | 86254 | 907 | 826 | 705 |
| Kansas City | 898 | 60568 | 629 | 527 | 512 |
| Missouri non-MSA | 595 | 42060 | 617 | 564 | 554 |
| Columbia-Jefferson City | 69 | 13297 | 213 | 190 | 174 |
| Springfield | 184 | 14718 | 192 | 162 | 177 |
| Joplin | 99 | 7674 | 84 | 73 | 77 |
| Cape Girardeau-Sikeston | 85 | 5032 | 67 | 61 | 63 |
| St. Joseph | 54 | 4071 | 34 | 44 | 50 |
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
| St. Louis-Farmington | Missouri | St. Louis | 892 | 31585 | 312 | 284 | 229 |
| Kansas City | Kansas | Johnson | 205 | 14897 | 178 | 140 | 119 |
| Kansas City | Missouri | Kansas City | 213 | 15245 | 161 | 124 | 132 |
| St. Louis-Farmington | Missouri | St. Charles | 156 | 11501 | 157 | 144 | 125 |
| Springfield | Missouri | Greene | 140 | 9574 | 112 | 96 | 105 |
| Kansas City | Missouri | Jackson | 140 | 10480 | 102 | 99 | 96 |
| St. Louis-Farmington | Missouri | Jefferson | 89 | 5935 | 73 | 61 | 55 |
| St. Louis-Farmington | Missouri | St. Louis City | 225 | 8746 | 73 | 63 | 51 |
| Columbia-Jefferson City | Missouri | Boone | 15 | 6364 | 67 | 55 | 54 |
| St. Louis-Farmington | Illinois | Madison | 158 | 7554 | 67 | 62 | 55 |
| Columbia-Jefferson City | Missouri | Cole | 26 | 3310 | 65 | 63 | 57 |
| Joplin | Missouri | Jasper | 77 | 5523 | 61 | 53 | 56 |
| Kansas City | Kansas | Wyandotte | 165 | 8505 | 56 | 44 | 47 |
| St. Louis-Farmington | Illinois | St. Clair | 224 | 8247 | 52 | 56 | 48 |
| St. Louis-Farmington | Missouri | Franklin | 48 | 2879 | 48 | 42 | 37 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 1460 | 44 | 33 | 26 |
| St. Louis-Farmington | Missouri | St. Francois | 29 | 3021 | 35 | 31 | 29 |
| Kansas City | Missouri | Clay | 48 | 2713 | 33 | 30 | 29 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 55 | 2825 | 32 | 29 | 33 |
| Springfield | Missouri | Christian | 16 | 2433 | 31 | 26 | 32 |
| Kansas City | Missouri | Cass | 32 | 2188 | 27 | 23 | 22 |
| Missouri non-MSA | Missouri | Taney | 35 | 1858 | 27 | 23 | 21 |
| Missouri non-MSA | Missouri | Pettis | 24 | 1757 | 27 | 26 | 19 |
| Missouri non-MSA | Missouri | Butler | 8 | 1301 | 25 | 22 | 21 |
| St. Louis-Farmington | Missouri | Lincoln | 5 | 1288 | 22 | 18 | 16 |
| Joplin | Missouri | Newton | 22 | 2151 | 22 | 19 | 21 |
| Springfield | Missouri | Polk | 10 | 1080 | 22 | 15 | 13 |
| St. Joseph | Missouri | Buchanan | 43 | 3072 | 22 | 28 | 34 |
| Missouri non-MSA | Missouri | Howell | 14 | 1254 | 21 | 19 | 20 |
| St. Louis-Farmington | Illinois | Clinton | 31 | 1877 | 20 | 24 | 21 |
| Cape Girardeau-Sikeston | Missouri | Scott | 26 | 1519 | 20 | 21 | 20 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1235 | 19 | 17 | 14 |
| Missouri non-MSA | Missouri | Camden | 36 | 1675 | 18 | 17 | 21 |
| Springfield | Missouri | Webster | 16 | 1232 | 17 | 15 | 18 |
| Missouri non-MSA | Missouri | Miller | 15 | 956 | 17 | 15 | 14 |
| Missouri non-MSA | Missouri | Pulaski | 11 | 1059 | 16 | 13 | 12 |
| Missouri non-MSA | Missouri | Johnson | 10 | 1567 | 16 | 12 | 15 |
| Missouri non-MSA | Missouri | Lawrence | 24 | 1177 | 16 | 16 | 18 |
| St. Louis-Farmington | Illinois | Monroe | 30 | 1016 | 16 | 12 | 10 |
| Missouri non-MSA | Missouri | Barry | 9 | 898 | 16 | 14 | 13 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 471 | 15 | 13 | 8 |
| Kansas City | Missouri | Lafayette | 26 | 902 | 15 | 12 | 12 |
| Missouri non-MSA | Missouri | Phelps | 27 | 916 | 14 | 12 | 14 |
| Missouri non-MSA | Missouri | Marion | 14 | 991 | 14 | 13 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1185 | 13 | 15 | 12 |
| Missouri non-MSA | Missouri | Laclede | 23 | 1252 | 13 | 14 | 19 |
| Columbia-Jefferson City | Missouri | Moniteau | 12 | 689 | 12 | 15 | 12 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 548 | 12 | 11 | 12 |
| Missouri non-MSA | Missouri | Washington | 20 | 723 | 12 | 10 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 15 | 937 | 12 | 13 | 13 |
| Kansas City | Kansas | Leavenworth | 18 | 2603 | 11 | 12 | 13 |
| Missouri non-MSA | Missouri | Morgan | 8 | 732 | 11 | 12 | 11 |
| Kansas City | Missouri | Platte | 13 | 1047 | 11 | 11 | 11 |
| Missouri non-MSA | Missouri | Randolph | 3 | 674 | 11 | 13 | 13 |
| Missouri non-MSA | Missouri | Stone | 11 | 747 | 11 | 8 | 9 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 3 | 541 | 11 | 8 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 1 | 371 | 11 | 7 | 5 |
| Missouri non-MSA | Missouri | Perry | 8 | 865 | 10 | 8 | 7 |
| Missouri non-MSA | Missouri | Crawford | 9 | 685 | 10 | 11 | 9 |
| Missouri non-MSA | Missouri | Audrain | 10 | 639 | 10 | 8 | 6 |
| Missouri non-MSA | Missouri | Adair | 0 | 572 | 10 | 8 | 7 |
| St. Louis-Farmington | Illinois | Macoupin | 11 | 854 | 10 | 10 | 9 |
| Missouri non-MSA | Missouri | Saline | 11 | 1001 | 9 | 8 | 9 |
| Missouri non-MSA | Missouri | Henry | 8 | 436 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | Madison | 3 | 543 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Hickory | 4 | 254 | 8 | 5 | 4 |
| Kansas City | Missouri | Clinton | 24 | 540 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 812 | 8 | 8 | 9 |
| Springfield | Missouri | Dallas | 2 | 399 | 8 | 8 | 6 |
| St. Louis-Farmington | Missouri | Warren | 2 | 664 | 8 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 4 | 661 | 8 | 7 | 7 |
| Kansas City | Kansas | Miami | 2 | 563 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Texas | 3 | 628 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | McDonald | 12 | 1259 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 188 | 7 | 5 | 3 |
| Kansas City | Missouri | Ray | 2 | 309 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Monroe | 2 | 190 | 6 | 4 | 3 |
| St. Louis-Farmington | Illinois | Bond | 9 | 532 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 14 | 756 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Macon | 1 | 246 | 6 | 3 | 3 |
| Missouri non-MSA | Missouri | Maries | 0 | 218 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Vernon | 3 | 362 | 5 | 5 | 5 |
| St. Joseph | Missouri | Andrew | 8 | 468 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Pike | 8 | 380 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 281 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Shannon | 5 | 262 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Carroll | 4 | 214 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Barton | 4 | 449 | 5 | 4 | 8 |
| Missouri non-MSA | Missouri | Cedar | 4 | 253 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Dent | 4 | 273 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Ripley | 4 | 284 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Wright | 8 | 612 | 4 | 4 | 8 |
| Missouri non-MSA | Missouri | Reynolds | 1 | 94 | 4 | 2 | 1 |
| St. Joseph | Missouri | DeKalb | 2 | 316 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Lewis | 2 | 220 | 4 | 3 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 147 | 3 | 3 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 192 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Grundy | 11 | 282 | 3 | 3 | 2 |
| Kansas City | Missouri | Bates | 8 | 267 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Livingston | 9 | 580 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Ozark | 1 | 225 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Clark | 1 | 128 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Wayne | 3 | 321 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Benton | 7 | 498 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Douglas | 12 | 302 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 459 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Oregon | 0 | 244 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Ralls | 0 | 221 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 3 | 189 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 265 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Chariton | 0 | 73 | 2 | 1 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 21 | 485 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 7 | 173 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Iron | 0 | 113 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 0 | 149 | 2 | 1 | 2 |
| St. Joseph | Kansas | Doniphan | 1 | 215 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Gentry | 10 | 195 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Holt | 1 | 124 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 128 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 112 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 197 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 4 | 229 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Atchison | 1 | 84 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 1 | 80 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 60 | 1 | 0 | 0 |
| Kansas City | Kansas | Linn | 1 | 117 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 66 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 35 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 70 | 0 | 0 | 0 |
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
