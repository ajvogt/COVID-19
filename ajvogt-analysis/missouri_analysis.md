# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 10/09/2020  
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
| St. Louis-Farmington | 1700 | 68716 | 516 | 504 | 525 |
| Missouri non-MSA | 353 | 28997 | 509 | 384 | 393 |
| Kansas City | 671 | 48487 | 472 | 414 | 377 |
| Springfield | 108 | 10843 | 206 | 168 | 171 |
| Columbia-Jefferson City | 38 | 8854 | 111 | 84 | 102 |
| Joplin | 68 | 5909 | 81 | 56 | 69 |
| St. Joseph | 35 | 2966 | 60 | 44 | 40 |
| Cape Girardeau-Sikeston | 37 | 3531 | 55 | 47 | 50 |
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
| Kansas City | Missouri | Kansas City | 149 | 12623 | 192 | 122 | 92 |
| St. Louis-Farmington | Missouri | St. Louis | 826 | 25709 | 143 | 163 | 162 |
| Springfield | Missouri | Greene | 91 | 7253 | 122 | 103 | 106 |
| Kansas City | Kansas | Johnson | 161 | 11949 | 90 | 99 | 98 |
| Joplin | Missouri | Jasper | 55 | 4433 | 86 | 53 | 57 |
| St. Louis-Farmington | Missouri | St. Charles | 115 | 8354 | 86 | 63 | 69 |
| Kansas City | Missouri | Jackson | 108 | 7973 | 55 | 64 | 63 |
| Kansas City | Kansas | Wyandotte | 134 | 7446 | 52 | 45 | 38 |
| St. Louis-Farmington | Missouri | Jefferson | 66 | 4642 | 51 | 42 | 49 |
| Columbia-Jefferson City | Missouri | Cole | 14 | 1913 | 47 | 30 | 29 |
| St. Joseph | Missouri | Buchanan | 30 | 2337 | 44 | 33 | 30 |
| St. Louis-Farmington | Illinois | Madison | 148 | 6188 | 42 | 48 | 53 |
| St. Louis-Farmington | Illinois | St. Clair | 200 | 7091 | 42 | 47 | 44 |
| Springfield | Missouri | Christian | 6 | 1756 | 40 | 29 | 30 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 18 | 2060 | 36 | 31 | 32 |
| St. Louis-Farmington | Missouri | Franklin | 32 | 1999 | 34 | 25 | 27 |
| Missouri non-MSA | Missouri | Taney | 37 | 1439 | 31 | 19 | 15 |
| St. Louis-Farmington | Missouri | St. Louis City | 213 | 7413 | 30 | 32 | 32 |
| Springfield | Missouri | Webster | 5 | 851 | 26 | 17 | 18 |
| St. Louis-Farmington | Missouri | St. Francois | 14 | 2313 | 26 | 24 | 31 |
| Missouri non-MSA | Missouri | Howell | 3 | 816 | 26 | 17 | 15 |
| Missouri non-MSA | Missouri | Laclede | 10 | 845 | 25 | 17 | 16 |
| Missouri non-MSA | Missouri | Camden | 17 | 1192 | 24 | 20 | 19 |
| Columbia-Jefferson City | Missouri | Boone | 11 | 4884 | 22 | 24 | 43 |
| Missouri non-MSA | Missouri | Lawrence | 13 | 772 | 19 | 13 | 12 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 915 | 18 | 12 | 9 |
| Missouri non-MSA | Missouri | Randolph | 2 | 386 | 17 | 11 | 7 |
| St. Louis-Farmington | Illinois | Clinton | 23 | 1355 | 16 | 18 | 16 |
| Missouri non-MSA | Missouri | Butler | 7 | 771 | 16 | 11 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 8 | 912 | 16 | 10 | 11 |
| Cape Girardeau-Sikeston | Missouri | Scott | 17 | 1002 | 15 | 11 | 10 |
| Missouri non-MSA | Missouri | Stoddard | 14 | 622 | 14 | 9 | 10 |
| Columbia-Jefferson City | Missouri | Callaway | 3 | 774 | 14 | 11 | 11 |
| Missouri non-MSA | Missouri | Saline | 9 | 829 | 14 | 8 | 7 |
| Kansas City | Missouri | Cass | 26 | 1626 | 14 | 12 | 15 |
| Missouri non-MSA | Missouri | Wright | 0 | 457 | 14 | 11 | 11 |
| Kansas City | Kansas | Leavenworth | 15 | 2296 | 13 | 23 | 18 |
| Missouri non-MSA | Missouri | Barton | 2 | 280 | 12 | 7 | 5 |
| Kansas City | Missouri | Lafayette | 19 | 619 | 12 | 9 | 11 |
| Springfield | Missouri | Polk | 5 | 751 | 12 | 15 | 13 |
| Missouri non-MSA | Missouri | Morgan | 2 | 457 | 12 | 9 | 9 |
| Missouri non-MSA | Missouri | Miller | 2 | 593 | 11 | 8 | 9 |
| Missouri non-MSA | Missouri | Pettis | 12 | 1241 | 11 | 11 | 12 |
| Missouri non-MSA | Missouri | Nodaway | 10 | 875 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | Washington | 11 | 508 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | Texas | 2 | 404 | 10 | 7 | 8 |
| Kansas City | Missouri | Clay | 42 | 1901 | 10 | 9 | 12 |
| Missouri non-MSA | Missouri | New Madrid | 16 | 609 | 10 | 6 | 5 |
| Missouri non-MSA | Missouri | Stone | 6 | 541 | 10 | 7 | 7 |
| Missouri non-MSA | Missouri | Livingston | 3 | 479 | 10 | 5 | 4 |
| Missouri non-MSA | Missouri | Benton | 5 | 403 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Pulaski | 7 | 743 | 9 | 7 | 10 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 226 | 9 | 5 | 4 |
| Missouri non-MSA | Missouri | Marion | 14 | 734 | 9 | 6 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 24 | 760 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Henry | 5 | 267 | 8 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 491 | 8 | 5 | 6 |
| Missouri non-MSA | Missouri | Barry | 6 | 550 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 10 | 592 | 8 | 6 | 6 |
| St. Joseph | Missouri | Andrew | 3 | 315 | 8 | 5 | 5 |
| Missouri non-MSA | Missouri | Vernon | 2 | 239 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Perry | 7 | 686 | 7 | 5 | 7 |
| Kansas City | Missouri | Clinton | 0 | 293 | 7 | 5 | 4 |
| Kansas City | Missouri | Platte | 10 | 758 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Lewis | 2 | 138 | 6 | 4 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 5 | 370 | 6 | 5 | 5 |
| St. Louis-Farmington | Illinois | Macoupin | 8 | 620 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Shannon | 1 | 154 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Linn | 1 | 128 | 6 | 4 | 2 |
| Kansas City | Missouri | Bates | 3 | 168 | 6 | 4 | 2 |
| Springfield | Missouri | Dallas | 1 | 232 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 0 | 159 | 5 | 4 | 3 |
| St. Joseph | Missouri | DeKalb | 2 | 173 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 1 | 159 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Crawford | 5 | 443 | 5 | 3 | 7 |
| Missouri non-MSA | Missouri | Adair | 0 | 386 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Phelps | 12 | 523 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | Oregon | 0 | 159 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 233 | 4 | 2 | 3 |
| Missouri non-MSA | Missouri | Grundy | 4 | 224 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Harrison | 1 | 144 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 329 | 4 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 3 | 236 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Hickory | 3 | 135 | 3 | 3 | 2 |
| Kansas City | Kansas | Miami | 1 | 433 | 3 | 5 | 5 |
| Kansas City | Missouri | Ray | 2 | 192 | 3 | 2 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 125 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Macon | 0 | 174 | 3 | 1 | 2 |
| Missouri non-MSA | Missouri | Audrain | 5 | 470 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Pike | 4 | 264 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Gentry | 9 | 147 | 3 | 2 | 1 |
| St. Louis-Farmington | Missouri | Warren | 1 | 503 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 230 | 3 | 3 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 19 | 420 | 2 | 2 | 3 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 196 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Ozark | 1 | 147 | 2 | 1 | 2 |
| St. Louis-Farmington | Illinois | Bond | 8 | 368 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Dade | 0 | 88 | 2 | 2 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 141 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 243 | 2 | 2 | 4 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 371 | 2 | 2 | 6 |
| Missouri non-MSA | Missouri | Clark | 0 | 79 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Madison | 1 | 326 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Scotland | 1 | 44 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 96 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Iron | 0 | 68 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 98 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 0 | 64 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 2 | 142 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 160 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 1 | 88 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 1 | 77 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1125 | 1 | 5 | 4 |
| Missouri non-MSA | Missouri | Dent | 2 | 157 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 23 | 172 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 82 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Chariton | 0 | 53 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 90 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 55 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 3 | 112 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Monroe | 1 | 95 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 43 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 85 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 31 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 66 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 34 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 22 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 1 | 154 | -2 | 0 | 1 |
| Joplin | Missouri | Newton | 13 | 1476 | -4 | 3 | 11 |
| Missouri non-MSA | Missouri | Johnson | 5 | 1044 | -9 | -1 | 10 |
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
