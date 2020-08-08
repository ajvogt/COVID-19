# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/08/2020  
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
| St. Louis-Farmington | 1238 | 33991 | 602 | 729 | 602 |
| Kansas City | 379 | 24853 | 396 | 476 | 435 |
| Missouri non-MSA | 98 | 9080 | 184 | 209 | 173 |
| Springfield | 13 | 2172 | 54 | 68 | 54 |
| Columbia-Jefferson City | 10 | 2195 | 51 | 60 | 48 |
| Joplin | 36 | 2606 | 26 | 32 | 40 |
| Cape Girardeau-Sikeston | 19 | 1117 | 12 | 17 | 20 |
| St. Joseph | 12 | 1247 | 5 | 7 | 7 |
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
| St. Louis-Farmington | Missouri | St. Louis | 662 | 14563 | 240 | 303 | 242 |
| Kansas City | Missouri | Kansas City | 61 | 6476 | 96 | 137 | 120 |
| Kansas City | Kansas | Johnson | 102 | 5522 | 91 | 88 | 101 |
| Kansas City | Missouri | Jackson | 64 | 3909 | 84 | 112 | 82 |
| St. Louis-Farmington | Missouri | St. Louis City | 172 | 5058 | 81 | 89 | 78 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 3954 | 74 | 111 | 91 |
| Kansas City | Kansas | Wyandotte | 99 | 4810 | 62 | 59 | 70 |
| St. Louis-Farmington | Illinois | St. Clair | 160 | 3897 | 55 | 61 | 60 |
| St. Louis-Farmington | Illinois | Madison | 74 | 2470 | 53 | 55 | 46 |
| Springfield | Missouri | Greene | 10 | 1440 | 36 | 46 | 35 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1544 | 35 | 47 | 33 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1328 | 25 | 33 | 28 |
| Missouri non-MSA | Missouri | Taney | 3 | 548 | 22 | 23 | 14 |
| Kansas City | Missouri | Clay | 20 | 1011 | 18 | 23 | 16 |
| Joplin | Missouri | Jasper | 30 | 1738 | 16 | 21 | 28 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 376 | 12 | 12 | 9 |
| Kansas City | Missouri | Cass | 9 | 705 | 12 | 22 | 17 |
| Missouri non-MSA | Missouri | Pettis | 4 | 487 | 11 | 16 | 11 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 590 | 11 | 11 | 11 |
| Joplin | Missouri | Newton | 6 | 868 | 10 | 10 | 11 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 360 | 10 | 11 | 8 |
| Springfield | Missouri | Christian | 1 | 335 | 10 | 12 | 9 |
| Kansas City | Kansas | Leavenworth | 8 | 1459 | 9 | 8 | 8 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 350 | 9 | 9 | 6 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 300 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 230 | 8 | 7 | 6 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 387 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Camden | 5 | 339 | 7 | 12 | 8 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 305 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Stone | 1 | 123 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Marion | 1 | 181 | 6 | 7 | 5 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 5 | 636 | 6 | 8 | 12 |
| Kansas City | Missouri | Platte | 10 | 343 | 6 | 8 | 6 |
| Missouri non-MSA | Missouri | Butler | 2 | 275 | 5 | 7 | 5 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 381 | 5 | 7 | 6 |
| St. Louis-Farmington | Missouri | Warren | 0 | 191 | 5 | 5 | 4 |
| St. Louis-Farmington | Illinois | Jersey | 2 | 98 | 5 | 2 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 234 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Johnson | 2 | 486 | 4 | 5 | 9 |
| Missouri non-MSA | Missouri | Barry | 4 | 248 | 4 | 4 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 116 | 4 | 5 | 3 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 156 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 211 | 4 | 6 | 5 |
| Kansas City | Missouri | Ray | 2 | 116 | 4 | 5 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 139 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 175 | 4 | 7 | 5 |
| Missouri non-MSA | Missouri | Pike | 1 | 95 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Miller | 1 | 114 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | McDonald | 7 | 950 | 3 | 5 | 9 |
| Kansas City | Missouri | Lafayette | 2 | 175 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Howell | 2 | 152 | 3 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 142 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 55 | 3 | 3 | 1 |
| Missouri non-MSA | Missouri | Crawford | 0 | 71 | 3 | 2 | 1 |
| Springfield | Missouri | Polk | 0 | 209 | 3 | 4 | 6 |
| St. Joseph | Missouri | Buchanan | 10 | 1076 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Perry | 4 | 223 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 152 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 197 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 90 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Texas | 0 | 50 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 27 | 2 | 1 | 0 |
| Kansas City | Missouri | Clinton | 0 | 79 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Saline | 7 | 424 | 2 | 4 | 4 |
| Springfield | Missouri | Webster | 1 | 128 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 0 | 78 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 224 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 0 | 30 | 2 | 1 | 0 |
| Kansas City | Kansas | Miami | 0 | 133 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Douglas | 2 | 83 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Randolph | 1 | 67 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Washington | 1 | 69 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 1 | 40 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 27 | 1 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 60 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 28 | 1 | 1 | 0 |
| St. Louis-Farmington | Illinois | Bond | 3 | 59 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 51 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 20 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Phelps | 0 | 81 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 29 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 21 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 45 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 20 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 60 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 41 | 1 | 1 | 0 |
| Kansas City | Missouri | Bates | 1 | 44 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 64 | 1 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 88 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 76 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 53 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 199 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Laclede | 1 | 195 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | Madison | 0 | 24 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 141 | 1 | 1 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 36 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 49 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ozark | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 57 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 61 | 0 | 0 | 1 |
| Kansas City | Kansas | Linn | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 49 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 134 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carroll | 0 | 100 | 0 | 2 | 2 |
| St. Joseph | Kansas | Doniphan | 0 | 48 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 38 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 69 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Gentry | 9 | 83 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 9 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 9 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Grundy | 1 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 43 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
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
